---
description: Jev (TypeSafe AI) — System One модель для быстрых структурированных решений. 40-200x быстрее LLM, 40-400x дешевле, 0% галлюцинаций. JevRouter — маршрутизатор для агентов.
tags: [llm, routing, decision-model, typesafe, jev, system-one, guardrails, mcp, codex, claude-code]
related:
  - tech/ternary-bonsai-2
  - hardware/xe2690-workstation
  - tech/free-llm-api-resources
---

# Jev + JevRouter (TypeSafe AI)

## Что такое Jev

**Jev** — это НЕ обычный LLM. Это первая публичная **System One модель** от TypeSafe AI (основатель — Диогу Алмейда, соавтор ChatGPT в OpenAI).

Ключевое отличие: Jev **не генерирует текст**. Он принимает структурированное состояние (state) и возвращает **типизированные решения с вероятностями** за один параллельный проход.

> «Think of Jev as a frontier-intelligence function call: unstructured state in, typed probabilistic decisions out.»

## Характеристики

| Свойство | Frontier LLM (GPT-5.6, Opus 5) | Jev (System One) |
|----------|-------------------------------|-------------------|
| **Выход** | Генерация строк, нужен парсинг | Типизированные значения, гарантия схемы |
| **Сэмплинг** | Последовательный (токен за токеном) | Параллельный, один запрос |
| **Цена ввода / 1M токенов** | $0.20–$10 | **$0.042** |
| **Цена вывода** | ~5x от ввода | **Бесплатно** |
| **Латентность** | 3–329с | **70–500мс** |
| **Галлюцинации** | Возможны | **Математически невозможны** |
| **Confidence** | Завышена, неконсистентная | **Калиброванная** |

## Типы вопросов (question types)

| Тип | Описание | Пример |
|-----|----------|--------|
| **Choice** | Выбор из набора опций | Категория тикета: {billing, technical, sales, spam} |
| **Score** | Оценка по шкале | Срочность: 0–100 |
| **Noul** | Да/нет с вероятностью | Срочен ли тикет? → 0.999 |

Можно задавать **несколько вопросов к одному состоянию** в одном запросе — все параллельно.

## Применение (не только браузер!)

### 1. Роутинг моделей
Jev решает, какую LLM вызвать для каждого запроса. Простые задачи → дешёвая модель, сложные → мощная.

```python
router = ModelRouterMiddleware(choices={
    "fast": ModelChoice(model="deepseek-v4-flash", criteria="Простые задачи"),
    "powerful": ModelChoice(model="mimo-v2.5", criteria="Сложные задачи"),
})
```

### 2. Роутинг инструментов и субагентов
Какой MCP-сервер, навык или subagent должен обработать следующий шаг? Jev выбирает за 70мс.

### 3. Guardrails / Auto Mode
Классификация рискованных вызовов инструментов **до** их выполнения. Блокировка опасных действий.

### 4. Триаж тикетов/писем
Классификация по срочности, команде, типу — с калиброванной вероятностью.

### 5. Map-reduce по большим данным
Обработка миллионов строк за копейки. 50M строк × $0.0004 = ~$20.

### 6. Real-time решения
Игра в Doom (10 решений/сек, ~$7/час), live-trading, реальные приложения где 3с — это слишком.

## Бенчмарки (Toolathlon, 10 задач)

| Метрика | Jev serial | Jev decompose+thread | DeepSeek V4.1 Flash |
|---------|-----------|---------------------|-------------------|
| Position-wise hits | 38% | **44%** | 24% |
| Prefix alignment (mean LCP) | 0.9 | **1.6** | 0.5 |
| Latency per task | **1.58с** | 10.6с | 8.65с |
| Cost per 10 tasks | **$0.0058** | $0.0055 | ~$0.0407 |

## JevRouter

**JevRouter** — открытый (MIT) маршрутизатор, который ставит Jev перед вашими инструментами. Решает: какая способность (модель, MCP, CLI, subagent) обработает запрос.

### Ключевые принципы
- **Decision-only** — ничего не исполняется молча; medium/high/critical требуют подтверждения
- **Receipts** — append-only логи решений с provenance-хэшами
- **Единый контракт** для моделей, субагентов, Skills, MCP tools, CLI, плагинов

### Интерфейсы

| Интерфейс | Команда | Примечание |
|-----------|---------|------------|
| CLI | `route`, `plan`, `discover` | stdout = JSON |
| SDK | `route()`, `plan()` | Inline candidates |
| HTTP | `serve --port 8787` | POST /route, GET /capabilities |
| MCP | `serve-mcp` | Один инструмент `jev_route` |

### Установка

```bash
# С ключом OpenRouter
export OPENROUTER_API_KEY="your-key"
npx --yes github:BillionsBobby/JevRouter agent start --agent codex --provider openrouter

# Или для Claude Code
npx --yes github:BillionsBobby/JevRouter agent start --agent claude --provider openrouter

# Проверка
npx --yes github:BillionsBobby/JevRouter agent doctor --live
```

### Multi-step plans

```bash
# Запланировать 3-шаговую задачу
npx --yes github:BillionsBobby/JevRouter plan --provider openrouter \
  --request "Найти источники, обобщить, сохранить в notes.md" \
  --candidates-file candidates.json --steps 3 --mode serial
```

Стратегии: `serial` (пошагово), `batch` (все сразу), `decompose` (разбиение на подцели).

## Стоимость

- Ввод: **$0.042/MTok**
- Вывод: **бесплатно**
- Один вызов: **~$0.0004**
- 50M решений: **~$20**

## Ссылки

- https://typesafe.ai — официальный сайт TypeSafe AI
- https://typesafe.ai/blog/introducing-system-one-models-and-jev — анонс
- https://github.com/BillionsBobby/JevRouter — JevRouter (MIT)
- https://www.jevrouter.co — сайт JevRouter
- https://docs.typesafe.ai — документация API
- https://docs.langchain.com/oss/python/integrations/providers/typesafe — LangChain интеграция
- OpenRouter — Jev доступен как модель

## Релевантность для our stack

- **Hermes/DSH**: JevRouter может маршрутизировать между провайдерами (opencode-go, qwen-tp, deepseek) на основе сложности запроса
- **Guardrails**: блокировка опасных tool calls перед выполнением
- **MCP**: JevRouter имеет MCP-адаптер — можно подключить к текущим MCP-серверам
- **Стоимость**: для高频 роутинга (каждый запрос → решение какую модель) — effectively free

## Статус

⏳ **Нужно попробовать** — особенно роутинг моделей и guardrails.
