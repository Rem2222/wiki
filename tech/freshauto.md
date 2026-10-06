---
description: "freshauto.ru без парсера вёрстки: каталог живёт в SSR-блобе _piniaInitialState, фильтры — path-сегменты, инкремент — diff sitemap.xml. Полный дамп 10 417 авто + часовой монитор новых под фильтр."
tags: [freshauto, scraping, ssr, pinia, sitemap, sqlite, cron, parsing, russia, cars]
created: 2026-10-04
source: https://freshauto.ru
related:
  - "[[tech/ozon-purchase-history]]"
  - "[[tech/ru-marketplace-mcp]]"
---

# freshauto.ru — вытягивание каталога API-путём

Задача: полный дамп каталога подержанных авто + часовой монитор новых под фильтр.
Хар-запись дала только `filter-engine` (Basic-auth) и `mobile.freshauto.ru` — сам каталог
через них не идёт. Основной путь оказался в HTML.

## 1. Данные лежат в SSR-блобе, а не в API

Каждая страница каталога несёт `<script>` с JSON:

```
_piniaInitialState["vehicles"]["vehiclesData"]["vehicles"]  → список карточек
_piniaInitialState["vehicles"]["vehiclesData"]["meta"]      → total_count, page_count
_piniaInitialState["vehicles"]["filterOptions"]["applied_filters"] → что применено
```

Ни одного fetch'а внутри — рендер на стороне сервера, Vue/Pinia уже сериализован.
`page_count` из `meta` → известно количество страниц заранее (346 при 10 348 авто).

**Поля карточки в списке:** `id, slug, brand_name, model_name, complectation_name,
modification_name, year, min_price_by_discounts, price, city, body_type, drive_type,
engine_type, vehicle_kind, vehicle_state, vehicle_type, mileage, photos, discount_percent,
published, status, updated_at, avito_video, benefits, monthly_payment`.

Пагинация: `?page=N`. В `_piniaInitialState` списка `filterOptions` **нет** — фильтры
нужно читать отдельно или из `meta`.

## 2. Фильтры — это path-сегменты, не query

`?price_from=`, `?order_by=`, `?body_type=` сервер **игнорирует**: в `applied_filters`
остаётся `default` при любом значении. Работают только сегменты в пути:

| Что | Сегмент | Пример |
|---|---|---|
| Марка | `/cars/{brand}/` | `/cars/toyota/` |
| Модель | `/cars/{brand}/{model}/` | `/cars/toyota/rav4/` |
| Пробег | `maxkm-{n}` | `/cars/maxkm-140000/` |
| Кузов | `body-{slug}` | `/cars/body-vnedorozhnik/` |
| Цена | `minprice-{n}`, `maxprice-{n}` | `/cars/maxprice-2500000/` |
| Мест | `seats-{n}` | `/cars/seats-7/` |
| Новые/с пробегом | `/cars/new/`, `/cars/used/` | `/cars/new/` |

Порядок сегментов произвольный. Проверено на живом:

```
/cars/seats-7/minprice-1200000/maxprice-2500000/
→ total=144, applied_filters={place_count:[7], price_from:1200000, price_to:2500000}
```

### Ловушка: «7 мест» нельзя фильтровать по тексту

Числового поля мест в карточке **нет** — есть только текст комплектации
(«High-Tech (7 мест)»). SQL по `complectation_name LIKE '%7 мест%'` из 10 417 находит
**4 машины** вместо 144. Единственный источник — серверное поле `place_count`,
доступное только через `seats-{n}`. Заодно `seats-` сидит внутри `/cars/`
(`car_class=car`), так что автобусы отсекаются сами.

## 3. Инкремент — diff sitemap.xml

Сортировки «сначала новые» нет (`order_by=oldest/newest/price_asc` → всё тот же
`sort=default`), так что обходить 346 страниц ради дельты — мимо: порядок живой,
будут и пропуски, и дубли.

Работает `https://freshauto.ru/sitemap-cars.xml` — 2,8 МБ, 10 326 карточек с `lastmod`
у каждой. Один запрос вместо 346.

**`/root/scripts/fa_delta.py`** — схема:

1. читает sitemap, сравнивает slug'и с `cars`;
2. реестр `sitemap_seen(slug, lastmod, first_seen)` в той же БД — по нему ловятся и
   *изменившиеся* карточки (вырос `lastmod`), а не только новые;
3. **первый прогон** — реестр пуст, поэтому сравнение идёт с `fetched_at` карточки,
   иначе перечитался бы весь каталог;
