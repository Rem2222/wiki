---
description: "AI-платформа с полным LLM API на OpenAI/Anthropic-совместимых протоколах (api.b.ai/v1): мульти-модельный чат, оплата картой или криптой, без привязки личности."
tags: [ai,provider,llm,api,web3]
related: [[tech/command-code]] [[tech/opencode-deepseek]] [[ops/services/hermes-agent]]
---

# B.AI (chat.b.ai)

## Что это

AI-платформа: мульти-модельный чат + полный LLM API на OpenAI/Anthropic-совместимых протоколах. Позиционируется как Web3-сервис: вход через Google или кошелёк, оплата картами (Stripe), WeChat Pay, Alipay, UnionPay и криптой (USDT и др.). Привязка реальной личности не требуется.

- 🌐 https://chat.b.ai/chat (зеркало: chat.bankofai.io)
- 📄 https://docs.b.ai/llmservice/api/ (API Reference)
- 📄 https://docs.b.ai/llmservice/pricing-and-usage/ (цены)
- 📄 https://docs.b.ai/llmservice/promotions-and-pricing-notices/ (акции)

## API

- **Base URL:** `https://api.b.ai/v1`
- **Auth:** `Authorization: Bearer <BAI_API_KEY>` или `x-api-key: <BAI_API_KEY>` (эквивалентны)
- Один ключ на все протоколы, SSE-стриминг.

| Метод | Эндпоинт | Протокол |
|---|---|---|
| POST | `/v1/chat/completions` | OpenAI Chat Completions |
| POST | `/v1/responses` | OpenAI Responses (агенты, Codex) |
| POST | `/v1/messages` | Anthropic Messages (Claude SDK/Claude Code) |
| POST | `/v1/decisions` | TypeSafe System One (классификация/скоринг) |
| GET | `/v1/models` | список моделей ключа |
| GET | `/v1/balance` | баланс и квоты |

Нюансы:
- Responses API принимает GPT и DeepSeek семейства. DeepSeek **не поддерживает web search** (в Codex ставить `web_search = "disabled"`).
- Готовые гайды: Claude Code × B.AI, Codex × B.AI.

## Модели и цены (USD за 1M токенов, input / output)

| Модель | In | Out | Cache read |
|---|---|---|---|
| DeepSeek V4 Flash (off-peak) | $0.15 | $0.60 | $0.003 |
| DeepSeek V4 Pro (off-peak) | $0.66 | $1.98 | $0.022 |
| GLM-5.3 Flash | $0.15 | $0.50 | $0.03 |
| MiMo-V2.6-Flash | $0.14 | $0.28 | $0.0028 |
| MiniMax M3 | $0.30 | $1.20 | $0.06 |
| Kimi K3 | $3.00 | $15.00 | $0.30 |
| Qwen3.8-Flash | $0.16 | $0.47 | $0.016 |
| Claude Sonnet 5 | $2.00 | $10.00 | $0.20 |
| Claude Opus 5 | $5.00 | $25.00 | $0.50 |
| GPT-5.6 Sol | $4.00 | $20.00 | $0.40 |
| GPT-6 Luna | $0.10 | $0.50 | $0.01 |
| Gemini 3.1 Pro | $2.00 | $12.00 | $0.20 |
| Grok 4.6 | $2.00 | $6.00 | $0.50 |

Ставки = рыночная розничная цена (без наценки). DeepSeek — time-based: off-peak вдвое дешевле (peak по пекинскому UTC+8: пн-пт 09:00-12:00 и 14:00-18:00), **в чате B.AI DeepSeek считается всегда по off-peak**.

Биллинг: 1 USD = 1,000,000 Credits, списание в Credits.

## Активные акции (с 2026-09-25, UTC+8)

- **MiMo-V2.6-Flash — 10% от цены** ($0.014 / $0.028 за 1M)
- DeepSeek-V4.1-Flash — 30%
- GLM-5.3-Flash — 30%
- Qwen3.8-Flash — 30%
- MiMo-V2.6-Pro — 50%
- GLM-5.2 — 60%, GLM-5.3 — 90%

## Реферальная программа

- Связь приглашения живёт **2 года**, каждый пользователь привязан только к одному пригласившему.
- Пригласивший получает **1%** с твоих топ-апов/подписок (Coin → Credits, 1 Coin = 1,000,000 Credits; Credit'ы из редемпта валидны 30 дней).
- Сетtlement: крипто-топ-ап — на следующий день, фиат/подписка — 30 дней.
- Для приглашённого: «up to $100 in rewards» на топ-апе (детали на платформе).

## Для чего это тебе (Rem)

- ✅ **Настоящий API с нативным tool calling** — в отличие от эмуляции в [[tech/opencode-deepseek]]. Можно подключить к [[ops/services/hermes-agent]] как custom provider (base_url `https://api.b.ai/v1`), к DSH/claude-code — через Anthropic-совместимый `/messages`.
- ✅ Дил на MiMo-V2.6-Flash (10%) — самый дешёвый мимо из виденного, а mimo у тебя основная модель.
- ✅ Один ключ покрывает Claude/GPT/Gemini/Grok/DeepSeek — альтернатива [[tech/command-code]] (там 88 моделей за $15/мес PAYG, здесь без подписки но и без включённых кредитов).
- ⚠️ Крипто-платформа: юрисдикция, стабильность и судьба баланса — риски. Реферальная связь на 2 года при регистрации по invite-ссылке.
- ⚠️ Нет включённых бесплатных кредитов за сам факт регистрации.

## Связи

- [[tech/command-code]] — прямой конкурент (Provider API, no markup)
- [[tech/opencode-deepseek]] — бесплатный, но эмулирует tool calling; B.AI как раз закрывает этот пробел нормально
- [[ops/services/hermes-agent]], [[tech/deepseek-harness]]
