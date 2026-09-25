---
description: Сервисы с бесплатным LLM API-доступом и триальные кредиты. Две части: cheahjs/free-llm-api-resources (25.5k ⭐) + полевой обзор шести малоизвестных сервисов @Ungated из Habr 1085352 (сент. 2026): Atria, Vireonix, ShareLLM, OdiRouter, Selora, Routeway.
tags: [tech, llm, free, api, providers, habr]
updated: 2026-09-23
related:
  - tech/freellmapi
  - tech/free-claude-code
  - tech/jawl-howto-add-provider
  - tech/freenimapi
---

# Free LLM API Resources

**Источники:**
- https://github.com/cheahjs/free-llm-api-resources (25.5k ⭐, 421 коммит, 2.6k форков) — секция «Бесплатные провайдеры» и «Триальные кредиты»
- https://habr.com/ru/articles/1085352/ — автор @Ungated, секция «Обзор @Ungated» и «Ловушки» (сент. 2026)

> [!NOTE]
> Не злоупотребляй этими сервисами — иначе мы их потеряем.
> 
> Список исключает нелегитимные сервисы (реверс-инжиниринг готовых чатботов).

---

## Бесплатные провайдеры

### OpenRouter ⭐

**Лимиты:** 20 req/min, 50 req/day (до 1000 req/day с $10 lifetime topup)

**Модели (23 free):**
- `nvidia/nemotron-3-nano-30b-a3b:free` — NVIDIA 30B
- `nvidia/nemotron-3-super-120b-a12b:free`
- `nvidia/nemotron-3-ultra-550b-a55b:free`
- `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- `nvidia/nemotron-nano-12b-v2-vl:free`
- `nvidia/nemotron-nano-9b-v2:free`
- `google/gemma-4-26b-a4b-it:free`
- `google/gemma-4-31b-it:free`
- `qwen/qwen3-coder:free`
- `qwen/qwen3-next-80b-a3b-instruct:free`
- `meta-llama/llama-3.3-70b-instruct:free`
- `meta-llama/llama-3.2-3b-instruct:free`
- `cohere/north-mini-code:free`
- `liquid/lfm-2.5-1.2b-instruct:free`
- `liquid/lfm-2.5-1.2b-thinking:free`
- `openai/gpt-oss-120b:free`
- `openai/gpt-oss-20b:free`
- `poolside/laguna-m.1:free` / `laguna-xs-2.1:free` / `laguna-xs.2:free`
- `cognitivecomputations/dolphin-mistral-24b-venice-edition:free`

**Использование в Hermes:**
```yaml
model:
  provider: openrouter
  default: google/gemma-4-26b-a4b-it:free
