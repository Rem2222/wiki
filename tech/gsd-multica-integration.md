---
description: Интеграция GSD (Get Shit Done) и Multica — мультиагентный фреймворк для структурированной разработки встречает платформу управления AI-агентами.
tags: [gsd, multica, agents, integration, orchestration]
related: [[tech/multica]], [[tech/sdd-orchestrator-v2]], [[tech/heisenberg-team-gpt]]
---

# GSD × Multica: интеграция мультиагентной разработки

**GSD** (Get Shit Done) — мета-промптовый фреймворк для структурированной разработки ПО. Предоставляет 33 специализированных агента (исследователи, планировщики, исполнители, верификаторы, аудиторы, документаторы) и полный пайплайн: требования → исследование → планирование → исполнение → верификация.

**Multica** ([github.com/multica-ai/multica](https://github.com/multica-ai/multica)) — open-source платформа управления AI-агентами. Добавляет слой оркестрации поверх кодинг-агентов: назначение задач через Issues, коллаборация, дашборд, reusable skills.

Интеграция позволяет совместить **структурированную методологию GSD** с **платформенным управлением Multica**: агенты GSD работают внутри Multica-воркспейса, получают задачи через Issues, отчитываются через комментарии, а Multica обеспечивает видимость и координацию.

---

## Зачем объединять GSD и Multica

| Аспект | GSD сам по себе | Multica сама по себе | Вместе |
|--------|-----------------|---------------------|--------|
| **Методология** | Полный SDLC-пайплайн (research → plan → execute → verify) | Нет встроенной методологии | GSD-пайплайн работает внутри Multica |
| **Управление задачами** | Файловая система (`.planning/`) | Issues со статусами, приоритетами, дедлайнами | GSD-фазы как Issues; прозрачный прогресс |
| **Агенты** | 33 специализированных роли | Любые CLI-агенты (Claude Code, Codex, OpenClaw) | GSD-агенты = агенты Multica |
| **Коллаборация** | Последовательный пайплайн | Параллельные агенты, @упоминания, комментарии | Параллельные GSD-агенты с коммуникацией |
| **Видимость** | Файлы в `.planning/` | Дашборд, Issue board, комментарии | Весь прогресс виден в UI Multica |

---

## Архитектура интеграции

```
┌──────────────────────────────────────────────────────⎤
│                   MULTICA                             │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐  │
│  │  Issue Board │   │  Scheduler  │   │  Dashboard  │  │
│  │  (tasks)     │   │  (runs)     │   │  (logs)     │  │
│  └──────┬───────┘   └──────┬──────┘   └─────────────┘  │
│         │                  │                            │
│  ┌──────▼──────────────────▼──────────────────────┐    │
│  │              multica CLI + API                   │    │
│  │  issue get | issue comment add | repo checkout  │    │
│  └──────────────────────┬──────────────────────────┘    │
└─────────────────────────┼──────────────────────────────⎥
                          │
┌─────────────────────────▼──────────────────────────────⎤
│                      GSD                                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐           │
│  │ Research  │   │ Planning │   │Execution │           │
│  │  agents   │   │  agents  │   │  agents  │           │
│  └──────────┘   └──────────┘   └──────────┘           │
│       │               │               │                 │
│  ┌────▼───────────────▼───────────────▼────┐           │
│  │         .planning/ (state files)         │           │
│  │  PROJECT.md, ROADMAP.md, PLAN.md, ...   │           │
│  └──────────────────────────────────────────┘           │
│       │               │               │                 │
│  ┌────▼───────────────▼───────────────▼────┐           │
│  │        gsd CLI + gsd-tools.cjs          │           │
│  └──────────────────────────────────────────┘           │
└────────────────────────────────────────────────────────⎥
```

Интеграция работает на двух уровнях:

### 1. Задачи (Tasks) — Multica Issues как GSD-фазы

Каждая GSD-фаза представляется как Issue в Multica:

- **Issue type** → фаза (research, plan, execute, verify)
- **Status** → todo → in_progress → in_review → done
- **Assignee** → GSD-агент, выполняющий фазу
- **Description** → контекст фазы, ссылки на `.planning/` файлы
- **Parent issue** → привязка к milestone/project

### 2. Исполнение (Execution) — GSD-агенты внутри Multica

GSD-агенты запускаются как кодинг-агенты под управлением Multica:

1. Multica назначает Issue агенту
2. Агент получает в `AGENTS.md` инструкции Multica Runtime (multica CLI) + GSD Agent Card
3. Агент исполняет GSD-пайплайн, используя `gsd` CLI и `multica` CLI
4. Результаты коммитятся в `.planning/` и публикуются в комментарий к Issue

---

## 33 агента GSD: как они вписываются в Multica

GSD поставляет 33 агента с ролями, инструментами и цветовой кодировкой. Каждый может быть зарегистрирован как отдельный агент в Multica.

### Категории агентов (из AGENTS.md)

| Категория | Кол-во | Агенты | Роль в Multica |
|-----------|--------|--------|----------------|
| **Исследователи** | 3 | project-researcher, phase-researcher, ui-researcher | Собирают контекст по задаче; пишут research-документы |
| **Анализаторы** | 2 | assumptions-analyzer, advisor-researcher | Анализируют код и серые зоны; возвращают структурированные решения |
| **Синтезаторы** | 1 | research-synthesizer | Сводят результаты параллельных исследований |
| **Планировщики** | 1 | planner | Декомпозируют задачу в атомарные шаги |
| **Роадмапперы** | 1 | roadmapper | Строят roadmap проекта с фазами |
| **Исполнители** | 1 | executor | Пишут код, коммитят, создают SUMMARY |
| **Чекеры** | 3 | plan-checker, integration-checker, ui-checker | Верифицируют планы и связи между фазами |
| **Верификаторы** | 1 | verifier | Проверяют достижение целей фазы |
| **Аудиторы** | 3 | nyquist-auditor, ui-auditor, security-auditor | Заполняют пробелы тестами, аудируют UI/безопасность |
| **Мапперы** | 1 | codebase-mapper | Исследуют кодовую базу и пишут analysis docs |
| **Дебаггеры** | 1 | debugger | Расследуют баги научным методом |
| **Документаторы** | 2 | doc-writer, doc-verifier | Пишут и верифицируют документацию |
| **Профайлеры** | 1 | user-profiler | Анализируют поведение разработчика |
| **Специализированные** | 12 | pattern-mapper, code-reviewer, code-fixer, ai-researcher, eval-planner, eval-auditor, framework-selector, intel-updater, doc-classifier, doc-synthesizer, debug-session-manager, domain-researcher | Узкие роли для специфических сценариев (code review, AI-интеграция, eval) |

### Принцип наименьших привилегий

У GSD-агентов строго ограниченные инструменты (из AGENTS.md):

- **Чекеры** — read-only (нет Write/Edit)
- **Исследователи** — имеют веб-доступ
- **Исполнители** — имеют Edit, но нет веб-доступа
- **Мапперы** — имеют Write, но не Edit

Это отлично сочетается с моделью безопасности Multica: каждый агент Multica тоже имеет ограниченный контекст и CLI.

---

## Практическая настройка

### 1. Развернуть Multica

```bash
git clone https://github.com/multica-ai/multica.git
cd multica
cp .env.example .env
## Отредактировать .env — минимум JWT_SECRET
docker compose -f docker-compose.selfhost.yml up -d
```

### 2. Установить Multica CLI

```bash
brew tap multica-ai/tap
brew install multica
multica login
multica daemon start
```

### 3. Установить GSD в агент

Для каждого GSD-агента, который будет работать через Multica:

```bash
## Установить GSD (если агент — Claude Code или Codex)
gsd install

## Проверить установку
gsd --version
```

### 4. Зарегистрировать GSD-агента в Multica

Через дашборд Multica добавить агента с рантаймом, на котором установлен GSD.

Multica runtime (`AGENTS.md`) будет содержать:

```markdown
<!-- BEGIN MULTICA-RUNTIME (auto-managed; do not edit) -->
## Multica Agent Runtime

You are a GSD agent in the Multica platform.

**Identity:** gsd-planner (ID: ...)

## Available Commands
- `multica issue get <id> --output json`
- `multica issue comment add <id> --content "..."`
- `multica repo checkout <url>`
- `multica issue status <id> <status>`
<!-- END MULTICA-RUNTIME -->
```

Поверх него GSD добавляет свой Agent Card:

```markdown
## GSD Agent Role

**You are gsd-planner.** You create executable phase plans.
- Tools: Read, Write, Bash, Glob, Grep, WebFetch, mcp
- Produces: {phase}-{N}-PLAN.md
- Read PROJECT.md, REQUIREMENTS.md, CONTEXT.md, RESEARCH.md
```

### 5. Рабочий процесс

#### Создание задачи

1. В Multica создаётся Issue: «Implement auth phase — planning»
2. Issue назначается агенту `gsd-planner`
3. В описании Issue — ссылки на `.planning/` и PROJECT.md

#### Исполнение агентом

```bash
## Агент получает задачу
multica issue get MUL-123 --output json

## Переключает статус
multica issue status MUL-123 in_progress

## Чекаутит репозиторий
multica repo checkout https://github.com/user/project.git

## Запускает GSD-пайплайн
/gsd-plan-phase          # или эквивалент gsd CLI

## По окончании — комментарий
multica issue comment add MUL-123 --content "Phase plan created: auth-1-PLAN.md. 3 tasks, dependency wave 1→2. Ready for review."

## Переключает статус
multica issue status MUL-123 done
```

### 6. Параллельные агенты

Multica может запускать несколько GSD-агентов параллельно. Например:

- `gsd-project-researcher` × 4 (stack, features, architecture, pitfalls) — 4 параллельных исследования
- `gsd-research-synthesizer` — собирает результаты после них
- `gsd-planner` — планирует на основе синтеза

Каждый исследователь — отдельный Multica Issue с parent-ссылкой на общий milestone. После завершения всех research-Issues запускается synthesizer.

---

## Интеграционные сценарии

### Сценарий 1: Новый проект

```
Multica Issue: MUL-1 "New project: auth-service"
  ├── MUL-2 [research] GSD project-researcher (4 parallel)
  │     └── MUL-3 [research] stack research
  │     └── MUL-4 [research] features research
  │     └── MUL-5 [research] architecture research
  │     └── MUL-6 [research] pitfalls research
  ├── MUL-7 [synthesis] GSD research-synthesizer
  ├── MUL-8 [roadmap] GSD roadmapper
  └── Пофазно...
       ├── MUL-9 [plan] GSD planner → auth-phase
       ├── MUL-10 [execute] GSD executor → auth-phase
       └── MUL-11 [verify] GSD verifier → auth-phase
```

### Сценарий 2: Code Review

```
Multica Issue: MUL-50 "Review auth-phase code"
  ├── MUL-51 [review] GSD code-reviewer → REVIEW.md
  ├── (Если --fix) MUL-52 [fix] GSD code-fixer → REVIEW-FIX.md
  └── MUL-53 [verify] GSD verifier → checks fixes
```

### Сценарий 3: Debug-сессия

```
Multica Issue: MUL-100 "Bug: login redirect loop"
  ├── MUL-101 [debug] GSD debugger (interactive)
  │     └── Коммуникация через комментарии с пользователем
  └── MUL-102 [fix] GSD code-fixer → патч
```

### Сценарий 4: AI-интеграция

```
Multica Issue: MUL-200 "Add AI chat feature"
  ├── MUL-201 [select] GSD framework-selector → опрос, выбор фреймворка
  ├── MUL-202 [research] GSD domain-researcher → §1b AI-SPEC.md
  ├── MUL-203 [research] GSD ai-researcher → §3-§4b AI-SPEC.md
  ├── MUL-204 [eval] GSD eval-planner → §5-§7 AI-SPEC.md
  └── ...дальше стандартный пайплайн
```

---

## Multica Runtime vs GSD Runtime

Оба рантайма предоставляют агенту CLI-интерфейс и контекстную информацию.

| Аспект | GSD Runtime | Multica Runtime |
|--------|-------------|-----------------|
| **Что даёт агенту** | Agent Card (роль, инструменты, правила) | `multica` CLI + identity + issue context |
| **Формат** | Markdown Agent Card в `agents/gsd-*.md` | `AGENTS.md` с `<!-- BEGIN MULTICA-RUNTIME -->` |
| **Коммуникация** | Пишет файлы в `.planning/` | Пишет комментарии в Issues |
| **Координация** | Последовательный пайплайн | @mentions, parent-issues, статусы |
| **Состояние** | `.planning/STATE.md` + git | Multica issue metadata + workspace |

При интеграции оба рантайма **склеиваются**: агент получает `AGENTS.md` с секциями от Multica и Agent Card от GSD.

---

## Преимущества интеграции

1. **Прозрачность.** Весь прогресс GSD-пайплайна виден в Multica Dashboard. Не нужно открывать файлы `.planning/` — достаточно взглянуть на Issue Board.

2. **Параллелизм.** GSD-агенты изначально спроектированы для параллельной работы (до 4 экземпляров project-researcher). Multica предоставляет инфраструктуру для одновременного запуска.

3. **Аудит.** Каждое действие агента логируется: комментарий к Issue, смена статуса, git-коммит. Полная история.

4. **Масштабирование.** Можно добавить несколько экземпляров одного GSD-агента (например, 3 executor для параллельных фаз) — Multica распределяет задачи.

5. **Human-in-the-loop.** Multica Issues позволяют человеку проверять результаты на каждом этапе: проверить план перед execution, проверить код перед merge.

6. **Reusable Skills.** GSD-паттерны (например, шаблон security-audit) могут быть сохранены как Multica Skills для переиспользования в других проектах.

---

## Ограничения

- **Задержка.** Каждый spawn агента через Multica добавляет latency (создание Issue, ожидание раннера). Для быстрых итераций лучше прямой GSD.
- **Стоимость.** Множественные вызовы LLM через Multica + GSD могут увеличить расходы. Рекомендуется тюнинг model_profile (Sonnet для research, Haiku для mapper, Opus для planner).
- **Дублирование состояний.** `.planning/` GSD и Multica issue metadata могут рассинхронизироваться. Нужен чёткий протокол обновления.

---

## Связанные технологии

- [[tech/multica]] — базовая статья о Multica
- [[tech/sdd-orchestrator-v2]] — альтернативный подход к оркестрации агентов
- [[tech/heisenberg-team-gpt]] — мультиагентная коллаборация
- [[tech/cockpit]] — веб-администрирование серверов для self-hosted Multica

---

## Источники

- [GSD Repository](https://github.com/open-gsd/get-shit-done-redux) — `docs/AGENTS.md`, `docs/ARCHITECTURE.md`, `docs/INVENTORY.md`, `agents/gsd-*.md`
- [Multica Repository](https://github.com/multica-ai/multica) — `AGENTS.md` Runtime, CLI reference
- [Multica.ai](https://multica.ai) — документация платформы
