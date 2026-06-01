---
description: Инструменты для скачивания истории покупок из личного кабинета Ozon (для физических лиц) — Chrome-расширение и Python-парсер
tags: [ozon, personal-account, purchase-history, export, chrome-extension, parser]
related: [[tech/ozon-seller-api]]
---

# Ozon — история покупок (экспорт для физлиц)

У Ozon нет публичного API для личного кабинета покупателя-физлица. Доступные инструменты работают через браузерную автоматизацию или перехват трафика.

## Chrome-расширение: Ozon History

**[lomik/ozon-history](https://github.com/lomik/ozon-history)**

Расширение для Chrome (Manifest v3) на Svelte, которое сохраняет всю историю заказов.

**Возможности:**
- Заходит на `ozon.ru/my/orderlist` → считывает ID пользователя
- Автоматически перебирает все заказы по порядку (`?fetchAll=1`)
- Извлекает: дату заказа, название товара, цену, количество, продавца, статус доставки, ссылку на товар, фото
- Хранит данные в `chrome.storage.local`
- Показывает историю с поиском и фильтрацией

**Установка:**
```bash
git clone https://github.com/lomik/ozon-history
cd ozon-history
npm install && npm run build
```
В Chrome: `chrome://extensions` → Загрузить распакованное → выбрать папку `dist/`

**Плюсы:** не требует API-ключей, работает через браузер с вашей сессией, может собрать всю историю разом.
**Минусы:** данные только в памяти браузера, нет экспорта в CSV/Excel "из коробки".

## Python-парсер: Ozon Personal Account Parser

**[TwastyK/Ozon-Personal-Account-Parser](https://github.com/TwastyK/Ozon-Personal-Account-Parser)**

Скрипт на Python + Playwright для автоматизированного сбора данных о заказах.

**Возможности:**
- Открывает Ozon через сохранённый браузерный профиль (cookies)
- Перехватывает сетевые запросы к внутреннему API (orderlist, orderdetails)
- Собирает JSON с данными по всем заказам
- Извлекает: ID заказа, статус, состав, стоимость, адрес, QR-код, трек-номер
- Мониторит изменения и уведомляет о смене статуса

**Запуск:**
```bash
pip install playwright
playwright install chromium
python main.py
```

**Плюсы:** данные локально в JSON, можно интегрировать куда угодно, мониторинг в реальном времени.
**Минусы:** нужен Playwright, требует сессии браузера, нет прямого экспорта в CSV/Excel.

## Альтернативные варианты

- **[kaaes/ozon-parser.js](https://github.com/kaaes/ozon-parser)** — старый скрипт для парсинга страниц товаров, может быть доработан.
- **[VSPlekhanov/OzonCheckSlackBot](https://github.com/VSPlekhanov/OzonCheckSlackBot)** — Slack-бот для отслеживания статуса доставки заказов.
- **Самописный вариант** — через Selenium/Playwright логин и парсинг страницы `/my/orderlist`.

**Рекомендация:** для разового экспорта всех покупок лучше всего подходит **lomik/ozon-history** — готовое расширение с автосбором. Нужно только дописать экспорт в CSV/Excel.
