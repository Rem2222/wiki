---
description: Исследование AI-агентов и Mercury Agent
tags: [agent, ai, research]
related: [[tech/hermes-memory-setup-vps]] [[tech/jawl-skills-registry]] [[tech/hermes-mcp-setup]]
---

# Mercury Agent Skills


## Описание

Открытая библиотека готовых скиллов для AI-агентов от Cosmic Stack (создатели Mercury Agent).

- **URL**: https://github.com/cosmicstack-labs/mercury-agent-skills
- **130+ скиллов** в 20 категориях
- **Формат**: SKILL.md — совместим с Mercury Agent, Claude Code, Cursor, Codex CLI, Gemini CLI, Hermes Agent
- **Звёзд**: 66 | **Форков**: 8

## Потенциал для Hermes Agent

Библиотека напрямую совместима с Hermes Agent (указан в описании). Многие скиллы можно взять как есть или адаптировать.

### Наиболее ценные для Hermes

#### AI & ML (10 скиллов)
| Скилл | Описание | Применимость |
|-------|----------|--------------|
| **Memory Management** | 5-tier память (working→semantic→archival), контекстная оптимизация, summarization, GC | Высокая — Hermes уже имеет memory-систему, но 5-tier подход углубляет |
| **Agent Handoff Protocols** | Контекст-пасс между агентами, escalation chains, conversation continuity | Высокая — напрямую решает проблему multi-agent коммуникации |
| **Token Budget Tracking** | Per-agent бюджеты, real-time мониторинг, cost attribution, proactive optimization | Высокая — критично для production |
| **Agent Health Monitoring** | Liveness checks, anomaly detection, observability dashboards | Высокая — то, чего сейчас нет |
| **Error Recovery & Retry** | Exponential backoff, circuit breakers, stateful recovery, dead-letter queue | Высокая — production-ready паттерны |
| **Prompt Engineering** | CoT, few-shot, role prompting, structured outputs | Средняя — базовые техники Hermes уже поддерживает |
| **Agent Task Delegation** | Task queue, load balancing, priority scheduling | Средняя — актуально при масштабировании |
| **Prompt Version Management** | Version control, A/B testing, canary rollouts для промптов | Средняя |
| **Agent Audit Logging** | Structured audit events, compliance reporting | Низкая — для enterprise |

#### DevOps (9 скиллов)
Kubernetes, Terraform, Docker, CI/CD, Monitoring — имеют прямое применение для инфраструктурных воркфлоу Hermes.

#### Automation (8 скиллов)
Workflow automation, shell scripting, data sync, RPA — полезно для кастомных автоматизаций.

### Структура SKILL.md

Каждый скилл содержит:
- Frontmatter с name, description, metadata (author, version, category, tags)
- Overview с объяснением проблемы
- Core Concepts с таблицами и диаграммами
- Step-by-Step Implementation с готовым кодом
- Trigger Phrases — фразы-триггеры для вызова
- Anti-Patterns — что не стоит делать

```
---
name: memory-management
description: '...'
metadata:
  author: cosmicstack-labs
  version: 1.0.0
  category: ai-ml
  tags: [memory-management, context-window, vector-database, ...]
---

## Memory Management for Long-Running Agents

## Overview

## Core Concepts

## Step-by-Step Implementation

## Trigger Phrases

## Anti-Patterns
```

### Trigger Phrases (примеры)

| Фраза | Действие |
|-------|----------|
| "What do you remember about..." | Search semantic memory |
| "Remember this for later" | Store with high importance |
| "Show token usage" | Display current consumption by agent |
| "What's the budget status?" | Show budget vs. actual |
| "Retry that" | Retry last failed operation |
| "Check circuit breakers" | Show circuit breaker status |
| "Degrade gracefully" | Switch to reduced capability mode |
| "Hand off to [agent]" | Initiate warm handoff |

## Категории (20)

