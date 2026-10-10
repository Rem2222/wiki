---
title: "ai-tools-proxy-domains — списки хостов для split-tunnel AI-инструментов"
description: "comol/ai-tools-proxy-domains: доменные списки и маски Proxifier для Cursor/Codex/Claude/Grok/OpenClaw/Hermes без полного VPN. Проверка полноты относительно нашего кода Hermes: точный список покрывает 4 из 17 доменов nousresearch.com. Telegram CIDR сверены с официальными. Записано для дела — не применялось."
tags: [split-tunnel, proxy, Proxifier, firewall, cursor, openai, claude, hermes-domains, telegram-cidr, router]
created: 2026-10-09
source: https://github.com/comol/ai-tools-proxy-domains
related:
  - "[[tech/kun-chen-tdd-eval]]"
---

# ai-tools-proxy-domains

**Переслано от «IT Does Matter» 09.10.2026 14:00** — «забирайте, для
роутера/админов пригодится».
**Статус:** записано для дела, **не применялось** — по правилу Романа новые
внешние списки сначала в вики.

## Что это

`comol/ai-tools-proxy-domains` — **19⭐**, 0 форков, 0 issue, создан
**07.09.2026**, последний пуш **09.10.2026** (в день разбора), лицензия **MIT**
(указано `NOASSERTION` в API, но сам файл LICENSE — MIT, с атрибуцией
Alexander Malyaev за Proxifier-маски). Язык не определён — это не код, а
**списки хостов и конфигов**.

Суть: split-tunnel для AI-инструментов **без полного VPN на всю машину**.
Два варианта на выбор:

1. **Точные домены** — узкий туннель. Меньше побочек, но ломается, если вендор
   завёл новый поддомен
2. **Маски Proxifier** — «лучше перебдеть». Ловит CDN/телеметрию, но `*google*`,
   `*github*`, `*cloudflare*` заворачивают почти всё подряд

## Структура и объёмы (проверено по файлам)

| Файл | Записей | Назначение |
|---|---:|---|
| `hosts/exact-split-tunnel.txt` | 68 | Общий точный список: Anthropic, OpenAI, DeepSeek, Cursor, Grok, OpenClaw/Hermes, Kiro |
| `hosts/cursor-required-domains.txt` | 36 | Required Domains из настроек Cursor + документация |
| `hosts/openai-domains.txt` | 37 | API, ChatGPT, Codex, файлы, CDN, вход |
| `hosts/claude-domains.txt` | 21 | Web/Desktop/Code, обновления, артефакты, MCP |
| `hosts/grok-domains.txt` | 14 | Grok, xAI API, вход, Grok Build |
| `hosts/agent-integrations.txt` | 16 | OpenClaw/Hermes: провайдеры, Nous, каналы |
| `hosts/optional-dependencies.txt` | 17 | Пакеты, плагины, JS-библиотеки, шрифты |
| `networks/telegram-ipv4-cidrs.txt` | 9 | IPv4-подсети Telegram для маршрутизации |
| `proxifier/ai-services-masks.txt` | ~40 масок | Строка Target Hosts для Proxifier |
| `proxifier/rules.md` | — | Порядок правил + брандмауэр |
| `docs/service-domains.md` | 14 КБ | Назначение адресов, лимиты, источники |

## Проверки, которые я прогнал

### 1. Telegram CIDR — совпали полностью ✅

Все **9 IPv4-подсетей** из `networks/telegram-ipv4-cidrs.txt` сверены с
официальным `core.telegram.org/resources/cidr.txt` на 09.10.2026 — **полное
совпадение**: `91.108.4.0/22`, `91.108.8.0/22`, `91.108.12.0/22`,
`91.108.16.0/22`, `91.108.20.0/22`, `91.108.56.0/22`, `91.105.192.0/23`,
`149.154.160.0/20`, `185.76.151.0/24`.

Официальный список содержит ещё 5 IPv6-подсетей — их в файле репо **нет**.
Для IPv4-роутера это не проблема, но для полного туннеля IPv6 уйдёт мимо.