4. грузит только нужное поштучно (та же SSR-структура, поля идентичны списку);
5. `--dry-run` — показать, ничего не трогая; `--prune` — проданные уходят в `gone`.

Проверка: 62 новых / 91 пропало, загрузка 62 карточек ≈ 8 с, повторный прогон — **0**
(идемпотентно).

## 4. Часовой монитор

**`/root/.hermes/scripts/freshauto-watch.py`** → cron `freshavto-hourly` (`57ee62b38964`),
`0 * * * *` по `timezone: Europe/Moscow`, `--no-agent`, доставка `telegram:386235337:188570`.

### Два режима

| | Первый прогон (или `--full`) | Обычный часовой |
|---|---|---|
| Что | весь Ростов под фильтром со ссылками + топ-10 по другим городам | только появившееся за прогон |
| Счётчик | `140 машин, Ростов-на-Дону: 7` | `Машин нет — новых за прогон: 0. под фильтром сейчас: 140 (…)` |

### Только иномарки

По слову Романа (04.10.2026) отечественные марки исключаются — `DOMESTIC` в скрипте:
`LADA (ВАЗ), UAZ, Москвич, ГАЗ, ТагАЗ, Амберавто, ЗАЗ` (сверено по всему каталогу:
это все бренды с кириллицей + `Belgee`/`Lifan`/`Vortex` отфильтрованы отдельно).
Под фильтром их было **4 из 144** (все — Largus 2025), стало **140**.
Фильтр применяется в `main` **после** `rescue_missing` — тому нужны бренды из БД,
и **до** подсчёта baseline.

Спорный случай зафиксирован явно: **китайская сборка в РФ (Haval, Chery) и
белорусский Belgee считаются иномарками** — бренд иностранный, отличается только
площадка. Поменять — одна строка в `DOMESTIC`.

Полный режим включается, пока в `/root/freshavto_watch.state.json` нет
`full_done: true` — стейт пишет сам скрипт. `--full` форсирует повтор, стейт не трогает.

### Топ-10: цена/год/пробег

Три метрики нормируются линейно в 0..1 **внутри выдачи** и складываются:

```
score = 0.45 · цена + 0.30 · возраст + 0.25 · пробег
```

Чем ниже балл, тем выгоднее. Веса выбраны так: цена — главный критерий, год и
пробег — поправки. Пробег в БД не пустует ни у одной машины (проверено: 0 NULL).

### Догрузка мимо sitemap

**sitemap отстаёт от выдачи**: 2 карточки уже висят в `/cars/seats-7/…/`, а в
`sitemap-cars.xml` их ещё нет. Только по sitemap они выпали бы из отчёта на
неопределённое время. Поэтому `rescue_missing()` берёт slug'и выдачи, которых
нет в БД, и грузит их поштучно через `fa_delta.parse_card` — они же сразу
считаются «новыми».

### Ещё детали

- фильтр (1,2–2,5 млн, 7 мест, не автобус) применяет **сайт**, не наш SQL;
- «новые» = `Δ слагов за прогон ∪ догруженные мимо sitemap ∩ слаги выдачи`;
- сортировка: Ростов-на-Дону первым, дальше по цене — из нашей БД;
- метки «7 мест» в строке больше нет: фильтр сам гарантирует `place_count=7`,
  а текст комплектации у большинства машин его просто не содержит;
- при сбое печатает `⚠️ Сбор упал` + последние строки ошибки: в `--no-agent` пустой
  stdout = тишина, а тишина на сбое выглядела бы как «всё ок».

Префикс `🤖 Регулярный отчёт · <имя> (<расписание>)` на все cron-доставки дописывает
патч MUL-10191. Топик в логе подтверждается явно:
`delivered to telegram:386235337 via live adapter thread=188570 message_id=25294`.

## 5. Файлы

| Файл | Что |
|---|---|
| `/root/freshavto_dump.db` | основная БД (`cars`, `sitemap_seen`), 10 417 авто |
| `/root/freshavto_dump.csv` | тот же дамп в CSV |
| `/root/scripts/fa_dump.py` | полный обход 346 страниц, 6 потоков |
| `/root/scripts/fa_delta.py` | инкремент по sitemap |
| `~/.hermes/scripts/freshauto-watch.py` | обёртка для cron: дельта + фильтр + отчёт |
| `/root/freshavto_watch.state.json` | `full_done` — полный отчёт уже отправлен |

HAR `/root/freshavto_har/cars_filtered.har` (30 МБ) удалён — не понадобился.
