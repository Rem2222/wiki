---
type: concept
title: Mul 239 Codegraph In Gsd
ingested_via: 'mcp:put_page'
ingested_at: '2026-06-14T22:30:02.984Z'
source_kind: 'mcp:put_page'
---

---
description: Добавить CodeGraph (code knowledge graph) в экосистему GSD squad — интеграция с оркестратором и агентами
tags: [gsd, codegraph, task, integration, ai-agents]
related: [[tech/gsd]], [[tech/codegraph]], [[tech/gsd-multica-integration]]
---

# MUL-239: Добавить CodeGraph в GSD squad

## Цель

Внедрить CodeGraph (npm-пакет `@leanlabsinnov/codegraph`, v1.1.11) в воркфлоу GSD squad — чтобы специализированные агенты имели доступ к графу зависимостей кодовой базы для более точного анализа.

## Текущий статус

- ✅ CodeGraph установлен (npm, v1.1.11)
- ✅ Проиндексирован Multica (1269 файлов, 17248 нод, 50886 рёбер)
- ✅ MCP-сервер запущен на порту 3748 (SSE transport)
- ✅ systemd-сервис `codegraph.service` создан и включён
- ✅ Конфиг Hermes обновлён — MCP подключение через SSE
- ✅ Автопилот «Обнова мультика» обновлён (пункт 4 — CodeGraph)

## Что нужно сделать

### 1. Доработать Оркестратор GSD

При старте нового проекта:
- Создавать БД CodeGraph в папке проекта: `codegraph index <path> --no-embed`
- Сохранять repo id для дальнейшего использования
- OR: проверять существует ли уже граф для этого пути (`codegraph status <path>`)

### 2. Внедрить CodeGraph в агентов GSD

Основные агенты для внедрения (по приоритету):

| Агент | Как использовать CodeGraph | Момент вызова |
|-------|--------------------------|---------------|
| **codebase-mapper** | Получение карты зависимостей: кто кого вызывает, импорты, структура | В начале `/gsd-map-codebase` |
| **assumptions-analyzer** | Поиск всех использований функции/класса через `code_refs` | При анализе кода фазы |
| **debugger** | `code_flow` от точки входа до side-effect, `code_callers`/`code_callees` | При расследовании бага |
| **integration-checker** | `code_flow` для проверки e2e интеграций, поиск сломанных связей | При кросс-фазовом аудите |
| **planner** | `code_def` для нахождения определений, `code_refs` для поиска использований | При планировании изменений |
| **executor** | `code_blast` для оценки радиуса изменений | Перед внесением изменений |
| **security-auditor** | `code_flow` для обнаружения неожиданных путей данных | При аудите безопасности |
| **pattern-mapper (новый)** | Использовать граф для выявления архитектурных паттернов | Новая роль |

### 3. Доступные MCP-инструменты CodeGraph

После подключения через Hermes MCP, агентам будут доступны:

- `mcp_codegraph_code_callers` — кто вызывает функцию
- `mcp_codegraph_code_callees` — что вызывает функция
- `mcp_codegraph_code_def` — где определён символ
- `mcp_codegraph_code_refs` — все упоминания символа
- `mcp_codegraph_code_flow` — цепочка вызовов от entry point
- `mcp_codegraph_code_blast` — радиус изменений
- `mcp_codegraph_code_traversal_cache_clear` — сброс кэша

### 4. Примеры использования

```bash
# Узнать кто вызывает функцию
mcp_codegraph_code_callers symbol="syncMultica"

# Найти определение
mcp_codegraph_code_def symbol="IssueService"

# Проследить поток данных до БД
mcp_codegraph_code_flow entry_point="handleRequest"

# Оценить радиус изменений
mcp_codegraph_code_blast symbol="updateAutopilot"
```

## Приоритет

Средний — внедрить после базовой стабилизации GSD squad.
