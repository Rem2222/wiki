---
description: Инструкция: YouTube через собственный релей внутри страны — телефон смотрит видео из локального кэша Google (nginx маскировка + xray mux.cool + sing-box маршрутизация + zapret DPI). Видеопоток не выходит за границу.
tags: [youtube, vpn, vless, zapret, dpi, sing-box, xray, nginx, relay, dpi-bypass]
related: "[[ops/services/lightpanda]] [[tech/lightpanda-browser]]"
---

# YouTube через собственный релей внутри страны

Инструкция по схеме, при которой телефон вне дома смотрит YouTube, а видеопоток
**не выходит за границу**: он забирается из локального кэша Google внутри страны.

Все имена, адреса и ключи в примерах — заглушки. Подставьте свои.

| Заглушка | Что это |
|---|---|
| `relay.example.com` | домен релея внутри страны |
| `RELAY_IP` | адрес релея |
| `FOREIGN_IP` | адрес заграничного узла для нецензурного трафика |
| `UUID` | идентификатор пользователя, свой на каждого клиента |

---

## 1. Идея

Обычная схема «весь трафик в заграничный VPN» для видео работает плохо: трансграничный канал
узкий, его шейпят, и он общий на всех.

Здесь иначе. Телефон подключается к **релею внутри своей же страны**, а релей ломает DPI
локально (zapret/nfqws) и берёт видео из **ближайшего кэша Google**. Заграница остаётся только
для того трафика, которому она действительно нужна.

Выигрыш: видео едет по короткому внутреннему маршруту, скорость упирается в кэш провайдера,
а не в перегруженный канал за рубеж.

### Маршрут пакета

```
телефон (клиент VLESS)
   │  VLESS + WebSocket + TLS, порт 443, путь /link
   ▼
nginx :443  ── маскировка: на корень отдаётся обычная страница
   │
   ▼
xray :18082  ── принимает mux.cool клиента (sing-box его НЕ понимает)
   │  socks
   ▼
sing-box :10808  ── маршрутизация
   ├── домены Google/YouTube ──► direct ──► zapret (обход DPI) ──► локальный кэш Google
   ├── порт 53 ─────────────────► direct
   ├── IPv6 ────────────────────► reject (если у релея нет IPv6)
   └── всё остальное ───────────► VLESS ──► заграничный узел
```

### Почему в цепочке два прокси

