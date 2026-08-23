---
description: "Плагин OpenCode, шлёт ntfy-уведомления о событиях (permission/complete/error/question)."
tags: [opencode,ntfy,plugin,notifications]
related: [[tech/opencode]] [[ops/services/ntfy]]
---

# opencode-notifier-ntfy

**opencode-notifier-ntfy** — плагин для [opencode]([[tech/opencode]]), шлёт [ntfy]([[ops/services/ntfy]])-уведомления при событиях. MIT, TypeScript.

## Возможности

Уведомляет о 5 событиях (каждое настраивается):
- `permission` — когда сессии нужен апрув
- `complete` — завершение главной сессии
- `subagent_complete` — завершение субагента (по умолчанию выкл.)
- `error` — ошибка сессии
- `question` — вопрос из question-tool

Работает с любым ntfy-сервером (публичным или self-hosted).

## Установка

В `opencode.json` / `opencode.jsonc`:

```json
{ "plugin": ["@ongyishen/opencode-notifier-ntfy@latest"] }
```

Перезапустить OpenCode. Pinning версии — указать `@1.0.x`. Кэш плагинов: `~/.cache/opencode`, после апдейта версии чистить (`rm -rf ~/.cache/opencode/node_modules/@ongyishen/opencode-notifier-ntfy`).

## Настройка

Конфиг `~/.config/opencode/opencode-notifier-ntfy.json`:
- `ntfy`: `url` (по умолч. `https://ntfy.sh`), `topic`, `priority` (min/low/default/high/max), `tags`
- `events`: per-event on/off
- `messages`: текст для каждого события
- `command`: выполнить кастомную команду при событии, токены `{event}`/`{message}`, `minDuration` (сек) — гейт по времени с последнего промпта

## Заметки
- Плагин автоматически ставит теги/приоритеты по типу события.
- Обновление вручную (нет авто-апдейта): чистить кэш плагина.

## Репо
`ongyishen/opencode-notifier-ntfy` · 2★ · MIT · updated 2026-05
