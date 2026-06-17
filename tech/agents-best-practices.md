---
description: Универсальный провайдеро-независимый Agent Skill с best practices для проектирования, аудита и рефакторинга агентных систем
tags: [agents, best-practices, architecture, safety, skills, harness]
related: [[tech/skillopt]]
source: https://github.com/DenisSergeevitch/agents-best-practices
author: Denis Shiryaev
license: MIT
created: 2026-05-27
updated: 2026-05-27
---

# Agents Best Practices

Универсальный, провайдеро-независимый **Agent Skill** для проектирования, генерации MVP-блупринтов, аудита, рефакторинга и объяснения агентных обвязок (harnesses).

**Ключевая философия:** «Модель предлагает действия; обвязка проверяет, авторизует, исполняет, записывает и возвращает наблюдения.»

## Структура репозитория

```references/```
- `mvp-agent-blueprint.md` — MVP-блупринт
- `architecture.md` — компонентная модель обвязки
- `agentic-loop.md` — агентный цикл, инварианты, бюджеты
- `tools-and-permissions.md` — дизайн инструментов, риски
- `planning-and-goals.md` — режим планирования
- `context-memory-compaction.md` — контекст, память, компактизация
- `prompt-caching-and-cost.md` — кэширование, контроль стоимости
- `skills-and-connectors.md` — Agent Skills, MCP
- `system-prompts-instructions.md` — иерархия инструкций
- `provider-api-patterns.md` — OpenAI, Anthropic, API
- `security-evals-observability.md` — безопасность, эвалы
- `agent-legibility-feedback-loops.md` — читаемость среды
- `checklists.md` — чеклисты
- `coverage-audit.md` — проверка покрытия тем

## Ключевые концепты

### 1. Агентный цикл (provider-agnostic)
```
while not done:
  build context → call model → validate → check permissions → execute → append results → compact
```

### 2. Инструменты — узкие и типизированные
**Плохо:** `execute_anything(command)`  
**Хорошо:** `search_policy_docs(query)`, `draft_customer_email(case_id, tone)`

Каждый инструмент: схема, риск-класс, permission policy, timeout, лимит, retry policy.

### 3. Риск-классификация
- read_only, search_only, compute_only, draft_only
- write_internal, write_external, financial, communication
- identity_access, destructive, privileged_admin

### 4. Draft vs Commit
Опасные действия разделены на два инструмента: `draft_*` (автономно) и `commit_*` (требует approval).

### 5. Планирование
Read-only режим сбора информации. План — долговечный артефакт (не в промпте).

### 6. Авто-компактизация
Не разговорное сжатие, а **операционный handoff**: цель, ограничения, план, approvals, ключевые факты.

### 7. Кэширование промптов
Стабильный префикс (инструкции, схемы) + динамический суффикс (timestamp, результаты поиска).

### 8. Иерархия инструкций
Provider Policy → Org Policy → Product Instructions → Agent Role → Workspace → User Task → Plan → Observations → Retrieved Content (недоверенные данные)

### 9. Safety
Input guardrails → Context guardrails → Schema guardrails → Tool guardrails → Permission guardrails → Output guardrails → Trace guardrails

## Установка
- `npx skills add DenisSergeevitch/agents-best-practices -g`
- Копирование промпта агенту
- Ручная установка в `~/.codex/skills/` или `~/.claude/skills/`
