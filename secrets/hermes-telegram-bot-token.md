---
type: concept
title: Hermes Telegram Bot Token
description: Telegram Bot Token for Hermes Gateway Telegram integration
ingested_via: 'mcp:put_page'
ingested_at: '2026-06-14T21:46:35.039Z'
source_kind: 'mcp:put_page'
tags:
  - bot
  - hermes
  - secrets
  - telegram
---

# Telegram Bot Token

**Назначение:** Используется Hermes Gateway для подключения к Telegram Bot API.

**Расположение:** `/root/.hermes/.env`, переменная `TELEGRAM_BOT_TOKEN`

**Формат:** `8600383341:AAFE..._r56iw` (46 символов, стандартный Bot API token)

**Chat ID:** `386235337` (Rem)

**Используется в:**
- Hermes Gateway (telegram platform)
- check-ntfy.sh — fallback-канал при недоступности ntfy сервера
- /opt/multica/inbox-bridge/ — Multica Inbox → Telegram Bridge

**Добавлено:** 14 июня 2026
