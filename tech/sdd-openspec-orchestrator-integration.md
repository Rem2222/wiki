---
title: "SDD: Orchestrator v2 — Orchestrator Integration"
description: "Spec для доработки Оркестратора с SDD workflow. Orchestrator как QA Gate, multi-layer SDD."
tags: [SDD, OpenSpec, Orchestrator, Requirements, Traceability, QA]
related: [[openspec]], [[sdd-openspec-sdd-developer]], [[sdd-orchestrator-v2]], [[tech/sdd-orchestrator-v2]]
---

# SDD: Orchestrator v2 — Orchestrator Integration

**Status:** Ready for Implementation  
**Version:** 1.0  
**Author:** Romul + Romul (AI)  
**Date:** 2026-05-04

---

## 1. Why (Зачем)

Текущий Оркестратор (v1):
- 8 агентов: Analyst → System → Writer → Reviewer → Backend → Frontend → Tester → Docs
- Linear интеграция
- ByteRover для знаний
- **Нет SDD** — требования не traceable, результат не фиксируется формально

Проблемы v1:
- Requirements размыты между сессиями
- Нет формальной связи между задачей и кодом
- Subagent работает без формального spec
- После завершения — непонятно что было реализовано, а что обсуждалось
- Каждый этап работает изолированно, нет сквозной traceability

**v2 должен:**
- Добавить OpenSpec/SDD слой перед каждым этапом
- Требования = SHALL (RFC 2119)
- Каждый §N требования — traceable в коде
- После архивации — specs мерджатся в единый SPECS/

---

## 2. Scope (Что входит в v2)

### Входит:
1. **OpenSpec инициализация** — `openspec init` в папке проекта
2. **Multi-layer SDD** — L0 → L1 → L2 → L3 (для каждого этапа)
3. **SDD Developer агент** — специализированный subagent для spec-first
4. **Orchestrator как QA Gate** — проверка specs перед передачей агенту
5. **Requirements traceability** — §N в коде и в Linear
6. **Archive workflow** — `openspec archive` после каждого этапа
7. **Hybrid context passing** — файлы + пути + summaries
8. **Layered SDD Developer** — Requirements Analyst = SDD общего плана, более высокий уровень

### Не входит (пока):
- Pre-commit hook (REM-197)
- Подключение к реальному проекту (REM-195)
- SDD Developer как отдельная сущность с собственным identity (REM-198)

---

## 3. Architecture — Крупными мазками

### 3.1 Flow (верхний уровень)

```
Человек → ССД (Requirements) → Аналитик по спекам
       → ССД (System) → Системный Аналитик по спекам
       → ССД (перед каждым этапом) → Агент этого этапа
       → Оркестратор QA Gate
       → archive
```

**Ключевое:** SDD Developer запускается перед КАЖДЫМ этапом. Перед Backend — свой SDD. Перед Frontend — свой. Каждый SDD видит спеки всех предыдущих слоёв.

### 3.2 Multi-layer SDD (детализация)

| Слой | Название | Вход | Выход | Кто читает |
|------|---------|------|-------|------------|
| **L0** | **Проектный SDD** | Задача от человека | Proposal + общие specs проекта | Все слои |
| **L1** | **Requirements SDD** | Proposal + specs проекта | Requirements specs (чё хочет человек) | System SDD, Implementation SDD |
| **L2** | **System SDD** | Requirements specs | System design specs (как сделать) | Implementation SDD, QA Gate |
| **L3** | **Implementation SDD** | System design specs | Tasks + code | Оркестратор QA Gate |

**Requirements Analyst** — это SDD Developer более общего/высокого уровня (слой L0-L1).
Он не пишет код, он описывает "чё хочет человек" в формальных requirements.

### 3.3 Orchestrator как QA Gate

Оркестратор проверяет перед каждым этапом:

| Проверка | Правило |
|----------|---------|
| SHALL/MUST | Каждый requirement содержит SHALL или MUST |
| Completeness | Минимум 3 requirements |
| Consistency | Нет противоречий с предыдущими этапами |
| Traceability | Каждый task привязан к §N |
| Visibility | SDD на слое N видит спеки слоёв 0, 1, 2...N-1 |

**Если не прошло — вернуть SDD Developer на доработку.**

### 3.4 File Naming Convention

```
SPECS/jawl-auth/
├── 00-proposal.md           ← L0: Зачем этот проект?
├── 01-requirements.md      ← L1: Что хочет человек (SHALL/MUST)
├── 02-system-design.md     ← L2: Как сделать архитектурно
└── 03-implementation.md     ← L3: Конкретные tasks
```

Имена файлов по номеру слоя — сразу понятно какой за чем.

---

## 4. Requirements (детализация)

### 4.1 OpenSpec Integration

When a new project is created, the Orchestrator SHALL initialize OpenSpec in the project folder.

```bash
cd ~/.openclaw/workspace/projects/<project-name>
openspec init --tools opencode
```

Resulting structure:
```
projects/<project-name>/
├── openspec/
│   ├── config.yaml
│   ├── specs/                     # Archive: все requirements
│   │   └── <feature-name>/
│   │       └── spec.md
│   └── changes/                  # Active changes
│       ├── <change-1>/
│       └── archive/
├── SPECS/                        # SDD layers
│   ├── 00-proposal.md
│   ├── 01-requirements.md
│   ├── 02-system-design.md
│   └── 03-implementation.md
└── ... (код проекта)
```

### 4.2 Requirements Format (RFC 2119)

Every requirement SHALL use SHALL or MUST:

```markdown
## §1 Requirement: Token validation

The system SHALL validate the token on each request.

### Acceptance Criteria
- Token is present and not expired
- Token signature is valid

### Edge Cases
- If token is missing → return 401
- If token is expired → return 401 with "token expired" message
```

