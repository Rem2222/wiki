---
description: MAX Messenger (VK) plugin for Hermes Agent — интеграция, архитектура, инструкция
tags: [tech, integrations, hermes, max]
related: [[tech/hermes-agent-masterclass]] [[tech/specsmaxxing]]
---

# MAX Messenger Plugin for Hermes Agent

**Репозиторий:** https://github.com/Rem2222/hermes-max-plugin
**Локальный путь:** `~/.hermes/plugins/max/`

## Что это

Плагин для полноценной интеграции **MAX Messenger** (мессенджер на платформе VK) с **Hermes Agent** — как Telegram.

## Статус проекта

**MVP завершён ✅** (2026-06-14)

## Архитектура

**Plugin Path** — плагин в `~/.hermes/plugins/max/` без форка ядра Hermes.

```
~/.hermes/plugins/max/
├── plugin.yaml        # Метаданные, хуки, env vars
├── adapter.py         # MaxAdapter(BasePlatformAdapter) + register()
├── inbound.py         # Webhook/LL парсинг, self-message filter, allowlist
├── outbound.py        # Отправка текста/изображений, авто-сплит 4096, typing
├── keyboard.py        # Inline-клавиатуры (clarify, approval, model picker)
├── upload.py          # Raw multipart upload (обход бага MAX SDK)
├── types.py           # Pydantic-модели MAX Bot API
├── __init__.py        # Экспорт register()
├── AGENTS.md          # Инструкции для AI-агентов
└── README.md          # Документация
```

## Функции (MVP)

- **Текст** — входящие/исходящие, авто-сплит при >4096 символов
- **Изображения** — отправка и получение
- **Typing indicator** — «печатает» во время обработки
- **Inline-клавиатура** — кнопки для /clarify, /approve, выбора модели
- **Access control** — allowlist + self-message filter
- **Webhook (prod) / Long Polling (dev)**
- **Cron-доставка** — отчёты в MAX home-канал
- **Rate limiter** — 30 rps

## MAX Bot API сводка

| Параметр | Значение |
|----------|---------|
| Базовый URL | `https://platform-api.max.ru` |
| Авторизация | `Authorization: <token>` |
| Rate limit | 30 rps |
| HTTPS | обязательно с 25 мая 2026 |
| Лимит текста | 4096 символов |
| Кнопки | до 210, 30 рядов, 6 типов |
| Webhook | рекомендуется для production |

## Подключение

1. Создать бота через @BotFather в MAX Messenger
2. Добавить `MAX_TOKEN` в `.env` Hermes
3. `hermes plugins enable max-platform`
4. Перезапустить сессию Hermes
5. Написать боту «Привет»

## Проект в Multica

| Задача | Статус |
|--------|--------|
| MUL-226 — Исследование | done |
| MUL-227 — Инициализация | done |
| MUL-228 — Plan | done |
| MUL-229 — SPEC.md | done |
| MUL-233 — MVP Implementation | done (8 файлов, 28/28 тестов) |
| MUL-234 — Verify | done |
| MUL-235 — Code Review | done (3 BLOCKERa -> fix) |
| MUL-231 — Deliver | done |
| MUL-238 — Инструкция по подключению | todo |

## Технические нюансы
- **Upload token баг SDK:** MAX SDK теряет upload token при загрузке Buffer — raw multipart upload
- **Bot chats = группы:** MAX трактует чаты с ботами как `isGroup: true`
- **GET /chats deprecated** с июня 2026 — использовать `POST /subscriptions`
- **Файлы >10MB:** могут таймаутить (20s timeout в SDK)
