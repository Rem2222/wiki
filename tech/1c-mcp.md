---
title: "1С MCP Серверы"
description: | № | Сервер | Порт | Что делает |
tags: [1С, MCP, AI, Claude Code]
related: [[1c-mcp]], [[cursor-rules-1c]], [[v8std-mcp]]
---

# 1С MCP Серверы

## Готовые MCP серверы (vibecoding1c.ru)

| № | Сервер | Порт | Что делает |
|---|--------|------|------------|
| 1 | HelpSearchServer | 8003 | Поиск по справке платформы 1С (RAG) |
| 2 | Graph Metadata Search | 8006 | Граф связей метаданных |
| 3 | CodeMetadataSearchServer | 8000 | Поиск по коду и метаданным |
| 4 | SSLSearchServer | 8008 | Поиск по БСП |
| 5 | SyntaxCheckServer | 8002 | Проверка синтаксиса BSL |
| 6 | TemplatesSearchServer | 8004 | Шаблоны кода + память |
| 7 | 1CCodeChecker | 8007 | Глубокое ревью через 1С:Напарник |
| 8 | FormsServer | 8011 | Генерация форм 1С |

**Все в Docker** — `docker run` и работает.

## Коллекция Untru/1c-mcp

**GitHub:** github.com/Untru/1c-mcp

### Метаданные и анализ
- `1c-mcp` (EDT plugin) — навигация, анализ кода
- `mcp-1c-metadata` — REST API для метаданных
- `1c-mcp-graph` — Neo4j граф связей

### Поиск и RAG
- `help-mcp` — справка платформы
- `1c-help-search` — RAG с Qdrant
- `1c-elasticsearch-search` — Elasticsearch

### Тестирование
- `yaxunit-mcp` — запуск тестов
- `bsl-ls-mcp` — LSP → MCP транслятор

### Graph Metadata Search (onerpa.ru) — детально

**Docker образ:** `comol/1c_graph_metadata:latest`
**Порт:** 8006
**Тип:** HTTP (MCP через `/mcp` или по REST)
**Основа:** Neo4j граф + FastAPI

**Из чего состоит:**
- **Neo4j** (:7474 browser, :7687 bolt) — графовая БД связей метаданных
- **MCP сервер** (:8006) — HTTP API + веб-интерфейс

**Требования:**
1. Docker Desktop
2. LM Studio (или OpenAI API) для эмбеддингов — модель Qwen3-Embedding-4B
3. Экспорт метаданных из Конфигуратора 1С
4. **LICENSE_KEY** — лицензионный ключ (получить у onerpa.ru)

**Compose:**
```yaml
services:
  neo4j:
    image: neo4j:latest
    ports: ["7474:7474", "7687:7687"]
    environment:
      NEO4J_AUTH=neo4j/password123
    volumes:
      - ./neo4j:/data
  mcp-app:
    image: comol/1c_graph_metadata:latest
    ports: ["8006:8006"]
    environment:
      LICENSE_KEY: YOUR_LICENSE_KEY       # ← обязателен
      NEO4J_URI: bolt://neo4j:7687
      NEO4J_USERNAME: neo4j
      NEO4J_PASSWORD: password123
      METADATA_DIRECTORY: /app/metadata
      RESET_DATABASE: "false"
      OPENAI_API_BASE: http://host.docker.internal:1234/v1
      OPENAI_API_KEY: lm-studio
      OPENAI_EMBEDDING_MODEL: Qwen3-Embedding-4B
      TEMPLATE_MODE_ENABLED: "true"
      LOAD_BSL_SIGNATURES: "true"
    volumes:
      - ./Report:/app/metadata
      - ./Files:/app/metadata_files
```

**18 MCP инструментов:** search_metadata, search_metadata_by_description, get_metadata_prompt, execute_metadata_cypher, find_objects_using_object, find_usages_of_object, find_register_movement_docs, search_code, business_search, answer_metadata_question, get_object_dossier, trace_impact, trace_call_chain, find_by_guid, resolve_qualified_name, compare_base_and_extension, + Template Mode операции

**Время индексации:** от часов (маленькая конфа) до 20-60ч (большая) + 5-10ч с BSL графом.

**Источник:** https://docs.onerpa.ru/mcp-servery-1c/servery/graph-metadata-search

### Интеграции
- `1c-naparnik-mcp` — чат с 1С:Напарник
- `1c-buh-mcp` — интеграция с Бухгалтерией

## Как работает MCP Server (Python + FastMCP)

