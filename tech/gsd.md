---
description: SDD-фреймворк «Get Shit Done» — интервью-ориентированный подход к SDD
tags: [sdd, framework, specification, claude-code]
related: [[concepts/sdd]] [[tech/bmad-method]] [[tech/openspec]] [[tech/spec-kit]]
---

# GSD — Get Shit Done

**GitHub (Redux/активный):** https://github.com/open-gsd/get-shit-done-redux
**GitHub (оригинал):** https://github.com/gsd-build/get-shit-done

Spec-Driven Development фреймворк. Философия: **«сложность в системе, а не в твоём workflow»**.

## Фишка

Самый внятный процесс интервью: GSD задаёт вопросы → ты отвечаешь → на выходе готовая спецификация.

## Особенности

- **Интервью для прояснения задачи** — задаёт вопросы, вы отвечаете → получается точное описание
- **Лучшая декомпозиция** — разбиение на этапы практически не требует правок
- **Проверка спецификации** на внутреннюю непротиворечивость и полноту

## Минусы

- **Утомительное интервью** — робот задаёт «тупые» вопросы, процесс длинный
- **Сложно читать документы** — специфический формат и система перекрёстных ссылок
- **Требует постоянного внимания** — GSD может встать в ожидании ответа в любой момент

## Оригинал vs Redux

| | Оригинал (gsd-build) | Redux (open-gsd) |
|---|---|---|
| Язык | Bash | TypeScript/Node.js |
| AI-таргет | Claude (Anthropic) | AI-agnostic |
| Архитектура | Монолитные промпты | Федеративные агенты (Explorer, Designer, Developer, Reviewer) |
| Состояние | Эфемерно | Persistent `.sdd/` с build cache |
| Лицензия | Restrictive | Open-source |

## Агенты GSD (33 шт.)

GSD Redux использует **федеративную мульти-агентную архитектуру**: тонкие оркестраторы (workflow-файлы) спавнят специализированных агентов с **чистыми контекстными окнами** (до 200K токенов). Каждый агент имеет узкую роль, ограниченный набор инструментов и производит конкретные артефакты.

### Принципы

| Принцип | Описание |
|---------|----------|
| **Fresh Context** | Каждый агент получает чистый контекст — никакого «контекстного гниения» от накопленного чата |
| **Thin Orchestrators** | Workflow-файлы не делают тяжёлой работы: загружают контекст, спавнят агентов, собирают результаты |
| **Least Privilege** | Checkers — read-only, Researchers — веб-доступ, Executors — Edit без веба |

### Категории

| Категория | Кол-во | Агенты |
|-----------|--------|--------|
| Исследователи (Researchers) | 3 | project-researcher, phase-researcher, ui-researcher |
| Анализаторы (Analyzers) | 2 | assumptions-analyzer, advisor-researcher |
| Синтезаторы (Synthesizers) | 1 | research-synthesizer |
| Планировщики (Planners) | 1 | planner |
| Роадмапперы (Roadmappers) | 1 | roadmapper |
| Исполнители (Executors) | 1 | executor |
| Чекеры (Checkers) | 3 | plan-checker, integration-checker, ui-checker |
| Верификаторы (Verifiers) | 1 | verifier |
| Аудиторы (Auditors) | 3 | nyquist-auditor, ui-auditor, security-auditor |
| Мапперы (Mappers) | 1 | codebase-mapper |
| Дебаггеры (Debuggers) | 1 | debugger |
| Документаторы (Doc Writers) | 2 | doc-writer, doc-verifier |
| Профилировщики (Profilers) | 1 | user-profiler |

### 21 Primary Agent (полные role cards)