```

### Google AI Studio

Вне UK/CH/EEA/EU данные используются для обучения. Нужен API-ключ.

| Модель | Лимиты |
|--------|--------|
| Gemini 3.5 Flash | 20 req/day, 5 req/min |
| Gemini 3 Flash | 20 req/day, 5 req/min |
| Gemini 3.1 Flash-Lite | 500 req/day, 15 req/min |
| Gemini 2.5 Flash | 20 req/day, 5 req/min |
| Gemini 2.5 Flash-Lite | 20 req/day, 10 req/min |
| Gemma 3 27B Instruct | 14400 req/day, 30 req/min |

### NVIDIA NIM

Требует подтверждения номера телефона.
**Лимиты:** 40 req/min
**Модели:** Различные open модели на https://build.nvidia.com/models

### Mistral (La Plateforme)

Free tier (Experiment) — данные на обучение. Требует телефон.
**Лимиты:** 1 req/s, 500K tok/min, 1B tok/мес (per-model)
**Модели:** https://docs.mistral.ai/getting-started/models/models_overview/

### Mistral Codestral

Сейчас бесплатно, подписка.
**Лимиты:** 30 req/min, 2000 req/day
**Модель:** Codestral

### HuggingFace Inference Providers

Серверные модели до 10GB (некоторые популярные больше).
**Лимиты:** $0.10/мес в кредитах
**Модели:** Различные open модели

### Vercel AI Gateway

Роутинг к разным провайдерам.
**Лимиты:** $5/мес

### OpenCode Zen

Free модели могут использовать данные для улучшения.
**Модели:** Big Pickle Stealth, Nemotron 3 Super Free, DeepSeek V4 Flash Free
**Endpoint:** https://opencode.ai/zen/go/v1

### Cerebras

| Модель | Лимиты |
|--------|--------|
| gpt-oss-120b | 30 req/min, 60K tok/min, 14.4K req/day |
| Llama 3.1 8B | 30 req/min, 60K tok/min, 14.4K req/day |

### Groq

| Модель | Лимиты |
|--------|--------|
| qwen/qwen3.6-27b | 1K req/day, 8K tok/min |
| qwen/qwen3-32b | 1K req/day, 6K tok/min |
| Llama 3.3 70B | 1K req/day, 12K tok/min |
| Llama 4 Scout | 1K req/day, 30K tok/min |
| openai/gpt-oss-120b | 1K req/day, 8K tok/min |
| Llama 3.1 8B | 14.4K req/day, 6K tok/min |
| groq/compound-mini | 250 req/day, 70K tok/min |

### Cohere

**Лимиты:** 20 req/min, 1K req/мес (общий пул моделей)
**Модели:** Command A/A+/Reasoning/Translate/Vision, Aya Expanse 32B, Aya Vision 32B, c4ai, Command R/R+/R7B

### GitHub Models

Лимиты зависят от подписки Copilot (Free/Pro/Pro+/Business/Enterprise).
**Модели:** Codestral 25.01, DeepSeek-R1/-V3-0324, Llama 4 Maverick/Scout/Llama-3.3/3.2, Mistral Medium 3, Small 3.1, Ministral 3B, OpenAI GPT-5/GPT-5-mini/GPT-5-nano, o3, o4-mini, GPT-4.1/4o/4o-mini, Phi-4, Phi-4-mini

### Cloudflare Workers AI

**Лимиты:** 10 000 neurons/day
**Модели:** Kimi K2.6/K2.7-code, Qwen3-30b-a3b-fp8, GLM-4.7-flash/GLM-5.2, Nemotron-3-120b, GPT-OSS-120b/20b, Llama 4 Scout/Llama 3.3 70B/Llama 3.1 8B, Gemma 4 26B, Mistral Small 3.1, Qwen QwQ 32B и другие.

---

## Обзор @Ungated (Habr, сент. 2026)

Вторичный источник — [Habr 1085352](https://habr.com/ru/articles/1085352/) (автор [@Ungated](https://t.me/AIUngated), ведёт TG-канал AI Ungated). Все шесть проверены живыми запросами. В cheahjs-списке этих сервисов **нет**.

| Сервис | Лимиты | Модели | Без ключа |
|--------|--------|--------|----------|
| **Atria** | **100M токенов** при регистрации; 50 RPM (в доке заявлено 60) | 1 — `Atria-Dawn-Preview` (744B MoE GLM-5.2, Shanghai AI Lab), 256K ctx, 65K out, только текст | нет |
| **Vireonix** | **20M in / 200K out токенов в час**, ctx 1M | 1 — `auto` (автоподбор из MiniMax, GLM, Qwen, Llama, Nemotron, GPT-OSS) | **да** |
| **ShareLLM** | 120 req/5 ч, 600 req/нед | 39 маршрутов; проверено 10/10 → 200 | нет |
| **OdiRouter** | пул `free-*` | claude-haiku-4.5, gemini-2.5-flash/pro, gpt-5.4-mini, minimax-m2.7, qwen3.5-plus | нет |
| **Selora** | **$5/4 ч, $30/нед**, 30 RPM | 10/10 → 200: claude-opus-5, claude-sonnet-5, gpt-5-6-sol, gpt-6-astra, kimi-k3 | нет |
| **Routeway** | 5 RPM, 200 req/сут | `minimax-m2.7:free`, `muse-glimmer-30b:free` | нет |

### Atria

`https://api.atria-asi.ai/v1` · доки `https://api.atria-asi.ai/docs`

100M токенов начисляются сразу после регистрации. Модель одна — `Atria-Dawn-Preview`, агентная, на базе **744B MoE GLM-5.2** (Shanghai AI Lab), только текст.

**Три API, все HTTP 200:**
- Chat Completions — только текст
- Responses API — отдельно `reasoning` + финальный ответ
- Anthropic Messages — блоки `thinking` + `text`

Общий лимит на аккаунт для всех трёх. Заголовок `x-rpm-limit: 50` — фактический лимит ниже задокументированного 60. RPD не заявлен.

### Vireonix (самый простой вход)

`https://vireonix.ai/v1` · доки `https://vireonix.ai/docs`

**API-ключа нет вообще** — обычный OpenAI-совместимый запрос. `/v1/models` → один маршрут `auto`, который сам выбирает модель из общего пула (конкретная не раскрывается, в ответе только `auto`).

Квота считается по IP, обновляется каждый час. `/api/limits` подтверждает, что это **штатная политика, а не временная акция** (`temporary: false`).

### ShareLLM

`https://sharellm.net/v1`

После регистрации выдают отдельный Free-маршрут. Из 39 моделей проверено 10 — все HTTP 200: `gpt-5.6-luna`, `grok-4.6`, `deepseek-v4.1-flash`, `glm-5.3`, `glm-5.3-flash`, `kimi-k3`, `qwen3.8-max`, `minimax-m3`, `gemini-3.8-flash`, `step-5`.

Имя маршрута не всегда совпадает с тем, что вернётся в поле `model` — воспринимать `/models` как список маршрутов:

| Запрошен | Вернётся в `model` |
|---|---|
| `gpt-5.6-luna` | `codex-auto-review` |
| `glm-5.3` | `codely-core` |
| `kimi-k3` | `kimi-k3-oc` |
| `qwen3.8-max` | `qwen/qwen3.8-max:free` |
| `step-5` | `step-5-preview` |

