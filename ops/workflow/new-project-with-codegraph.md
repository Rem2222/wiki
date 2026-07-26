---
description: "При создании нового проекта — поднимать CodeGraph для навигации по коду"
tags: [ops, workflow, new-project]
type: guide
related:
  - ops/services/codegraph
---
# Как создать новый проект с CodeGraph

При старте нового проекта (особенно большого, с несколькими файлами/классами) нужно сразу настроить CodeGraph для навигации по коду.

## Шаги

### 1. Спросить у Романа

Перед началом работы спросить: "Нужен ли CodeGraph для этого проекта?"

### 2. Проиндексировать

```bash
CODEGRAPH_DATA_DIR=~/.codegraph/<project-slug> codegraph index /path/to/project --no-embed
```

### 3. Запустить сервер

```bash
codegraph serve --port <unique-port>
```

Порт выбирать свободный (проверить `ss -tlnp`). Обычно 3748, 3749, 3750...

### 4. Прописать в config.yaml Hermes

В `~/.hermes/config.yaml` добавить в `mcp_servers`:

```yaml
  codegraph-<project-name>:
    url: http://127.0.0.1:<port>/mcp
    headers:
      Authorization: "Bearer <token>"
```

Токен взять из `~/.codegraph/config.json` → `server.bearerToken`.

### 5. Перезапустить Hermes

После рестарта появятся тулы `mcp_codegraph_*_code_callers`, `code_def`, `code_refs`.

## Что даёт

- `code_callers(symbol)` — кто вызывает функцию
- `code_def(symbol)` — где определён символ
- `code_refs(symbol)` — все упоминания
- `code_flow(symbol)` — цепочка вызовов до DB/HTTP/IO
- `code_blast(symbol)` — кто сломается если изменить X

## Эмбеддинги

Без эмбеддингов (`--no-embed`) работает tree-sitter граф: навигация, поиск символов, определения. Эмбеддинги добавляют семантический поиск (найти код по описанию intent'а), но не обязательны.

Текущий провайдер: **OpenRouter** → `openai/text-embedding-3-small` через OpenCode Go.
