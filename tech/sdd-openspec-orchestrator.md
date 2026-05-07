---
title: "SDD: OpenSpec — интеграция в Оркестратор"
description: "Spec-first workflow: OpenSpec change перед запуском subagent-ов"
tags: [SDD, OpenSpec, Orchestrator, subagent]
related: [[openspec]], [[openspec-usage]], [[sdd-openspec-real-project]], [[tech/sdd-orchestrator-v2]]
---

# SDD: Интеграция OpenSpec в Оркестратор

**Sub-task:** REM-196  
**Status:** Draft  
**Author:** Romul  
**Date:** 2026-05-03

---

## 1. Why (Зачем)

Сейчас Оркестратор получает задачу и сразу запускает subagent-ов. Результат:
- Subagent-ы работают без формального понимания что exactly должно быть
- Нет traceable link между задачей и кодом
- Оркестратор держит всё в голове

Spec-first решает это: subagent получает spec.md с requirements, реализует по tasks, результат traceable.

---

## 2. Scope (Что входит)

**Входит:**
- Изменение ORCHESTRATOR_PROMT.md — добавление openspec workflow
- Команда `/оркестр <задача>` — создаёт change + proposal + specs
- Subagent при спавне получает путь к spec.md
- После завершения — archive

**Не входит:**
- SDD-Developer как отдельная сущность (REM-198)
- Pre-commit hook (REM-197)
- Изменение структуры OpenSpec

---

## 3. Requirements

### 3.1 Spec-First Workflow

When the Orchestrator receives a task via `/оркестр <task>`, the Orchestrator SHALL:

1. Create an OpenSpec change: `openspec new change <task-name>`
2. Write `proposal.md` — why this task, what problem it solves
3. Write `specs/*.md` — minimum 3 requirements with SHALL keyword
4. Write `design.md` — how it will be structured
5. Write `tasks.md` — checklist for subagent
6. Spawn subagent with link to `tasks.md`
7. After implementation — run `openspec archive <name> --yes`

### 3.2 Orchestrator Prompt Change

The Orchestrator prompt SHALL include this workflow:

```
## Spec-First Workflow

При получении новой задачи:

1. Если задача новая (не continuation):
   - Создай change: `openspec new change <имя-из-задачи>`
   - Напиши proposal.md (зачем?)
   - Напиши specs/*.md — минимум 3 requirements с SHALL
   - Напиши design.md (как?)
   - Напиши tasks.md (чеклист)
   - Запусти subagent-ов с ссылкой на tasks.md

2. После завершения subagent-ов:
   - Проверь результат
   - `openspec validate <change>`
   - `openspec archive <change> --yes`
```

### 3.3 Subagent получает Spec

When a subagent is spawned for a change, the Orchestrator SHALL pass the path to `tasks.md` as part of the task description.

Example:
```
Subagent task: Implement feature X
Spec: openspec/changes/feature-x/specs/feature-x/spec.md
Tasks: openspec/changes/feature-x/tasks.md
```

The subagent SHALL follow tasks.md and reference requirements in code comments.

### 3.4 Requirements Traceability

Each implementation artifact SHALL reference the requirement it satisfies.

Example in code:
```python
# Requirement: jawl-uptime-display.spec.md §3.1
# "The system SHALL display uptime in format Xd Xh Xm"
def format_uptime(start_time: float) -> str:
    ...
```

---

## 4. Workflow Diagram

```
Оркестратор (меняется)
  │
  ├── /оркестр "добавить uptime в JAWL"
  │
  ├── 1. openspec new change jawl-uptime-display
  │
  ├── 2. Пишет proposal.md
  │
  ├── 3. Пишет specs/uptime/spec.md
  │         Requirement: SHALL display uptime in Xd Xh Xm
  │         Requirement: SHALL update every 60 seconds
  │         Requirement: SHALL store start_time in state
  │
  ├── 4. Пишет design.md
  │
  ├── 5. Пишет tasks.md
  │         - [ ] Add uptime module
  │         - [ ] Add bottom-bar rendering
  │         - [ ] Add timer
  │
  ├── 6. Spawn subagent: "implement tasks.md"
  │
  └── 7. Archive: openspec archive jawl-uptime-display --yes
              │
              └── specs/uptime/spec.md → merged to openspec/specs/
```

---

## 5. Acceptance Criteria

- [ ] ORCHESTRATOR_PROMT.md содержит spec-first workflow
- [ ] При `/оркестр <task>` создаётся change + все artifacts
- [ ] Subagent получает tasks.md и следует ему
- [ ] Requirements traceable в коде (# Requirement: spec.md §3.1)
- [ ] После выполнения — archive
- [ ] Specs мерджатся в openspec/specs/

---

## 6. Open Questions

1. **Минимум requirements** — 3 достаточно или нужно больше?
2. **Кто пишет specs** — Оркестратор (я) всегда, или иногда можно пропустить для мелких задач?
3. **Subagent reference** — передавать путь к spec.md или копировать content в task description?
