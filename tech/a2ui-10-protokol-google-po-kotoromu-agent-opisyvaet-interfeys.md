---
description: "Открытый протокол Google для генеративного UI: агент присылает JSON-описание, приложение рисует нативными компонентами. Проверено по первоисточникам 12.11.2026: протокол 1.0 стабилен, библиотеки всё ещё 0.x (React 0.15, Python SDK 0.11, Kotlin legacy). Вывод: как зависимость не берём, принцип «сцена как данные» — берём."
tags: [google,protocol,generative-ui,agents,mcp,ui]
related:
  - tech/vidzhety-telegram-html-pryamo-v-soobschenii-widget-sandbox
  - tech/ag-ui-i-a2ui-protokoly-agent-prilozhenie-i-agent-interfeys-razbor-slayda-pro-dsh
  - tech/hermes-external-integrations
created: 2026-11-12
updated: 2026-11-12
source: "https://developers.googleblog.com/a2ui-10-build-delightful-fast-reliable-agentic-experiences/"
---

# A2UI 1.0 — протокол Google, по которому агент описывает интерфейс

## Что это

A2UI — открытый протокол Google, по которому агент описывает интерфейс, а приложение рисует его **своими нативными компонентами**. Агент не пишет HTML и не присылает картинку: он отправляет JSON-сообщения («покажи карточку с такими-то полями и кнопками»), клиент собирает экран из зарегистрированных компонентов своего дизайн-системы.

Главная мысль, ради которой всё сделано: одно и то же описание сцены работает и в родном приложении компании, и внутри сторонних ассистентов, которые хостят MCP-приложения — Gemini, Claude. Пользователь при этом видит нативные элементы, а не веб-вью.

Репозиторий `a2ui-project/a2ui`: **17 105 звёзд**, лицензия Apache-2.0, язык TypeScript, создан 24.09.2025, 474 открытых issue, каталоги `specification`, `typescript`, `python`, `dart`, `swift`, `kotlin`, `catalogs`, `conformance`, `eval`, `skills`.

## Что нового в 1.0

По официальному блогу Google (12.11.2026): «Version 1.0 adds bidirectional function calls, so a flight or reservation picker can check availability on the spot. The protocol also adds support for accessibility and extensions for any additional metadata».

То есть три вещи: двусторонние вызовы функций (компонент может сходить за данными в момент нажатия — проверить наличие мест, посчитать цену), доступность и расширения для собственных метаданных.

По `specification/versions.json` версия 1.0 помечена как **current**, 0.9.1 — previous, 0.8 — deprecated. В README спецификации прямо: «This version was previously known as version 0.10. This specification is stable. Breaking changes go into a future major version».

Живая проверка цифр разошлась с постами в одном важном месте:

- протокол 1.0 — да, стабилен (`v1_0` в спецификации, `protocolVersion: "1.0"` в каталоге)
- **библиотеки к нему — всё ещё 0.x**: `@a2ui/react` **0.15.0** на npm, `a2ui-agent-sdk` **0.11.0** и `a2ui-core` **0.6.0** на PyPI, теги `v0.10.0+swift`, `v0.9`, `v0.8`
- Jetpack Compose действительно отстаёт: в репозитории каталог `kotlin/agent_sdk_legacy`, тега версии 1.0 для Kotlin нет
- рендереры по a2ui.org: React, Lit, Angular, Flutter, SwiftUI, Jetpack Compose плюс «community renderers»
- SDK: Python, TypeScript, Dart (`dart`, `python`, `typescript` в репозитории); на pub.dev пакеты `a2ui`, `a2ui_flutter`, `a2ui_core`

Значит «релиз 1.0» — это про стабильность **протокола**, а не про готовые библиотеки 1.0.

## Каталог компонентов — и что из него выживает в Telegram

Базовый каталог (`catalogs/basic/v1/catalog.json`, 42 КБ JSON Schema) — 19 компонентов: Text, Image, Icon, Video, AudioPlayer, Row, Column, List, Card, Tabs, Divider, Modal, Button, TextField, CheckBox, ChoicePicker, Slider, DateTimeInput. Плюс 15 функций рендерера: `formatNumber`, `formatCurrency`, `formatDate`, `pluralize`, `openUrl`, `regex`, `email`, `length`, `numeric` и логические `and`/`or`/`not`.

Ядро спецификации (`docs/a2ui_protocol.md`) — **107 КБ** текста. Это весомый документ, не «страница».

