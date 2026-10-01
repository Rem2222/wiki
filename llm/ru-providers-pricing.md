---
title: Недорогие LLM-провайдеры РФ — сравнение цен
tags: [llm, providers, pricing, cheap]
updated: 2026-10-01
---

# Недорогие LLM-провайдеры РФ: сравнитель цен

Цель — дешёвые провайдеры для Hermes/агентов. Цены: «вход/выход за 1 млн токенов», валюта как у провайдера (USD или ₽). Скидки меняются в реальном времени — сверять перед покупкой.

## 1. TeamoRouter (ru) — роутер, «самый дешёвый сейчас в РФ»
[teamorouter.com/ru](https://teamorouter.com/ru#pricing) · API-доки: [teamorouter.com/ru/docs/api-integration](https://teamorouter.com/ru/docs/api-integration)
Ключ получен 01.10.2026, хранится как `TEAMO_KEY` в `~/.hermes/.env` (sk-teamo-…). Цены в **USD/1M**, тарификация по скидке на момент вызова.

| Модель | Вход | Выход | Скидка |
|---|---|---|---|
| GPT-6 Luna | $0.05 | $0.25 | −50% |
| GPT 6.1 Sol | $0.20 | $1.00 | −90% |
| GPT-6 Astra | $1.41 | $7.05 | −86% |
| GPT-6 Astra (Fast) | $2.00 | $10.00 | −90% |
| GPT-5.6 Terra | $0.316 | $1.90 | −84% |
| Claude sonnet 5.5 | $0.60 | $3.00 | −70% |
| Claude Haiku 4.5 | $0.121 | $0.605 | −88% |
| Claude Opus 5.5 | $0.992 | $4.96 | −75% |
| Gemini 3.8 Flash | $0.306 | $1.53 | −59% |
| DeepSeek V4.1 Flash | $0.113 | $0.451 | −25% |
| GPT Image 2.5 | ≈ $0.005–0.016/изобр | | −84…−97% |

## 2. b.ai — DeepSeek V4.1 Flash (хорошие скидки)
Доки: [docs.b.ai/llmservice/models/deepseek-v4-1-flash/](https://docs.b.ai/llmservice/models/deepseek-v4-1-flash/)
1M ctx · 384K out · multimodal (image+text→text) · tool-calling · context cache.

| Период | Вход | Кэш-write | Кэш-read | Выход |
|---|---|---|---|---|
| Off-Peak | $0.15 | $0.15 | $0.003 | $0.60 |
| Peak | $0.30 | $0.30 | $0.006 | $1.20 |

- **Промо с 25.09.2026**: тариф 30% от стандартной цены (и дальше ступенчато).
- Peak: пн-пт 09:00–12:00 и 14:00–18:00 (UTC+8). Кэш-read = 0.02× вход.
- провайдер `bai` уже есть в `config.yaml` (`api.b.ai/v1`), но **баланс $0** — после пополнения рестарт гейтвея.

## 3. neuraldeep (₽) — свой, оплата в рублях
[hub.neuraldeep.ru/models](https://hub.neuraldeep.ru/models) · куплен: **free-тариф + безлимит qwen = 512 ₽** + `qwen3.6-unlim` дефолт. OpenAI-совместимый `/v1/chat/completions` + `/v1/responses`. Цены ₽/1M.

| Модель | Вход | Выход | Кэш | Примечание |
|---|---|---|---|---|
| qwen3.6-35b-a3b (+noreason) | 7,14 | 40,8 | 0,71 | 256k, tools·reasoning·vision |
| qwen3.6-fp8 (+noreason) | 7,14 | 40,8 | 0,71 | FP8 fast-lane |
| qwen3.8-27b (+noreason) | 24,48 | 122,4 | 2,45 | 256k |
| kimi-k2.6 | 99,75 | 420 | 16,32 | reasoning, long-horizon (Starter·Pro) |
| deepseek-v4-flash-b24 (Битрикс24) | 48,75 | 139,75 | 1,47 | pay-as-you-go, 1M |
| gemma-b24 | 10 | 30 | 1 | pay-as-you-go |
| qwen3.6-unlim / -noreason | ∞ | ∞ | — | **безлимит по подписке** |

**Прочее одним ключом:** embedding (bge-m3, qwen3-embedding-4b/8b, giga-embeddings, frida, jina-v4, e5), rerank (qwen3-reranker-8b, bge-reranker), STT (whisper-1, whisper-podlodka-turbo, gigaam-v3), **TTS** `qwen3-tts` + `espeech-tts` (`/v1/audio/speech`, RU с ударениями), **картинки** `Qwen-Image-2.1` (`/v1/images/generate` → task → result), Drift-агент.

## 4. Из памяти — пробованные/фоновые
- **Hermes фоллбэк-цепочка**: `deepseek-v4-flash → qwen-tp → openrouter` (секция `fallback_providers` config.yaml).
- **opencode-go** — текущий основной модель-провайдер Hermes (aux: vision/compression/session_search).
- **freeqwenapi / freedeepseekapi** — остановлены 30.09 (WAF).
- **OpenModel** — бесплатный deepseek-v4-flash (2026-07; возможно устарело).
- **ChatLLM/Abacus** — $7/мес (неясно по моделям); **Go/ChatLLM** — ~$10/мес без vision.
- **Ali токены** — дорого (месячная экспирация).
- Каталог бесплатных API: [github.com/cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources).

## Вывод
- **Самая дешёвая точка входа** — **TeamoRouter** (роутер, до −90%, дешёвые GPT-6 Luna / Sol и Claude Haiku).
- **Самый «свой»/рублёвый** — **neuraldeep** (512₽ безлим qwen + всё остальное тем же ключом).
- **b.ai** — выгоден для DeepSeek V4.1 Flash, особенно кэш-read и промо −70%.

Источники: teamorouter.com/ru#pricing · docs.b.ai …deepseek-v4-1-flash · hub.neuraldeep.ru/models · память OV (Roman/llm_providers, free_llm_api_resources).