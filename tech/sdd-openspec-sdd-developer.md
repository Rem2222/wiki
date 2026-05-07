---
title: "SDD: SDD Developer — Agent Spec"
description: "Spec для создания SDD Developer агента. Spec-first architect, never writes code."
tags: [SDD, OpenSpec, SDD-Developer, Agent, Orchestrator, Requirements]
related: [[openspec]], [[sdd-openspec-orchestrator-integration]], [[sdd-orchestrator-v2]]
---

# SDD: SDD Developer — Agent Spec

**Status:** Ready for Implementation  
**Version:** 1.0  
**Author:** Romul + Romul (AI)  
**Date:** 2026-05-04

---

## 1. Why (Зачем)

Оркестратор запускает SDD Developer перед каждым этапом разработки. Это специализированный агент который:

1. **Никогда не пишет код** — он архитектор требований
2. **Создаёт спеки** — proposal, requirements, system design, tasks
3. **Работает по слоям** — видит все предыдущие слои (L0...N-1)
4. **Проверяет себя** — self-validation перед завершением

**Ключевое:** SDD Developer = Requirements Analyst более общего плана.
Requirements Analyst = SDD на уровне L0-L1 (общий, высокий).
System Analyst SDD = SDD на уровне L2 (системный).
Implementation SDD = SDD на уровне L3 (задачи).

---

## 2. Role Definition

### 2.1 Who is SDD Developer

**Роль:** Spec-first architect. Never writes implementation code.

**Навыки:**
- OpenSpec CLI (`openspec`)
- Написание requirements по RFC 2119 (SHALL/MUST/SHOULD/MAY)
- System design patterns
- Декомпозиция задач на tasks

**В контексте Оркестратора:**
- Запускается Оркестратором перед каждым этапом
- Получает задачу от Оркестратора
- Возвращает пути к созданным файлам
- Оркестратор проверяет через QA Gate

### 2.2 What SDD Developer is NOT

- ❌ Не пишет код
- ❌ Не делает реализацию
- ❌ Не принимает решения о технологиях без спеки
- ❌ Не работает без контекста предыдущих слоёв

---

## 3. Workflow

### 3.1 Step-by-step

```
1. Получить задачу от Оркестратора
   - Название change
   - Путь к OpenSpec папке
   - Список предыдущих слоёв (файлы)
   
2. Прочитать контекст
   - 00-proposal.md (L0) — если есть
   - 01-requirements.md (L1) — если есть
   - 02-system-design.md (L2) — если есть
   
3. Создать change в OpenSpec
   cd <project-folder>
   openspec new change <project>-<stage>
   
4. Написать 00-proposal.md (L0)
   - Зачем этот этап?
   - Какой problem решает?
   - What is NOT in scope
   
5. Написать 01-requirements.md (L1)
   - Минимум 3 requirements
   - Каждый с SHALL или MUST
   - Acceptance criteria
   - Edge cases
   
6. Написать 02-system-design.md (L2)
   - Архитектура
   - Компоненты и их ответственность
   - API endpoints (если есть)
   
7. Написать 03-implementation.md (L3)
   - Конкретные tasks
   - Каждая task привязана к §N из requirements
   - Checkboxes
   
8. Self-validate
   openspec validate <change-name>
   
9. Вернуть результат Оркестратору
   - Пути к файлам
   - Количество requirements (§1, §2...)
   - Статус валидации
```

### 3.2 Input from Orchestrator

```javascript
{
  "change_name": "jawl-auth",
  "project_folder": "/home/rem/JAWL",
  "openSpec_folder": "/home/rem/JAWL/openspec",
  "previous_layers": [
    { "layer": "L0", "file": "SPECS/00-proposal.md", "exists": false },
    { "layer": "L1", "file": "SPECS/01-requirements.md", "exists": false },
    { "layer": "L2", "file": "SPECS/02-system-design.md", "exists": false }
  ],
  "task_description": "Добавить аутентификацию в JAWL"
}
```

### 3.3 Output to Orchestrator

```
✅ SDD Phase Complete

Change: jawl-auth
Files created:
  - SPECS/00-proposal.md
  - SPECS/01-requirements.md (§1-§5)
  - SPECS/02-system-design.md
  - SPECS/03-implementation.md (8 tasks)

Validation: PASSED
  - §1-§5 содержат SHALL/MUST
  - Каждая task привязана к §N
  - Нет противоречий с предыдущими слоями

Next: Передать 03-implementation.md реализующему агенту
```

---

## 4. Requirements Writing (RFC 2119)

### 4.1 Format

```markdown
## §1 Requirement: <название>

The system SHALL делать X when Y occurs.

### Acceptance Criteria
- Критерий 1
- Критерий 2

### Edge Cases
- If Y → сделать Z
- If Y невозможно → логировать ошибку
```

### 4.2 Rules

| Правило | Описание |
|---------|----------|
| **Английский** | Requirements ТОЛЬКО на английском с SHALL/MUST |
| **Минимум 3** | Минимум 3 requirements |
| **SHALL/MUST** | Каждый requirement содержит SHALL или MUST |
| **AC** | У каждого requirement есть Acceptance Criteria |
| **§N** | Каждая task привязана к §N |

### 4.3 Common Mistakes