Если рендерить A2UI в Telegram-виджет (песочница QuickJS, где по контракту SDK v1 **нет ввода с клавиатуры и элементов форм**), от каталога остаётся меньше половины: Text, Row, Column, List, Card, Tabs, Divider, Button-как-ссылка, Image только через `data:`. Все поля ввода, чекбоксы, слайдеры и выбор даты в Telegram не работают.

## Чем это отличается от виджетов Telegram

Задачу решают одну — «агент отвечает не простынёй текста, а интерфейсом» — но путями, которые почти не пересекаются.

Виджеты Telegram: HTML-документ в песочнице, до 4 КБ после сжатия, интерактив через запросы к боту, работает **уже сейчас** в обычном Bot API, но только внутри Telegram.

A2UI: JSON-описание плюс нативные компоненты, без ограничения по размеру в 4 КБ, работает везде, где есть рендерер, — но рендерер нужен свой на каждой платформе, и в Telegram его нет.

Блог приводит замер сценария «заболел утром, шесть дел»: шесть приложений — 86 нажатий и всё ещё не сделано; текстовый агент — 5–7 раундов переписки и 199 слов на чтение; агент с A2UI — 3 нажатия, все шесть дел закрыты. Видео-ролик показывает тот же сценарий: карточка «Your sick day» с плитками Call in sick / Reschedule / Mute pings / Order soup, выбор времени 9:00–10:30 и зелёная плашка «All set. Rest up.»

Кто уже строит: Atlassian в Jira (агент задаёт вопрос карточкой внутри рабочей задачи), Alation (фиды с графиками и SQL под ними, рендерятся и в Claude), Bloomberg, ByteDance — выпустил рендерер для Lynx ещё в июне 2026, там же в playground модель решений Jev выбирает компоненты и значения вместо написания текста. Внутри Google на 0.9.1 работают карточки Gemini Notebook и агенты Gemini Enterprise.

Отдельная деталь: A2UI распространяется как **скилл для агентов** — на сайте быстрый старт `npx skills add a2ui-project/a2ui`, в репозитории каталог `skills/a2ui`. То есть они целятся ровно в такие системы, как наша.

## Надо ли нам

Вывод: **как зависимость — нет, как ориентир — да.**

Почему не берём сейчас:

1. Рендерить негде. У нас нет своего приложения с нативными компонентами. Есть Telegram (песочница HTML), браузерные отчёты на `rem2222.top`, почта и ntfy. A2UI требует клиента с рендерером — в Telegram его нет и не появится.
2. Библиотеки 0.x при стабильной спецификации: 0.15 React, 0.11 Python SDK, Kotlin помечен как `legacy`. 474 открытых issue. Ставить сейчас — кормить себя миграциями.
3. У нас уже есть рабочая замена для реальных задач: `tgwidget` с JSON-описанием карточек (`title`, `rows`, `bars`, `notes`, `buttons`) — 200 строк, работает живьём, четыре карточки отправлены и видны.

Что стоит взять уже сейчас: сам принцип «сцена как данные, а не текст». Наши JSON-описания карточек стоит держать в форме, близкой к A2UI (список компонентов + данные отдельно от разметки), чтобы будущая конвертация была дешёвой.

Когда вернуться к вопросу:

- если появится браузерный рендерер A2UI, который ужимается в самодостаточный HTML на 4 КБ (сейчас React-рендерер в песочницу Telegram не влезет)
- если понадобится отдавать интерфейсы в чужие MCP-хосты (Claude, Gemini) — там A2UI уже язык общения
- если сцен станет много и один формат понадобится сразу для Telegram, HTML-отчёта и писем: тогда писать компилятор A2UI → HTML реально, базовый каталог всего 19 компонентов, а в Telegram из них нужно девять

## Статус

Разобрано по первоисточникам 12.11.2026: блог Google, `a2ui.org`, GitHub API репозитория, `versions.json`, каталог компонентов, реестры npm/PyPI/pub.dev. Видео-ролик (41 секунда) просмотрен покадрово — это промо того же сценария «заболел утром», без технических деталей.

Ничего не устанавливалось и не подключалось. Проверено расхождение с пересказом: «A2UI 1.0» — это стабильный протокол, а не версии библиотек.

Ссылки: [блог Google](https://developers.googleblog.com/a2ui-10-build-delightful-fast-reliable-agentic-experiences/), [сайт и доки](https://a2ui.org/), [репозиторий](https://github.com/a2ui-project/a2ui), [спецификация 1.0](https://a2ui.org/specification/v1.0-a2ui/).
