---
description: "jev-ultrafast — браузерный агент от Browser Use на Jev (System One). Динамическая индексированная область действий: одна операция + цель за один запрос. 20.6k⭐ за 10 дней. Цифры, ограничения и пригодность для нашего VPS."
tags: [browser-agent, jev, typesafe, browser-use, automation, python, llm-routing]
created: 2026-09-26
source: https://github.com/browser-use/jev-ultrafast
related:
  - "[[tech/jev-jevrouter]]"
  - "[[tech/webwright]]"
  - "[[tech/lightpanda-browser]]"
  - "[[tools/agent-reach]]"
---

# Jev Ultrafast — браузерный агент на Jev

**Репо:** github.com/browser-use/jev-ultrafast · MIT · Python · `main`

| | |
|---|---|
| ⭐ | **20 646** / 1 419 форков |
| Создан | **16.09.2026** (10 дней до записи) |
| Последний пуш | 25.09.2026 |
| Описание | «Fastest and cheapest web agent» |
| Зависимости | две штуки: `browser-harness==0.1.13`, `httpx[http2]>=0.28,<1` |
| Python | **≥3.12** |

Официальный репозиторий организации **Browser Use** (тот самый browser-use-фреймворк), не форк. Рост ~2 000 звёзд/день.

Суть: первый **реальный прод-кейс Jev** (TypeSafe System One) — см. [[tech/jev-jevrouter]], где Jev был описан теоретически.

## Идея

Вместо того чтобы LLM генерил команду, каждое наблюдение строит **таблицу индексированных элементов**:

```text
[1] button    Change ticket type · Round trip
[2] combobox  Where from?        · San Francisco
[3] combobox  Where to?          · empty
[4] textbox   Departure          · empty
```

**Один запрос к Jev** возвращает и операцию, и цель. Набор операций: `CLICK`, `TYPE_TEXT`, `SELECT`, `SCROLL_UP`, `SCROLL_DOWN`, `WAIT`, `DONE`, `BLOCKED`.

```text
                      один TypeSafe-запрос
                     ┌───────────────────────────┐
страница → таблица → │ operation                 │
  элементов          │ click_target              │
                     │ type_text_target          │
                     │ select_target (если есть) │
                     └─────────────┬─────────────┘
                         применить только целевой
                     ┌─────────────┴─────────────┐
                     │ CLICK [7] / TYPE_TEXT [3]  │ → браузер
                     └─────────────┬─────────────┘
                            маленький LLM → текст → браузер
```

**Ключевой ход — спекулятивные вопросы.** Jev отвечает на `click_target` и `type_text_target` одновременно, но исполняется только тот, что совпадает с выбранной операцией. Два решения — **один сетевой раунд**. Каждый target-head содержит только совместимые элементы.

`TYPE_TEXT` — единственный случай, когда включается маленький LLM (OpenAI-совместимый хелпер). Он должен вернуть JSON ровно с одним валидным полем `text`; код не выцепляет литералы из текста свободной формы.

В политике **нет** site-specific скриптов и заранее подготовленных строк полей. Скриншоты отключены по умолчанию в библиотечном вызове (`screenshots=True` или `record_dir=...` включают).

## Цифры

**Задача:** Google Flights, Zürich → London, one-way, 20.09.2026, economy, 1 adult → **7 073 мс** при 1×. Таймер стартует после первой наблюдаемой страницы и включает model-вызовы, генерацию текста, работу браузера, stale-решения и ожидания загрузки.

Сравнение с их же исходной версией, **6 чередующихся прогонов** с одинаковыми моделями и настройками:

| Метрика | Было | Стало |
|---|---|---|
| Медиана времени задачи | 9.450 с | **7.092 с** (−25%) |
| Jev-запросов на прогон | 22 | **17** |
| Browser protocol calls (медиана) | 1 092 | **101** |
| Прошли верификацию | 3/3 | 3/3 |

Расход на записанный прогон: **90 558 входных токенов TypeSafe**, два текст-вызова = **$0.00006272** через OpenRouter. Медианная латентность Jev — **178 мс**.

Прочие замеры: Wikipedia-статья за **2.798 с**, локальный hotel-фильтр за **1.896 с**.