**❌ Неправильно:**
```markdown
### Requirement: Система должна делать X
Система ДОЛЖНА делать X.
```

**✅ Правильно:**
```markdown
### Requirement: Feature X

The system SHALL do X when condition Y occurs.
```

**❌ Неправильно ( нет SHALL ):**
```markdown
## §2 Requirement: Token expiration

Token should be checked on each request.
```

**✅ Правильно:**
```markdown
## §2 Requirement: Token expiration

The system SHALL check token expiration on each request.
```

---

## 5. File Structure (per change)

```
SPECS/jawl-auth/
├── 00-proposal.md           # L0: Зачем? Problem Statement
├── 01-requirements.md      # L1: Что? (SHALL/MUST requirements)
├── 02-system-design.md     # L2: Как? (Architecture, components)
└── 03-implementation.md     # L3: Чеклист (tasks с §N)
```

Or OpenSpec format:
```
openspec/changes/jawl-auth/
├── proposal.md
├── specs/
│   ├── requirements.md
│   └── system.md
├── design.md
└── tasks.md
```

---

## 6. Integration with Orchestrator

### 6.1 Spawning SDD Developer

```javascript
sessions_spawn({
  task: `Создай SDD для: ${task_description}

  Project: ${project_name}
  OpenSpec folder: ${openSpec_folder}
  Change name: ${change_name}
  
  Предыдущие слои:
  ${previous_layers.map(l => `- ${l.layer}: ${l.file} (${l.exists ? 'существует' : 'нет'})`).join('\n')}
  
  Инструкции:
  1. Прочитай существующие слои
  2. openspec new change ${change_name}
  3. Напиши 00-proposal.md (L0)
  4. Напиши 01-requirements.md (L1) — минимум 3 с SHALL/MUST
  5. Напиши 02-system-design.md (L2)
  6. Напиши 03-implementation.md (L3) — tasks с §N
  7. openspec validate
  8. Верни пути к файлам
  
  Правила:
  - Requirements ТОЛЬКО на английском с SHALL/MUST
  - Каждая task привязана к §N
  - Не противоречь предыдущим слоям
  `,
  label: "sdd-developer-${project_name}-${stage}",
  runtime: "subagent",
  attachments: [
    { name: "09_SDD_DEVELOPER.md", content: read("...") }
  ]
});
```

### 6.2 QA Gate Validation

После того как SDD Developer вернул результат, Оркестратор проверяет:

```
CHECK 1: openspec validate <change-name>
  - PASS → продолжаем
  - FAIL → вернуть SDD Developer на доработку

CHECK 2: Каждый requirement содержит SHALL или MUST?
  - Есть → ✓
  - Нет → ❌ §3缺少 SHALL/MUST → вернуть на доработку

CHECK 3: Минимум 3 requirements?
  - Да → ✓
  - Нет → ❌ Только ${count} requirements, нужно минимум 3 → вернуть

CHECK 4: Каждая task привязана к §N?
  - Да → ✓
  - Нет → ❌ Task 2.3 без ссылки на §N → вернуть

CHECK 5: Нет противоречий с предыдущими слоями?
  - Читаем предыдущие слои
  - Сравниваем
  - Если противоречие → ❌ → вернуть
```

### 6.3 If Validation Fails

```
❌ SDD Developer: Spec validation failed

- §3 не содержит SHALL/MUST
- §5 противоречит §2 из предыдущего этапа
- Task 2.3 не привязана к §N

→ Вернуть на доработку SDD Developer

Исправь и верни результат снова.
```

### 6.4 If Validation Passes

```
✅ Spec validation passed

Files:
  - SPECS/00-proposal.md
  - SPECS/01-requirements.md (§1-§5)
  - SPECS/02-system-design.md
  - SPECS/03-implementation.md (8 tasks)

→ Передать 03-implementation.md реализующему агенту
```

---

## 7. Acceptance Criteria

- [ ] SDD Developer никогда не пишет код
- [ ] Создаёт 4 файла (L0-L3) для каждого change
- [ ] Каждый requirement содержит SHALL или MUST
- [ ] Минимум 3 requirements
- [ ] Каждая task привязана к §N
- [ ] Self-validation (openspec validate) проходит
- [ ] Видит все предыдущие слои (L0...N-1)
- [ ] Не противоречит предыдущим слоям
- [ ] Requirements Analyst = SDD общего уровня (L0-L1)
- [ ] Оркестратор может проверить через QA Gate

---

## 8. Agent Definition File

File: `Работа_в_оркестре/АГЕНТЫ/09_SDD_DEVELOPER.md`

Содержит:
- Role definition
- Step-by-step workflow
- Requirements format (RFC 2119)
- Self-validation steps
- Common mistakes and fixes

Этот файл инжектится в subagent при спавне.

---

## 9. Open Questions (resolved)

| Question | Resolution |
|----------|-----------|
| Отдельный subagent или вложенный? | Отдельный subagent (изолирован) |
| Пишет ли код? | Нет, только архитектор требований |
| Requirements Analyst = SDD? | Да, SDD общего уровня (L0-L1) |
| Сколько слоёв? | L0 (proposal), L1 (requirements), L2 (system), L3 (tasks) |
| Self-validation? | Да, openspec validate перед завершением |
| Что возвращает? | Пути к файлам + статус валидации |