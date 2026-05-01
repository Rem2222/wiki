---
created: 2026-05-01
tags: [jawl, react, flow, reference]
parent: "[[tech/jawl]]"
---

# JAWL ReAct Loop

Бесконечный цикл reasoning → action → observation. Сердце агента.

## Flow

```
Heartbeat Timer (300s)
       │
       ▼
┌─── Tick Start ───┐
│ 1. Load Context   │ ← Context Builder
│ 2. LLM Call       │ ← Chat Completions / Responses API
│ 3. Parse Response │ ← tool_calls or fallback JSON
│ 4. Execute Skills │ ← L2 Interface
│ 5. Observe        │ ← SkillResult
│ 6. Update State   │ ← AgentState
│ 7. Send Messages  │ ← SimpleSend (throttle + hardblock)
│                   │
│ └─→ Repeat 1-7    │   (max_react_steps, default 15)
└───────────────────┘
       │
       ▼
  Sleep until next tick
```

## Tool Choice Strategy

1. **Первый вызов** — `tool_choice={"type": "function", "function": {"name": "execute_skill"}}` (forced)
2. **Если tool_calls=[]** — retry без tools (free-form)
3. **Fallback** — 3-level JSON parsing (direct, regex, markdown block)

Toggle: `/tmp/jawl_tool_choice.txt` — ON/OFF. Dashboard кнопка `🔧 Tools`.

## API Format Detection

loop.py определяет формат по `api` полю в models.json:

| api | SDK вызов |
|-----|-----------|
| `openai-completions` | `session.chat.completions.create()` |
| `openai-responses` | `session.responses.create()` |
| `anthropic-messages` | через OpenAI-совместимый прокси |

## Response Parsing

```python
def _extract_response_content(message_obj):
    # 1. tool_calls → execute skill
    if message_obj.tool_calls:
        return parse_tool_calls(...)
    
    # 2. content field
    if message_obj.content:
        return message_obj.content
    
    # 3. reasoning field (reasoning models)
    if message_obj.reasoning:
        return message_obj.reasoning
```

## Context Truncation

Прогрессивные лимиты при накоплении событий:

| Events | Max Tokens |
|--------|-----------|
| 0-5 | 20 |
| 6-10 | 15 |
| 11-15 | 10 |
| 16-20 | 7 |
| 21-25 | 5 |
| 26+ | 3 |
| 30+ | 1 |

Класс `ContextTruncator` в `context/truncator.py`.

## Known Issues

- **SYSTEM_CORE_START loop** — heartbeat перезапускает калибровку вместо обработки сообщений
- **Дубли сообщений** — модель генерирует несколько действий отправки за шаг
- **SQL лимиты** — tasks/mental_states забиваются (лимит 10)
