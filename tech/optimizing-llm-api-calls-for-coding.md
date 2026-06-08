---
description: Модели с большим контекстным окном (1M токенов) делают множество последовательных API-вызовов вместо того, чтобы прочитать всё за раз, подумать и выдать готовый код. Каждый вызов = списание квоты (...
tags: [tech]
related: [[tech/multica]] [[tech/opencode]] [[tech/subquadratic]]
---

# optimizing-llm-api-calls-for-coding

**Дата:** 2026-05-11
**Контекст:** Настройка трёх Multica-агентов на базе OpenCode Go моделей (DeepSeek V4 Pro, V4 Flash, Qwen3.6 Plus)

## Проблема

Модели с большим контекстным окном (1M токенов) делают множество последовательных API-вызовов вместо того, чтобы прочитать всё за раз, подумать и выдать готовый код. Каждый вызов = списание квоты (OpenCode Go имеет лимиты по количеству запросов, не по токенам).

## Решение: два варианта

### Вариант А — Быстрый (применён)
Обновление `instructions` и `custom_env` уагентов через Multica API:

```json
{
  "instructions": "batch-read → think → deliver — не итерироваться",
  "custom_env": {"HERMES_MAX_ITERATIONS": "3"}
}
```

**Эффект:** вместо 15-20 вызовов на задачу → 3-5.

### Вариант Б — Изолированный профиль (в планах)
- Создать `hermes profile create coder`
- `max_turns: 3`, `reasoning_effort: high`
- Зарегистрировать отдельный runtime в Multica под профилем кодера
- Привязать кодер-агентов к новому runtime

## Созданные агенты

| Агент | Модель | Контекст |
|-------|--------|----------|
| `OCodeGo-Deepseek-v4-pro` | DeepSeek V4 Pro | 1M |
| `OCodeGo-Deepseek-v4-flash` | DeepSeek V4 Flash | 1.05M |
| `OpenCodeGo-qwen3.6-plus` | Qwen3.6 Plus | 1M |

Все используют OpenCode Go ($10/мес), Hermes runtime `e3c53f75-...`.

## Ключевые параметры

- `agent.max_turns` — глобальный для runtime (сейчас 90, цель ≈ 3-5 для кодера)
- `agent.reasoning_effort` — `high` заставляет модель дольше думать внутри reasoning (скрытые токены не считаются в output)
- `instructions` — системный промпт агента (per-agent, через Multica)
- `custom_env.HERMES_MAX_ITERATIONS` — жёсткий лимит итераций

## Дополнительные провайдеры

В процессе настройки рассмотрены:
- **Logfare.ai** — бесплатный прокси с `deepseek-v4-flash` (tier 1), `gemini-3-flash` и `kimi-k2.6` (tier 2, требуют consent на продажу данных). Добавлен в конфиг, затем удалён.
- **FreeTheAI** — требовал ежедневный Discord check-in (`/checkin`). Удалён из конфига.