| Агент | Роль | Спавнится командой | Инструменты | Цвет |
|-------|------|-------------------|-------------|------|
| **gsd-project-researcher** | Исследует экосистему домена перед созданием роадмапа (стек, фичи, архитектура, pitfalls) | `/gsd-new-project`, `/gsd-new-milestone` | Read, Write, Bash, Grep, Glob, WebSearch, WebFetch, mcp | cyan |
| **gsd-phase-researcher** | Исследует реализацию конкретной фазы перед планированием | `/gsd-plan-phase` | Read, Write, Bash, Grep, Glob, WebSearch, WebFetch, mcp | — |
| **gsd-ui-researcher** | Создаёт UI design contract (UI-SPEC.md) для фронтенд-фаз | `/gsd-ui-phase` | Read, Write, Bash, Grep, Glob, WebSearch, WebFetch, mcp | `#E879F9` (fuchsia) |
| **gsd-assumptions-analyzer** | Анализирует кодбазу фазы, возвращает структурированные предположения с evidence и confidence | `discuss-phase-assumptions` workflow | Read, Bash, Grep, Glob | cyan |
| **gsd-advisor-researcher** | Исследует одно «серое» решение в режиме advisor, возвращает таблицу сравнения | `discuss-phase` (advisor mode) | Read, Bash, Grep, Glob, WebSearch, WebFetch, mcp | cyan |
| **gsd-research-synthesizer** | Собирает результаты параллельных исследователей в единый SUMMARY.md | `/gsd-new-project` | Read, Write, Bash | purple |
| **gsd-planner** | Создаёт исполняемые планы фаз с task breakdown и goal-backward verification | `/gsd-plan-phase`, `/gsd-quick` | Read, Write, Bash, Glob, Grep, WebFetch, mcp | green |
| **gsd-roadmapper** | Создаёт роадмап проекта с разбивкой на фазы и маппингом требований | `/gsd-new-project` | Read, Write, Bash, Glob, Grep | purple |
| **gsd-executor** | Исполняет планы с атомарными коммитами, обработкой отклонений и checkpoint'ами | `/gsd-execute-phase`, `/gsd-quick` | Read, Write, Edit, Bash, Grep, Glob | yellow |
| **gsd-plan-checker** | Верифицирует планы по 8 измерениям (покрытие требований, атомарность, зависимости и др.) | `/gsd-plan-phase` (verification loop) | Read, Bash, Glob, Grep | green |
| **gsd-integration-checker** | Верифицирует кросс-фазовую интеграцию и end-to-end сценарии | `/gsd-audit-milestone` | Read, Bash, Grep, Glob | blue |
| **gsd-ui-checker** | Валидирует UI-SPEC.md на соответствие quality dimensions | `/gsd-ui-phase` (validation loop) | Read, Bash, Glob, Grep | `#22D3EE` (cyan) |
| **gsd-verifier** | Целевая верификация фазы через goal-backward анализ (PASS/FAIL) | `/gsd-execute-phase` | Read, Write, Bash, Grep, Glob | green |
| **gsd-nyquist-auditor** | Заполняет пробелы Nyquist-валидации генерацией тестов (не трогает реализацию) | `/gsd-validate-phase` | Read, Write, Edit, Bash, Grep, Glob | — |
| **gsd-ui-auditor** | Ретроактивный визуальный аудит по 6 pillar'ам (копирайтинг, визуалы, цвет, типографика, отступы, UX) | `/gsd-ui-review` | Read, Write, Bash, Grep, Glob | `#F472B6` (pink) |
| **gsd-codebase-mapper** | Исследует кодбазу и пишет структурированные analysis-документы (7 шт.) | `/gsd-map-codebase` | Read, Bash, Grep, Glob, Write | cyan |
| **gsd-debugger** | Расследует баги научным методом с персистентным состоянием (6 стадий lifecycle) | `/gsd-debug`, `/gsd-verify-work` | Read, Write, Edit, Bash, Grep, Glob, WebSearch | orange |
| **gsd-user-profiler** | Анализирует сессионные сообщения по 8 behavioral dimensions → профиль разработчика | `/gsd-profile-user` | Read | magenta |
| **gsd-doc-writer** | Пишет и обновляет проектную документацию (10 doc types) | `/gsd-docs-update` | Read, Write, Bash, Grep, Glob | purple |
| **gsd-doc-verifier** | Верифицирует фактические утверждения в документации против живой кодбазы | `/gsd-docs-update` | Read, Write, Bash, Grep, Glob | orange |
| **gsd-security-auditor** | Верифицирует, что threat mitigations из PLAN.md реализованы в коде | `/gsd-secure-phase` | Read, Write, Edit, Bash, Glob, Grep | `#EF4444` (red) |

### 12 Advanced / Specialized Agents

Эти агенты используются специализированными workflow и несут полный frontmatter в своих `agents/gsd-*.md` файлах.

