---
title: xKiro — AI-шлюз с бесплатными моделями (api.xkiro.com)
type: tool
status: checked
tags: [llm, api-gateway, free-models, openai-compatible, aggregator, reseller]
url: https://xkiro.com
license: сервис (не open-source)
added: 2026-10-16
---

# xKiro — AI-агрегатор с бесплатным тиром (api.xkiro.com/v1)

AI-шлюз: один OpenAI- и Anthropic-совместимый API на 129 моделей (22 провайдера). Модель —
параметр запроса; есть отдельные эндпоинты картинок, TTS и веб-поиска.

- **Base URL:** `https://api.xkiro.com/v1` — ключ `Authorization: Bearer …` или `x-api-key`
- **`GET /v1/models` — публичный** (проверено 16.10.2026: 200 без ключа, 50 КБ, 124 chat-модели);
  у каждой записи `access_tier` (`free`/`paid`/`premium`), `pricing`, `capabilities`, `context_length`
- **`GET /v1/usage`** — план, окна расхода, остаток free-токенов, кошелёк. Бесплатно и без лимитов
- Нет `/v1/embeddings` (404); есть `/v1/search`, `/v1/fetch`, `/v1/images/generations`, `/v1/audio/speech`
  (без ключа → 401, значит существуют)

## Бесплатный тир (проверено по докам и каталогу)

- **51 chat-модель с `access_tier: free`, input/output = $0** (каталог API на 16.10.2026).
  По провайдерам: qwen 19, cohere 16, mistralai 9, meta 2, meituan 2, stealth 2, sensenova 1
- **Квота: 500 000 токенов/сутки** бесплатно, карта не нужна (окно скользящее, не в полночь).
  Привязка Telegram к аккаунту удваивает до **1 000 000/сутки** — навсегда, плюс одноразовый
  бонус **30 000 000 токенов** на 30 дней (тратится только после дневной квоты)
- Бесплатная квота и платный расход — **разные бюджеты**: free-лимит не трогает кошелёк
- Тир `paid` — нужен план или баланс; `premium` — только реальный депозит (бонусы/промо не открывают)
- Веб-поиск/чтение страниц: 20 запросов в день без плана; картинки — бесплатные генерации в сутки

## Что бесплатно (самое интересное)

- **Qwen 3.5–3.8 всё семейство**: `qwen3.8-max:free`, `qwen3.7-max/plus/flash:free`,
  `qwen3.6-plus:free`, `qwen3.5-flash:free` — 1M контекст, vision, reasoning, tools;
  `qwen3-coder-plus:free` (1.05M), `qwen3-vl-plus:free`, `qwen3.5-397b-a17b:free`
- **Mistral всё семейство**: `mistral-large-4-0` (524K, vision+reasoning), `mistral-medium-3.5`,
  `mistral-small-2603`, `codestral-2508`, `devstral-medium`, `ministral-14b/8b/3b`
- **Cohere 16 моделей**: `command-a-plus` (436K, vision+reasoning), `command-a-reasoning`,
  `north-mini-code`, Aya-семейство, Command R/R+/R7B
- **LongCat**: `longcat-2.5-preview:free`, `longcat-2.0` (1M) — те же «stealth» модели, что в OpenCode
- **Stealth/прочее**: `big-pickle`, `space-bunny-alpha:free`, `sensenova-6.8-flash-lite` (262K vision),
  `lfm-2.5-2.6b`, `ling-3.0-flash-sante`, `apodex-1.1-mini`, `dots-3-note-preview`
- ⚠️ **`meta/muse-spark-1.2/1.3-contributor:free`** — помечены `contributor`: отдаёшь промпты на
  обучение Meta. Ранее уже решено: Muse Spark НЕ использовать для памяти/личных данных

## Предупреждения (важно)

1. **Это посредник, а не провайдер.** Terms прямо говорят: каталог и цены зависят от третьих
   сторон, модели могут исчезнуть без предупреждения; пользователю запрещено «нарушать условия
   третьих провайдеров, через которых маршрутизируются запросы». Т.е. доступ перепродаётся, и
   риск ToS-конфликта с апстримами (OpenAI/Anthropic/Google) лежит на пользователе.
2. **Юрлицо не указано** — на сайте только `© 2026 xKiro` и Contact; платежи через PayOS/PayPal/
   Lemon Squeezy/OxaPay. Для персональных/рабочих данных — не использовать.
3. **Блог/снапшоты расходятся с живым каталогом**: в анонсах «DeepSeek V4.1 Flash — free tier»,
   MiniMax «free» — а в `/v1/models` они `premium`/`paid`. Верить только живому эндпоинту.
4. Регистрация бесплатна (Google/GitHub/Apple), ключ показывается один раз — хранить сразу.

## Как подключить к Hermes (если решим)

Провайдер OpenAI-совместимый: `base_url: https://api.xkiro.com/v1`, ключ в `/root/.hermes/.env`,
`discover_models: true` (каталог публичный). Кандидат на роль бесплатного резерва для vision
(`qwen3.8-max:free` — та же модель, которой обходим 429 на opencode-go).

**Статус: разведано, НЕ регистрировались и НЕ подключали.** Ключа нет — чат без ключа → 401
(проверено). Реальный free-вызов можно проверить только после регистрации.