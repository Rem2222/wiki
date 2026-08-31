---
description: "ChatGPT Web для Codex — использовать ChatGPT Web (включая Pro) как нативные модели Codex"
tags: [tools, codex, chatgpt, ai, coding]
source: https://github.com/miuuyy/codex-chatgpt-web
stars: 2900
---

# codex-chatgpt-web

Использовать ChatGPT Web (включая Pro) как нативные модели Codex.

## Что это

Бесплатные и Go-аккаунты получают ChatGPT Web (Luna) в нативном выборе моделей Codex. Аккаунты с reasoning selector получают Instant, Medium, High, Extra High и Pro в зависимости от подписки.

## Как работает

```
Codex task ──Responses + SSE──▶ codex-chatgpt-web ──embedded browser──▶ ChatGPT
     ▲                                │                                      │
     └──────── native UI, context, images, tracing, and tool lifecycle ──────┘
```

Codex сохраняет нативный task, context lifecycle, UI и tool harness. Локальный Responses bridge направляет только выбранную модель в task-bound ChatGPT Temporary Chat; в полном режиме MCP подключает ChatGPT обратно к инструментам того же Codex task до следующей compaction boundary.

## Возможности

- **Free/Go аккаунты**: ChatGPT Web (Luna) как нативная модель в Codex
- **Pro аккаунты**: все tier'ы (Instant → Pro)
- **Reasoning selector**: если аккаунт поддерживает
- **Images**: встраивание изображений в запросы
- **MCP обратная связь**: ChatGPT может использовать инструменты Codex
- **Нативный UI**: Codex UI остаётся прежним, меняется только бэкенд

## Установка

```bash
git clone https://github.com/miuuyy/codex-chatgpt-web.git
cd codex-chatgpt-web
bun install  # или npm install
```

## Структура проекта

- `src/` — основной код bridge
- `launcher/` — лаунчер
- `scripts/` — скрипты
- `docs/` — документация
- `tests/` — тесты

## Лицензия

MIT

## Связанные проекты

Автор также создал ChatGPT Persona Voice — локальное приложение для изменения голоса ChatGPT/Codex в реальном времени.
