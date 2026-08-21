---
name: hindsight-mental-models
description: Use when filling Hindsight mental models / knowledge pages.
version: 1.0.0
author: buba
license: MIT
tags: [hindsight, memory, mental-models, knowledge-pages, hermes, mcp]
metadata:
  hermes:
    tags: [hindsight, memory, mental-models, knowledge-pages, hermes, mcp]
    related_skills: [memory-management]
---

# Hindsight Mental Models & Knowledge Pages

## When to Use

- Заполнять/освежать mental models (MM) и knowledge pages (KP) Hindsight — обычно
  в Ночной рутине (ретроспектива дневных observations), либо явно при устойчивом
  факте/паттерне в текущей сессии.
- Когда нужно создать постоянный «живой ответ» на повторяющийся вопрос о
  пользователе/стеке/проекте, или справочную страницу-процедуру.
- НЕ использовать при каждом чихе — observations делают основную работу.

Hindsight (память Hermes с MUL-874, база `hindsight-db`, порт 8888, bank `hermes`)
имеет **курируемые слои** — mental models и knowledge pages. В отличие от observations
(создаются автоматически консолидацией), эти слои **создаются только явно**, через
MCP-инструменты Hindsight.

## Три уровня памяти Hindsight (иерархия)

| Layer | Создаётся | Гранулярность |
|---|---|---|
| **Mental models** | **Явно** (MCP `create_mental_model`) | один цельный документ на вопрос |
| **Observations** | Автоматически (консолидация) | одно убеждение на кластер фактов |
| **Raw facts / units** | Автоматически (retain) | один факт на утверждение |

Mental model — «живой ответ на постоянный вопрос». Задаёшь вопрос один раз →
Hindsight пишет ответ и сам переписывает в фоне. Чтение = DB read, без LLM.

## Когда создавать / обновлять mental models

**Создавать** — когда появился **устойчивый** паттерн, который стоит сохранять
как постоянный ответ на повторяющийся вопрос. НЕ на каждый чих.

**Обновлять** — ретроспективно, раз в день (в Ночной рутине): прочитать дневные
observations → «какие устойчивые паттерны заслужили постоянный ответ?» →
create/refresh.

Не путать с observations: MM — курируемое обобщение, KP — справка/процедуры.
Observations появляются сами, их не дублировать в MM без причины.

## Что писать (разделение)

- **Mental models** — на вопросы «про кого/что человек/агент»:
  - «Какие предпочтения Романа?» (стиль, формат ответов, что ценит/не терпит)
  - «Текущий фокус / проекты в работе»
  - «Что за инфраструктура VPS и как устроена»
- **Knowledge pages** — на вопросы «как/что такое» (справка, процедуры):
  - «Инфраструктура: сервисы, порты, как бэкапится»
  - «Процедуры: как обновить Hermes / Multica / провайдеры»
  - «Конфиги: где живут секреты, как устроен провайдер»

## MCP-инструменты (Hindsight)

- `create_mental_model` — создать MM. Параметры важные:
  - `question` — постоянный вопрос
  - `trigger_refresh_after_consolidation: true` — авто-обновлять после консолидации
  - `trigger.refresh_cron` — опционально по расписанию
  - `tags` — скоп (изменает допустимые источники и видимость)
- `refresh_mental_model` (и `update_mental_model`) — переписать/настроить.
- `create_knowledge_page` / `create_knowledge_folder` — страницы/папки «вики».

Проверка доступности: MCP-инструменты Hindsight регистрируются сервером
(`hindsight-api`, порт 8888). Инструменты `create_mental_model` и т.д. — только если
включены в конфигурации MCP-клиента Hermes.

## Как писать хороший вопрос MM

- Один вопрос = один документ (цельный ответ).
- Вопрос должен быть стабилен во времени («предпочтения Романа», а не
  «что Роман сказал про Hindsight 20.08»).
- Формулировка должна поддаваться обновлению по мере накопления памяти.

## Pitfalls

- **НЕ создавать MM автоматически «на ходу»** каждую сессию — это засорит слой.
  MM создаются осознанно (ретроспектива), observations делают основную работу.
- **НЕ дублировать observations** в MM без причины — MM для синтеза/обобщения,
  не для копии фактов.
- review-форк Hermes (background_review) **НЕ имеет доступа** к create_mental_model
  (whitelist: только memory+skills) — создание MM делается в сессии с полными
  инструментами (или в Ночной рутине), не в автоматическом ревизоре.
- `hermes update` может перезаписать патчи кода Hermes — поэтому создание MM
  НЕ должно зависеть от правки `background_review.py`.
- Проверять, что bank_id правильный (`hermes`), иначе создастся в другой bank.

## Verification

- После create/refresh — MM появляется в `mental_models`, KP — в `knowledge_pages`
  (проверять через SQL `docker exec hindsight-db psql`).
- Refresh-флаг: проверить `trigger` в метаданных модели (get_mental_model).