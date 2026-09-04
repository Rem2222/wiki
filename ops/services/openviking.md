---
title: OpenViking
created: 2026-09-04
status: partial
tags: [memory, ai, context-database, bytedance]
related:
  - [[ops/services/hindsight]]
  - [[ops/services/agentmemory]]
---

# OpenViking

Контекстная база данных для AI-агентов от ByteDance (Volcengine). Хранит память, ресурсы и навыки как виртуальную файловую систему `viking://` с трёхуровневой загрузкой контекста (L0/L1/L2).

## Статус

**Частично развёрнут.** Контейнер работает, данные НЕ загружены. Ожидает задачу MUL-10057.

## Инфраструктура

- **Контейнер:** `openviking` (Docker, `ghcr.io/volcengine/openviking:latest`, v0.4.17.1)
- **Порт:** `127.0.0.1:8900` (внутренний, без внешнего доступа)
- **Сеть:** `--network host` (доступ к Ollama на `:11434`)
- **Конфиг:** `/root/.openviking/ov.conf`
- **Данные:** `/root/.openviking/data/`
- **Автозапуск:** `--restart unless-stopped`

## Модели

| Роль | Модель | Провайдер | Примечание |
|------|--------|-----------|------------|
| **Embedding** | bge-m3 (1024 dim) | Ollama `:11434` | Локальная, ~5 сек/запрос |
| **VLM** | mimo-v2.5 | OpenCode Go API | Обработка L0/L1/L2 слоёв |

## Архитектура обработки

Очередь из 7 стадий (мониторинг через `/api/v1/observer/queue`):

1. **Embedding** — векторизация через bge-m3
2. **Semantic** — генерация L0 (abstract ~100 токенов), L1 (overview ~2k токенов), L2 (детали)
3. **ExternalParse** — парсинг внешних ресурсов (URL, файлы)
4. **AddResource** — обработка добавленных ресурсов
5. **SessionCommit** — коммит сессий в долгосрочную память
6. **UserDeletion** — удаление
7. **Semantic-Nodes** — обновление графа связей

## API (доступные изнутри VPS)

| Endpoint | Описание |
|----------|----------|
| `GET /health` | Health check |
| `GET /api/v1/system/status` | Статус системы |
| `GET /api/v1/observer/queue` | Статус очереди обработки |
| `GET /api/v1/observer/system` | Системные компоненты |
| `POST /api/v1/content/write` | Запись файла (uri + content + mode) |
| `POST /api/v1/content/batch-write` | Пакетная запись (root_uri + operations[]) |
| `GET /api/v1/fs/ls?uri=viking://` | Список директорий |
| `POST /api/v1/fs/mkdir` | Создание директории |
| `POST /api/v1/search/search` | Семантический поиск |
| `POST /api/v1/search/recall` | Recall (как в Hindsight) |
| `POST /api/v1/search/find` | Поиск по файлам |
| `GET /openapi.json` | Полная схема API |

## Файловая система

```
viking://
├── resources/              # Ресурсы (URL, файлы, репозитории)
└── user/
    └── default/
        └── memories/       # Память агента
            ├── facts/      # Факты (текущая загрузка)
            └── test/       # Тестовые данные
```

## Batch-write формат

```json
{
  "root_uri": "viking://user/default/memories/facts",
  "operations": [
    {"uri": ".../file.md", "content": "...", "mode": "create"}
  ],
  "wait": false
}
```

**Важно:** 
- `mode: create` требует расширение файла (`.md`)
- `wait: false` — асинхронная обработка (embedding + semantic в фоне)
- `root_uri` должна существовать (создать через `mkdir`)

## Конфигурация (ov.conf)

```json
{
  "server": {"host": "127.0.0.1", "port": 8900, "auth_mode": "dev"},
  "storage": {"workspace": "/root/.openviking/data"},
  "embedding": {
    "dense": {
      "provider": "ollama",
      "api_key": "ollama",
      "api_base": "http://172.17.0.1:11434/v1",
      "model": "bge-m3",
      "dimension": 1024,
      "input": "text"
    }
  },
  "vlm": {
    "provider": "openai",
    "api_key": "<OPENCODE_GO_API_KEY>",
    "api_base": "https://opencode.ai/zen/go/v1",
    "model": "mimo-v2.5",
    "max_tokens": 4096
  }
}
```

## Известные проблемы

- **Embedding медленный:** ~5-60 сек/запрос через Ollama bge-m3 на CPU
- **AGPL-3.0:** нельзя модифицировать код без open-sourcing
- **Нет внешнего доступа:** пока не настроен nginx (.todo)
- **Нет интеграции с Hermes:** только один memory provider за раз (todo)

## Управление

```bash
# Статус
docker ps | grep openviking
curl -s http://127.0.0.1:8900/health

# Перезапуск
docker restart openviking

# Логи
docker logs openviking --tail 50

# Очередь обработки
curl -s http://127.0.0.1:8900/api/v1/observer/queue

# Файловая система
curl -s "http://127.0.0.1:8900/api/v1/fs/ls?uri=viking://"
```
