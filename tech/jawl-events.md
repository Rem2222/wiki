---
description: Асинхронная Pub/Sub шина для слабосвязанного взаимодействия модулей.
created: 2026-05-01
tags: [jawl, events, eventbus, reference]
related: [[tech/jawl]] [[tech/jawl-architecture]] [[tech/jawl-heartbeat]]
parent: "[[tech/jawl]]"

# JAWL EventBus

Асинхронная Pub/Sub шина для слабосвязанного взаимодействия модулей.

## Архитектура

```
EventConfig (registry.py)          ← определение
    ↓
Events class (registry.py)         ← глобальный реестр
    ↓
EventBus (bus.py)                   ← маршрутизация
    ├── subscribe(event, handler)   ← регистрация
    ├── publish(event, *args)       ← отправка
    └── listeners: dict[str, list[Callable]]
```

## Уровни важности

| Уровень | Значение | Пример |
|---------|----------|--------|
| CRITICAL | 50 | SYSTEM_REBOOT_REQUESTED |
| HIGH | 40 | INCOMING_MESSAGE |
| MEDIUM | 30 | MESSAGE_SENT |
| LOW | 20 | SKILL_EXECUTED |
| BACKGROUND | 10 | HEARTBEAT_TICK |
| INFO | 0 | — |

## Ключевые события

### Входящие
- `INCOMING_MESSAGE` (HIGH) — новое сообщение от пользователя, прерывает heartbeat sleep
- `HEARTBEAT_TICK` (BACKGROUND) — периодический тик

### Исходящие
- `MESSAGE_SENT` (MEDIUM) — сообщение отправлено
- `SKILL_EXECUTED` (LOW) — навык выполнен

### Системные
- `SYSTEM_REBOOT_REQUESTED` (CRITICAL) — запрос перезагрузки
- `SYSTEM_CORE_START` (HIGH) — инициализация ядра (баг: триггерится на каждом heartbeat)

## Подписка и публикация

```python
## Подписка
bus.subscribe(Events.INCOMING_MESSAGE, handler)

## Публикация
await bus.publish(Events.INCOMING_MESSAGE, source="telegram", data=msg)

## Обработчик (sync или async)
async def handler(*args, **kwargs):
    ...
```

## Как добавить событие

→ [[tech/jawl-howto-add-event|HOWTO: Добавить событие]]

## Связанные статьи

- [[tech/jawl-heartbeat|Heartbeat]] — главный publisher
- [[tech/jawl-react-loop|ReAct Loop]] — реагирует на HIGH/CRITICAL