sing-box не поддерживает `mux.cool` — мультиплексор, которым пользуются клиенты на движке Xray
(в том числе v2rayNG). Известная несовместимость:
[SagerNet/sing-box#1876](https://github.com/SagerNet/sing-box/issues/1876).

Без мультиплексора **каждое** соединение платит полное рукопожатие туннеля. Замерено ~183 мс
при задержке 42 мс до релея. Приложение YouTube на старте открывает под сотню соединений —
отсюда многосекундная пауза.

Поэтому Xray ставится **только ради приёма mux** и сразу передаёт трафик в sing-box, где живёт
вся маршрутизация. Если ваш клиент умеет мультиплексор sing-box (smux/yamux), Xray не нужен —
уберите звено и слушайте клиента напрямую.

---

## 2. Что должно быть на релее

| Служба | Порт | Роль |
|---|---|---|
| `nginx` | 443, 80 | TLS, маскировка, развод путей |
| `xray` | 18082 (loopback) | вход клиента, принимает `mux.cool` |
| `sing-box` | 10808 (loopback) | приём от xray, вся маршрутизация |
| `sing-box` | 18081 (loopback) | запасной вход без mux |
| `zapret` (nfqws) | очередь 200 | обход DPI для TCP/443 |
| `zapret` (nfqws) | очередь 201 | обход DPI для QUIC (UDP/443) |

Плюс сертификат Let's Encrypt на домен релея (`certbot`), автопродление.

Релею хватает одного ядра, если соблюдать ограничение `connbytes` (см. §3.4).

---

## 3. Конфигурация сервера

### 3.1 nginx

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name relay.example.com;
    location /.well-known/acme-challenge/ { root /var/www/html; }
    location / { return 301 https://$host$request_uri; }
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    http2 on;
    server_name relay.example.com;

    ssl_certificate     /etc/letsencrypt/live/relay.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/relay.example.com/privkey.pem;

    # Основной путь клиента: xray (умеет mux.cool).
    location /link {
        proxy_pass http://127.0.0.1:18082;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_read_timeout 300s;
        proxy_send_timeout 300s;
        proxy_buffering off;
    }

    # Запасной путь: напрямую в sing-box, без mux.
    location /link0 {
        proxy_pass http://127.0.0.1:18081;
        # заголовки те же, что выше
    }

    # Маскировка: на корень отдаём безобидную страницу, а не пустоту.
    location / {
        root /var/www/html;
        index index.nginx-debian.html;
    }
}
```

**Маскировка обязательна.** При зондировании корня отдаётся обычный сайт с валидным
сертификатом — снаружи узел выглядит рядовым веб-сервером. Туннель прячется на неочевидном пути;
не используйте `/ws`, `/vless` и прочие говорящие имена.

### 3.2 xray

```json
{
  "log": { "loglevel": "warning", "access": "/var/log/xray/access.log" },
  "inbounds": [{
    "listen": "127.0.0.1", "port": 18082, "protocol": "vless",
    "settings": {
      "clients": [{ "id": "UUID", "email": "phone" }],
      "decryption": "none"
    },
    "streamSettings": { "network": "ws", "wsSettings": { "path": "/link" } },
    "sniffing": { "enabled": true, "destOverride": ["http","tls","quic"], "routeOnly": false }
  }],
  "outbounds": [{
    "protocol": "socks", "tag": "to-singbox",
    "settings": { "servers": [{ "address": "127.0.0.1", "port": 10808 }] }
  }]
}
```

`sniffing` включать обязательно: он извлекает имя домена из рукопожатия. Без него sing-box
увидит только IP, не отличит YouTube от прочего и погонит видео за границу.

Новый UUID: `xray uuid`.

### 3.3 sing-box

Входы:

```json
{ "type": "vless", "tag": "vless-phone", "listen": "127.0.0.1", "listen_port": 18081,
  "users": [{ "uuid": "UUID", "name": "phone" }],
  "transport": { "type": "ws", "path": "/link" },
  "multiplex": { "enabled": true, "padding": false } }

{ "type": "socks", "tag": "phone-socks", "listen": "127.0.0.1", "listen_port": 10808 }
```

Правила маршрутизации — **порядок критичен**, читаются сверху вниз:

```json
{ "action": "sniff" }

{ "inbound": ["vless-phone","phone-socks"], "ip_version": 6, "action": "reject" }

{ "inbound": ["vless-phone","phone-socks"], "port": [53], "outbound": "direct" }

{ "inbound": ["vless-phone","phone-socks"],
  "domain_suffix": ["googlevideo.com","youtube.com","youtu.be","yt.be","ytimg.com",
                    "ggpht.com","googleapis.com","google.com","gstatic.com",
                    "googleusercontent.com","youtube-nocookie.com","googlesyndication.com",
                    "google-analytics.com","gvt1.com","gvt2.com"],
  "outbound": "direct" }
```

Выход по умолчанию — заграничный VLESS. У выхода `direct` поставьте
`"domain_strategy": "ipv4_only"`, если у релея нет IPv6.

**Почему все домены Google в одном правиле.** Ссылка на видеопоток, которую выдаёт API плеера,
содержит внутри IP того, кто её запросил (параметр `ip=` прямо в URL). Заберёте видео с другого
адреса — получите 403. Поэтому API и видеосервер обязаны выходить через один и тот же адрес.
Разделять их нельзя ни при каких обстоятельствах.

**Почему IPv6 отвергается.** Если у релея нет IPv6, а клиент шлёт адрес IPv6 напрямую (литералом,
минуя DNS), соединение будет висеть до таймаута. Явный отказ дешевле.

### 3.4 zapret — обход DPI

Обход TCP:

```sh
#!/bin/sh
exec /opt/zapret/nfq/nfqws \
  --user=daemon \
  --dpi-desync-fwmark=0x40000000 \
  --qnum=200 \
  --filter-tcp=443 \
  --hostlist=/opt/zapret/ipset/hosts-google.txt \
  --dpi-desync=fake,fakeddisorder \
  --dpi-desync-split-pos=10,midsld \
  --dpi-desync-fake-tls=/opt/zapret/files/fake/tls_clienthello_www_google_com.bin \
  --dpi-desync-fake-tls-mod=rnd,dupsid,sni=fonts.google.com \
  --dpi-desync-fooling=badseq,badsum
```

Обход QUIC:

```sh
#!/bin/sh
exec /opt/zapret/nfq/nfqws \
  --user=daemon \
  --dpi-desync-fwmark=0x40000000 \
  --qnum=201 \
  --filter-udp=443 \
  --hostlist=/opt/zapret/ipset/hosts-google.txt \
  --dpi-desync=fake \
  --dpi-desync-repeats=6 \
  --dpi-desync-fake-quic=/opt/zapret/files/fake/quic_initial_www_google_com.bin
```

Конкретная стратегия десинхронизации **зависит от вашего провайдера** — подбирайте
через `blockcheck` из комплекта zapret. Приведённая работает не везде.

> **Запускайте через скрипт-обёртку, а не строкой в systemd.**
> nfqws перезаписывает собственный argv, и аргумент вида `--dpi-desync=fake,fakeddisorder`
> в юните systemd разъезжается по запятой на два отдельных аргумента. Стратегия теряется
> наполовину и работает через раз. Проверка реальной команды: `systemctl show -p ExecStart <юнит>`.

Список хостов — **минимальный**. В большинстве случаев там ровно одна строка:

```
googlevideo.com
```

> **Не расширяйте список «на всякий случай».** Незаблокированные домены десинхронизация
> ломает. На практике добавление `google.com` дало сотни повторных запросов и неработающий
> YouTube — при том что сам по себе он открывался прекрасно.

Правила iptables:

```sh
iptables -t mangle -A OUTPUT -p tcp --dport 443 \
  -m mark ! --mark 0x40000000/0x40000000 \
  -m connbytes --connbytes 1:100 --connbytes-mode packets --connbytes-dir original \
  -j NFQUEUE --queue-num 200 --queue-bypass

iptables -t mangle -A OUTPUT -p udp --dport 443 \
  -m mark ! --mark 0x40000000/0x40000000 \
  -j NFQUEUE --queue-num 201 --queue-bypass
```

Выше очереди добавьте `ACCEPT` для адреса заграничного узла — проксируемому трафику обход
не нужен, а лишняя обработка съедает процессор:

```sh
iptables -t mangle -I OUTPUT -p tcp -d FOREIGN_IP --dport 443 -j ACCEPT
iptables -t mangle -I OUTPUT -p udp -d FOREIGN_IP --dport 443 -j ACCEPT
```

`connbytes 1:100` — в очередь попадают только первые пакеты соединения, где лежит рукопожатие.
Остальной поток идёт мимо. Без этого ограничения слабый сервер захлебнётся на видеопотоке.

`--dpi-desync-fwmark` и проверка `! --mark` не дают пакетам самого nfqws попасть в очередь
повторно.

---

## 4. Настройка клиента

### 4.1 Профиль

```
vless://UUID@relay.example.com:443?encryption=none&security=tls&sni=relay.example.com&fp=chrome&type=ws&host=relay.example.com&path=%2Flink#Relay
```

| Параметр | Значение |
|---|---|
| сервер / порт | `relay.example.com` : 443 |
| шифрование | none |
| security | tls, SNI = домен релея, fingerprint `chrome` |
| сеть | ws, host = домен релея, path `/link` |

> **Почему именно VLESS + WebSocket + TLS.** У Shadowsocks первые байты не похожи на TLS,
> и мобильные операторы глушат его по сигнатуре — при том что в домашней сети он прекрасно
> работает. WS+TLS на 443 неотличим от обычного захода на сайт.

### 4.2 Настройки приложения

| Настройка | Значение | Зачем |
|---|---|---|
| Мультиплексирование | **включить** | иначе каждое соединение платит рукопожатие; выигрыш ~40% |
| Concurrency (TCP/XUDP) | 8 | |
| QUIC в мультиплексном туннеле | отклонять | QUIC поверх TCP-туннеля на мобильной сети делает хуже |
| IPv6 | выключить | если у релея нет IPv6 |
| Sniffing («анализировать пакеты») | включить | иначе маршрутизация по доменам не сработает |
| Домен только для маршрутизации | включить | |

> Настройки применяются **только при переподключении**. Свернуть приложение недостаточно —
> выключите и включите туннель.

### 4.3 Маршрутизация — порядок правил решает всё

```
1.  YouTube    geosite:youtube, youtubei.googleapis.com, googlevideo.com,
               ytimg.com, ggpht.com                        → proxy
2.  QUIC       udp/443                                     → block
3.  Google     geosite:google                              → direct
4.  локалка    geoip:private, geosite:private              → direct
```

> **Правило YouTube обязано стоять выше правила Google.** `geosite:google` включает в себя
> и youtube, и googlevideo. Поставите его первым — видео уйдёт напрямую и его задушит DPI.

> **Многие клиенты добавляют новые правила НАВЕРХ списка, а не вниз.** Проверьте фактический
> порядок после добавления. Чтобы поднять правило выше — удалите и создайте заново.

**Зачем правило «остальной Google → direct».** Android постоянно опрашивает `www.google.com`
фоновой проверкой связи. Замеры на реальном устройстве: **3.2 соединения в секунду**,
144 соединения за 45 секунд, и **ни одного байта полезных данных** — 129 из них содержали
только рукопожатие и закрывались через секунду.

Через туннель каждая такая пустышка стоит 146–231 мс и занимает канал. После правила через
туннель поехало только видео: было ~150 запросов в минуту, стало 3.

> **Но урезать набор ютубных доменов нельзя.** Проверено: если оставить в туннеле только API
> плеера и видеосервер, приложение перестаёт работать — операторы душат и сам `youtube.com`.
> Весь ютубный набор должен идти через релей.

---

## 5. Проверка

### Состояние служб

```bash
systemctl is-active sing-box xray nginx <юниты zapret>
ss -tlnp | grep -E '18081|18082|10808|443'
certbot certificates | grep -E 'Certificate Name|Expiry'
systemctl show -p ExecStart <юнит zapret>     # аргументы не должны разъехаться
iptables -t mangle -L -v -n | grep NFQUEUE     # счётчики должны расти
```

### Сквозная проверка туннеля

Поднимите клиент рядом с сервером и прогоните трафик:

```bash
X="-x http://127.0.0.1:PORT -s -m 20"
curl $X https://api.ipify.org                                    # должен быть заграничный узел
curl $X -o /dev/null -w '%{http_code}\n' https://www.youtube.com # 200
curl $X -o /dev/null -w '%{http_code}\n' https://www.google.com/generate_204  # 204
curl $X -o /dev/null -w 'TLS %{time_appconnect}\n' https://<видеохост>.googlevideo.com/
```

Норма: обычный трафик выходит заграничным адресом, видеосервер отвечает за десятые доли секунды.

### Работает ли мультиплексор

Мерить **соотношением** за одинаковое окно времени: сколько запросов приложения пришлось на одно
реальное соединение до сервера.

```bash
X1=$(wc -l < /var/log/xray/access.log); N1=$(grep -c 'GET /link ' /var/log/nginx/access.log)
sleep 60
X2=$(wc -l < /var/log/xray/access.log); N2=$(grep -c 'GET /link ' /var/log/nginx/access.log)
echo "запросов $((X2-X1)) на $((N2-N1)) соединений"
```

Больше 2.5 — мультиплексор работает. Около 1 — не применяется.

> **Не ищите в журнале сервера метку `v1.mux.cool`.** Xray записывает уже распакованные адреса
> назначения, а не мультиплексную обёртку. Поиск по этой метке всегда даёт ноль и приводит
> к ложному выводу «mux выключен».

### Что реально едет через туннель

```bash
tail -n 200 /var/log/xray/access.log \
  | awk '{for(i=1;i<=NF;i++) if($i=="accepted"){print $(i+1); break}}' \
  | sed 's#^tcp:##;s/:443$//' | sort | uniq -c | sort -rn | head
```

Норма — только ютубные домены. Если полез `www.google.com`, значит на клиенте слетело правило
маршрутизации.

---

## 6. Чего эта схема не даёт

Замеры на стенде с задержкой 42 мс до релея (близко к мобильной сети), имитация старта YouTube:

| | без mux | с mux |
|---|---|---|
| 15 запросов DNS по TCP через туннель | 4.28 с | 2.28 с |
| 40 TLS-соединений | 9.24 с | 5.85 с |
| **итого** | **13.5 с** | **8.1 с** |

Стоимость одного TLS-соединения через туннель — **~146 мс**, и ниже её не опустить никакими
настройками: TLS сквозной, клиент договаривается с Google лично, релей только передаёт байты.
Мультиплексор убирает рукопожатие *туннеля*, но не рукопожатие *TLS*.

Для сравнения: при локальном обходе DPI (zapret прямо на роутере, без туннеля) то же соединение
стоит ~40 мс.

**Отсюда честный потолок.** Схема даёт быстрый и стабильный **видеопоток** — он идёт из
локального кэша. Но **старт приложения** останется медленнее, чем при локальном обходе, потому
что клиент открывает десятки соединений, и каждое платит за путь до релея.

Если нужен именно мгновенный старт — обходите DPI на самом устройстве (на Android это
ByeDPI, PowerTunnel и подобные), то есть повторяйте логику роутера, а не стройте туннель.
Туннель выигрывает там, где локальный обход не справляется с DPI оператора.

---

## 7. Грабли

- **Аргументы nfqws в systemd** разъезжаются по запятой — только скрипт-обёртка.
- **Список хостов zapret** расширять нельзя: десинхронизация ломает незаблокированные домены.
- **Домены плеера разделять нельзя** — в ссылке на видео зашит IP запросившего, иначе 403.
- **`reject` для UDP внутри туннеля** клиент видит как тишину, а не как отказ: ICMP через
  туннель не доходит. Приложение ждёт свой таймаут вместо мгновенного отката на TCP.
  Если протокол реально проходит — пропускайте, а не режьте.
- **Порядок правил** и на сервере, и на клиенте важнее их содержания.
- **Настройки клиента применяются при переподключении**, а не при сохранении.
- **sing-box не понимает `mux.cool`** — отсюда Xray в цепочке.
- **Проверяйте имена переменных в скриптах правил.** Опечатка в имени (`$FRA` вместо `$FR`)
  тихо превращает исключение в пустую строку, и правило молча не работает.
- При разборе `tcpdump` фильтр SYN «есть `Flags [S]` и нет `ack`» ложно отсекает все пакеты:
  в опциях SYN присутствует `sackOK`. Правильно — проверять начало строки на `Flags [S]`
  и отбрасывать `Flags [S.]`.
- **Замеры со стороны сервера обманчивы.** Время установки соединения, которое видит релей,
  не включает путь «клиент → релей» — а именно там и лежит основная стоимость.