**ПРАВИЛО:** Requirements — ТОЛЬКО на английском с SHALL/MUST. Scenario (WHEN/THEN) — можно на русском.

### 4.3 Requirements Traceability

**В коде:**
```python
## Requirement: auth.spec.md §3.1
# "The system SHALL validate token on each request"
def validate_token(token: str) -> bool:
    ...
```

**В Linear задаче:**
```
[SDD] JAWL-auth: §1.Requirements → §2.System → §3.Implementation
```

**В коммитах:**
```
feat(auth): implement token validation §3.1
```

**Оркестратор при принятии кода проверяет:** каждый §X — покрыт? Если §3.2 не упомянут нигде — возврат агенту.

### 4.4 Hybrid Context Passing

When spawning an agent, the Orchestrator SHALL pass:

```javascript
attachments: [
  { name: "ОБЩИЕ_ПРАВИЛА.md", content: read("...") },
  { name: "ПРАВИЛА.md", content: read("...") },
  {
    name: "SDD_CONTEXT.txt",
    content: `
## Specs to read (from previous layers):
- L0-proposal: <path/to/00-proposal.md>
  Summary: Пользователь хочет X для решения проблемы Y

- L1-requirements: <path/to/01-requirements.md>
  Summary: 5 requirements, including §3.1 "SHALL validate token"

- L2-system: <path/to/02-system-design.md>
  Summary: Token-based auth с storage в config

Read these files before starting work.
    `
  }
]
```

Files are read by the agent itself; the Orchestrator passes paths + summaries.

### 4.5 Archive Workflow

After each stage is completed and validated:

```bash
openspec validate <change-name>
openspec archive <change-name> --yes
```

This merges specs into `openspec/specs/<feature-name>/`.

---

## 5. Orchestrator Promt Changes

### 5.1 New section: SDD WORKFLOW

Добавить в ОРКЕСТРАТОР_ПРОЕКТОВ_PROMT.md секцию SDD WORKFLOW после правил.

### 5.2 Commands

| Команда | Режим | Описание |
|---------|-------|---------|
| `/оркестр <задача>` | v1 | Обычный workflow (8 агентов, Linear) |
| `/оркестр sdds <задача>` | v2 | SDD-режим (spec-first, OpenSpec) |

SDD-режим также автоматический если в проекте есть папка `openspec/`.

### 5.3 QA Gate Checks

Добавить в контроль качества после каждого этапа:

**Если SDD-режим:**
6. ✅ Requirements содержат SHALL/MUST?
7. ✅ Каждый task привязан к §N?
8. ✅ `openspec validate` прошёл?
9. ✅ `openspec archive` выполнен?
10. ✅ Нет противоречий между слоями?

### 5.4 OpenSpec Init

При создании нового проекта:

```bash
## В Linear:
python3 linear_api.py project-create "Название" "Описание"

## В OpenSpec:
cd ~/.openclaw/workspace/projects/<название>
openspec init --tools opencode
```

---

## 6. Integration with Linear

| Linear Entity | OpenSpec Entity | Link |
|--------------|-----------------|------|
| Project | `openspec/` folder | Folder path in issue description |
| Issue | Change | Title: `[SDD] <project>: §L1 → §L2 → §L3` |
| Sub-task | tasks.md item | Checkbox = done |
| Comment | Spec change | Link to spec.md |

**In issue description:**
```markdown
## SDD Context

- Spec: [01-requirements.md](path/to/01-requirements.md) — §1-§5
- System: [02-system-design.md](path/to/02-system-design.md)
- Tasks: [03-implementation.md](path/to/03-implementation.md)

## Traceability
- §1: Implemented in auth/token.py §1
- §2: Implemented in auth/middleware.py §2
```

---

## 7. Acceptance Criteria

- [ ] New projects: `openspec init` run automatically
- [ ] Each stage: SDD Developer creates change with 4 artifacts (L0-L3)
- [ ] Each requirement: contains SHALL or MUST (RFC 2119)
- [ ] Orchestrator: validates specs before passing to agents
- [ ] Code: references §N from requirements
- [ ] Linear: issue title contains § references
- [ ] After completion: `openspec archive` merges specs
- [ ] SDD Developer: never writes implementation code
- [ ] Hybrid context: paths + summaries passed to agents
- [ ] SDD on layer N sees specs from layers 0...N-1
- [ ] Backward compatible: existing Linear workflow still works
- [ ] Requirements Analyst = SDD общего уровня (L0-L1)

---

## 8. Migration from v1

**Existing projects:** Continue with v1 workflow. SDD integration is opt-in for new projects.

**New projects:** Use v2 with SDD from the start.

**Trigger for SDD mode:**
- Explicit: `/оркестр sdds <задача>`
- Or: automatic for projects with `openspec/` folder

---

## 9. Open Questions (resolved)

| Question | Resolution |
|----------|-----------|
| Separate subagent or nested? | Separate subagent (SDD Developer is isolated) |
| Who implements? | Implementation agents, not SDD Developer |
| How many parallel agents? | Max 2-3 (existing limit) |
| Spec files in context or paths? | Hybrid: paths + summaries |
| What if not enough info? | Orchestrator asks user before spawning SDD |
| Auto or on-command? | On-command: `/оркестр sdds <task>` |
| Requirements Analyst = SDD? | Да, SDD общего уровня (более высокий слой) |
| SDD layer N sees previous layers? | Да, каждый SDD читает файлы слоёв 0...N-1 |
| File naming? | 00-proposal, 01-requirements, 02-system, 03-implementation |