```python
## Установка
pip install mcp

## Простой пример
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my_1c_server")

@mcp.tool()
def search_1c_docs(query: str) -> str:
    """Поиск по документации 1С"""
    return results

@mcp.tool()
def get_metadata(config_path: str) -> dict:
    """Получить метаданные конфигурации"""
    return metadata

## Запуск
mcp.run(transport="stdio")
```

## cursor_rules_1c

**GitHub:** github.com/comol/cursor_rules_1c

- 11 AI-агентов (архитектор, разработчик, ревьювер и др.)
- 24+ скиллов для форм, запросов, шаблонов, ролей
- Антипаттерны 1С
- SDD-интеграции
- MCP подключения

---

## Собственный MCP сервер для 1С (на FastMCP)

**Идея:** Написать персональный MCP сервер (или набор) для работы с 1С на FastMCP.  
**Инициатор:** @rem2222  
**Статус:** Идея, проект в Multica

### 4 ключевых модуля

| Модуль | Что делает | Технология |
|--------|-----------|------------|
| **Metadata Explorer** | Получение структуры данных из конфигурации 1С (справочники, документы, регистры, реквизиты, измерения, ресурсы) | Парсинг XML выгрузки конфигурации / EDT / COM |
| **Module Extractor** | Получение любого модуля и процедуры с выгрузкой в отдельную БД и автообновлением | SQLite/Postgres + триггеры обновления |
| **Help Server** | Поиск по встроенной справке конфигурации 1С | RAG (векторная БД + эмбеддинги) |
| **OData Gateway** | Подключение к 1С через OData — чтение справочников/документов, запуск отчетов | HTTP OData стандарт 1С |

### Почему FastMCP

1. **Единый фреймворк** для всех 4 модулей — не 4 разных решения, а 1 сервер с 4 группами инструментов
2. **Декораторы** — каждый модуль = несколько Python-функций с `@mcp.tool`, минимум boilerplate
3. **fastmcp-remote** — можно запустить на VPS или на работе, а подключиться через Claude Code/Cursor
4. **Клиентская часть** — можно дёргать инструменты из Hermes (через native MCP) или из скриптов
5. **OAuth/Security** — если OData требует авторизации, FastMCP умеет пробрасывать Bearer токены

### Примерная архитектура

```python
from fastmcp import FastMCP
from typing import Optional

mcp = FastMCP("1C-Work")

# --- Metadata Explorer ---
@mcp.tool
def get_metadata_structure(conf_path: str) -> list[dict]:
    """Получить структуру метаданных из выгрузки CF"""
    ...

@mcp.tool
def find_object(obj_name: str) -> dict | None:
    """Найти объект метаданных по имени"""
    ...

# --- Module Extractor ---
@mcp.tool
def get_module_code(object_name: str, module_type: str) -> str:
    """Получить код модуля объекта"""
    ...

@mcp.tool
def search_procedure(name: str, conf_path: str) -> list[dict]:
    """Найти процедуру по имени во всех модулях конфигурации"""
    ...

# --- OData Gateway ---
@mcp.tool
def odata_query(entity: str, filter: str = "", top: int = 100) -> list[dict]:
    """Выполнить OData запрос к 1С"""
    ...

@mcp.tool
def run_report(report_name: str, params: dict = {}) -> str:
    """Запустить отчёт 1С"""
    ...
```

### Связь с существующими решениями

- **vibecoding1c.ru** — готовые Docker-серверы (HelpSearch, Metadata, SyntaxCheck, Forms). Их можно использовать как основу или поднять параллельно.
- **Untru/1c-mcp** — EDT плагины и REST API, можно интегрировать как бэкенд для FastMCP сервера.
- **onerpa.ru** (Graph Metadata Search) — Neo4j граф метаданных, можно использовать как источник данных для Metadata Explorer модуля.

### План реализации

1. Настроить FastMCP + базовый каркас сервера
2. Metadata Explorer — парсинг XML выгрузки/EDT
3. OData Gateway — подключение к рабочей базе
4. Module Extractor — парсинг модулей + БД
5. Help Server — RAG по справке конфигурации

---

## Быстрый старт (готовые серверы)

```bash
## HelpSearchServer — поиск по справке
docker run -p 8003:8000 vibecoding/helps...

## SyntaxCheckServer — проверка синтаксиса  
docker run -p 8002:8000 vibecoding/syntaxcheck...
```

## Полезные ссылки

- [vibecoding1c.ru/mcp_server](https://vibecoding1c.ru/mcp_server)
- [github.com/Untru/1c-mcp](https://github.com/Untru/1c-mcp)
- [modelcontextprotocol.io](https://modelcontextprotocol.io)
