---
description: Lightweight orchestration platform built for the agentic AI era. Kanban-доска для AI-агентов.
tags: [project]
---

# veritas-kanban

**URL:** https://github.com/BradGroux/veritas-kanban

## Описание

Lightweight orchestration platform built for the agentic AI era. Kanban-доска для AI-агентов.

## Стек

- **Frontend:** React/Vite
- **Backend:** Express
- **Real-time:** WebSockets
- **Storage:** Markdown + YAML frontmatter (без базы данных)
- **API:** REST

## Ключевые фичи

1. **AI Agent Orchestration** — агенты создают задачи, трекают время, обновляют статус через REST API
2. **Git Worktree Integration** — каждая задача получает свой git worktree
3. **No Database** — задачи хранятся как human-readable Markdown файлы
4. **Real-time updates** — WebSockets

## Для чего интересен

- Референс реализации Kanban-доски для AI-агентов
- Подход с Git worktree per task — интересная идея
- Альтернатива собственному Dashboard (OpenClaw Dashboard)
- Интеграция с MCP Registry — может подключаться к OpenClaw

## Статистика

- GitHub Stars: 576
- License: MIT

## Альтернатива

- OpenClaw Dashboard — кастомная доска с Kanban, Sessions, Subagents, Cron
- Superpowers framework — workflow для AI-агентов

## Tags

#ai-agents #kanban #orchestration #open-source