### 2. Ссылки на наш код Hermes — живые ✅

В `agent-integrations.txt` есть ссылки на конкретный коммит нашего репо
(`73162b00...`). Проверила: `hermes_constants.py` и
`tools/managed_tool_gateway.py` на этом коммите — **200**, документация
`hermes-agent.nousresearch.com/docs/integrations/providers` — **200**.
Ссылки не выдуманные.

### 3. DNS — все домены резолвятся ✅

`portal`, `inference-api`, `tool-gateway`, `connector-gateway` (все
`.nousresearch.com`), `api.telegram.org`, `openrouter.ai`, `api.deepseek.com`,
`clawhub.ai` — **все 8 разрешились в IP**.

### 4. **Полнота списка для Hermes — наша главная находка** ⚠️

Точный список `exact-split-tunnel.txt` даёт для нас **только 4 домена**:

```
portal.nousresearch.com
inference-api.nousresearch.com
tool-gateway.nousresearch.com
connector-gateway.nousresearch.com
```

А фактически в нашем коде (`/usr/local/lib/hermes-agent/`) значится **17
доменов `.nousresearch.com`**, и ещё 10 в документации/дизайн-доках:

```
agent.nousresearch.com          gateway.nousresearch.com
agents.nousresearch.com         hermes.nousresearch.com
api.nousresearch.com            hermes-agent.nousresearch.com
firecrawl-gateway.nousresearch.com      inference.nousresearch.com
gateway-gateway.nousresearch.com        telemetry.nousresearch.com
openai-audio-gateway.nousresearch.com   staging.nousresearch.com
stg-inference-api.nousresearch.com      ocs-hermes--agent.nousresearch.com
```

То есть **точный список покрывает 4 из 17 — 24%**. Не хватает
`gateway.nousresearch.com` (сам шлюз), `telemetry.nousresearch.com`,
`api.nousresearch.com`, `hermes-agent.nousresearch.com` и других.

Почему так: автор честно пишет в шапке точного списка — «This compatibility
list is exact-only and **partial**. Use service profiles for dynamic
subdomains». А в `agent-integrations.txt` у него лежит маска
`**.nousresearch.com` (wildcard), которая покрывает всё. То есть для Hermes
надо брать **именно профиль** `agent-integrations.txt`, а не общий точный
список. Если кто-то возьмёт `exact-split-tunnel.txt` как самодостаточный —
половина Hermes полетит.

### 5. `connector-gateway.nousresearch.com` — DNS есть, в коде домена нет

В `agent-integrations.txt` он указан со ссылкой на
`docs/connector-gateway-auth-design.md`. Я проверила: этот документ существует,
но `nousresearch.com` в нём **не упоминается**, и в текущем коде
`connector-gateway.nousresearch.com` тоже **не значится** (значатся лишь
строки «connector-gateway-auth-design» как имя файла). Домен при этом
резолвится (216.150.16.1 — общий IP с `tool-gateway`, похоже на wildcard/CDN
зону). Вывод: домен **правдоподобен, но не подтверждён нашим кодом** — это
вывод автора по аналогии с `tool-gateway`. Для туннеля лишним не будет, но
опираться на него как на обязательный не стоит.

## Схема применения (из `proxifier/rules.md`)

Авторская схема работает **без VPS**, с локальным прокси (`127.0.0.1:8090`):

**Порядок правил Proxifier (сверху вниз):**

1. **Direct:** localhost/127.0.0.1/`%ComputerName%`/`::1`/LAN — чтобы прокси
   не закольцевался; Docker, ADB, AdGuard, системный Node, PowerShell
2. **Proxy chain:** AI Services (маски из `ai-services-masks.txt`) → Cursor →
   ChatGPT/Codex → Google/Antigravity → VS Code → Ollama
3. **Default = Direct**

