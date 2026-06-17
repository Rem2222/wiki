---
description: Web-based серверное администрирование. Установка, reverse proxy через nginx, Authelia SSO, плагины, решение проблем.
tags: [cockpit, admin, monitoring, nginx, sso, authelia]
related: [[tech/authelia]], nginx, docker
---

# Cockpit

**URL:** https://cockpit-project.org  
**License:** LGPLv2.1+  
**Репозиторий:** https://github.com/cockpit-project/cockpit

## Что это

Cockpit — веб-интерфейс для администрирования Linux-сервера. Позволяет управлять: сетью, дисками, хранилищем, пакетами (через PackageKit), контейнерами, мониторингом через браузер. Не требует установки агентов — работает через systemd-сокет.

## Установка

На Ubuntu/Debian обычно предустановлен. Если нет:

```bash
apt install cockpit cockpit-storaged cockpit-networkmanager cockpit-packagekit
```

Запускается через socket activation:

```bash
systemctl enable --now cockpit.socket  # порт 9090
```

## Настройка reverse proxy через nginx + Authelia SSO

### Проблема

Cockpit по умолчанию слушает на `0.0.0.0:9090` с самоподписанным TLS-сертификатом. При попытке проксировать через nginx возникают ошибки TLS-рукопожатия (`gnutls_handshake failed`), т.к. Cockpit-tls не рассчитан на работу за reverse proxy.

### Решение

Отключить TLS в Cockpit и слушать только на localhost:

**1. /etc/cockpit/cockpit.conf**

```ini
[WebService]
Origins = https://rem2222.top https://rem2222.top:443
ProtocolHeader = X-Forwarded-Proto
ForwardedForHeader = X-Forwarded-For
LoginTitle = rem2222.top — Cockpit
```

**2. Systemd override для cockpit.service**

```bash
systemctl edit cockpit.service
```

```ini
[Service]
ExecStart=
ExecStart=/usr/lib/cockpit/cockpit-tls --no-tls --idle-timeout=0
```

**3. Systemd override для cockpit.socket**

```bash
systemctl edit cockpit.socket
```

```ini
[Socket]
ListenStream=
ListenStream=127.0.0.1:9090
```

**4. Nginx location**

```nginx
location /cockpit/ {
    rewrite ^/cockpit(/.*)$ $1 break;
    proxy_pass http://127.0.0.1:9090;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;

    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";

    include /etc/nginx/snippets/authelia-location.conf;
}
```

**5. Authelia** — добавить правило

```yaml
access_control:
  rules:
    - domain: rem2222.top
      policy: one_factor
      resources:
        - '^/cockpit(/.*)?$'
```

### Результат

`https://rem2222.top/cockpit/` → Authelia SSO → Cockpit через валидный HTTPS.

## Плагины

### Установленные

| Плагин | Что даёт | Установка |
|--------|----------|-----------|
| cockpit-storaged | Диски, RAID, NFS, iSCSI | preinstalled |
| cockpit-networkmanager | Сеть + фаервол | preinstalled |
| cockpit-packagekit | Обновления ПО | preinstalled |
| cockpit-navigator | Файловый браузер с деревом папок | `apt install cockpit-navigator` |
| cockpit-benchmark | Тест скорости дисков (fio) | `apt install cockpit-benchmark` |
| cockpit-dockermanager | Управление Docker-контейнерами | вручную с GitHub |

### cockpit-dockermanager

**GitHub:** [chrisjbawden/cockpit-dockermanager](https://github.com/chrisjbawden/cockpit-dockermanager)

Ставится вручную, т.к. нет в apt:

```bash
wget https://github.com/chrisjbawden/cockpit-dockermanager/releases/latest/download/cockpit-dockermanager.deb
dpkg -i cockpit-dockermanager.deb
```

**Возможности:**
- Список запущенных контейнеров
- Start/Stop/Restart
- Просмотр статуса, uptime, портов
- In-window терминал в контейнер
- Управление образами

**Работает с уже запущенными контейнерами** — не создаёт свои, использует Docker API.

### cockpit-tailscale — НЕДОСТУПЕН

Пакета `cockpit-tailscale` нет в apt. Единственный источник — [github.com/gbraad-cockpit/cockpit-tailscale](https://github.com/gbraad-cockpit/cockpit-tailscale) — проект **не обновлялся 3 года**, только RPM для Fedora. Для Ubuntu deb-пакета нет.

## Решение проблем

### "Cannot refresh cache whilst offline" в Software Updates

**Симптом:** Cockpit → Software Updates: «Loading available updates failed — Cannot refresh cache whilst offline».

**Root cause:** NetworkManager в состоянии `disconnected` (CONNECTIVITY=unknown), если сеть настраивается через netplan/systemd-networkd. PackageKit проверяет NetworkManager и отказывается работать, когда NM говорит «офлайн».

**Решение:** Создать NM ethernet-соединение с теми же настройками, что в netplan:

```bash
nmcli connection add type ethernet con-name eth0-nm ifname eth0 \
  ipv4.addresses 81.17.100.103/22 \
  ipv4.gateway 81.17.100.1 \
  ipv4.dns "213.136.95.10 213.136.95.11" \
  ipv4.method manual \
  ipv6.addresses 2a02:c207:2320:5830::1/64 \
  ipv6.gateway fe80::1 \
  ipv6.method manual \
  connection.autoconnect yes
```

**Проверка:**
```bash
nmcli general status        # STATE — connected
pkcon refresh force         # должно работать
pkcon get-updates
systemctl restart packagekit
```

### gnutls_handshake failed / TLS через reverse proxy

**Симптом:** Пустая страница Cockpit через nginx, в логах `gnutls_handshake failed: The TLS connection was non-properly terminated`.

**Root cause:** Cockpit-tls на 0.0.0.0:9090 с самоподписанным сертификатом — при проксировании через nginx TLS-терминация конфликтует.

**Решение:** `--no-tls` + `127.0.0.1:9090` (описано в разделе настройки reverse proxy выше).

