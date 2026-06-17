---
description: MY_EVENT = EventConfig(
created: 2026-05-01
tags: [jawl, howto, event, eventbus]
related: [[tech/jawl]] [[tech/jawl-events]] [[tech/jawl-heartbeat]]
parent: "[[tech/jawl]]"

# HOWTO: Добавить событие в JAWL EventBus

## Шаги

### 1. Определить в registry.py

```python
## src/utils/event/registry.py → class Events

MY_EVENT = EventConfig(
    name="my_event",
    description="Что происходит при этом событии",
    level=EventLevel.MEDIUM,
    requires_attention=True    # True = прервёт heartbeat sleep
)
```

### Уровни важности

| Уровень | Значение | Когда |
|---------|----------|-------|
| CRITICAL | 50 | Система падает |
| HIGH | 40 | Новое сообщение |
| MEDIUM | 30 | Значимое действие |
| LOW | 20 | Рутина |
| BACKGROUND | 10 | Фоновые задачи |

### requires_attention
- `True` — прерывает heartbeat sleep, ReAct запускается немедленно
- `False` — обработается в следующем тике

### 2. Опубликовать

```python
from src.utils.event.registry import Events

await bus.publish(Events.MY_EVENT, source="my_module", data={...})
```

### 3. Подписаться

```python
class MyComponent:
    def __init__(self, bus: EventBus):
        bus.subscribe(Events.MY_EVENT, self._handler)
    
    async def _handler(self, *args, **kwargs):
        ...
```

### 4. Проверить

```
[System] Подписка: '_handler' -> 'my_event'
```

## Связанные статьи

- [[tech/jawl-events|EventBus]] — все существующие события
- [[tech/jawl-heartbeat|Heartbeat]] — как events прерывают sleep