| Категория | Кол-во | Примеры скиллов |
|-----------|--------|-----------------|
| Development | 9 | clean-code, git-workflow, code-review, debugging-mastery, testing-strategies |
| Frontend | 8 | react-patterns, tailwind-css, nextjs-patterns, state-management, web-performance |
| Backend | 9 | api-design, python-patterns, nodejs-patterns, database-design, auth |
| DevOps | 9 | docker-patterns, ci-cd-pipeline, kubernetes-patterns, terraform-iac, monitoring |
| AI & ML | 10 | prompt-engineering, memory-management, error-recovery-retry, token-budget-tracking |
| Security | 7 | security-audit, secure-coding, threat-modeling, api-security |
| Product | 7 | product-strategy, user-research, product-discovery, experimentation-ab-testing |
| Marketing | 8 | seo-strategy, content-creation, local-business-growth, social-media-strategy |
| Design | 7 | ui-design-system, accessibility, ux-research, prototyping-wireframing |
| Business | 7 | negotiation, startup-strategy, financial-modeling, sales-strategy |
| Automation | 8 | workflow-automation, shell-scripting, web-scraping, test-automation |
| Data | 7 | data-pipeline, sql-optimization, data-modeling, data-visualization |
| Mobile | 5 | ios-swift-patterns, android-kotlin-patterns, react-native-patterns |
| Testing & QA | 5 | test-strategy, e2e-testing, performance-testing, api-testing |
| Shop & Restaurant | 8 | inventory-optimizer, menu-engineer, staff-scheduler, review-responder |
| Creative & Personal Dev | 8 | storytelling-advisor, decision-matrix, daily-standup-journal, content-repurposer |
| Career | 5 | resume-writing, interview-prep, career-planning, linkedin-optimization |
| Finance & Legal | 5 | financial-analysis, budgeting-forecasting, contract-review, privacy-compliance |
| Health & Wellness | 5 | fitness-planning, nutrition-planning, mental-health, sleep-optimization |
| Education & Learning | 5 | curriculum-design, learning-science, teaching-methods, assessment-design |

## Детальный разбор ключевых скиллов

### Memory Management

**Проблема**: Long-running agents не могут помнить всё, но забывают важное.

**Решение**: 5-tier система:

| Tier | Хранилище | Объём | Скорость | Стоимость |
|------|-----------|-------|----------|-----------|
| L1 — Working | In-context (LLM window) | 8K-200K tokens | Instant | $$$ |
| L2 — Recent | Sliding window buffer | ~2K turns | <10ms | $$ |
| L3 — Episodic | Event log / timeseries | Millions | <50ms | $ |
| L4 — Semantic | Vector database | Unlimited | <100ms | $ |
| L5 — Archival | Object storage | Unlimited | >1s | $ |

**Ключевые паттерны**:
- Context window management с importance scoring
- Hierarchical summarization (rolling + importance-weighted)
- Memory consolidation & GC с дедупликацией и merging
- Retrieval с multi-stage ranking (vector search → LLM reranking)
- Trigger phrases: "What do you remember about...", "Run memory consolidation"

**Применимость к Hermes**: Уже есть memory/mempalace, но 5-tier архитектура + consolidation + reranking — ценное дополнение.

### Agent Handoff Protocols

**Проблема**: При передаче задачи между агентами теряется контекст.

**Решение**:
- HandoffContext — полный контекст (original_task, current_state, key_facts, decisions_made, collected_data)
- Handoff types: warm (full context) vs cold (task only) vs supervised vs broadcast
- Escalation chains: agent → specialist → human
- Conversation continuity across handoffs

**Ключевые паттерны**:
- HandoffDecider — LLM-driven decision when to hand off
- ConversationContinuity — maintain thread across agents
- Dead-letter queue для unrecoverable tasks

**Применимость к Hermes**: Multica уже имеет agent-to-agent коммуникацию, но формализованный HandoffContext с conversation continuity был бы ценен.

### Token Budget Tracking

**Проблема**: Один runaway agent может сжечь сотни долларов за минуты.

**Решение**:
- TokenCounter с per-agent attribution
- TokenBudget с per-agent и period limits
- BudgetDashboard с real-time alerts
- TokenOptimizer с context compression
- CostController с proactive model selection

**Ключевые паттерны**:
- Predefined retry policies (tool_call, api_request, llm_generation, database_query)
- Budget alerting rules с severity levels
- Model tiering (cheap for easy tasks, expensive for hard)

**Применимость к Hermes**: Критично для production. Hermes сейчас не имеет per-agent token tracking.

### Error Recovery & Retry

**Проблема**: Agents fail — APIs timeout, models return garbage, tools throw exceptions.

**Решение**:
- Retry with exponential backoff + jitter
- Circuit breaker (CLOSED → OPEN → HALF_OPEN)
- Stateful agent recovery с checkpoints
- Graceful degradation (full → reduced → minimal → fallback)
- Dead-letter queue для unrecoverable tasks

**Ключевые паттерны**:
- CircuitBreakerRegistry — один registry на все dependencies
- AgentErrorHandler — central error handler с full recovery stack
- Retry policies per operation type

**Применимость к Hermes**: Ценные паттерны для production resilience.

## Что можно взять для Hermes Agent

### Взять как есть (copy-paste)
- Prompt Engineering — структура и trigger phrases
- Error Recovery & Retry — retry policies, circuit breaker implementation
- Token Budget Tracking — monitoring patterns

### Адаптировать
- Memory Management → дополнить существующую mempalace-систему
- Agent Handoff Protocols → формализовать коммуникацию между агентами в Multica

### Для вдохновения
- Shop & Restaurant скиллы (интересные domain-specific паттерны)
- Creative & Personal Development скиллы

## Задача

Изучено. Записано в wiki/tech/Mercury Agent Skills.md

#ai-agents #skills #hermes #cosmicstack