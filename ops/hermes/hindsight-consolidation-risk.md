---
description: "Риск: консолидация Hindsight (сборка фактов) жёстко на opencode-go/mimo-v2.5 без fallback. Что делать при падении лимитов opencode-go."
tags:
  - hindsight
  - memory
  - opencode-go
  - риск
related:
  - "[[tech/hindsight]]"
  - "[[ops/hermes]]"
created: 2026-08-21
---
# Риск: консолидация Hindsight без fallback на opencode-go

## Суть
Сборка фактов (consolidation) для новой памяти Hindsight жёстко настроена на
**opencode-go / mimo-v2.5** БЕЗ fallback-цепочки внутри Hindsight.

- `HINDSIGHT_API_LLM_PROVIDER=opencode-go` (env контейнера hindsight-app)
- `HINDSIGHT_API_LLM_MODEL=mimo-v2.5`
- Дублируется в `/root/.hermes/hindsight/config.json` (`llm_provider: opencode-go`, `llm_model: mimo-v2.5`)

## Последствия при падении opencode-go по лимитам
- 🔴 Ложится **фоновое пополнение фактов** (консолидация) — Hindsight шлёт на opencode-go и ловит ошибки.
- ✅ Сама память НЕ страдает: БД (Postgres hindsight-db), поиск, recall, эмбеддинги (bge-m3 через Ollama) — это отдельные сервисы, читать/искать можно.

## Отличие от основного агента
| Потребитель | Fallback? | Поведение |
|---|---|---|
| Основной агент Hermes | ✅ Да (`opencode-go→qwen-tp→openrouter`) | переключится сам |
| Консолидация Hindsight | ❌ Нет | упрётся, пока opencode-go не оживёт |

## Решение (согласовано, 21.08.2026)
Оставить как есть. **Переключать вручную** на qwen-tp при падении opencode-go:

1. Остановить: `docker stop hindsight-app`
2. Поменять в контейнере: `HINDSIGHT_API_LLM_PROVIDER=qwen-tp` (LLM в yaml/комpose hindsight-app)
3. Поменять `/root/.hermes/hindsight/config.json`: `llm_provider: qwen-tp`
4. `docker start hindsight-app`
5. Проверить: тестовая сборка факта или логи контейнера за последние минуты.

⚠️ Замечание: для AgentMemory (старый провайдер) было правило «deepseek/kimi/qwen → 500 на
XML-запросах, работает mimo-v2.5». Hindsight — другой форк, его поведение на XML может отличаться,
поэтому перед переводом на qwen-tp стоит проверить тестовой сборкой факта.

## Следить
- Ночная рутина, Шаг 12 (проверка бэкапов и сервисов) — добавить проверку здоровья hindsight-app.