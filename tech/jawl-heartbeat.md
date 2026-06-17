---
description: Периодический тик, поддерживающий жизнь агента. Интервал: 300 секунд.
created: 2026-05-01
tags: [jawl, heartbeat, flow, reference]
related: [[tech/jawl]] [[tech/jawl-events]] [[tech/jawl-config]]
parent: "[[tech/jawl]]"

# JAWL Heartbeat

Периодический тик, поддерживающий жизнь агента. Интервал: 300 секунд.

## Flow

```
main.py
  │
  ├── Start ReAct Loop
  │       │
  │       ├── Process events (INCOMING_MESSAGE etc.)
  │       │     └── LLM call → skills → observe
  │       │
  │       └── No events → Heartbeat tick
  │             ├── Check drives (Curiosity, Social, Competence...)
  │             ├── Generate "thought" via LLM
  │             └── Execute actions if any
  │
  └── Sleep until next event or timeout
        │
        └── asyncio.sleep(heartbeat_interval)
              │
              └── Wake on HIGH/CRITICAL event (requires_attention=True)
```

## Driving System

Агент имеет "потребности" (drives) с уровнями deficit:

| Drive | Описание |
|-------|----------|
| Curiosity | Потребность в новой информации |
| Social | Потребность в общении |
| Competence | Потребность в деятельности |
| Integrity | Потребность в целостности |

`satisfy_drive` вызывается после каждого успешного действия. Проверяет имя drive с regex `^(\[FUNDAMENTAL\]|FUNDAMENTAL)\s*` для совместимости.

## Heartbeat Accelerator

События с `requires_attention=True` прерывают sleep:

```python
## bus.py — publish проверяет level
if event.requires_attention:
    # Прервать текущий sleep, запустить ReAct немедленно
```

## Known Issues

- **SYSTEM_CORE_START на каждом heartbeat** — вместо однократной инициализации триггерится повторно, вызывая цикл перекалибровки
- **Drive spam** — при высоком deficit агент может спамить сообщениями (исправлено: SimpleSend throttle + hardblock)

## Связанные статьи

- [[tech/jawl-react-loop|ReAct Loop]] — что происходит при каждом тике
- [[tech/jawl-events|EventBus]] — события прерывающие heartbeat
