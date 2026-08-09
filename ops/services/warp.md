---
description: Cloudflare WARP — VPN-клиент, ставился для обхода обрывов "incomplete chunked read" при доступе к opencode.ai. Сейчас не используется (ALL_PROXY закомментирован).
tags:
  - ops
  - service
  - network
type: service
related:
  - ops/services/tor
  - ops/services/tailscale
  - tech/free-llm-api-resources
service:
  name: warp
  category: network
  purpose: Cloudflare WARP VPN (обход обрывов chunked read у opencode.ai)
  install_date: 2026-06-03
  last_verified: 2026-08-10
  health_url: 
  type: systemd
  ports:
    -
      port: 40000
      protocol: tcp
      bind: 127.0.0.1
      description: warp-svc (SOCKS5/HTTP прокси, режим WarpProxy)
  systemd_units:
    - warp-svc
  depends_on:
    []
  notes: >
    Установлен 3 июня 2026 (apt-get install -y cloudflare-warp) из-за проблемы с opencode.ai.
    Есть systemd таймер warp-health (каждые 5 мин проверяет прокси). С 2 августа 2026
    ALL_PROXY в ~/.hermes/.env закомментирован — прокси никто не использует. Можно удалить.
---

# Cloudflare WARP — зачем ставился и почему больше не нужен

## Проблема, которую решал WARP

**Симптом:** при обращении к **opencode.ai** (API-провайдер моделей, `https://opencode.ai/zen/go/v1`) из Hermes/gateway периодически падали запросы с ошибкой **"incomplete chunked read"** — обрывы на Cloudflare-protected origin.

**Причина (записана в `~/.hermes/.env`, секция «CLOUDFLARE WARP PROXY»):**
> route traffic through Cloudflare internal backbone to avoid "incomplete chunked read" drops on Cloudflare-protected origins (opencode.ai). SOCKS5 proxy provided by warp-svc.

## Решение

1. Установлен `cloudflare-warp` (dpkg log: 2026-06-03 10:45).
2. Включён режим **WarpProxy** на порту **40000** (SOCKS5/HTTP-прокси).
3. В `~/.hermes/.env` прописан `ALL_PROXY=socks5://127.0.0.1:40000` (+ `NO_PROXY` для локалки).
4. 3 июля добавлен `warp-health.sh` + systemd-timer: каждые 5 минут проверяет, что прокси на 40000 отвечает; если нет — перерегистрирует WARP и подключает заново (логи: `/root/.hermes/logs/warp-health.log`).

## Текущее состояние (2026-08-05)

- **Прокси больше не используется:** `#ALL_PROXY=socks5://127.0.0.1:40000` закомментирован в `.env` с 2 августа 2026 — ни Hermes, ни gateway через WARP не ходят.
- **Прямое подключение к opencode.ai работает:** `direct: 200 за ~0.43s`, через warp: `200 за ~0.43s` — разницы нет, обрывов нет.
- Порт 40000 никто не слушает из приложений (`ss` пусто), только сам warp-svc.
- WARP держит ~650 МБ RAM (пик 925 МБ) — просто «на всякий случай».

## Вывод

WARP больше не нужен. Если проблема «incomplete chunked read» у opencode.ai вернётся — решение задокументировано здесь, включается обратно:
```bash
# включить прокси в .env (раскомментировать ALL_PROXY), затем:
systemctl enable --now warp-svc warp-health.timer
```
Для удаления:
```bash
systemctl disable --now warp-svc warp-health.timer warp-health.service
apt remove -y cloudflare-warp
```
