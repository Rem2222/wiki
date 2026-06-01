---
description: Визуализация графа знаний для MemPalace — D3.js force-directed graph с семантической кластеризацией, MCP интеграцией и Cloudflare zero-trust хостингом
tags: [mempalace, vizualization, d3js, mcp, knowledge-graph]
related: [[concepts/mcp]]
source: https://github.com/JoeDoesJits/mempalace-viz
author: Joe Guarino / G5 Labs
license: MIT
created: 2026-05-27
updated: 2026-05-27
---

# MemPalaceViz

**Walk the halls of your AI's memory.** Хрустальный дворец-визуализация для [MemPalace](https://mempalaceofficial.com) — каждый ящик это воспоминание, каждая комната это тема, каждое крыло это проект.

Репозиторий: [github.com/JoeDoesJits/mempalace-viz](https://github.com/JoeDoesJits/mempalace-viz)

## Стек

- **Граф:** D3.js v7 (force simulation)
- **Рендеринг:** SVG nodes + Canvas particles
- **Кластеризация:** TF-IDF + k-means++ на клиенте
- **Данные:** MCP Streamable HTTP протокол ([[concepts/mcp]])
- **Хостинг:** Cloudflare Pages (free tier), CF Access + Tunnel
- **Сборка:** ноль — единый HTML-файл, всё inline

## Возможности

- Force-directed граф с сотнями узлов знаний
- Интеграция с MemPalace v3.3.x: `list_drawers`, `get_drawer`, `update_drawer`, `delete_drawer`, `add_drawer`, `find_tunnels`
- 5 режимов раскраски: Room, Recency, Size, Decay, Semantic Topics
- 3 режима раскладки: Explode, Orbit, Cluster
- Crystal Palace светлая тема с sparkle-частицами
- Fuzzy multi-token поиск с фильтром по датам
- Структурный анализ — Palace Health Score (0-100)
- Таймлайн-слайдер с play/pause
- Командная палитра (Ctrl+K, 20+ команд)
- Полная клавиатурная навигация
- Mobile responsive с touch-жестами
- Экспорт в PNG и JSON

## Подключение

Три режима подключения к MemPalace:
- **Local Server** — через `mcp-proxy` на `localhost:8000`
- **Hosted** — удалённый сервер с bearer token
- **Demo** — встроенный демо-набор (42 ящика, 8 комнат)

## Развёртывание

Полностью бесплатный secure хостинг через Cloudflare (Pages + Access + Tunnel) — см. [docs/DEPLOYMENT.md](https://github.com/JoeDoesJits/mempalace-viz/blob/main/docs/DEPLOYMENT.md).

## Статус

- Версия: **v1.5.0** (2026-05-25)
- Коммитов: 25
- Звёзд: ⭐ 8
- Форков: 🍴 4
- Лицензия: MIT
