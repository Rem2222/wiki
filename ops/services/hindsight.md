---
description: "Hindsight — семантическая память напарника Hermes (Postgres). Локаль :8888 + удалённый доступ rem2222.top/hindsight-api"
tags: [ops, service, memory, ai]
type: service
related:
  - ops/services/postgresql.md
  - ops/services/hermes-agent.md
service:
  name: hindsight
  category: ai-platform
  purpose: "Семантическая долговременная память Hermes напарника: recall/retain/reflect, observations, mental models, knowledge pages. Выбрано как memory.provider в MUL-874."
  install_date: 2026-08-20
  last_verified: 2026-08-28
  health_url: http://localhost:8888/health
  type: docker
  ports:
    - port: 8888
      protocol: tcp
      bind: 0.0.0.0
      description: "Hindsight REST API (Bearer-токен; без токена 401 на /v1/, /health открыт)"
    - port: 9999
      protocol: tcp
      bind: 0.0.0.0
      description: "Hindsight MCP-сервер (streamable-http, 307 redirect; плагины dsh/openclaw подключаются сюда)"
  docker_containers:
    - hindsight-app
    - hindsight-db
  processes:
    - pattern: "hindsight"
      description: "API worker hindsight-app (poller consolidation)"
  config_paths:
    - /root/hindsight/docker-compose.yml
    - /root/.hermes/hindsight/config.json
  logs:
    - docker logs hindsight-app
  depends_on:
    - postgresql
  data_size_hint: "Postgres hindsight_db, ~31k memory_units"
  notes: "Двойной гейт консолидации: глобальный env HINDSIGHT_API_ENABLE_AUTO_CONSOLIDATION + bank config.enable_observations (оба должны быть true, случай 22.08). Внешний доступ: rem2222.top/hindsight-api/ через nginx (rewrite strip) + сам Bearer-токен."
---

# Hindsight

Семантическая долговременная память Hermes-напарника на Postgres (bank `hermes`). Выбрана как memory.provider Hermes в MUL-874 (`~/.hermes/hindsight/config.json`, mode local_external).

## Порты
- **8888** — REST API. Bearer-токен (`/root/.hermes/hindsight/config.json` → `api_key`). Без токена `/v1/...` = 401; `/health` открыт.
- **9177** — MCP-сервер (streamable-http).

## Внешний доступ (28.08.2026)
- Вынесен наружу для dsh (Windows) и внешних клиентов: **`https://rem2222.top/hindsight-api/`**
- nginx: `location ^~ /hindsight-api/` → `127.0.0.1:8888`, `rewrite ^/hindsight-api(/.*)$ $1 break`
- Защита: **сам Bearer-токен Hindsight** (не Authelia — API-клиент не пройдёт браузерный login). Проверено: без токена 401, с токеном данные идут.
- Hermes на VPS продолжает ходить на **localhost:8888** (быстрее, без зависимости от nginx).

## Настройки memory.provider Hermes (`~/.hermes/hindsight/config.json`)
- `memory_mode: hybrid`, `recall_prefetch_method: recall`, `auto_recall: true`, `auto_retain: true`
- `recall_budget: mid`, `llm_provider: opencode-go`, `llm_model: mimo-v2.5`, `embeddings_model: bge-m3` (Ollama)

## Консолидация
- **Двойной гейт** (оба должны быть true): глобальный env `HINDSIGHT_API_ENABLE_AUTO_CONSOLIDATION` + банковский `config.enable_observations`/`enable_auto_consolidation` в `banks.config` (JSONB). Случай 22.08: вернули только глобальный — банковский остался false, консолидация молча стояла 4 дня.
- Диагностика: `SELECT bank_id, config FROM banks WHERE bank_id='hermes';` (подробно в скилле memory-management).