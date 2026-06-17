---
description: Интеграция BMAD (Build More Architect Dreams) с Multica — архитектурный SDD-фреймворк + платформа управления AI-агентами
tags: [sdd, framework, architecture, specification, multica, bmad, integration]
related: [[tech/bmad-method]] [[tech/multica]] [[tech/gsd-multica-integration]] [[tech/gsd]]
---

# BMAD + Multica

**BMAD (Build More Architect Dreams)** — SDD-фреймворк с философией «Architecture First». **Multica** — open-source платформа управления AI-агентами. Их интеграция закрывает сценарий: *«у меня есть размытая идея — помоги исследовать, спроектировать архитектуру и реализовать через агентов»*.

---

## Чем BMAD дополняет Multica

У Multica и BMAD ортогональные сильные стороны:

| Аспект | Multica | BMAD |
|--------|---------|------|
| Управление задачами | ✅ Issues, приоритеты, статусы | ❌ нет |
| Инфраструктура агентов | ✅ Рантаймы, дашборд, CI | ❌ нет |
| Архитектурная проработка | ❌ нет | ✅ Exhaustive SDD до кода |
| Исследование неясных идей | ❌ нет | ✅ Задаёт вопросы, анализирует, перепроверяет |
| Reusable навыки | ✅ Skills | ✅ Skills (31+) |
| Party Mode (мульти-агент) | ✅ Squad | ✅ Party Mode |

**BMAD** хорош там, где непонятно «как делать» — он сам проведёт исследование, задаст вопросы, выявит противоречия, построит архитектуру.

**Multica** хороша там, где понятно «кто делает» — назначает агентов, отслеживает прогресс, хранит историю.

---

## Архитектура интеграции

### Вариант A: BMAD-оркестратор → Multica-исполнители (рекомендуемый)

```
Пользователь: "сделай CRM-систему"
       │
       ▼
┌──────────────────────────────┐
│  BMAD (в Claude Code)        │  ← Исследует, проектирует,
│  - bmad-brainstorming        │    задаёт вопросы,
│  - bmad-spec (SPEC.md)       │    создаёт архитектуру
│  - bmad-create-architecture  │
│      ↓ SPEC.md + ARCHITECTURE.md
│  - создаёт Issues в Multica  │  ← Каждый phase → отдельный issue
└──────────────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│  Multica                     │  ← Исполняет через агентов
│  - агент берёт issue         │
│  - реализует по SPEC.md     │
│  - отчитывается              │
└──────────────────────────────┘
```

**Процесс:**
1. Пользователь описывает идею в Claude Code с BMAD
2. BMAD проводит brainstorming → elicitation → spec → architecture
3. BMAD создаёт Issues в Multica (по одному на phase)
4. Multica-агенты выполняют issues
5. BMAD верифицирует результат

### Вариант B: BMAD-скиллы как Multica Skills

Каждый BMAD-скилл регистрируется как reusable skill в Multica. Агенты в Multica могут вызывать BMAD-скиллы как часть своего workflow.

```
Multica Agent → запускает bmad-advanced-elicitation skill → получает требования
              → запускает bmad-create-architecture skill → получает архитектуру
              → реализует
```

### Вариант C: Полный lifecycle BMAD → Multica → BMAD

```
bmad-brainstorming               ← Multica issue (идея)
       ↓
bmad-advanced-elicitation        ← Multica issue (требования)
       ↓
bmad-spec                        ← Multica issue (спецификация)
       ↓
bmad-create-architecture          ← Multica issue (архитектура)
       ↓
Multica-агенты реализуют         ← Issues по фазам
       ↓
bmad-editorial-review-structure  ← Multica issue (ревью)
       ↓
bmad-review-edge-case-hunter     ← Multica issue (edge cases)
```

---

## BMAD-скиллы и их применение в Multica

BMAD поставляется с 31+ скиллом. Ключевые для интеграции с Multica:

### Core-скиллы (core-skills/)

