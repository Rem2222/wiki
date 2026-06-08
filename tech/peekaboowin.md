---
description: Windows-first desktop automation sidecar (port of macOS Peekaboo by steipete).
tags: [tech]
related: [[tech/cloakbrowser]] [[concepts/mcp]]
---

# peekaboowin

**URL:** https://github.com/FelixKruger/PeekabooWin

Windows-first desktop automation sidecar (port of macOS Peekaboo by steipete).

## Overview

Даёт AI-агентам возможность "видеть" экран и управлять Windows-приложениями:
- Захват окон и экрана
- OCR видимого текста
- Клики и скролл по меткам
- Управление окнами
- MCP-сервер для AI IDE (Claude Code, Codex, etc.)

## Tech Stack

- **Language:** JavaScript / Node 22+
- **License:** MIT
- **Stars:** 11
- **Last push:** 2026-04-28

## Installation

```bash
## Clone
git clone https://github.com/FelixKruger/PeekabooWin.git
cd PeekabooWin

## Install
npm install

## Test
npm test

## Run MCP server for AI tools
npm run mcp
```

## Architecture

- **GUI sidecar** — для нетехнических пользователей
- **Local CLI** — direct control и workflows
- **MCP server** — AI tools могут управлять десктопом

## Related

- [Peekaboo (macOS)](https://github.com/steipete/Peekaboo) — оригинальный macOS проект
- [Peekaboo site](https://peekaboo.boo)
## See also
- [[tech/cloakbrowser]] — stealth Chromium с антифingerprint
