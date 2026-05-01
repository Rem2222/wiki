---
created: 2026-05-01
updated: 2026-05-01
tags:
  - ai-agents
  - autonomous
  - python
  - memory
  - jinx
type: tool
---

# JAWL — Just Another Workflow Library

**GitHub:** github.com/th0r3nt/JAWL
**Bot:** [@Jawl_Jinx_bot](https://t.me/Jawl_Jinx_bot)
**Dashboard:** Flask на порту 5000

Автономный AI-агент (персона "Jinx") с infinite ReAct loop, SQLite, Qdrant и Telegram.

## Слои архитектуры

```
L0 State        → Runtime состояние (AgentState, настройки)
L1 Databases    → SQLite (6 таблиц) + Qdrant (2 коллекции)
L2 Interfaces   → 7 интерфейсов (Telegram, Host OS, Calendar...)
L3 Agent        → ReAct loop, Context Builder, RAG
```

Подробнее: [[tech/jawl-architecture]]

## Основные подсистемы

- **ReAct Loop** — бесконечный цикл reasoning → action → observation (до 15 шагов за тик)
  → [[tech/jawl-react-loop]]
- **EventBus** — Pub/Sub шина для слабосвязанного взаимодействия модулей (22 события)
  → [[tech/jawl-events]]
- **Heartbeat** — периодический тик (300с), driving система потребностей
  → [[tech/jawl-heartbeat]]
- **Context Builder** — сборка промпта из system/user/knowledge/skills
  → [[tech/jawl-context]]

## L2 Интерфейсы

| Интерфейс | Реализация | Навыков |
|-----------|-----------|---------|
| Telegram Bot | Aiogram v3 | simple_send, messages, chats, moderation |
| Telegram Userbot | Telethon | admin, messages, chats, polls, reactions |
| Host OS | subprocess | execution, files, monitoring, network |
| Calendar | — | management |
| Meta | — | configuration, system |
| Multimodality | — | vision |
| Web Search | — | search |

Все навыки: [[tech/jawl-skills-registry]]

## Конфигурация

- `config/models.json` — провайдеры и модели (6 провайдеров)
- `settings.yaml` — системные параметры (heartbeat, SQL лимиты)
- `.env` — API ключи

Модели: MiniMax-M2.7, GLM-5/5.1, Xiaomi MiMo, gpt-5-nano (OpenCode Zen), бесплатные через OpenCode.

Подробнее: [[tech/jawl-config]]

## Dashboard

Flask на порту 5000. 15 API маршрутов, realtime polling, provider/model switching.
→ [[tech/jawl-dashboard]]

## HOWTO

- [[tech/jawl-howto-add-skill]] — добавить навык
- [[tech/jawl-howto-add-provider]] — добавить LLM провайдера
- [[tech/jawl-howto-add-event]] — добавить событие в EventBus
- [[tech/jawl-howto-add-interface]] — добавить L2 интерфейс

## Известные баги

1. **SYSTEM_CORE_START loop** — heartbeat триггерит повторную калибровку
2. **Дубли сообщений** — 2+ сообщения за один heartbeat
3. **SQL лимиты** — Tasks (10) и MentalStates (10) забиваются
4. **Telegram polling** — может тихо умирать под нагрузкой

## Скрипты

- `start-safe.sh` — запуск с очисткой зомби и блокировок
- `watchdog.sh` — мониторинг с лимитом 5 рестартов/5 мин
- `check-services.sh` — проверка статуса всех сервисов

## Локация

```
/home/rem/JAWL/          — код агента
/home/rem/JAWL/dashboard.py — Dashboard
/home/rem/JAWL/config/   — конфигурация
/home/rem/JAWL/logs/     — логи
```
