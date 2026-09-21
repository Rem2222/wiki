---
description: Cloudflare Tunnel (cloudflared) — бесплатный способ расшарить localhost через публичный URL за одну команду. Без VPN, без Tailscale.
tags: [networking, cloudflare, tunnel, localhost, sharing, dev-tools]
related:
  - tech/free-llm-api-resources
---

# Cloudflare Tunnel (cloudflared) — шарим localhost бесплатно

## Что это

Бесплатный сервис от Cloudflare, который делает твой `localhost` доступным по публичному URL за одну команду. Не нужен VPN, не нужен Tailscale, не нужен сервер.

## Установка

```bash
# macOS
brew install cloudflare/cloudflare/cloudflared

# Linux
curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared
chmod +x cloudflared
sudo mv cloudflared /usr/local/bin/

# Windows
winget install cloudflare.cloudflared
```

## Использование

```bash
# Запуск туннеля
cloudflared tunnel --url http://localhost:8000

# Результат:
# Your quick Tunnel has been created! Visit it at:
# https://random-name-here.trycloudflare.com
```

Готово. Любой по этому URL видит твой localhost:8000.

## Применение

- **Dev-демонстрации** — быстро показать клиенту/коллеге локальный проект
- **Вебхуки** — принять вебхук от GitHub/Stripe/Telegram на локальный сервер
- **AI-агенты** — дать доступ агенту к локальному приложению
- **Тестирование** — проверить webhook integration без деплоя
- **Remote access** — временный доступ к локальному сервису извне

## Ограничения

- **Временный URL** — меняется при каждом перезапуске
- **Не для продакшена** — latency через Cloudflare, нет SLA
- **Один порт** — только один сервис за раз (но можно несколько туннелей)
- **Бесплатно** — без лимитов на использование

## Когда использовать vs Tailscale

| Сценарий | cloudflared | Tailscale |
|----------|-------------|-----------|
| Быстро показать что-то на 5 минут | ✅ | ❌ (нужна установка на клиенте) |
| Постоянный доступ к серверу | ❌ (временный URL) | ✅ |
| Вебхук от внешнего сервиса | ✅ | ❌ (нужен публичный IP) |
| Безопасность/контроль | ❌ (публичный URL) | ✅ (приватная сеть) |

## Ссылки

- https://try.cloudflare.com — официальная страница
- https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/ — документация
