---
description: Полностью локальная система долговременной памяти для AI-агентов, без внешних API-зависимостей.
tags: [tech]
related:
  - tech/agentmemory-vs-current
  - tech/gbrain-lossless-agent-memory
  - tech/hermes-memory-setup-vps
---

# tencentdb-agent-memory

**Репозиторий:** https://github.com/TencentCloud/TencentDB-Agent-Memory
**Лицензия:** MIT
**Автор:** Tencent Cloud (腾讯云)
**Дата:** 2026 (v0.3.4+, npm: @tencentdb-agent-memory/memory-tencentdb)
**Статус:** ❓ Backlog — задача MUL-715 на тестирование

## Суть

Плагин памяти для AI-агентов (OpenClaw + Hermes Gateway). Девиз: «Agents remember, Humans innovate». Две опоры: символьная краткосрочная память + слоистая долгосрочная память. Вместо плоской векторной кучи — семантическая пирамида с полной трассируемостью.

## Архитектура

### 1. Memory Layering — семантическая пирамида L0–L3

| Уровень | Что хранит | Хранилище |
|:--|:--|:--|
| **L0 — Conversation** | Сырые диалоги | SQLite |
| **L1 — Atom** | Атомарные факты | SQLite |
| **L2 — Scenario** | Сцены/ситуации | Markdown |
| **L3 — Persona** | Профиль пользователя | Markdown |

Принцип: нижние слои = доказательства, верхние = структура. Полная цепочка: Persona → Scenario → Atom → Conversation.

### 2. Symbolic Memory — контекстная компрессия

- Тяжёлые логи выгружаются во внешние файлы (`refs/*.md`)
- В контексте остаётся Mermaid-диаграмма с `node_id`
- При необходимости агент обращается к полному тексту по `node_id`

## Бенчмарки

| Бенчмарк | Успех (до/после) | Токены (до/после) |
|:--|:--:|:--:|
| WideSearch | 33% → **50%** (+51%) | 221M → **85M** (-61%) |
| SWE-bench | 58.4% → **64.2%** (+10%) | 3474M → **2375M** (-33%) |
| PersonaMem | 48% → **76%** (+59%) | — |

## Интеграции

- **OpenClaw plugin** — `openclaw plugins install @tencentdb-agent-memory/memory-tencentdb` (zero-config, SQLite + sqlite-vec из коробки)
- **Hermes Gateway** — провайдер `memory_tencentdb` (директория ОБЯЗАТЕЛЬНО с подчёркиванием: `memory_tencentdb`)
  - `memory.provider: memory_tencentdb` в config.yaml
  - Отдельный Gateway-процесс на :8420 (Node ≥22.16, `npx tsx src/gateway/server.ts`), авто-запуск через Popen при первом диалоге
  - Env: `MEMORY_TENCENTDB_GATEWAY_CMD/HOST/PORT`, LLM через `TDAI_LLM_API_KEY/BASE_URL/MODEL` или конфиг `~/.memory-tencentdb/memory-tdai/tdai-gateway.json`
  - Docker-образ: `docker/opensource/Dockerfile.hermes` (порт 8420)
  - Windows-native: `scripts/setup-hermes-memory-tencentdb.bat`
  - Безопасность (опционально): `TDAI_GATEWAY_API_KEY` (Bearer, кроме /health), `TDAI_CORS_ORIGINS`
- **Бэкенды**: SQLite + sqlite-vec (из коробки), Tencent Cloud Vector Database
- **Retrieval**: BM25 + векторный + RRF-фузия (hybrid)

## Особенности

- White-box debugging — все промежуточные данные читаемые файлы
- Контекстная компрессия: mild при 50% контекста, aggressive при 85%
- Три уровня конфигурации (базовый / продвинутый / полный)
- Полная прослеживаемость без необратимой компрессии

## Конфигурация

Базовый минимум (OpenClaw):
```json
{
  "memory-tencentdb": {
    "enabled": true
  }
}
```

## Статус

❓ Backlog — MUL-715 (2026-08-02): протестировать на текущем стеке (Hermes + agentmemory). Ключевые вопросы: сосуществование с agentmemory (memory.provider — один слот), реальная экономия токенов на длинных задачах, качество PersonaMem. Даже если не ставить — взять идеи: Mermaid-канвас с node_id drill-down, прогрессивное раскрытие.

## Ссылки

- [GitHub](https://github.com/TencentCloud/TencentDB-Agent-Memory)
- [NPM](https://www.npmjs.com/package/@tencentdb-agent-memory/memory-tencentdb)
- [Discord](https://discord.gg/dJQM6mKMF)
- Связано: [[tech/agent-memory-research-2026]] [[tech/gbrain-lossless-agent-memory]] [[tech/supermemory-agent-memory]]