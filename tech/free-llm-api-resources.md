---
description: Список сервисов, предоставляющих бесплатный LLM API-доступ или триальные кредиты. Агрегировано из cheahjs/free-llm-api-resources (25.5k ⭐, обновлён 3 дня назад).
tags: [tech, llm, free, api, providers]
related:
  - tech/freellmapi
  - tech/free-claude-code
  - tech/jawl-howto-add-provider
  - tech/freenimapi
---

# Free LLM API Resources

**Источник:** https://github.com/cheahjs/free-llm-api-resources (421 коммитов, 2.6k форков)

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
