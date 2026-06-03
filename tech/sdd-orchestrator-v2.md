---
title: "SDD: Оркестратор v2 — SDD Integration"
description: "Интеграция OpenSpec/SDD workflow в Оркестратор. Multi-layer SDD, QA Gate, Traceability."
tags: [SDD, OpenSpec, Orchestrator, Requirements, Traceability]
related: [[openspec]], [[openspec-usage]], [[sdd-openspec-orchestrator]], [[tech/sdd-orchestrator-v2]]
---

# SDD: Оркестратор v2 — SDD Integration

**Status:** Draft → Ready for Implementation  
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

### Не входит (пока):
- Pre-commit hook (REM-197)
- Подключение к реальному проекту (REM-195)
- SDD Developer как отдельная сущность с собственным identity (REM-198)

---

## 3. Requirements

### 3.1 OpenSpec Integration

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
└── ... (код проекта)
```

### 3.2 Multi-Layer SDD

For each development stage, the Orchestrator SHALL create a separate OpenSpec change with layered specs:

**Layer 0: Proposal**
- Зачем этот проект/этап?
- Какой problem решает?
- What is NOT in scope

**Layer 1: Requirements** (только для этапа требований)
- Все requirements с SHALL/MUST
- Acceptance criteria
- Edge cases

**Layer 2: System Design** (только для этапа системного анализа)
- Архитектура
- Компоненты и их ответственность
- API endpoints (если есть)

**Layer 3: Implementation** (только для этапа разработки)
- Конкретные файлы и модули
- Interfaces
- Реализация §N из requirements

Each layer's output is stored in:
```
openspec/changes/<project>-<stage>/
├── proposal.md          # L0
├── specs/
│   ├── requirements.md # L1
│   └── system.md       # L2
├── design.md           # L2 (summary)
└── tasks.md            # L3
```

### 3.3 SDD Developer Agent

The Orchestrator SHALL use a specialized **SDD Developer** agent for the spec-first phase.

**Agent Definition:** `09_SDD_DEVELOPER.md` (in `Работа_в_оркестре/АГЕНТЫ/`)

**When spawned:**
```javascript
sessions_spawn({
  task: `Создай OpenSpec change для: <описание задачи>
  
  Контекст проекта:
  - OpenSpec initialized: <path>
  - Предыдущие этапы: <список change-ов>
  
  Инструкции:
  1. openspec new change <name>
  2. Напиши proposal.md
  3. Напиши specs/*.md (минимум 3 requirements с SHALL)
  4. Напиши design.md
  5. Напиши tasks.md
  
  Правила:
  - Requirements — ТОЛЬКО на английском с SHALL/MUST
  - Scenario — можно на русском
  - После завершения — передай пути к файлам
  `,
  label: "sdd-developer-<project>-<stage>",
  runtime: "subagent"
});
```

**SDD Developer не пишет код.** Он только архитектор требований.

### 3.4 Orchestrator as QA Gate

Before passing specs to an implementation agent, the Orchestrator SHALL validate:

| Check | Rule |
|-------|------|
| SHALL/MUST | Каждый requirement содержит SHALL или MUST |
| Completeness | Минимум 3 requirements |
| Consistency | Нет противоречий с предыдущими этапами |
| Traceability | Каждый task привязан к §N |

**If validation fails:**
```
❌ SDD Developer: Spec validation failed
  - §3缺少 SHALL/MUST
  - §5: Противоречие с §2 из предыдущего этапа
  → Вернуть на доработку SDD Developer
```

**If validation passes:**
```
✅ Spec validation passed
  → Передать tasks.md реализующему агенту
```

### 3.5 Requirements Traceability

Every requirement SHALL be traceable:

**In code:**
```python
## Requirement: auth.spec.md §3.1
# "The system SHALL validate token on each request"
def validate_token(token: str) -> bool:
    ...
```

**In Linear task title:**
```
[SDD] JAWL-auth: §1.Requirements → §2.System → §3.Implementation
```

**In commits:**
```
feat(auth): implement token validation §3.1
```

### 3.6 Archive Workflow

After each stage is completed and validated:

```bash
openspec validate <change-name>
openspec archive <change-name> --yes
```

This merges specs into `openspec/specs/<feature-name>/`.

### 3.7 Hybrid Context Passing

When spawning an agent, the Orchestrator SHALL pass:

```javascript
attachments: [
  { name: "ОБЩИЕ_ПРАВИЛА.md", content: read("...") },
  { name: "ПРАВИЛА.md", content: read("...") },
  {
    name: "SDD_CONTEXT.txt",
    content: `
## Specs to read (from previous layers):
- L0-proposal: <path/to/proposal.md>
  Summary: Пользователь хочет X для решения проблемы Y

- L1-requirements: <path/to/requirements.md>
  Summary: 5 requirements, including §3.1 "SHALL validate token"

- L2-system: <path/to/system.md>
  Summary: Token-based auth с storage в config

Read these files before starting work.
    `
  }
]
```

Files are read by the agent itself; the Orchestrator passes paths + summaries.

---

## 4. Architecture

### 4.1 Full v2 Workflow

```
Пользователь: "хочу auth в JAWL"
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│  Orchestrator (QA Gate)                          │
│                                                  │
│  1. Linear: создать issue                        │
│  2. openspec init (если новый проект)            │
│  3. SDD Developer (spec-first)                  │
└─────────────────────────────────────────────────┘
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
┌──────────────────┐  ┌──────────────────┐
│ SDD Developer    │  │ SDD Developer     │
│ (Requirements)  │  │ (System Design)  │
│                  │  │                  │
│ proposal.md      │  │ system.md        │
│ requirements.md  │  │ design.md        │
│ tasks.md         │  │ tasks.md         │
└──────────────────┘  └──────────────────┘
          │                   │
          └─────────┬─────────┘
                    ▼
