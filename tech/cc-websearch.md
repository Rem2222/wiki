---
description: Плагин WebSearch + WebFetch для Claude Code на DuckDuckGo (без API-ключей)
tags: [claude-code, search, plugin, duckduckgo, webfetch]
related: [[tech/context7]] [[tech/z-ai]]
---

# cc-websearch

**GitHub:** https://github.com/Djarvur/cc-websearch

Плагин для Claude Code, заменяющий встроенный WebSearch и WebFetch. Работает через DuckDuckGo — **без API-ключей, бесплатно**.

## Как работает

**WebSearch** — поиск через `lite.duckduckgo.com`, парсинг HTML-ответа, вывод XML `<search_results>` (как встроенный Claude).

**WebFetch** — HTTP-запрос → Mozilla Readability (выделение контента, тот же движок во Firefox Reader View) → Turndown (Markdown). Без LLM в пайплайне.

```bash
## Поиск
echo '{"query":"latest ECMAScript specification"}' | node "skills/websearch/scripts/websearch.cjs"

## Чтение страницы
echo '{"url":"https://example.com","prompt":"Summarize"}' | node "skills/webfetch/scripts/webfetch.cjs"
```

## Фишки

- **DuckDuckGo** — API-ключ не нужен, безлимитно
- **Домен-фильтры:** `allowed_domains`, `blocked_domains`
- **Retry:** 4 попытки с exponential backoff, таймаут 30s
- **Config:** `~/.config/websearch/config.json` + env-переменные

## Сравнение

| | cc-websearch | Z.AI | Anthropic built-in |
|---|---|---|---|
| API-ключ | Не нужен | Нужен (free 1000/мес) | Только Anthropic |
| Провайдер | DuckDuckGo | Z.AI MCP | Сервера Anthropic |
| WebFetch | Да | Нет | Встроенный |
| Установка | `claude plugin add Djarvur/cc-mplace` | `uvx @z-ai/mcp` | Из коробки |

## Установка

```bash
claude plugin marketplace add Djarvur/cc-mplace && \
claude plugin install cc-websearch
```

Или локально:
```bash
git clone https://github.com/Djarvur/cc-websearch.git && cd cc-websearch
claude --plugin-dir .
```

## Нужно ли

**Да, если** используешь Claude Code с не-Anthropic провайдерами (OpenCode Go, DeepSeek и т.п.).
**Нет, если** у тебя Anthropic со встроенным поиском или Z.AI MCP.
