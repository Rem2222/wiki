---
description: "Coarena (Coasty Systems, YC) раздаёт Free Model API: один ключ, 18 моделей включая наш deepseek-v4.1-flash-1017, бесплатно $5 использования в день при 30 запросах/мин. Проверено по живому API 12.11.2026: в доках обещано 22 модели и GPT-6, но API отдаёт 18 без GPT. Риск: арена видит промпты. Решение: подключать резервом, не дефолтом."
tags: [coarena,api,models,free,deepseek,providers]
related:
  - tech/vidzhety-telegram-html-pryamo-v-soobschenii-widget-sandbox
  - tech/hermes-external-integrations
created: 2026-11-12
updated: 2026-11-12
source: "https://coarena.ai/"
---

# Coarena: бесплатный API к 18 моделям, $5 в день

## Что это

Coarena (`coarena.ai`, Coasty Systems, Inc., backed by Y Combinator) — арена computer-use бенчмарков, которая заодно бесплатно раздаёт доступ к чужим моделям через собственный ключ. Это не компания DeepSeek и не их акция: DeepSeek здесь просто одна из моделей в списке.

## Цифры

Проверено 12.11.2026 обходом их API и документации.

- Base URL два, ключ один: `https://coarena.ai/api/v1` (OpenAI SDK, Codex, LangChain) и `https://coarena.ai/api` (Anthropic SDK, Claude Code)
- Ключи создаются на `coarena.ai/account/api/keys`, вход через Google, карта не нужна
- Без ключа эндпоинт отвечает 401: «No API key was sent. Send your Coarena key as Authorization: Bearer ***»
- `/api/v1/models` отдаёт **18 моделей** без авторизации

Список: claude-fable-5, claude-fable-5-1, claude-fable-5-2, claude-haiku-5-5, claude-opus-5-5, claude-sonnet-5-5, **deepseek-v4-1-flash-1017**, gemini-3-8-flash, gemini-4-argon, gemini-4-carbon, glm-5-3-flash, grok-4-7, hy4, kimi-k3, kimi-k3-1-pro, mimo-v2-6-pro, minimax-m3-1-flash, qwen3-8-2-4t-a95b.

В документации при этом написано «22 models today» и перечислены `gpt-6-1-sol`, `gpt-6-astra` — но API их не отдаёт. Верить только `/api/v1/models`.

## Лимиты

Формулировка из их документации: «Free: $5 of model use a day, and Coarena pays». То есть это не нулевая цена за токен, а дневной кредит на $5 использования, который покрывает Coarena.

Дополнительно: 30 запросов в минуту, 2 одновременных, плюс дневной лимит запросов, который они могут задать. При исчерпании — ошибка `insufficient_quota` с текстом «Daily free limit reached: $5.00 of model usage today». Повышение лимита запрашивается отдельным вызовом API.

## Почему нам интересно

Наша модель по умолчанию — ровно `deepseek-v4.1-flash-1017`, и мы платим за неё Alibaba через token-plan. Coarena даёт тот же id бесплатно до $5 в день. При цене flash это десятки миллионов токенов в сутки — наш обычный рабочий день целиком.

Открытые веса при этом не выдумка: `deepseek-ai/DeepSeek-V4.1-Flash-1017` на Hugging Face, лицензия **mit**, 374 631 скачивание, 5 568 лайков, опубликована 17.10.2026.

## Риски

Третья сторона видит все промпты, а это арена, которая собирает данные для бенчмарков. Их Terms отдельно упоминают, что покрывают «saved credentials and agent memory» — в контексте их computer-use агентов, но звучит однозначно. В обороте появляется ещё один секрет.

Правило: обычная рутина и болтовня — можно, серверные доступы, ключи и личные данные — нет.

## Надо ли нам

Да, но как **резерв**, не как основной канал: подключить отдельным провайдером `coarena` с моделью `deepseek-v4.1-flash-1017` и включать, когда не хочется жечь платные токены. Ключ Роман заводит сам и кладёт на сервер по SSH, в чат он не попадает.

## Статус

Разобрано 12.11.2026 по живому API и документации. Ничего не подключено, ключ не заводился.

Ссылки: [coarena.ai](https://coarena.ai/), [ключи](https://coarena.ai/account/api/keys), [веса на HF](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017).