┌─────────────────────────────────────────────────┐
│  Orchestrator: QA Gate                           │
│                                                  │
│  ✓ §1-§5 содержат SHALL/MUST?                   │
│  ✓ Нет противоречий между этапами?               │
│  ✓ Каждый task привязан к §N?                   │
└─────────────────────────────────────────────────┘
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
┌──────────────────┐  ┌──────────────────┐
│ Dev-Backend      │  │ Dev-Frontend      │
│                  │  │                  │
│ Читает:          │  │ Читает:          │
│ - tasks.md       │  │ - tasks.md       │
│ - requirements.md│  │ - requirements.md│
│                  │  │ - system.md      │
│ Пишет:           │  │                  │
│ # §3.1 реализован│  │ Пишет:           │
└──────────────────┘  └──────────────────┘
          │                   │
          └─────────┬─────────┘
                    ▼
┌─────────────────────────────────────────────────┐
│  Orchestrator: Validate + Archive                 │
│                                                  │
│  openspec validate <change>  → ✅               │
│  openspec archive <change> --yes                 │
│       → specs → merged to openspec/specs/        │
│                                                  │
│  Linear: issue done                              │
└─────────────────────────────────────────────────┘
```

### 4.2 File Structure (per project)

```
projects/JAWL/
├── openspec/
│   ├── config.yaml
│   ├── specs/                      # ARCHIVE: все requirements
│   │   ├── auth/
│   │   │   └── spec.md           # §1-§5 после archive
│   │   └── memory/
│   │       └── spec.md
│   └── changes/                   # ACTIVE
│       ├── jawl-auth/
│       │   ├── proposal.md
│       │   ├── specs/
│       │   │   ├── requirements.md
│       │   │   └── system.md
│       │   ├── design.md
│       │   └── tasks.md
│       └── archive/
│           └── 2026-05-04-jawl-auth/
└── src/
    ├── auth/
    │   └── token.py              # §3.1 реализован
    └── ...
```

---

## 5. Agent Definitions

### 5.1 SDD Developer (New Agent)

File: `Работа_в_оркестре/АГЕНТЫ/09_SDD_DEVELOPER.md`

**Role:** Spec-first architect. Never writes implementation code.

**Skills:**
- OpenSpec CLI
- RFC 2119 requirements writing
- System design patterns
- Task decomposition

**Workflow:**
1. Read context (previous layers' specs)
2. Create OpenSpec change
3. Write proposal.md (L0)
4. Write requirements.md (L1) — minimum 3 with SHALL/MUST
5. Write system.md (L2)
6. Write tasks.md (L3)
7. Self-validate: all requirements have SHALL/MUST
8. Return file paths to Orchestrator

### 5.2 Updated Agent Workflows

All existing agents (Backend, Frontend, etc.) SHALL be updated to:

**Before starting work:**
```python
## Read and understand specs
spec_files = read_from_attachments("SDD_CONTEXT.txt")
for path in spec_files:
    read(path)

## Identify relevant requirements
# §1, §2, §3...
```

**During implementation:**
```python
## Every significant code block references a requirement
## Requirement: auth.spec.md §3.1
# "The system SHALL validate token on each request"
def validate_token(token: str) -> bool:
    ...
```

**After completion:**
```python
## Self-check: did I cover all §N from tasks.md?
## If §4 is missing → implement it before declaring done
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

- Spec: [requirements.md](path/to/requirements.md) — §1-§5
- System: [system.md](path/to/system.md)
- Tasks: [tasks.md](path/to/tasks.md)

## Traceability
- §1: Implemented in auth/token.py §1
- §2: Implemented in auth/middleware.py §2
```

---

## 7. OpenSpec CLI Usage

### Init
```bash
cd projects/<name>
openspec init --tools opencode
```

### Create change
```bash
openspec new change <project>-<stage>
## Example: openspec new change jawl-auth
```

### Get instructions
```bash
openspec instructions proposal --change jawl-auth
openspec instructions specs --change jawl-auth
openspec instructions design --change jawl-auth
openspec instructions tasks --change jawl-auth
```

### Validate
```bash
openspec validate jawl-auth
## Must pass: all requirements have SHALL/MUST
```

### Archive
```bash
openspec archive jawl-auth --yes
## Merges specs to openspec/specs/
```

---

## 8. Acceptance Criteria

- [ ] New projects: `openspec init` run automatically
- [ ] Each stage: SDD Developer creates change with 4 artifacts
- [ ] Each requirement: contains SHALL or MUST (RFC 2119)
- [ ] Orchestrator: validates specs before passing to agents
- [ ] Code: references §N from requirements
- [ ] Linear: issue title contains § references
- [ ] After completion: `openspec archive` merges specs
- [ ] SDD Developer: never writes implementation code
- [ ] Hybrid context: paths + summaries passed to agents
- [ ] Backward compatible: existing Linear workflow still works

---

## 9. Migration from v1

**Existing projects:** Continue with v1 workflow. SDD integration is opt-in for new projects.

**New projects:** Use v2 with SDD from the start.

**Trigger for SDD mode:**
- Explicit: `/оркестр sdds <задача>`
- Or: automatic for projects with `openspec/` folder

---

## 10. Open Questions (resolved)

| Question | Resolution |
|----------|-----------|
| Separate subagent or nested? | Separate subagent (SDD Developer is isolated) |
| Who implements? | Implementation agents, not SDD Developer |
| How many parallel agents? | Max 2-3 (existing limit) |
| Spec files in context or paths? | Hybrid: paths + summaries |
| What if not enough info? | Orchestrator asks user before spawning SDD |
| Auto or on-command? | On-command: `/оркестр sdds <task>` |