### Их собственные оговорки (важно)

- 6 прогонов → **p = 0.25**, сами пишут «too few for a strong statistical claim»
- «two websites do not establish broad reliability»
- Это **не** общий бенчмарк агентов, а замер одной задачи на одном профиле Chrome
- Выбор `DONE` **не** доказывает успех — верификация исхода независимая
- `$0.00006272` — это **только** плата за text-helper вызовы через OpenRouter, **не** полная стоимость задачи. У TypeSafe есть счётчики токенов, но **не** сумма в долларах; browser-стоимость тоже не учтена
- Google, сетевые ответы, маршрутизация и кэши браузера в замере **живые** — измерение не изолировано
- Пять прогонов до заморозки кандидата (9.302–7.559 с) — это development-попытки с менявшимся кодом, **не** сравнение выше

Условия замера: TypeSafe `jev-1.13.0`, `inception/mercury-2.5`, viewport 1120×780, отключённый text-reasoning, обе руки на одном профиле Chrome. Оригинал — замороженный коммит `68c077bf79caca4e817b8e8a5854b2efa0c81ff6` (обе руки на Mercury, чтобы не смешать смену хелпера с изменением кода).

Полные замеры и границы: `docs/performance.md`, `docs/design.md`, `docs/full-speed-measurement.json` (31 КБ).

## Ограничения

**Не поддерживается:** shadow roots, frames, canvas, загрузка файлов, новые вкладки, вложенный скроллинг, произвольные keyboard-виджеты. Прямо указано в README — это MVP.

**Лимиты рана** (`docs/design.md`): **60** браузерных действий, **120** decision-запросов, до **250** action-кандидатов (обрезанные не выбираются). Сервис loopback-only, проверяет Host/Origin/local token. Вкладки делят существующий профиль Chrome.

**DOM-reader** покрывает обычные HTML/ARIA-контролы, **не** полный accessible-name спек.

**Слабое место стабильности:** runtime-агент «ломается при first-mile/last-mile, prompt-injection-гонках, DevTools/экспортных фильтрах на 1000+ элементов».

### Что исправили после первого демо

- Прототип использовал 5 вручную подготовленных шагов и копировал строки из кавычек — **не** демонстрировал декомпозицию задач и генерацию текста. Текущая политика использует исходный goal целиком.
- Аудит нашёл: каждое INPUT считалось редактируемым → чекбоксы классифицировались неверно. Теперь TYPE_TEXT зависит от editable-роли.
- Freshness сравнивает **семантическое** состояние, а не считает DOM-мутации.

## Установка

```bash
git clone https://github.com/browser-use/jev-ultrafast.git
cd jev-ultrafast
uv sync
cp .env.example .env
# заполнить TYPESAFE_API_KEY и TEXT_MODEL_API_KEY
uv run jev
```

Инспектор на **http://127.0.0.1:8766** → **Start demo → Run automatically**. Показывает нумерованные элементы, вероятности операций и целей, исполняемые действия. **Choose next** — пауза перед выполнением.

Библиотека:

```python
from jev_ultrafast import Agent

with Agent(
    "https://www.google.com/travel/flights?hl=en",
    "Find one-way flights from Zurich to London on September 20, 2026, "
    "for one adult in economy. Stop when matching flight options are visible.",
) as agent:
    for state in agent.run():
        print(state["elapsed_ms"], state["status"])
```

### Переменные окружения (`.env.example`)

| Переменная | Дефолт | Что это |
|---|---|---|
| `TYPESAFE_API_KEY` | — | ключ Jev, **обязателен** |
| `TYPESAFE_MODEL` | `jev-latest` | |
| `TEXT_MODEL_API_KEY` | — | ключ OpenAI-совместимого хелпера, **обязателен для TYPE_TEXT** |
| `TEXT_MODEL_BASE_URL` | `https://openrouter.ai/api/v1` | |
| `TEXT_MODEL` | `inception/mercury-2.5` | Gemini, GLM, DeepSeek тоже работают |
| `TEXT_MODEL_REASONING` | `none` | |

## Цена Jev

