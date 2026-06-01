---
description: CLI Printing Press — генератор CLI/MCP-серверов для любых API, оптимизированных для AI-агентов
tags: [cli, mcp, api, ai-agents, go, generator]
related: [[tech/hermes-mcp-setup]] [[tech/context7]] [[tech/gsd]]
---

# CLI Printing Press

**GitHub:** https://github.com/mvanhorn/cli-printing-press
**Лицензия:** MIT
**Звёзды:** 2641+
**Язык:** Go
**Автор:** mvanhorn

**CLI Printing Press** — генератор, который читает документацию любого API (или сниффает сайт без API), изучает существующие CLI/MCP-серверы конкурентов и печатает три артефакта:

1. **Go CLI бинарник** — токен-эффективный, с SQLite кэшем, составными командами
2. **MCP сервер** — для вызова агентами (Hermes, Claude Code и др.)
3. **Claude Code skill** — команды вида `/printing-press <app-name>`

## Фишка

Генерирует CLI, который отвечает на вопросы, на которые оригинальный API **не может ответить одним запросом**. Использует локальный SQLite для сложных джойнов и агрегаций.

## Каталог

Уже напечатано **209 CLI в 17 категориях** — каталог на https://printingpress.dev

| CLI | Источник | Пример запроса |
|-----|----------|----------------|
| `espn-pp-cli` | ESPN (снифф, без API) | «Ночные матчи NBA со счётом, скорерами, травмами» |
| `flight-goat` | Kayak + Google Flights | «Рейсы из Сиэтла на 4-х, 24.12-1.1, дешёвые» |
| `linear-pp-cli` | Linear API (SQLite mirror) | «Заблокированные issue, чей блокер завис на неделю» |
| `sentry-pp-cli` | Sentry | «Новые ошибки в релизе с растущей частотой» |

## Установка

```bash
curl -fsSL https://raw.githubusercontent.com/mvanhorn/cli-printing-press/main/scripts/install.sh | bash
```

Требует: Go 1.26.3+, Node/npm.

## Использование

```bash
# Напечатать CLI для API по имени
/printing-press Notion

# По URL (даже без OpenAPI specs)
/printing-press https://postman.com/explore

# Перепечатать существующий
/printing-press-reprint notion
```

Каждый запуск производит:
- `<api>-pp-cli` — Go бинарник
- `<api>-pp-mcp` — MCP сервер
- Research-документы
- Verification proofs
- Quality Score

## Совместимость с Hermes

Из трёх артефактов Hermes напрямую использует **MCP сервер**. Claude Code skill не подходит (Hermes не Claude Code), но MCP-сервер подключается через `mcp_servers` в `config.yaml`.

**Нюанс:** сам генератор завязан на Claude Code (основной рантайм). Для генерации под Hermes нужно либо:
- Использовать Codex-режим (`/printing-press HubSpot codex`)
- Либо запускать генерацию в Claude Code, а MCP-сервер потом подключать к Hermes

## Ссылки

- [[tech/hermes-mcp-setup]] — настройка MCP серверов в Hermes
- [[tech/context7]] — MCP сервер документации
- [[tech/gsd]] — спецификация задач для разработки
