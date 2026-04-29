# Сравнение Dashboard-ов для OpenClaw

_Обзор: 2026-04-29_

---

## Участники

| Инструмент | Репозиторий | Стек | Порты |
|------------|-------------|------|-------|
| **JAWL Dashboard** | `github.com/Rem2222/JAWL` | Python/Flask + Socket.io | 5000 |
| **OpenClawfice** | `github.com/openclawfice/openclawfice` | Next.js + TypeScript | 3333 |
| **ClawMetry** | `github.com/vivekchand/clawmetry` | Python/Flask | 8900 |
| **OpenClaw Dashboard** | `github.com/mudrii/openclaw-dashboard` | Go (zero deps) | 8080 |

---

## Сравнительная таблица

| Критерий | JAWL Dashboard | OpenClawfice | ClawMetry | OpenClaw Dashboard |
|----------|---------------|--------------|-----------|--------------------|
| **Суть** | AI-компаньон с memory + мониторинг | Sims-style наблюдение за агентами | Real-time observability, "see your agent think" | Command center, at-a-glance overview |
| **Стиль UI** | Функциональный, glass morphism | Pixel-art NPC, игровой | Дашборд с diagrams | 6 тем, glass morphism, дашборд |
| **Модель мониторинга** | Наблюдение + действия | Observation-driven (смотришь кто работает) | Flow visualization, live events | Метрики, метрики, метрики |
| **Rooms/Комнаты** | — | Work Room, Lounge, Meeting Room | — | — |
| **Социальные фичи** | — | Water Cooler, DMs, Trading Cards, Leaderboard | — | — |
| **Геймификация** | — | XP & Levels, Quest Log, Achievements, Chiptune | — | — |
| **Task tracking** | ✅ Kanban доска, Beads integration | — | — | — |
| **Memory** | ✅ Векторная память (Qdrant) | — | ✅ Memory tab (файлы) | — |
| **AI Chat** | — | — | — | ✅ AI Chat panel |
| **Flow-диаграмма** | — | — | ✅ Messages flowing through channels | — |
| **Token/cost tracking** | — | — | ✅ Usage tab, daily/weekly/monthly | ✅ Cost cards, breakdown |
| **Channels support** | Через OpenClaw | Через OpenClaw | ✅ 18 channels (Telegram, iMessage, WhatsApp, Discord...) | — |
| **Sub-agents** | ✅ | — | — | ✅ Sub-Agent Activity panel |
| **Cron monitoring** | — | — | ✅ Crons tab | ✅ Cron Jobs panel |
| **Logs** | — | — | ✅ Real-time log streaming | ✅ Merged tail view |
| **System metrics** | — | — | — | ✅ CPU/RAM/disk (Top Metrics Bar) |
| **Themes** | — | — | — | ✅ 6 built-in (3 dark + 3 light) |
| **System service** | — | — | Docker | ✅ launchd / systemd |
| **Zero config** | — | ✅ | ✅ | ✅ |
| **Local only** | ✅ | ✅ | ✅ | ✅ |
| **Data в облако** | — | — | optional sync daemon | — |
| **Установка** | `bash install.sh` | `curl -fsSL install.sh` | `pip install clawmetry` | `brew` / `curl -fsSL install.sh` |

---

## Детальное сравнение

### JAWL Dashboard
**Плюсы:**
- Векторная память (Qdrant) — можно спрашивать о прошлых сессиях
- Task tracking с Beads (Kanban доска)
- Интеграция с JAWL (AI-компаньон)

**Минусы:**
- Привязан к JAWL
- Нет token/cost tracking
- Нет cron monitoring
- UI менее polished

**Для кого:** Кто использует JAWL и хочет memory-driven мониторинг

---

### OpenClawfice
**Плюсы:**
- Уникальный Sims-style подход — observation-driven
- Социальные фичи (Water Cooler, DMs)
- Геймификация (XP, Levels, Trading Cards)
- Полностью zero config
- Демо онлайн (10 сек без установки)

**Минусы:**
- Не метрики, а наблюдение — нет cost/tracking/cron
- Больше развлечение чем инструмент
- Не показывает detail сессий (live feed есть, но в игровом стиле)

**Для кого:** Кто хочет визуально наблюдать за агентами в игровом формате

---

### ClawMetry
**Плюсы:**
- 18 каналов — универсальный мониторинг всех channels
- Flow-диаграмма — уникальная визуализация потока сообщений
- Brain tab — live agent event stream
- Security tab
- NemoClaw / OpenShell support
- Docker ready

**Минусы:**
- Нет task tracking
- Нет cron monitoring как отдельная фича (но есть)
- Flask-based, не zero-deps

**Для кого:** Кто использует много channels и хочет observability потока сообщений

---

### OpenClaw Dashboard (mudrii)
**Плюсы:**
- Zero dependencies (Go binary)
- 12 панелей — самый полный мониторинг
- AI Chat — спрашивай о дашборде на естественном языке
- 6 тем (dark + light)
- Accurate model resolution (5-level chain)
- System service management (launchd/systemd)
- Rate limiting, HTTP timeouts
- Responsive (desktop/tablet/mobile)

**Минусы:**
- Нет social/gamification фичей
- Нет memory
- Много метрик, может быть overkill для простых нужд

**Для кого:** Кто хочет максимум метрик и AI Chat в одном месте

---

## Выводы

```
              ┌─────────────────────────────────────────────────────┐
              │              Мой текущий JAWL Dashboard             │
              │   ✅ Memory (Qdrant)   ✅ Task tracking   ❌ Cost    │
              └──────────────────────────┬──────────────────────────┘
                                         │
         ┌───────────────┬───────────────┴───────────────┬───────────────┐
         ▼               ▼                               ▼               ▼
   OpenClawfice      ClawMetry              OpenClaw Dashboard     Others
   (игровой стиль)  (channels + flow)       (метрики + AI chat)
```

**Если нужно больше метрик** → OpenClaw Dashboard (mudrii) или ClawMetry

**Если нужно наблюдение** → OpenClawfice

**Если нужно memory** → JAWL Dashboard (текущий)

**ClawMetry vs OpenClaw Dashboard (mudrii):**
- ClawMetry лучше для multi-channel (18 channels)
- OpenClaw Dashboard лучше для cost/trend анализа и AI chat

---

## Рекомендация для моей связки

Мой текущий **JAWL Dashboard** покрывает:
- ✅ Memory (Qdrant) — уникальная фича, которой нет у остальных
- ✅ Task tracking (Beads)

Можно добавить из **OpenClaw Dashboard (mudrii)**:
- Token/cost tracking
- AI Chat panel
- Более polished UI с темами

Можно добавить из **ClawMetry**:
- Flow-диаграмма
- 18 channels support (если используются)

---

*Добавлено: 2026-04-29*
*Источники: репозитории каждого проекта на GitHub*