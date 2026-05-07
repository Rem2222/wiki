---
title: "SDD: OpenSpec — подключение к реальному проекту"
description: "Spec-Driven Development для JAWL или Dashboard"
tags: [SDD, OpenSpec, JAWL, Dashboard]
related: [[openspec]], [[openspec-usage]], [[sdd-openspec-orchestrator]]
---

# SDD: Подключение OpenSpec к реальному проекту

**Sub-task:** REM-195  
**Status:** Draft  
**Author:** Romul  
**Date:** 2026-05-03

---

## 1. Why (Зачем)

Сейчас JAWL и Dashboard развиваются без формальной спецификации требований. Изменения вносятся "по ситуации",没有一个中心化的视图来追踪哪些需求已经被实现,哪些还在规划中。Результат:

- Требования теряются между сессиями
- Неясно что уже реализовано, а что только обсуждалось
- При рефакторинге непонятно что должно сохраняться

OpenSpec даёт структуру: spec-first → implementation → archive. Это превращает разработку из хаоса в traceable процесс.

---

## 2. Scope (Что входит)

**Выбор проекта:**
- JAWL (более живой, частые изменения)
- Dashboard (более стабильный, но больше специфики)

**Входит:**
- Структура `openspec/` в выбранном проекте
- Первый real change с минимум 3 requirements
- Полный цикл: spec → implementation → validate → archive
- Документация процесса

**Не входит (пока):**
- Интеграция с Оркестратором (REM-196)
- Pre-commit hook (REM-197)

---

## 3. Requirements (Что должно быть)

### 3.1 Структура OpenSpec

The system SHALL create an `openspec/` directory in the project root.

```bash
cd /home/rem/JAWL
openspec init --tools opencode
```

Структура:
```
JAWL/
├── openspec/
│   ├── config.yaml
│   ├── specs/
│   │   └── <feature-name>/
│   │       └── spec.md
│   └── changes/
│       ├── <active-change>/
│       └── archive/
└── .opencode/
    ├── commands/
    └── skills/
```

### 3.2 Варианты интеграции

**Вариант A — OpenSpec внутри проекта**

OpenSpec живёт внутри каждого проекта. Плюс: изоляция, каждый проект сам за себя. Минус: нет централизованного view.

```
JAWL/openspec/
Dashboard/openspec/
```

**Вариант B — Центральный в workspace**

Один OpenSpec в `~/.openclaw/workspace/openspec/`. Все проекты — как specs внутри. Плюс: единый SDD-взгляд на всё. Минус: нужно линковать.

```
~/.openclaw/workspace/openspec/specs/
├── jawl/
│   ├── auth/spec.md
│   └── memory/spec.md
└── dashboard/
    └── api/spec.md
```

**Рекомендация:** Вариант B — больше контроля и visibility.

### 3.3 Первый Real Change

При выборе change:
- Простая задача которая уже понятна (напр. "добавить uptime display")
- Минимум 3 requirements
- Реализация за 1-2 сессии

Пример первого change:
```
Change: jawl-uptime-display
Purpose: Добавить uptime в bottom bar JAWL
Requirements:
  - SHALL показать uptime в формате "Xd Xh Xm"
  - SHALL обновлять каждые 60 секунд
  - SHALL хранить start time в state
```

### 3.4 Процесс

The workflow SHALL follow this sequence:

1. `openspec new change jawl-uptime-display` — создать change
2. `openspec instructions specs --change jawl-uptime-display` — получить template
3. Написать `specs/uptime/spec.md` — 3+ requirements с SHALL
4. Реализовать код
5. `openspec validate jawl-uptime-display` — проверить SHALL/MUST
6. `openspec archive jawl-uptime-display --yes` — заархивировать

---

## 4. Deliverables (Что на выходе)

| Artifact | Описание |
|----------|---------|
| `openspec/` в проекте | Структура OpenSpec |
| Первый change | Минимум 3 requirements |
| Spec.md | Requirements с SHALL |
| Archive | Завершённый change в archive |
| Лог в wiki | Описание что сработало, что нет |

---

## 5. Acceptance Criteria (Когда готово)

- [ ] OpenSpec инициализирован в выбранном проекте
- [ ] Создан первый real change
- [ ] Минимум 3 requirements в spec.md
- [ ] Код реализован и проверен
- [ ] Change заархивирован
- [ ] Specs смерджены в `openspec/specs/`
- [ ] Записано в wiki что сработало

---

## 6. Notes (Заметки)

**Примечание:** Вариант B (центральный) предпочтительнее потому что:
1. Один OpenSpec проще поддерживать
2. Все specs в одном месте
3. Оркестратор может читать все specs не заходя в проекты

**Риск:** Если JAWL/Dashboard в разных репозиториях — центральный workspace не покрывает. В этом случае — вариант A.