| Агент | Роль | Спавнится | Цвет |
|-------|------|-----------|------|
| **gsd-pattern-mapper** | Картирует новые файлы на ближайшие существующие аналоги → PATTERNS.md для planner'а | `/gsd-plan-phase` (между research и planning) | magenta |
| **gsd-debug-session-manager** | Запускает полный цикл `/gsd-debug` (checkpoint + continuation) в изолированном контексте | `/gsd-debug` | orange |
| **gsd-code-reviewer** | Адверсариальный ревью кода: баги, security, качество → REVIEW.md | `/gsd-code-review` | `#F59E0B` (amber) |
| **gsd-code-fixer** | Применяет фиксы из REVIEW.md с атомарными коммитами → REVIEW-FIX.md | `/gsd-code-review --fix` | `#10B981` (emerald) |
| **gsd-ai-researcher** | Исследует документацию AI-фреймворка → AI-SPEC.md (§3–§4b) | `/gsd-ai-integration-phase` | `#34D399` (green) |
| **gsd-domain-researcher** | Поверхностные domain-критерии оценки AI-системы → AI-SPEC.md (§1b) | `/gsd-ai-integration-phase` | `#A78BFA` (violet) |
| **gsd-eval-planner** | Проектирует стратегию оценки AI-фазы → AI-SPEC.md (§5–§7) | `/gsd-ai-integration-phase` | `#F59E0B` (amber) |
| **gsd-eval-auditor** | Ретроактивный аудит покрытия eval'ами → EVAL-REVIEW.md (COVERED/PARTIAL/MISSING) | `/gsd-eval-review` | `#EF4444` (red) |
| **gsd-framework-selector** | Интерактивная decision-matrix (≤6 вопросов) с ранжированием AI-фреймворков | `/gsd-ai-integration-phase` | `#38BDF8` (sky blue) |
| **gsd-intel-updater** | Пишет структурированные intel-файлы (JSON + Markdown) в `.planning/intel/` для query-доступа | `/gsd-map-codebase --query` | cyan |
| **gsd-doc-classifier** | Классифицирует planning-документ (ADR/PRD/SPEC/DOC/UNKNOWN), пишет JSON | `/gsd-ingest-docs` (fan-out) | yellow |
| **gsd-doc-synthesizer** | Синтезирует классифицированные документы в единый контекст с детекцией конфликтов | `/gsd-ingest-docs` (fan-in) | orange |

### Матрица инструментов (Primary Agents)

| Агент | Read | Write | Edit | Bash | Grep | Glob | WebSearch | WebFetch | MCP |
|-------|------|-------|------|------|------|------|-----------|----------|-----|
| project-researcher | ✓ | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| phase-researcher | ✓ | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ui-researcher | ✓ | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| assumptions-analyzer | ✓ | | | ✓ | ✓ | ✓ | | | |
| advisor-researcher | ✓ | | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| research-synthesizer | ✓ | ✓ | | ✓ | | | | | |
| planner | ✓ | ✓ | | ✓ | ✓ | ✓ | | ✓ | ✓ |
| roadmapper | ✓ | ✓ | | ✓ | ✓ | ✓ | | | |
| executor | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | |
| plan-checker | ✓ | | | ✓ | ✓ | ✓ | | | |
| integration-checker | ✓ | | | ✓ | ✓ | ✓ | | | |
| ui-checker | ✓ | | | ✓ | ✓ | ✓ | | | |
| verifier | ✓ | ✓ | | ✓ | ✓ | ✓ | | | |
| nyquist-auditor | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | |
| ui-auditor | ✓ | ✓ | | ✓ | ✓ | ✓ | | | |
| codebase-mapper | ✓ | ✓ | | ✓ | ✓ | ✓ | | | |
| debugger | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | |
| user-profiler | ✓ | | | | | | | | |
| doc-writer | ✓ | ✓ | | ✓ | ✓ | ✓ | | | |
| doc-verifier | ✓ | ✓ | | ✓ | ✓ | ✓ | | | |
| security-auditor | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | |

---

## Установка

Per-project. Для нового проекта — через `claude plugin`:

```bash
claude plugin add open-gsd/get-shit-done-redux
```

## Когда выбирать

✅ **Большая и технически сложная задача**, которую надо доформулировать и доформализовать в процессе.
❌ Простые задачи — интервью будет too much.