**Брандмауэр-лок (критически важный шаг):** outbound **block** для
`cursor.exe`, `codex.exe`, `code.exe`, `antigravity.exe` и их `node.exe` —
иначе Proxifier промахнётся, а Default Direct = утечка мимо прокси. Плюс
блокировка публичного DNS по IPv6, если прокси IPv4-only.

**Честно перечисленные дыры («Known holes»):**

- DNS в Proxifier = системный DNS → хостнеймы утекают **до** CONNECT
- Неизвестный хост вендора + Default Direct + нет правила брандмауэра = утечка
- `*windowsupdate*`, `*microsoft.com*`, `*github*`, `*cloudflare*` — заворачивают
  почти всё, «ожидайте сломанного или тормозящего Windows Update, npm и
  случайного HTTPS»

Автор отмечает: **оплата Cursor/Codex через эту схему у него проходит**.

## Чего здесь НЕТ (из README, дословно по смыслу)

- Готового прокси/VPS и чужих ключей
- Исходников rust-анализатора exe (упоминался, в репо не вошёл)
- Скриншотов с чужими путями `%USERNAME%`

И главное — сам автор предупреждает: **«Адреса собирались агентом из открытых
источников — на полноту и точность никто не подписывается»**.

## Что не решается списком доменов (из `docs/service-domains.md`)

- **Потоковые ответы** — нужны WebSocket/SSE без буферизации, Cursor Tab и
  часть API требует HTTP/2
- **Сертификаты** — при TLS-инспекции сверять CA с документацией клиента,
  не отключать проверку
- **IP-адреса** — CDN меняется, предпочтительны доменные правила, а не IP

Итоговый совет автора: после применения проверять отдельно вход, текстовый
запрос, потоковый ответ, загрузку файла, обновления и интеграции. В Cursor
для этого есть **Run Diagnostic**.

## Соответствие нашему контексту

- **Для VPS:** у нас нет прокси-проблемы на уровне AI-инструментов — трафик
  идёт напрямую. Но доменные списки пригодятся, если понадобится вывести
  часть исходящего через конкретный выход (см. нерешённый Ozon-кейс MUL-112 —
  там блок по IP-репутации Hetzner, и список доменов его не обходит, нужен
  именно другой выходящий IP)
- **Для роутера/дома:** это ровно тот случай, ради которого репо и прислали —
  split-tunnel на уровне роутера. Ключевой шаг, который легко забыть:
  **брандмауэр-лок на исходящие**, иначе правила Proxifier не гарантируют ничего
- **Для нашего кода:** `agent-integrations.txt` полезен как чек-лист доменов
  Hermes/Telegram, но его надо читать вместе с wildcard `*.nousresearch.com`,
  а не вместо него
- **IPv6:** если туннель делается, закрывать и IPv6 — в файле CIDR только IPv4

## Решение

**Не применялось.** Списки не нигде не импортировались, прокси и правила
браузмауэра не менялись. Зафиксировано для дела.

Практический вывод для использования: брать **профиль по сервису**
(`agent-integrations.txt` для Hermes), а не общий точный список; сверять
полноту по своему коду (мой пункт 4 выше — наглядный пример, почему);
при применении — не забыть брандмауэр-лок и IPv6.

## Источники

- 🌐 github.com/comol/ai-tools-proxy-domains → README (полный), `hosts/*`,
  `proxifier/rules.md`, `docs/service-domains.md`
- 🌐 GitHub API: 19⭐, создан 07.09.2026, пуш 09.10.2026, MIT
- 🌐 core.telegram.org/resources/cidr.txt — сверка 9 подсетей (совпали)
- 🌐 raw.githubusercontent.com/NousResearch/hermes-agent/73162b00 → 200 по
  `hermes_constants.py` и `tools/managed_tool_gateway.py`
- 📋 /usr/local/lib/hermes-agent/ — grep по `.nousresearch.com`, 17 доменов
- 📋 наша сессия 09.10.2026 — DNS-резолв 8 доменов, подсчёт записей
- 📄 wiki tech/kun-chen-tdd-eval — контекст (раздел E2E/LDD, AXI-инструменты)
