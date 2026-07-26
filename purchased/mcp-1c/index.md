---
type: purchased
title: MCP-серверы для 1С (OneRPA)
description: Набор Docker-контейнеров MCP для работы ИИ-ассистентов с платформой 1С — поиск по справке, метаданным, коду, БСП, проверка синтаксиса, шаблоны
tags: [1c, mcp, purchased, cursor, bsl, docker]
related:
  - purchased/mcp-1c/help-search
  - purchased/mcp-1c/code-metadata-search
  - purchased/mcp-1c/graph-metadata-search
  - purchased/mcp-1c/ssl-search
  - purchased/mcp-1c/syntax-check
  - purchased/mcp-1c/templates-search
  - purchased/mcp-1c/1c-code-checker
source: https://docs.onerpa.ru/mcp-servery-1c
vendor: OneRPA
license: Куплено
ingested_at: '2026-07-23'
---

# MCP-серверы для 1С

**OneRPA MCP Server** — набор Docker-контейнеров, реализующих Model Context Protocol для платформы 1С. Позволяет ИИ-ассистентам (Cursor, Claude Code, Hermes) понимать код 1С, метаданные, справку, бизнес-логику и конфигурации.

## Состав

| Сервер | Порт | Назначение | Нужны данные |
|---|---|---|---|
| [HelpSearchServer](purchased/mcp-1c/help-search) | 8003 | Поиск по справке платформы 1С | Да (папка bin) |
| [CodeMetadataSearchServer](purchased/mcp-1c/code-metadata-search) | 8000 | Поиск по метаданным и коду конфигурации | Да (выгрузка) |
| [Graph Metadata Search](purchased/mcp-1c/graph-metadata-search) | 8006 | Графовый поиск связей метаданных | Да (выгрузка) |
| [SSLSearchServer](purchased/mcp-1c/ssl-search) | 8008 | Поиск по БСП (Библиотека стандартных подсистем) | Нет |
| [SyntaxCheckServer](purchased/mcp-1c/syntax-check) | 8002 | Проверка синтаксиса BSL | Нет |
| [TemplatesSearchServer](purchased/mcp-1c/templates-search) | 8004 | Шаблоны кода 1С | Нет |
| [1CCodeChecker](purchased/mcp-1c/1c-code-checker) | 8007 | Проверка через 1С:Напарник | Нет (нужен токен) |

## Системные требования

- Docker Desktop
- 8+ GB RAM (рекомендуется 16+)
- Для embedding моделей: NVIDIA GPU (рекомендуется) или CPU

## Embedding модели

| Вариант | Когда использовать |
|---|---|
| **LM Studio + Qwen** | ✅ Есть GPU NVIDIA — лучшее качество и скорость |
| **CPU режим** | Нет GPU — работает везде, но медленнее |

⚠️ При использовании CPU-моделей требуется скачивание с huggingface.co (может быть заблокирован). Рекомендуется LM Studio.

## Порядок установки

### Быстрый старт (без подготовки данных)
Серверы, не требующие данных: SyntaxCheckServer, TemplatesSearchServer, SSLSearchServer

```bash
docker run -d --name 1c-syntax-checker-mcp -p 8002:8000 onerpa/syntax-check-server
```

### Полная настройка
1. Установить Docker Desktop
2. Запустить базовые серверы
3. Подготовить данные для CodeMetadataSearchServer и HelpSearchServer
4. Настроить Cursor через mcp.json

## Интеграция с Cursor

Создать `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "1c-syntax-checker-mcp": {
      "url": "http://localhost:8002/mcp",
      "connection_id": "1c_lsp_service_001"
    }
  }
}
```

## Важно

⚠️ **Монтировать volumes для сохранения индексов!** Индексация может занимать от нескольких часов до суток. Без монтирования томов все индексы будут потеряны при перезапуске контейнера.

## Ссылки

- [Документация OneRPA MCP Server](https://docs.onerpa.ru/mcp-servery-1c)
- [Видеокурс по вайбкодингу](https://docs.onerpa.ru/mcp-servery-1c#videomaterialy)
- [Cursor Rules для 1С](https://docs.onerpa.ru/mcp-servery-1c#cursor-rules-dlya-1s)

## Детальные страницы

- [HelpSearchServer](purchased/mcp-1c/help-search)
- [CodeMetadataSearchServer](purchased/mcp-1c/code-metadata-search)
- [Graph Metadata Search](purchased/mcp-1c/graph-metadata-search)
- [SSLSearchServer](purchased/mcp-1c/ssl-search)
- [SyntaxCheckServer](purchased/mcp-1c/syntax-check)
- [TemplatesSearchServer](purchased/mcp-1c/templates-search)
- [1CCodeChecker](purchased/mcp-1c/1c-code-checker)
