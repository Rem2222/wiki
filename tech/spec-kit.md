---
description: 94k stars, 8.2k forks, 931 commits (as of May 2026)
tags: [tech]
---

# Spec Kit (GitHub)

## Links
- https://github.com/github/spec-kit
- https://github.github.io/spec-kit/
- Quick Start: https://github.github.com/spec-kit/quickstart.html

## Stats
94k stars, 8.2k forks, 931 commits (as of May 2026)

## What is it

**Spec-Driven Development (SDD)** — GitHub open-source toolkit для управления AI coding agents.

Specifications становятся **executable** — не просто направляют код, а напрямую генерируют working implementations.

```
Раньше: спеки = строительные леса → выбросили → пишем код
Теперь: спеки = основа → генерируют implementation напрямую
```

Ключевая идея: дать AI-агенту набор **structured commands** (`/speckit.*`), которые ведут его через спецификацию → план → имплементация → ревью.

## Workflow Commands

| Command | Purpose |
|---------|---------|
| `/speckit init` | Инициализация spec-orkspace в проекте |
| `/speckit.constitution` | Governing principles проекта — что допустимо, что нет |
| `/speckit.specify` | Define "what" — functional requirements |
| `/speckit.clarify` | AI задаёт уточняющие вопросы к спеку |
| `/speckit.plan` | Выбор стека, architecture decisions, steps |
| `/speckit.tasks` | Задачи с зависимостями (directed acyclic graph) |
| `/speckit.implement` | Генерация кода по спеку |
| `/speckit.review` | Проверка что код соответствует спеку |

> **Codex CLI note:** В режиме skills вместо `/speckit.*` используется `$speckit-*`

## Development Phases

- **0-to-1 (Greenfield)** — Generate from scratch, starting with Constitution
- **Creative Exploration** — Parallel implementations, разные стеки
- **Iterative Enhancement (Brownfield)** — Add features, modernize legacy

## Supported Agents

30+ AI coding agents — CLI и IDE:
- Claude Code
- GitHub Copilot
- Cursor
- Codex CLI
- Gemini CLI
- И др.

Install Specify CLI: `uvx --from github-spec-kit specify --help`

## Core Philosophy

- Focus на **what** и **why**, не **how**
- Guardrails + organizational principles (Constitution)
- Итеративный процесс вместо one-shot generation
- Спеки — living documents, не одноразовые

## Compared to Intent

| | Spec Kit | Intent |
|---|---|---|
| Cost | Free, open-source | Commercial |
| Scope | Works with any agent | Orchestration, living specs, enterprise compliance |
| Focus | Structured spec workflow | Broader agent orchestration |
| Lock-in | None (open, agent-agnostic) | Proprietary |

## When to Use

**Good for:**
- Teams using multiple AI coding agents
- Projects needing structured spec → code workflow
- Reducing "vibe coding" — making AI output deterministic

**Less suitable for:**
- Simple scripts / one-off tasks
- Teams already happy with their workflow
- Enterprise compliance needs (→ Intent instead)

## See Also
- [[sdd-deep-guide]] — глубокое руководство по SDD
- [[openspec]] — альтернативный инструмент
- [[vibe-coding-workflow]] — контраст с vibe coding