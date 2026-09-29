---
description: "Кодинг-агент с системой taste-1 и Provider API — 88 моделей (Claude, GPT, DeepSeek, Kimi, GLM) через OpenAI/Anthropic-совместимый эндпоинт."
tags: [ai,provider,llm,api,coding-agent]
related: [[ops/services/hermes-agent]] [[tech/deepseek-harness]] [[tech/opencode-go]]
---

# Command Code (commandcode.ai)

## Что это

Кодинг-агент в терминале + Provider API. Открыт исходник (GitHub `CommandCodeAI/command-code`), разработчик — Ahmad Awais, команда подняла $5M. Фишка — мета-нейросимволическая система `taste-1`: агент наблюдает, как ты пишешь код (принято/отклонено/отредактировано), и адаптирует стиль под тебя.

## Provider API

Совместима с OpenAI и Anthropic — можно подключить как провайдер в Hermes / DSH / любой клиент.

**Эндпоинты:**
- `POST https://api.commandcode.ai/provider/v1/chat/completions` — OpenAI Chat Completions
- `POST https://api.commandcode.ai/provider/v1/responses` — OpenAI Responses
- `POST https://api.commandcode.ai/provider/v1/messages` — Anthropic Messages
- `GET https://api.commandcode.ai/provider/v1/models` — список моделей
- `POST https://api.commandcode.ai/provider/v1/systemone` — decision model `typesafe/jev` (вероятности, не текст)

**Аутентификация:** `Authorization: Bearer <CMD_API_KEY>` — один и тот же ключ для CLI и API, создаётся в Studio.

**Правило маршрутизации:** Claude-модели принимаются только на `/v1/messages`, остальные — на `/chat/completions`. Отправляешь Claude на `/chat/completions` — получаешь 400 с подсказкой.

**Медиа:** принимается text + images. Audio/file/document — отклоняются схемой.

## Тарифы

| План | Цена/мес | Кредиты | Назначение |
|---|---|---|---|
| Go | $1 | $10 | open-модели, старт |
| GOAT | $10 | $70 (~75K req) | лучший по соотношению |
| Pro | $20 | $80 (~100K req) | + премиум-модели |
| **Provider** | **$15** | **PAYG без наценки** | **чистый API** |
| Max 10× | $100 | $150 (~219K req) | ежедневный шипинг |
| Max 20× | $200 | $300 (~437K req) | всё без лимитов |
| Team Pro | $40 | ~35K req | пул кредитов |

- Все, кроме Go, имеют доступ к API.
- Кредиты топ-апа не сгорают никогда.
- Лимиты-окна: 5-часовое и недельное (капают только включённые кредиты; on-demand/топ-апы не троттлятся).
- Лимиты окон: Go $2/$5, GOAT $14/$35, Pro $16/$40, Max10 $45/$90, Max20 $90/$180.

## Модели (88 штук)

**Закрытые:** Claude (Opus 4.8, Sonnet 4-6), GPT-5.6 Sol / Luna, Gemini, Grok 4.5.

**Открытые:** Kimi K3 / K2.7 Code / K2.6 / K2.5, GLM-5.3 / 5.2 / 5.1 / 5, MiniMax M3 / M2.7 / M2.5, DeepSeek V4 Pro / Flash / V4.1 Flash, Qwen 3.8 27B / 3.7 Max / 3.7 Plus, Tencent Hy4 / Hy3, MiMo v2.5, Step, Inkling, Nemotron.

**Бесплатно (превью):** Space Bunny Alpha, Pixel Canary, Laguna S 2.1, Ling 3.0 Flash Sante.

### Интересные ставки (за 1M токенов)

| Модель | Context | In | Out | Cache read |
|---|---|---|---|---|
| DeepSeek V4 Flash | 1M | $0.15 | $0.60 | $0.003 |
| DeepSeek V4 Pro | 1M | $0.66 | $1.98 | $0.022 |
| GLM-5.3 Flash | 1M | $0.15 | $0.50 | $0.03 |
| Tencent Hy3 | 262K | $0.14 | $0.58 | $0.035 |
| MiniMax M3 | 1M | $0.60 | $0.30 | $0.12 |
| Kimi K2.7 Code | 256K | $0.95 | $4.00 | $0.19 |

DeepSeek V4 Pro/Flash — off-peak тариф (17ч/день), peak в пн-пт 01–04 и 06–10 UTC дороже ×2.

## Активные DEALs (по состоянию на 2026-09)

- `deepseek-v4.1-flash` — boosted usage ($10 Go / $60 GOAT / $70 Pro), без даты окончания
- `minimax-m3` — 2× usage
- `mimo-v2.5` + `mimo-v2.5-pro` — до 99% скидки
- 4 модели бесплатно (stealth preview / capacity)

## Ограничения данных

- Никогда не тренирует на коде.
- 99% моделей идут через ZDR-совместимых upstream'ов; `CMD_ZDR=1` форсит только ZDR-каналы, иначе фейлит запрос.
- Режим `taste` хранит learning-данные локально на машине.

## Практическая ценность

- **Как дешёвый OpenAI-совместимый endpoint:** Provider plan $15/мес + DeepSeek V4 Flash по $0.15/$0.60 — дёшево для вспомогательных задач.
- **Для DSH/Hermes:** можно подключить как кастомного провайдера (base_url `https://api.commandcode.ai/provider/v1`, key из Studio).
- **Не для:** замены основной подписки Claude — там свой CLI-харнесс с taste-1, а API отдаёт голые модели.
- Родственные темы: [[ops/services/hermes-agent]], [[tech/opencode-go]] (похожий по роли агрегатор моделей), [[tech/deepseek-harness]].

## Ссылки

- 🌐 https://commandcode.ai
- 🌐 https://commandcode.ai/provider (Provider API)
- 📄 https://commandcode.ai/docs/provider (документация)
- 📄 https://commandcode.ai/pricing (тарифы)
- 🐙 https://github.com/CommandCodeAI/command-code
- 🐙 https://github.com/CommandCodeAI
