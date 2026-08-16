---
description: ru-marketplace-mcp — 12 MCP-серверов (33+1 инструмент) для чтения цен, наличия, рейтингов и отзывов с 9 российских маркетплейсов + Taobao, плюс сравнение цен по всем сразу. Только чтение, API-ключи не нужны. Python, MIT, 64⭐ (16.08.2026).
tags: [mcp, marketplace, wildberries, ozon, avito, yandex-market, taobao, scraping, price-comparison, russia, python]
related: "[[tech/youtube-relay-setup]] [[tech/agent-memory-research-2026]]"
---

# ru-marketplace-mcp

## Что это

MCP-серверы для российских и китайских маркетплейсов: **Wildberries, Ozon, Яндекс Маркет, Детский мир, Авито, Taobao, Мегамаркет, Lamoda, DNS, Ситилинк**. Читают цены, наличие, рейтинги, отзывы и реквизиты продавцов. Плюс `compare_prices` — «где дешевле» одним вызовом по всем источникам.

- **Репозиторий:** https://github.com/Vladimir-Human/ru-marketplace-mcp
- **Статус:** активная разработка, v1.5.1 (16.08.2026)
- **Stars:** 64 (16.08.2026), forks 10, 0 open issues
- **Лицензия:** MIT, Python 3.12+, `uv`
- **Создан:** 26.07.2026, коммиты ежедневные

## Архитектура

- **12 серверов / 33 инструмента** на общем рантайме `mcp-core`
- **Объединённый `marketplace-mcp`** — монтирует всё разом (1 запись в конфиге вместо 12), 34 инструмента (включая `marketplace_sources` — диагностику, кто поднялся, кто отвалился)
- Транспорт: stdio и HTTP
- CDP-источники (Ozon, Авито, Taobao, Мегамаркет, Lamoda-поиск, DNS, Ситилинк) читаются через **ваш собственный Chrome** — коннекторы сами держат паузу между запросами (burst роняет DNS/Taobao)
- **MPStats** (опционально, платный токен `MPSTATS_MP_AUTH`): продажи/остатки/графики за 30 дней по SKU Ozon/WB — единственный платный источник, остальные 12 не затрагивает

## Качество

- CI на 3 ОС (Ubuntu/Windows/macOS) × Python 3.12/3.13
- mypy 87 файлов, 0 ошибок; **1182 теста** (1181 passed, 1 skipped)
- e2e-проверка всех 13 серверов, аудиты (AUDIT_REPORT.md — 4 независимых аудита после v1.4.0)
- Гейты релиза: ruff, mypy, pytest, check_no_print, check_versions, check_test_count
- **Бандл DeepSeek Harness** (v1.5.0): 13 Agent Skills в `dsh/`, установка `dsh plugin --profile web add github:Vladimir-Human/ru-marketplace-mcp#path:/dsh`

## Анти-бот реальность (из их ANTI_BOT.md, проверено с датацентрового IP)

| Источник | Датацентр IP | Требование |
|---|---|---|
| Wildberries | ✅ анонимно | ничего |
| Яндекс Маркет | ✅ анонимно (SmartCaptcha dormant) | ничего |
| Детский мир | ✅ анонимно | ничего |
| Lamoda (карточки) | ✅ анонимно (GraphQL) | ничего |
| Ozon | ❌ 307 loop (Cloudflare) | ваш Chrome (CDP) |
| Авито | ❌ 403 firewall (IP reputation) | Chrome + российский домашний IP, запросы вразрядку |
| Taobao | ⚠️ shell only (signed mtop API) | Chrome + активный вход |
| Мегамаркет | ❌ ServicePipe | Chrome + активный вход (анонимной сессии API отдаёт пусто) |
| Lamoda (поиск) | ⚠️ anti-bot redirect loop | ваш Chrome |
| DNS | ❌ Qrator JS proof-of-work | ваш Chrome |
| Ситилинк | ❌ Qrator rate block | ваш Chrome |

**Ключевые грабли из их доки:**
- «Anti-bot posture, not API quality, decides whether a marketplace is usable» — у WB кривой API, но работает; у Мегамаркета чистый, но недоступен без браузера
- Авито блокирует датацентровые IP — глухой отказ (подтверждено на нашем VPS, Франция)
- DNS/Cитилинк: product-id regex — MongoDB ObjectId (24 hex) vs реальные slug'и (`/product/noutbuk-lenovo-2169270/` — цифры, `/product/b7a1667f9b19ed20/` — 16 hex) — парсинг давал 0 плиток
- Дешёвые позиции на WB — «Восстановленный»/«Витринный образец» (не отличить без словаря состояний — добавлен в compare_prices)
- Ситилинк рисует плитки внутри iframe — экстрактор, читающий только document, ломается
- Ни одного публичного эндпоинта, который делает эти источники здоровыми — нужен реальный браузер или резидентный IP

## Контекст для Rem

- С VPS (Франция) анонимно заработают: WB, Яндекс Маркет, Детский мир; Ozon — при наличии Chrome с CDP
- Авито/Taobao/Мегамаркет — только с российского домашнего IP (для Авито у нас и так работает r.jina.ai)
- Может стать источником данных для скилла `product-price-monitor`
- Дополняет `ozon-order-collector` (тот — заказы из ЛК, этот — публичные цены/карточки)
- Hermes подключает MCP через native MCP client (config.yaml)
- Пока не ставим — по правилу «новые инструменты в вики, не разворачивать без решения»
