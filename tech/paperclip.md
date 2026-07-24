---
type: tool
title: Paperclip — management layer для AI-агентов
description: Open-source платформа для оркестрации команды AI-агентов с Org Chart, heartbeats, goal alignment и cost control
tags: [agents, orchestration, management, open-source, hermess]
related:
  - tech/hermes-agent-masterclass
  - concepts/proactive-agents
  - concepts/graph-engineering
source: https://paperclip.ing/
source_github: https://github.com/paperclipai/paperclip
ingested_at: '2026-07-23'
---

# Paperclip

**Суть:** Management layer над AI-агентами. Позволяет собрать команду из агентов разных типов (Claude, Codex, Hermes, OpenClaw) под одним дашбордом, с иерархией, целями, бюджетами и трекингом.

Позиционирование: *«Если OpenClaw — сотрудник, Paperclip — компания»*

## Статистика (GitHub)

| Метрика | Значение |
|---|---|
| Stars | 74.6k |
| Forks | 13.9k |
| Коммитов | 3,241 |
| Branches | 653 |
| Tags | 900 |
| Issues | 2k |
| PRs | 2.9k |
| Активность | Последний коммит — часы назад |

## Ключевые возможности

### Org Chart
- Иерархия агентов: CEO → CTO → engineer → designer
- Reporting lines, роли, job descriptions
- Каждый агент имеет начальника и подчинённых

### Goal Alignment
- Каскад целей: Mission → Project Goal → Agent Goal → Task
- Каждая задача прослеживается до миссии компании
- Интеграция с SKILL.md (как и в Hermes)

### Heartbeats
- Агенты просыпаются по расписанию и проверяют свои обязанности
- Делегация задач вверх/вниз по Org Chart
- Кросс-командные запросы

### BYO Agent (Bring Your Own Agent)
- Совместимость с Claude, Codex, Hermes, OpenClaw, Gemini, Cursor, Pi, OpenCode
- Любой агент, который может получать heartbeat

### Cost Control
- Ежемесячные бюджеты на каждого агента
- При лимите — автоматическая остановка
- Прозрачность расходов

### Governance
- Approve/deny найма агентов
- Override стратегии
- Pause/terminate любого агента

### Ticket System
- Полный audit log всех вызовов
- Трейсинг tool calls
- Каждое решение объяснено

## Цены

Open-source, self-hosted. Бесплатно для самостоятельного развёртывания.

**Стоимость токенов:** зависит от подключённых агентов (каждый агент жжёт токены на heartbeat'ы и работу).

## Когда полезен

- Нужно управлять **несколькими агентами разных типов** из одного места
- Хочется **cost control** и лимиты на агентов (Hermes этого не даёт)
- Нужно **goal alignment** — чтобы все агенты работали к одной цели
- Уже есть OpenClaw, Hermes, Codex — Paperclip объединяет их под одним Org Chart

## Когда НЕ нужен

- Уже есть работающая связка Hermes + Dex + текущие скрипты
- Нет потребности в mixing разных типов агентов
- Heartbeat'ы Paperclip жгут токены вхолостую (даже когда агенты не делают полезной работы)
- UI красивый, но скрывает механику — сложно понять что реально происходит

## Практический опыт (из обзора)

> *«Credits улетали просто от heartbeat'ов, пока агенты «болтали» без реальной работы»*
> *«Автор вернулся к OpenClaw — 80% функционала уже есть там»*

Paperclip — оркестратор оркестраторов. Если твой текущий инструмент (Hermes/OpenClaw) уже умеет делегировать — Paperclip даёт в основном UI и cost control.

## Развёртывание

```bash
npx paperclipai onboard --yes
```

Или Docker Compose. Требует Node.js сервер + PostgreSQL.

## Релевантность к Dex/Hermes

Paperclip может работать как **CEO-уровень** над командой Hermes + Dex:
- Hermes/Dex подключаются как рядовые агенты
- Paperclip ставит цели, следит за бюджетом, логирует всё
- Heartbeat'ы дублируются (Paperclip + Dex) — потенциально избыточно

Альтернатива: Dex сам развить в сторону Org Chart и cost control, без внешнего оркестратора.
