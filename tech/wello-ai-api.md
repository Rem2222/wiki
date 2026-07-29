---
type: tool
title: Wello — единый API для Claude, GPT, Gemini
description: Российский сервис-прокси к топовым AI-моделям с Dev API, веб-чатом и десктоп-агентом. До 90% дешевле официальных API. Оплата в рублях и крипте.
tags: [api, llm, proxy, claude, gpt, gemini, dev-api, russia]
related:
  - tech/openrouter
  - tech/freellmapi
source: https://wello.dev
stars: 45000
ingested_at: '2026-07-29'
---

# Wello

**Wello** — российский сервис для доступа к AI-моделям через единый API, веб-чат и десктоп-агента. До 90% дешевле официальных подписок.

## Возможности

- **Dev API** — OpenAI-совместимый эндпоинт `https://api.wello.dev/v1`, работает с Cursor, Claude Code, OpenClaw, любым OpenAI-клиентом
- **Веб-чат** — 7 моделей в одном окне, изображения, поиск, кастомные навыки
- **Wello Code** — десктопный кодинг-агент с терминалом, live preview и git
- **Extended thinking** — режим рассуждений на флагманских моделях
- **Веб-поиск** — модель сама решает когда искать в интернете

## Модели и цены (за 1M токенов, input / output)

| Модель | Официально | На Wello | Экономия |
|---|---|---|---|
| Claude Fable 5 | $10 / $50 | $4 / $4 | до 90% |
| Claude Opus 5 | $5 / $25 | $2 / $2 | до 90% |
| Claude Opus 4.8 | $5 / $25 | $2 / $2 | до 90% |
| Claude Sonnet 5 | $2 / $10 | $1.60 / $1.60 | до 80% |
| GPT-5.5 | $5 / $30 | $1.60 / $1.60 | до 90% |
| Gemini 3.1 Pro | $2 / $12 | $1.60 / $1.60 | до 85% |

## Тарифы

| План | Цена | Особенности |
|---|---|---|
| Free | $0 | Пробный доступ, без карты |
| Pro | $5/мес | Все модели, PAYG сверх лимита |
| Max 5× | $19/мес | Лимит ×5, экономия 24% |
| Max 20× | $59/мес | Лимит ×20, экономия 41% |

Оплата: крипта (USDT), скоро карты. Нет авто-продления — продлеваешь вручную.

## Dev API

```
Base URL: https://api.wello.dev/v1
Auth: Bearer <api_key>
Mode: chat_completions (OpenAI-совместимый)
```

### Подключение к OpenClaw / Claude Code / Cursor

```yaml
providers:
  - name: wello
    api_key: ${WELLO_API_KEY}
    base_url: https://api.wello.dev/v1
    models:
      - claude-opus-5
      - claude-sonnet-5
      - gpt-5.5
      - gemini-3.1-pro
```

### Подключение к Minis (OpenMinis)

В Minis добавить как Custom OpenAI-совместимый провайдер:
- **Base URL:** `https://api.wello.dev/v1`
- **API Key:** скопировать из личного кабинета Wello
- **Модели:** любые из списка выше

## Промо

Промо-код: **FORGET** (при регистрации по ссылке https://wello.dev/FORGET)

## Ссылки

- [Сайт: wello.dev](https://wello.dev)
- [Документация для разработчиков](https://wello.dev/developers)
- [Статус](https://wello.dev/status)
- [Поддержка: @wellosupport](https://twitter.com/wellosupport)
