---
description: MCP-сервер документации библиотек и фреймворков для AI-агентов (проект Upstash)
tags: [mcp, documentation, claude-code, libraries, cursor, opencode]
related: [[tech/cc-websearch]] [[concepts/mcp]]
---

# Context7

**Сайт:** https://context7.com/
**Создан:** Upstash

MCP-сервис, дающий AI-агентам доступ к **актуальной документации** библиотек и фреймворков. Решает проблему галлюцинаций API.

## Как работает

1. `npx ctx7 setup` — установка одной командой для любого агента
2. Агент получает тул `search_documentation`
3. На запрос о библиотеке → Context7 → реальная документация с цитатами

## Поддерживаемые агенты

Claude Code, Cursor, OpenCode, Codex, Antigravity, VS Code, Windsurf, Gemini CLI, Trae, и 20+

## Возможности

- **200+ библиотек** — React, FastAPI, Go stdlib, Python, Stripe, LangChain
- **Всегда актуальная документация** — не из тренировочных данных
- **Skills (NEW):** `npx ctx7 skills install <owner/repo>` — доку конкретного репозитория
- **Add Docs:** своя документация (включая приватные репозитории)

## Установка

```bash
npx ctx7 setup
```

Либо через плагин Claude Code:
```bash
claude plugin install @context7/mcp
```

## Цены

| Тариф | Цена | API calls | Репозитории |
|-------|------|-----------|-------------|
| Free | $0 | 1,000/мес | Public only |
| Pro | $10/seat/мес | 5,000/seat + $10/1,000 | Private |
| Enterprise | Custom | Custom | SOC-2, SSO, Self-Hosted |

На Free после лимита — блок (20 bonus calls/день). Pro — никогда не блокирует.

## Нужно ли

**Однозначно да.** Must-have. Без Context7 модель гадает API — с ним получает актуальную доку.
