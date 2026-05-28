---
description: Универсальный поисковый плагин для Claude Code от автора статьи на Habr
tags: [claude-code, search, mcp, plugin]
related: [[tech/context7]] [[tech/z-ai]]
---

# cc-websearch

**GitHub:** https://github.com/Djarvur/cc-websearch

Поисковый плагин (skill) для Claude Code, написанный автором статьи как альтернатива существующим решениям. Поддерживает multiple search backends.

## Фишка

Один плагин, который умеет работать с разными поисковыми API — Google, Bing, SerpAPI, Tavily — без смены инструмента.

## Возможности

- **Multi-engine:** Google Custom Search, Bing, SerpAPI, Tavily
- **Configurable defaults:** выбор движка через `CC_SEARCH_ENGINE`, количество результатов через `CC_SEARCH_TOP_K`
- **LLM-friendly:** результаты форматируются с заголовками, сниппетами и URL
- **Async & rate-limited:** не блокирует агента

## Установка

```bash
claude plugin marketplace add Djarvur/cc-mplace
claude plugin install cc-websearch
```

## Зачем

Если стандартный websearch в Claude Code выключен (например, при использовании не-Anthropic провайдеров), cc-websearch — готовая замена с выбором бэкенда.

## Нужно ли

✅ **Да, если:** используешь Claude Code с не-Anthropic моделями (OpenCode Go, DeepSeek и т.п.) — у них нет встроенного поиска.
❌ **Нет, если:** у тебя Anthropic Claude с активным websearch или используешь Z.AI с поисковым MCP.
