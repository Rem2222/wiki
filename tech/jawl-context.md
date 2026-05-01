---
created: 2026-05-01
tags: [jawl, context, prompt, reference]
parent: "[[tech/jawl]]"
---

# JAWL Context Builder

Собирает промпт для LLM из множества источников.

## Структура промпта

```
┌─────────────────────────────────────┐
│ 1. System Prompt                     │
│    ├── Role & personality (SOUL.md)  │
│    ├── Communication style           │
│    ├── Drives & Taboos               │
│    └── Instructions                  │
├─────────────────────────────────────┤
│ 2. Available Skills                  │
│    └── List of @skill() signatures   │
├─────────────────────────────────────┤
│ 3. Knowledge (RAG)                   │
│    └── Top-K relevant documents      │
├─────────────────────────────────────┤
│ 4. Recent Events                     │
│    └── Missed events since last tick  │
├─────────────────────────────────────┤
│ 5. Chat History                       │
│    └── Last N messages (SQL)          │
├─────────────────────────────────────┤
│ 6. Current State                      │
│    ├── Step X/max_react_steps         │
│    ├── Active drives                  │
│    └── Tasks & mental states          │
└─────────────────────────────────────┘
```

## ContextTruncator

При накоплении событий (>5) применяются прогрессивные лимиты:

| Missed events | Max events в контексте |
|--------------|----------------------|
| 0-5 | 20 |
| 6-10 | 15 |
| 11-15 | 10 |
| 16-20 | 7 |
| 21-25 | 5 |
| 26+ | 3 |
| 30+ | 1 |

Файл: `src/l3_agent/context/truncator.py`

## Prompt Builder

Форматирование секций через шаблоны:
- `DRIVES.md` — текущие потребности агента
- `TABOOS.md` — запреты
- `COMMUNICATION_STYLE.md` — стиль общения
- `INSTRUCTIONS.md` — инструкции ReAct

Файл: `src/l3_agent/prompt/builder.py`

## RAG

Поиск релевантных знаний через Qdrant:
1. Embed текущий контекст
2. Search в коллекции `knowledge`
3. Top-K документов добавляются в секцию Knowledge

Файл: `src/l3_agent/rag/`

## Связанные статьи

- [[tech/jawl-react-loop|ReAct Loop]] — consumer контекста
- [[tech/jawl-architecture|Architecture]] — расположение файлов
