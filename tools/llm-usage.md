---
title: LLM-расход Hermes 30 дней — сравнение провайдеров
tags: [llm, usage, pricing, dashboard]
updated: 2026-10-01
html: https://rem2222.top/llm-usage.html
---

# LLM-расход · 30 дней · сравнение провайдеров

Интерактивный дашборд: [rem2222.top/llm-usage.html](https://rem2222.top/llm-usage.html) (HTML в `tools/llm-usage.html`).

## Объём (Hermes state.db `session_model_usage`, 01.09–01.10.2026)
- Вызовов: 99. Вход (без кэша) 25.9M · Выход+reasoning 4.3M · **Cache-read 618.5M** (≈24× входа — доминирующая статья).
- Модели: mimo-v2.6-flash (основной, 18.4M входа/530M кэш), mimo-v2.5 (VLM-консолидация), deepseek-v4-flash, qwen-tp, qwen3.6-unlim.
- Мультика ходит через Hermes → её вызовы уже в этой же выборке.

## Стоимость того же объёма (₽/мес, курс 83.69)
| Тир | Провайдер | ₽/мес |
|---|---|---|
| дешёвый | DeepSeek V4.1 Flash · b.ai | **698** |
| дешёвый | Qwen3.6-35b-a3b · neuraldeep | 801 |
| дешёвый | DeepSeek V4.1 Flash · TeamoRouter | 993 |
| средний | Claude Haiku 4.5 · TeamoRouter | 1108 |
| средний | GPT-6 Sol · TeamoRouter | 1831 |
| топовый | Qwen3.8-27b · neuraldeep | 2680 |
| топовый | Claude Opus 5.5 · TeamoRouter | 9084 |
| топовый | Kimi K2.6 · neuraldeep | 14497 |
| топовый | GPT-6 Astra (Fast) · TeamoRouter | 18314 |

Сейчас реально платится ≈ 0 ₽/токен (opencode-go бесплатно) + 512₽/мес neuraldeep безлим. Вывод: на per-token выгоднее всего DeepSeek V4.1 Flash (b.ai умеет дешёвый cache-read $0.003/M).