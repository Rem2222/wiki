---
description: "Нативный MCP-сервер read-only для семантического поиска по вики Rem через Zvec (гибрид bge-m3 + FTS, stdio, без OpenAI-ключа). Единая точка read поверх markdown-вики."
tags: [zvec,mcp,wiki,vector-db,hermes]
related: [[tech/zvec]] [[tools/wiki-search-current-state]]
---

# Zvec MCP — нативный поиск по вики для Hermes

## Что это

Нативный MCP-сервер для семантического поиска по вики Rem через Zvec. Делает то же,
что CLI `zvec-wiki`, но как MCP-инструмент: агент Hermes видит `zvec_wiki_search`
в списке своих инструментов, а не вызывает из shell.

## Архитектура

```
Hermes agent
   │  MCP stdio → /usr/local/bin/zvec-mcp → zvec_mcp_server.py (FastMCP)
   │       └─ zvec_wiki_search(query, topk, page_only)
   │            └─ /root/.zvec-wiki/index (гибрид bge-m3 + FTS, RRF)
```

- Транспорт: **stdio** (зарегистрирован `hermes mcp add zvec`).
- Эмбеддинги: **bge-m3 через Ollama** (:11434) — без OpenAI-ключа.
- Индекс: `/root/.zvec-wiki/index` — 1265+ документов.
- Только **read-only** поиск: вики остаётся источником правды (markdown-файлы),
  zvec — проекция (поисковый индекс).

## Инструмент

`zvec_wiki_search(query, topk=10, page_only=False)` → JSON `[{page, category, title, score, snippet}]`.

- Гибрид: вектор (bge-m3) + FTS, ранжирование RRF.
- `page_only` — дедуп по странице.

## Почему свой, а не официальный

Официальный `zvec-ai/zvec-mcp-server` (⭐7) требует OpenAI-ключа для embedding
и заточен на полный CRUD коллекций. Нам нужен read-only поиск по готовому индексу
bge-m3 из Ollama — поэтому сделали свой лёгкий FastMCP-сервер.

## Связанное

- Единый writer-скрипт `wiki-write` (/usr/local/bin/wiki-write) — запись страниц
  с валидным frontmatter + git + auto-rebuild индекса.
- Задача MUL-891.
