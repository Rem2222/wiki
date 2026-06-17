---
description: Полная архитектура JAWL. 85 файлов Python, ~13,200 строк кода.
created: 2026-05-01
tags: [jawl, architecture, reference]
related: [[tech/jawl]] [[tech/jawl-config]] [[tech/jawl-react-loop]] [[tech/jawl-multiagent]]
parent: "[[tech/jawl]]"
---

# JAWL Architecture

Полная архитектура JAWL. 85 файлов Python, ~13,200 строк кода.

## Общая схема

```
┌─────────────────────────────────────────────────┐
│                  L3 Agent                        │
│  ┌──────────┐ ┌───────────┐ ┌────────────────┐ │
│  │ ReAct    │ │ Context   │ │  Prompt        │ │
│  │ Loop     │ │ Builder   │ │  Builder        │ │
│  └────┬─────┘ └─────┬─────┘ └───────┬────────┘ │
│       │             │               │           │
│  ┌────┴─────────────┴───────────────┴────────┐  │
│  │              LLM Client                   │  │
│  └────────────────┬──────────────────────────┘  │
├───────────────────┼─────────────────────────────┤
│                   │       L2 Interfaces          │
│  ┌────┐ ┌────┐ ┌──┴──┐ ┌──────┐ ┌──────────┐  │
│  │ Tg │ │ Tg │ │Host │ │Calendar│ │  Meta    │  │
│  │Bot │ │User│ │ OS  │ │       │ │          │  │
│  └────┘ └────┘ └─────┘ └──────┘ └──────────┘  │
├─────────────────────────────────────────────────┤
│                  L1 Databases                    │
│  ┌──────────┐  ┌──────────┐  ┌───────────────┐ │
│  │  SQLite  │  │  Qdrant  │  │  EventBus     │ │
│  │  (6 tbl) │  │  (2 col) │  │  (22 events)  │ │
│  └──────────┘  └──────────┘  └───────────────┘ │
├─────────────────────────────────────────────────┤
│                  L0 State                        │
│  AgentState · Settings · EventBus · Memory       │
└─────────────────────────────────────────────────┘
```

## L0 — State

Runtime состояние без побочных эффектов.

- **AgentState** (`state.py`) — модель, температура, step tracking, heartbeat timer
- **Settings** (`settings.py`) — Pydantic, загружает YAML
- **EventBus** (`event/bus.py`) — Pub/Sub шина
- **Memory** — указатели на SQLite/Qdrant

## L1 — Databases

Хранилища данных.

### SQLite (6 таблиц)
| Таблица | Назначение | Лимит |
|---------|-----------|-------|
| tasks | Задачи агента | 10 |
| mental_states | Эмоциональные состояния | 10 |
| chat_history | История чата (persisted) | — |
| knowledge | Факты и знания | — |
| reflections | Рефлексии | — |
| events_log | Лог событий | — |

### Qdrant (2 коллекции)
- `knowledge` — semantic search по знаниям
- `reflections` — semantic search по рефлексиям

## L2 — Interfaces

7 интерфейсов с навыками. Каждый интерфейс:
- Имеет `Client` (подключение) + `Events` (обработка) + `Bootstrap` (инициализация)
- Регистрирует навыки через `@skill()` декоратор
- Публикует события в EventBus

Подробнее: [[tech/jawl-skills-registry]]

## L3 — Agent

### ReAct Loop (`react/loop.py`)
Бесконечный цикл: reasoning → action → observation. До 15 шагов за тик.
→ [[tech/jawl-react-loop]]

### Context Builder (`context/builder.py`)
Собирает промпт из секций: system, skills, knowledge, history, current state.
→ [[tech/jawl-context]]

### Prompt Builder (`prompt/builder.py`)
Форматирует секции промпта с DRIVES, TABOOS, COMMUNICATION_STYLE.

### RAG (`rag/`)
Поиск релевантных знаний через Qdrant перед каждым вызовом LLM.

### LLM Client (`llm/client.py`)
Единый клиент для всех провайдеров. Поддерживает Chat Completions и Responses API.
Сессии кэшируются по provider_id.
