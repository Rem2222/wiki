---
title: Clef / Clef-flash (Cloudflare) — decision-модели и 4 варианта в пайплайне Романа
tags: [llm, clef, cloudflare, workers-ai, decision-model, memory-routing, triage]
created: 2026-10-02
status: отложено — вернуться (пилот: пункт 3, маршрутизация памяти)
---

# Clef и Workers AI: что это и куда вставить в пайплайн

**Статус:** разобрано 02.10.2026. Роман: «Закинь в Вики, потом вернёмся к вопросу».
**Закреплено задачей:** [MUL-10180: Вернуться к маршрутизации памяти выбирающей моделью (Clef, пункт 3 из разговора 02.10)](mention://issue/01a0fee2-f318-7023-9d92-3a3d2823d848) — assignee rem2222, backlog.
**Наиболее интересен пункт 3** (маршрутизация памяти) — Роман думал об этом ещё при
разборе памяти. Пилот не запущен, решение не принято.

## Что такое Clef

**Это НЕ чат-LLM.** Clef (и Clef-flash) — семейство **decision-моделей**: на вход идёт
`state` (произвольный контекст) + схема типизированных вопросов, на выход —
**вероятности по каждому допустимому варианту каждого поля**. Генерации текста нет.
Категорию открыл Jev (Typesafe AI, System One) — Clef его прямой конкурент и **лидер
Jev Decision Index**.

| | Clef | Clef-flash | Jev |
|---|---|---|---|
| Бэкбон | **Qwen3.8-27B** | **Qwen3.5-9B** | — |
| Контекст | **65 536 (64k)** | 65 536 | 32k |
| Vision (картинки/видео) | **да** | **да** | нет (только текст) |
| Лицензия | **Apache 2.0**, веса на HF | Apache 2.0 | закрытая |
| Медианная задержка | 209.3 мс | **38.8 мс** | 524.1 мс |
| Цена (Workers AI) | $0.24/M input (21 818 нейр./M) | **$0.09/M input** (8 182 нейр./M) | — |

**Бенчи (blog, 01.10.2026) — Clef лучше Jev в большинстве:** BFCL 98.47/98.76 vs 95.75,
BANKING77 94.20 vs 79.74, CLINC150+OOS 97.43 vs 89.27, API-Bank 91.93 vs 88.19,
ToolRet 69.19 vs 65.28, Amazon ESCI 57.48 vs 55.21, Home appliances 82.95 vs 52.27.
**Jev впереди в:** When2Call 80.97 vs 72.37, BRIGHT 47.52 vs 45.91, PhishNChips (DiffusionGemma Jev 85.35 vs 79.60).
У Typesafe-своего eval-suite Clef выиграл 3 из 4 направлений.

**Как устроено (почему быстро):** Qwen делает **prefill-only проход**, дальше валидные
варианты схемы скорятся **параллельно, без авторегрессивной генерации**; пост-тренинг —
LoRA rank-256 + label-smoothed CE + Brier loss (калибровка вероятностей) + RLCD.

**Совместимость:** API **полностью совместим с Jev** → подмена «в одну строку».
Пример вызова (из блога): `POST https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/cloudflare/clef`
с `{"model":"clef","state":"...","questions":{"urgent":{"type":"noul",...},"team":{"type":"choice","criteria":{...}},"severity":{"type":"score","criteria":[...]}}}`.
Типы полей: **`noul`** (вероятность), **`choice`** (варианты + описания), **`score`** (порядковая шкала).

## Что такое Workers AI

**Серверless-инференс на GPU Cloudflare** — «Run machine learning models, powered by
serverless GPUs, on Cloudflare's global network». Доступно на **Free и Paid** планах.

- **50+ open-source моделей** (Llama, DeepSeek, GLM, Kimi, Mistral, Gemma, Nemotron…)
  + собственные (Clef) + **Bring Your Own Model** (технология из купленного Replicate)
- **Способы вызова:** биндинг `env.AI.run("@cf/…")` в Worker · **REST API**
  `POST /client/v4/accounts/{ACCOUNT_ID}/ai/run/{model}` (Bearer) ·
  **OpenAI-совместимые эндпоинты** · Vercel AI SDK · HF Chat UI · Dashboard · Batch API
- **Экосистема:** AI Gateway (кэш, rate-limit, fallback, prepaid-кредиты),
  Vectorize, Workers/Pages, R2, D1, KV
- Свежее: **сервис RL-файнтюнинга** (AI Gateway → Workers AI → Containers → Trainer → BYO Model)

### Цена
- **Нейроны:** **$0.011 / 1 000** (≈ 9.2 ₽ при 83.69 ₽/$)
- **Бесплатно: 10 000 нейронов/сутки**, сброс 00:00 UTC (≈ $0.11/сут ≈ 276 ₽/мес эквивалента, не переносится)
- Свыше квоты — Workers Paid либо prepaid AI Gateway credits
- В бесплатной квоте умещается: **clef-flash ≈ 1.22 M входных токенов/сут**
  (~1 200 вызовов по 1k), **clef ≈ 458 k/сут**
- Обе Clef-модели **не входят** в список «требует платный биллинг»
  (в отличие от kimi-k2.6/k2.7, glm-5.2/5.3, deepseek-v4-flash-0731/v4-pro-0813)

## 4 варианта применения в пайплайне Романа

Ранжировано «выгода ÷ трудоёмкость». Все — там, где сейчас решает LLM (деньги/задержки)
либо руки Романа.

### 1. Триаж алертов: шум или инцидент (ntfy + инбокс Мультики)
Боль (факты от 02.10): MUL-10149 — codegraph наспамил 232 warning/сутки;
MUL-10163 — `autopilot.err` 3836 строк; нога `mark_read` — 36×400 за 30ч; в инбоксе 11 непрочитанных.
```
state   = текст алерта + хвост лога        # 64k влезает целиком
questions:
  incident : noul    # реальный инцидент или шум/повтор?
  severity : score   [info, warning, critical]
  action   : choice  [вTG_сразу, в_backlog_молча, выбросить]
```
Отдача: 38.8 мс и бесплатно вместо LLM-вызова на каждую строку. Кейс Cloudflare из блога
(так они классифицируют домены угроз). Главная выгода — **внимание Романа**, а не деньги.

### 2. Триаж новых задач в Мультике
Боль: создание задачи = 4 ручных дропдауна (проект/статус/приоритет/исполнитель);
Quick Create диспатчит вслепую и **теряет задачу** при падении агента; на доске 190 In Review + 73 Todo.
```
state   = title + description issue        # 64k — с описанием и метками
questions:
  project : choice [Routine, GSD, Multica, Обучалка, Кворум, myRDP]
  priority: score  [none, low, medium, high, urgent]
  dispatch: choice [только_в_backlog, сразу_диспатчить]
  assignee: choice [Hermes Helper, buba, rem2222]
```

### 3. ★ Маршрутизация памяти в четыре корзины — ИНТЕРЕС РОМАНА, ВЕРНУТЬСЯ
Боль: правило памяти (факт → OpenViking, оперативное → MEMORY.md, правило → USER.md,
вики только по команде + запрет «решения по инструментам не писать», **кейс Needle 2**)
сейчас исполняется **суждением агента каждый турн** → отсюда непоследовательность и ошибки.
Это обсуждалось ещё при разборе памяти — Роман тогда думал именно про decision-модель.
```
state   = сообщение + хвосты MEMORY.md / USER.md   # контекст для решения
questions:
  store     : choice [ov_fact, memory_ops, user_profile, wiki_только_по_команде, skip]
  sensitive : noul   # секрет/личное — не сохранять
```
Отдача: не деньги (объём копеечный), а **консистентность** — сейчас цена ошибки выше цены вызова.
Следующий шаг: согласовать пилот → скрипт-инструмент через REST → прогон на реальной ленте сообщений.
Напоминание: [MUL-10180](mention://issue/01a0fee2-f318-7023-9d92-3a3d2823d848).

### 4. Стоимостной роутинг: сложность турна → дешёвая или сильная модель
Боль: правило «самую дешёвую рабочую» + дашборд Hermes 686/791/983 ₽ за 30 дней;
фоллбэк-цепочка срабатывает **только по ошибке провайдера**, а не по сложности —
подтверждения и чтение файлов идут на ту же модель, что и тяжёлая задача.
```
state   = хвост системного промпта + последний запрос
questions:
  complexity: score  [trivial, normal, hard]
  needs_tools: noul
  route      : choice [дешёвая, основная, топ]
```
Самая крупная экономия в деньгах и **самая тяжёлая в реализации** (хук/прокси на пути вызова,
а не внешний скрипт). Реалистично — как этап в AI Gateway или свой промежуточный слой.

## Ограничения (чтобы не разочароваться)
- **Не агент:** Clef только классифицирует, действие делает твой код/агент.
- **Данные уходят в Cloudflare.** Принцип Романа «чувствительное через прокси не гонять» —
  для пунктов 1 и 3 фильтровать, что кладём в `state`; либо локальные веса Apache 2.0,
  но на CPU-only VPS 27B (и даже 9B) — больно. Домашний ПК (GT 1030, 64 GB) — 9B quantized в теории.
- **Формат свой** (`state`+`questions`, не `messages`) → нужен маленький скрипт-инструмент
  в духе `dex_tools.py`, ~20 строк через REST с Bearer-токеном. OpenAI-совместимые эндпоинты
  Workers AI годятся для обычных LLM, но не для формата решений Clef.
- Не замена `vision_analyze`: Clef отдаёт вероятности по заданным вопросам, а не описание картинки.

## Источники
- 🌐 https://blog.cloudflare.com/clef-decision-models/ (01.10.2026)
- 🌐 https://developers.cloudflare.com/workers-ai/ — обзор платформы
- 🌐 https://developers.cloudflare.com/workers-ai/platform/pricing/ — нейроны, 10k/сутки, цены Clef
- 🌐 https://developers.cloudflare.com/workers-ai/models/clef и `/clef-flash` — спецификации
- 🌐 https://developers.cloudflare.com/workers-ai/platform/limits/ — rate limits (GA, обновлено 17.09.2026)
- 🌐 https://huggingface.co/Cloudflare/clef и https://huggingface.co/Cloudflare/clef-flash — веса
- 🌐 https://huggingface.co/spaces/multimodalart/jev-decision-index — общий бенчмарк
- 🌐 https://clef-evals.workers-ai-mle.workers.dev/ — живой демо-бенч
- 🌐 https://typesafe.ai/blog/introducing-system-one-models-and-jev — Jev, первоисточник категории