- Вход: **$0.042/MTok** ($42/млрд токенов), вывод **бесплатно**
- ⚠️ **`typesafe.ai/pricing` отдаёт 404** — официальной страницы цен нет
- Ключ — через **waitlist** (`console.typesafe.ai`), не мгновенно
- Цифра $0.042 подтверждается только сторонними обзорами, не официальным источником

## Пригодность для нашего стека

### На VPS — НЕ заработает как есть

| Требование | У нас |
|---|---|
| Настоящий Chrome через CDP + галочка в `chrome://inspect/#remote-debugging` | На 9222 стоит **lightpanda**, не Chrome |
| Python ≥3.12 | ✅ **3.12.3** на VPS, `uv 0.11.16` установлен |
| `TYPESAFE_API_KEY` (waitlist) | нет |
| `TEXT_MODEL_API_KEY` (OpenRouter) | есть OpenRouter |

Python и uv подходят — **узкое место только браузер**. `browser-harness` коннектится к настоящему Chrome через один editable CDP websocket; на headless VPS с lightpanda не подключиться.

### Зрелость кода — всего 3 коммита

```
1231850a0  2026-09-18  docs: announce the Cloud waitlist below the README title (#30)
452c1ad2d  2026-09-17  Reduce browser round trips and record a 7-second Flights demo
68c077bf7  2026-09-17  Build Jev Ultrafast browser agent and real-web demo
```

Весь репозиторий написан за **два дня** (17–18 сентября), дальше только документация. 20 646 звёзд набраны на трёх коммитах — это вирусный демо-репозиторий, а не вылизанная библиотека. Стоит иметь в виду перед использованием в реальных задачах.

### Где осмысленно — домашний ПК

Там Chrome есть, `chrome://inspect` доступен. Сценарий ровно наш: автоматизация веб-задач, где 3 секунды на решение слишком много.

### Чем отличается от существующего

Текущий `browser_exec` и lightpanda работают **по скриншотам/DOM**. Jev ест **структурированное состояние** и не тратит вызовы на картинки — отсюда разница 1 092 → 101 protocol calls. Это реальное архитектурное отличие, а не маркетинг.

См. также [[tech/webwright]] (сравнение Stagehand / browser-use / Webwright) — jеv-ultrafast туда пока не внесён.

### Следующий шаг

1. Проверить Python ≥3.12 на VPS
2. Встать в waitlist TypeSafe → получить `TYPESAFE_API_KEY`
3. Поставить на **домашнем ПК** (не на VPS)
4. Сравнить с `browser_exec` на одной задаче

## Файлы репо (40 файлов, 2.55 МБ, из них 1.1 МБ — demo.gif)

| Файл | Роль |
|---|---|
| `jev_ultrafast/agent.py` (7.9 КБ) | весь цикл + text-helper handoff |
| `jev_ultrafast/snapshot.js` (6.5 КБ) | атомарный DOM-снимок, индексированные контролы, freshness-guard'ы |
| `jev_ultrafast/browser.py` (9.2 КБ) | коннект, текущая геометрия, исполнение |
| `jev_ultrafast/model.py` (8.5 КБ) | динамические operation/target heads + генерация текста |
| `jev_ultrafast/questions.py` | инструкции модели |
| `jev_ultrafast/demo.py` | локальный инспектор |
| `tests/test_agent.py` (12.4 КБ) | тесты — **офлайн** |
| `scripts/check_guards.py` | реальные контролы в локальном браузере **без model-вызовов** |

Тесты офлайн. `scripts/record_flights.py` и `scripts/render_demo.py` делают платные API-вызовы. Ключи и сырые трейсы игнорируются git'ом.

## Ссылки

- 🌐 https://github.com/browser-use/jev-ultrafast
- 📄 `docs/performance.md` — замеры, границы, хэши исходников
- 📄 `docs/design.md` — архитектура политики и runtime
- 📄 `docs/measurement.json`, `docs/full-speed-measurement.json` — сырые данные
- 🌐 https://github.com/browser-use/browser-harness — CDP-коннект (зависимость)
- 🌐 https://docs.typesafe.ai/patterns/fan-out — speculative fan-out
- 🌐 https://browser-use.com/ultrafast — cloud waitlist (в README, утверждение не проверено)
- 📄 [[tech/jev-jevrouter]] — что такое Jev, JevRouter, MCP-адаптер
