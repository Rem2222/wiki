---
description: MAX Messenger (VK) plugin for Hermes Agent — интеграция, архитектура, инструкция
tags: [tech, integrations, hermes, max]
related:
  - tech/hermes-agent-masterclass
  - tech/specsmaxxing
  - tech/kanal-svyazi-pri-glushenii
---

# MAX Messenger Plugin for Hermes Agent

**Репозиторий:** https://github.com/Rem2222/hermes-max-plugin
**Локальный путь:** `~/.hermes/plugins/max/`

## Что это

Плагин для полноценной интеграции MAX Messenger (мессенджер на платформе VK) с Hermes Agent — как Telegram.

## Статус проекта

MVP завершён (2026-06-14)

**Проверено 02.11.2026 под Hermes 0.21.6:** плагин грузится штатно — импорт пакета ок,
`register(ctx)` → `register_platform(name="max", required_env=["MAX_TOKEN"],
max_message_length=4096)`, `MaxAdapter` реализует все абстрактные методы базового класса
(`connect`/`disconnect`/`get_chat_info`/`send`), host-API `_event_session_key` и
`MessageEvent.allow_gateway_control` на месте. Зависимости в venv есть (`aiohttp 3.14.3`,
`python-multipart 0.0.32`).

**Чего ждём:** `MAX_TOKEN`. Плагин включает себя сам через `_env_enablement()`, как только
токен появится в `.env` — правка `config.yaml` не нужна. Барьер: бота MAX дают только
юрлицам/ИП/самозанятым (подробный разбор и обходные пути —
[[tech/kanal-svyazi-pri-glushenii]]).

## Архитектура

Plugin Path — плагин в `~/.hermes/plugins/max/` без форка ядра Hermes.

8 файлов: adapter.py, inbound.py, outbound.py, keyboard.py, upload.py, types.py, __init__.py, plugin.yaml

## Функции MVP

- Текст — входящие/исходящие, авто-сплит при >4096 символов
- Изображения — отправка и получение
- Typing indicator
- Inline-клавиатура (clarify, approval, model picker)
- Access control — allowlist + self-message filter
- Webhook (prod) / Long Polling (dev)
- Cron-доставка
- Rate limiter 30 rps

## Подключение

1. Создать бота через @BotFather в MAX Messenger
2. Добавить MAX_TOKEN в .env Hermes
3. hermes plugins enable max-platform
4. Перезапустить сессию Hermes
5. Написать боту «Привет»

## MAX Bot API

Базовый URL: https://platform-api.max.ru
Авторизация: Authorization: <token>
Rate limit: 30 rps, HTTPS обязательно с 25 мая 2026
Лимит текста: 4096 символов

## Технические нюансы

- Upload token баг SDK — raw multipart upload обход
- Bot chats = группы (isGroup: true)
- GET /chats deprecated с июня 2026
- Файлы >10MB таймаутят (20s timeout)

## Проект в Multica

MUL-226 Research, MUL-227 Init, MUL-228 Plan, MUL-229 SPEC, MUL-233 MVP Impl, MUL-234 Verify, MUL-235 Code Review, MUL-231 Deliver — все done. MUL-238 инструкция todo.