`kimi-k3` отдаёт reasoning в `reasoning_content` + ответ в `content`; `minimax-m3` — reasoning внутри ` (и финальный ответ после него). Скорость сильно скачет: `deepseek-v4.1-flash` / `glm-5.3-flash` ~1.5 с, `glm-5.3` — до минуты.

### OdiRouter

`https://api.odirouter.ai/v1` · сайт `https://odirouter.ai`

Пул с префиксом `free-*`: `free-claude-haiku-4.5`, `free-claude-haiku-4-5-20251001`, `free-vclaude-haiku-4.5`, `free-gemini-2.5-flash`, `free-gemini-2.5-flash-lite`, `free-gemini-2.5-pro`, `free-gemini-3.1-flash-lite`, `free-gemini-3-flash-preview`, `free-gpt-5.4-mini`, `free-minimax-m2.5`, `free-minimax-m2.7`, `free-qwen3.5-flash`, `free-qwen3.5-plus`, `free-qwen-flash-character`.

**Нестабильно:** `free-gpt-5.4-mini` → 502, `free-gemini-2.5-flash-lite` → 503, два Gemini preview → 504.

### Selora

`https://api.selora.lol/v1` · доки `https://selora.lol/docs`

Бесплатный тариф **Nova — 14 дней**. Активация: привязать Telegram + вступить в канал.

10 моделей, все HTTP 200 через `/chat/completions`: `claude-fable-5`, `claude-fable-5-1`, `claude-haiku-4-5`, `claude-opus-4-8`, `claude-opus-5`, `claude-sonnet-5`, `gpt-5-6-luna`, `gpt-5-6-sol`, `gpt-6-astra`, `kimi-k3`. Есть Anthropic-совместимый `/v1/messages` (проверен на `claude-opus-5`).

Потолок `x-ratelimit-limit: 30` (30 RPM), отдельного RPD нет — вместо него денежные окна. Тест всех 10 моделей стоил **$0.000804** (с $5.000000 → $4.999196).

### Routeway

`https://api.routeway.ai/v1` · доки `https://docs.routeway.ai/`

Баланс после регистрации $0.00, но **бесплатные маршруты работают отдельно от баланса**. `/v1/models` → 263 модели, бесплатные помечены суффиксом `:free`.

- рабочие: `minimax-m2.7:free`, `muse-glimmer-30b:free`
- не работает: `deepseek-v4-flash:free` → 502 (4 подряд)

**Неудачные запросы едят дневную квоту** — `x-ratelimit-remaining-day` уменьшался и после 502, и после 429. `429 model_overloaded` = перегрузка самой модели, а не исчерпание лимита (следующие запросы снова 200).

---

## Ловушки при тестировании бесплатных API

**HTTP 200 + пустой `content` не значит сломанный маршрут.** У reasoning-моделей рассуждения съедают `max_tokens`. Пример из статьи: `free-qwen3.5-plus` при `max_tokens=256` вернул пустой финальный ответ, при `1024` — нормально завершил. Из 299 completion-токенов 283 пришлось на reasoning:

```
prompt_tokens: 25
completion_tokens: 299
reasoning_tokens: 283
finish_reason: stop
```

Проверять при пустом ответе: `reasoning_content`, `finish_reason`, поднять `max_tokens`.

**Формат reasoning у каждого свой:**
- отдельное поле `reasoning_content` — kimi-k3 на ShareLLM
- блок ` (и финальный текст после) — minimax-m2.7, minimax-m3
- блоки `thinking` + `text` — Anthropic Messages (Atria, Selora)
- отдельные `reasoning` + ответ — Responses API (Atria)

---

## Провайдеры с триальными кредитами

| Сервис | Кредиты | Модели |
|--------|---------|--------|
| **Fireworks** | $1 | Open модели |
| **Baseten** | $30 | Любые (оплата по времени) |
| **Nebius** | $1 | Open модели |
| **Novita** | $0.50/год | Open модели |
| **AI21** | $10/3 мес | Jamba family |
| **Upstage** | $10/3 мес | Solar Pro/Mini |
| **NLP Cloud** | $15 (нужен телефон) | Open модели |
| **Alibaba Cloud Model Studio** | 1M токенов/модель | Qwen модели |
| **Modal** | $5/мес (+$30 с картой) | Любые (оплата по времени) |
| **Inference.net** | $1 (+$25 за опрос) | Open модели |
| **Hyperbolic** | $1 | DeepSeek V3, Llama 3.3 70B, Qwen3-coder 480B |
| **SambaNova Cloud** | $5/3 мес | DeepSeek V3.1/3.2, Gemma-4 31B, GPT-OSS-120B, Llama 3.3 70B, MiniMax M2.7 |
| **Scaleway** | 1M free tokens | Mistral Medium 3.5, GLM-5.2, Qwen3, Gemma 4, Devstral 2 |
