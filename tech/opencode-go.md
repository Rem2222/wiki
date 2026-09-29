---
description: "Основной inference-провайдер Hermes — подписка OpenCode Go (0/мес) на endpoint opencode.ai/zen/go/v1: deepseek-v4-flash/mimo, chat_completions, первый канал fallback-цепочки."
tags: [ai,provider,llm,api,inference]
related: [[tech/qwen-tp]] [[tech/free-coding-agents-2026]] [[concepts/llm-tier-strategy]] [[tech/llm-as-a-verifier]] [[tech/opencode]]
---

# opencode-go

## Что это

**opencode-go** — основной inference-провайдер в стеке Hermes: подписка OpenCode Go ($10/мес), OpenAI-совместимый endpoint `https://opencode.ai/zen/go/v1` (`api_mode: chat_completions`, `default_model: deepseek-v4-flash`, `credential_pool_strategies: fill_first`).

Имя `opencode-go` — ключ провайдера в `/root/.hermes/config.yaml`, префикс моделей в Multica (`opencode-go:<model>`) и имя первого канала в fallback-цепочке.

## Роль в стеке

- **Основной канал:** `opencode-go/deepseek-v4-flash` — младшая модель (~80% задач), `opencode-go/deepseek-v4-pro` — старшая (код, ревью), `mimo-v2.5` — консолидация Hindsight.
- **Fallback-цепочка:** `opencode-go` → `qwen-tp` → `openrouter` → `freellmapi`.
- **Multica-агенты:** модели с префиксом `opencode-go:` сверяются с `/v1/models` провайдера — устаревший список валит агента.
- **Лимиты Go ($10/мес)** в долларовом эквиваленте использования: 5 часов ≈ $12, неделя ≈ $30, месяц ≈ $60; бесплатные модели работают и после исчерпания лимита.

## Модели

Актуальный список — только у провайдера: `GET https://opencode.ai/zen/go/v1/models` (источник истины). Curated-floor лежит в `hermes_cli/models.py` (слетает при `hermes update`), живой кэш — `~/.hermes/provider_models_cache.json` (TTL 1ч, stale-while-revalidate до 7д).

- Дешёвые на 28.08.2026: MiMo V2.5 ($0.14/$0.28), Hy3, LongCat-2.0, DeepSeek V4 Flash ($0.44 peak — подорожал после релиза DCS).
- ⚠️ `*-free` модели (`deepseek-v4-flash-free` и др.) — это **opencode-zen**, не go: префикс `opencode-go:*` для них ошибка.
- ⚠️ Muse Spark «Contributor» — opt-in на сбор промптов для обучения Meta; не для памяти и консиденциальных данных.

## Особенности вызова

- Заголовок `x-opencode-session` обязателен для `chat/completions` (без него → 400 `MissingSessionID`).
- Не-Python User-Agent: `Python-urllib` ловит Cloudflare 403 (`error code: 1010`).
- 401 — невалидный ключ, 400 `Model is unavailable` — модель реально снята; ошибки OpenCode ≠ недоступность модели.

## Связи

- [[tech/qwen-tp]] — токен-план Alibaba, первый fallback после opencode-go
- [[tech/free-coding-agents-2026]] — вердикт: inference в стеке уже закрыт
- [[concepts/llm-tier-strategy]] — раскладка «младшая/старшая» модель
- [[tech/llm-as-a-verifier]] — проверено вживую: top-k logprobs opencode-go не отдаёт
- [[tech/opencode]] — CLI OpenCode (anomalyco), отдельная история