| Скилл | Назначение | В Multica |
|-------|-----------|-----------|
| `bmad-advanced-elicitation` | Выявление требований через структурированные вопросы | Создаёт issue с полным описанием requirements |
| `bmad-spec` | Написание SPEC.md | Генерирует SPEC.md как attachment к issue |
| `bmad-brainstorming` | Мозговой штурм с 6 техниками | Исследует размытую идею, создаёт несколько issues |
| `bmad-party-mode` | Мульти-агентное обсуждение | Замена/усиление Squad Leader |
| `bmad-create-architecture` | Архитектурное проектирование (8 шагов) | Создаёт ADR и архитектурные issues |
| `bmad-editorial-review-structure` | Ревью структуры кода | Code review в Multica |
| `bmad-editorial-review-prose` | Ревью текста и документации | Документирование в issues |
| `bmad-review-adversarial-general` | Общий adversarial review | Усиление Verifier |
| `bmad-review-edge-case-hunter` | Поиск крайних случаев | Создаёт issues на edge cases |
| `bmad-shard-doc` | Дробление документации | Структурирование wiki |
| `bmad-index-docs` | Индексация документации | Поиск в issue history |
| `bmad-customize` | Кастомизация BMAD под проект | Настройка Multica agents |

### BMM-скиллы (bmm-skills/)

| Категория | Скиллы |
|-----------|--------|
| 1-analysis | Анализ требований, стейкхолдеры, риск-анализ |
| 2-plan-workflows | Планирование спринтов, оценка, приоритизация |
| 3-solutioning | **bmad-create-architecture** + ADR + паттерны |
| 4-implementation | Реализация, тесты, CI/CD |

---

## Squad на BMAD в Multica

Если собирать Squad из BMAD-ролей:

| Агент | BMAD-аналог | Роль |
|-------|-------------|------|
| **Leader** | Проектировщик + `bmad-help` | Координирует, решает какой скилл запустить |
| **Analyst** | `bmad-advanced-elicitation` | Выясняет требования, задаёт вопросы пользователю |
| **Architect** | `bmad-create-architecture` | Проектирует архитектуру, пишет ADR |
| **Developer** | GSD-Executor | Реализует (GSD-style) |
| **Reviewer** | `bmad-review-*` | Проверяет результат |

**Отличие от GSD-сценария:** BMAD-лидер больше **исследует и проектирует**, GSD-лидер больше **декомпозирует и делегирует**.

---

## Практическая настройка

```bash
## 1. Установить BMAD в проект
cd /path/to/project
npx bmad-method install --directory . --modules bmm --yes

## 2. Использовать BMAD для исследования
# → в Claude Code: запустить bmad-spec или bmad-brainstorming
# → BMAD создаст SPEC.md / REQUIREMENTS.md

## 3. Создать issue в Multica на основе SPEC
multica issue create \
  --title "Phase 1: реализовать по SPEC" \
  --description-file SPEC.md \
  --priority high

## 4. Назначить на агента или squad
multica issue assign <issue-id> --assignee "Hermes Helper"
```

---

## Когда BMAD vs GSD

| Сценарий | Что выбрать |
|----------|------------|
| **Понятная задача, нужно разбить на этапы** | GSD |
| **Размытая идея, непонятна архитектура** | BMAD |
| **Есть human-участники в squad** | BMAD (человекочитаемые вопросы) |
| **Чисто агентный squad** | GSD (лучшая декомпозиция) |
| **Эволюционирующий проект с частыми пересмотрами** | BMAD + OpenSpec |
| **Комбо:** исследовать → спроектировать → реализовать | BMAD → GSD → Multica |

---

## Ссылки

- [[tech/bmad-method]] — базовая статья о BMAD в этой wiki
- [[tech/gsd-multica-integration]] — GSD + Multica (альтернативный подход)
- [[tech/gsd]] — GSD-фреймворк
- [[tech/multica]] — платформа Multica
- GitHub BMAD: https://github.com/bmad-code-org/BMAD-METHOD
- Документация BMAD: https://docs.bmad-method.org
- GitHub Multica: https://github.com/multica-ai/multica
