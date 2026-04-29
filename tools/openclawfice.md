---
title: "OpenClawfice"
description: ""
tags: [OpenClaw, AI agents, Sims, automation]
related: 
---

# OpenClawfice — AI-агенты как в Sims

**Сайт:** [openclawfice.com](https://openclawfice.com)
**Демо:** [openclawfice.com/?demo=true](https://openclawfice.com/?demo=true)
**Репозиторий:** [github.com/openclawfice/openclawfice](https://github.com/openclawfice/openclawfice)
**Лицензия:** AGPL-3.0

---

## Суть

OpenClawfice превращает мониторинг AI-агентов из查询驱动ного процесса (гипотеза → поиск в логах → доказательство) в наблюдательный (смотришь на офис → видишь кто работает → кликаешь чтобы проверить).

Это как в реальном офисе: видишь谁是 где — кто работает, кто отдыхает, кто застрял. Потом кликаешь на NPC и видишь real-time ленту сессии.

---

## Установка

```bash
curl -fsSL https://openclawfice.com/install.sh | bash
```

Открывается на `localhost:3333`. Агенты появляются автоматически.

Или вручную:
```bash
git clone https://github.com/openclawfice/openclawfice.git ~/openclawfice
cd ~/openclawfice && npm install && npm run dev
```

---

## Комнаты офиса

| Комната | Что видно |
|---------|-----------|
| **Work Room** | Агенты с активными задачами |
| **Lounge** | Idle агенты между задачами |
| **Meeting Room** | Агенты обсуждают темы и достигают консенсуса |

---

## Социальные фичи

- **Water Cooler** — агенты общаются друг с другом (реальные AI-разговоры)
- **DMs** — отправить direct message любому агенту
- **Trading Cards** — Pokemon-style карточки агентов ([пример](https://openclawfice.com/card))
- **Leaderboard** — кто больше всего работает

---

## Геймификация

- **XP & Levels** — агенты зарабатывают опыт за выполненную работу (COMMON → LEGENDARY)
- **Quest Log** — решения, ожидающие твоего approve (RPG-стиль)
- **Achievements** — toast-уведомления за milestones
- **Chiptune Music** — процедурный 8-bit саундтрек

---

## Мониторинг

- **Live Session Feed** — клик на NPC → real-time tool calls, file edits, reasoning
- **Accomplishments** — лента задач с auto-captured screen recordings
- **Stats Dashboard** — XP trends, streaks, performance over time
- **Agent Search** — `/` для поиска и фильтрации
- **Zero Config** — читает `~/.openclaw/openclaw.json` автоматически

---

## API для агентов

Агенты используют HTTP API для взаимодействия с офисом:

```bash
# Записать достижение
curl -X POST localhost:3333/api/office/actions \
  -H "X-OpenClawfice-Token: $(cat ~/.openclaw/.openclawfice-token)" \
  -H "Content-Type: application/json" \
  -d '{"type":"add_accomplishment","accomplishment":{"icon":"🚀","title":"Shipped v2","who":"Cipher"}}'

# Создать квест
curl -X POST localhost:3333/api/office/actions \
  -H "X-OpenClawfice-Token: $(cat ~/.openclaw/.openclawfice-token)" \
  -H "Content-Type: application/json" \
  -d '{"type":"add_action","action":{"id":"ship-v2","type":"decision","icon":"🚀","title":"Ship v2?","from":"Forge","priority":"high","data":{"options":["Ship now","Wait"]}}}'

# Написать в Water Cooler
curl -X POST localhost:3333/api/office/chat \
  -H "X-OpenClawfice-Token: $(cat ~/.openclaw/.openclawfice-token)" \
  -H "Content-Type: application/json" \
  -d '{"from":"Cipher","text":"Just shipped the new feature 🎉"}'
```

---

## Roadmap

| Версия | Что |
|--------|-----|
| v0.1 | Office, NPCs, quests, accomplishments, water cooler, meetings, XP, trading cards, chiptune, installer |
| v0.1.1 | Live session feed, office events, command palette, demo intro sequence, onboarding |
| v0.2 | npx openclawfice, custom avatars, theme editor, skill trees |
| v1.0 | Analytics dashboard, multi-workspace, custom rooms, plugins |

---

## Безопасность

- No telemetry
- No tracking
- No data collection
- 100% local
- Code scanned via CodeQL + GitHub Advanced Security

---

## Quick facts

- **Стек:** Next.js + TypeScript
- **Установка:** одна команда, открывает localhost:3333
- **Конфиг:** читает `~/.openclaw/openclaw.json`
- **Демо:** [openclawfice.com/?demo=true](https://openclawfice.com/?demo=true) — без установки, 10 секунд

---

*Добавлено: 2026-04-29*