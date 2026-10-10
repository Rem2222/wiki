---
title: "page-mascot — питомец на странице сайта (koboyo)"
description: "Сервис/скилл page-mascot от Kamran Ahmed (koboyo.com): персонаж для страницы, следит за курсором и реагирует на клик. Демо-страница, 58 готовых персонажей, npm-пакет и скилл для агентов. Установлено на rem2222.top в виде vanilla-JS порта."
tags: [tool, web, mascot, frontend, rem2222]
status: установлено на rem2222.top
created: 2026-10-10
---

# page-mascot

Интерактивный персонаж для веб-страницы: **следит за курсором** и **моргает, когда его
«тыкают»**. Источник — `koboyo.com/page-mascot`, репозиторий `nilbuild/page-mascot`.

## Откуда взялось

10.10.2026 Роман прислал видео (44 с) и пересылку от AI Journal: «сервис Koboyo позволяет
поселить виртуальную зверушку прямо на веб-странице». Разбор видео показал, что название
в пересылке неточное: сервис называется **Koboyo**, а сам проект — **`page-mascot`**
(отдельная страница `koboyo.com/page-mascot`). Роман: «Хочу такого себе на rem2222.top».

## Что это технически

**Не** внешний виджет-скрипт и **не** SaaS с регистрацией. Это:

- **демо-страница** с 58 персонажами (`koboyo.com/page-mascot`), где можно посмотреть и
  скачать листы персонажа;
- **npm-пакет** `page-mascot` — React-компонент `<Mascot directions reactions />` (v0.1.0);
- **скилл для агентов** `npx skills add nilbuild/page-mascot --skill page-mascot --global --yes`,
  который рисует персонажа под запрос (нужен инструмент генерации картинок; Claude Code идёт
  через OpenAI Images API, Codex имеет свой).

Лицензия **MIT © Kamran Ahmed**. Репозиторий создан 14.09.2026, 1094⭐.

## Как устроен персонаж

Каждый персонаж — **две спрайт-папки 3×3** (1080×1080 каждая):

- **directions** — 9 направлений головы: `up-left, up, up-right, left, center, right,
  down-left, down, down-right`;
- **reactions** — 9 выражений: `blink, heart, sparkle, surprised, wink, bashful, sleepy,
  dizzy, delighted`.

CSS: `background-size: 300% 300%`, позиция ячейки = `(x%3)*50% (y)*50%`. Угол указателя от
центра выбирает ячейку направлений; **dead zone 70 px** — при близком курсоре голова
успокаивается на «center». Клик показывает реакцию на 560 мс: `blink` → payoff
(`heart`/`sparkle`/`delighted`) → сброс. **4 клика за 1600 мс** дают `dizzy` на 1100 мс.

Оригинал также соблюдает `prefers-reduced-motion` (без squash-анимации) и
**отключает трекинг без точного указателя** (`(hover: hover) and (pointer: fine)`) —
на тач-устройствах персонаж остаётся видимым, но не следит за пальцем.

Тот же персонаж рисуется в шести стилях: **colour, ink, sketch, riso, paper, pixel** —
меняется только отрисовка, выравнивание сохраняется. Готовая лиса есть в вариантах
`fox`, `fox-ink`, `fox-paper`, `fox-pixel`, `fox-riso`, `fox-sketch`.

## Что сделано у нас (10.10.2026)

Роман выбрал **fox-paper** (бумажный стиль лисы). Рассматривались две реализации:

- npm-пакет — **не подошёл**: это React-компонент, а `rem2222.top` — статический HTML,
  без сборщика;
- **выбран vanilla-JS порт**: логика `src/mascot.tsx` перенесена 1:1 на чистый JS.

Файлы:

- `/var/www/landing/mascots/fox-paper-directions.webp` (193 КБ)
- `/var/www/landing/mascots/fox-paper-reactions.webp` (222 КБ)
- `/var/www/landing/page-mascot.js` (6.8 КБ) — порт, константы совпадают с оригиналом
- `/var/www/landing/index.html` — добавлена одна строка `<script src="/page-mascot.js" defer>`
- бэкап страницы: `/root/backups/index.html.before-mascot.20261010-2008`

Место: **по центру страницы, в потоке** — между шапкой «Hermes VPS» и первым разделом с
карточками (после правки 10.10.2026 по просьбе Романа: «посади её по середине между заголовком
и таблицей»). Раскладка: блок `140×140` (≤600 px — 92×92), `margin: 0 auto`, `position: relative`.
Проверено: ровно по центру контейнера (720 px из 720), 32 px сверху и 28 px снизу, карточки не задевает.

Изначально (первая версия) крепился **fixed в правом нижнем углу** — этот режим сохранён в
скрипте как резервный: если элемента `#page-mascot` нет в разметке, скрипт создаёт его сам и
крепит плавающим в углу (`position: fixed; right/bottom: 20px; z-index: 9999`). Так маскот можно
переключать между двумя режимами, не меняя JS — достаточно убрать или вернуть `<div id="page-mascot">`
в HTML.

## Подводный камень nginx (важно на будущее)

Файлы `/mascots/*.webp` сначала отдавали **404**, причём ответ был HTML на 332 КБ — то есть
запрос уходил не в root сайта, а в **Multica (Next.js на порту 3001)**. Причина — regex-локейшн
в `/etc/nginx/sites-enabled/hermes`:

```
location ~ ^/[a-z][a-z0-9_-]*(/.*)?$ { proxy_pass http://127.0.0.1:3001; }
```

Он ловит любой односегментный путь из букв — то есть `/mascots/...`, но **не** ловит
`/page-mascot.js` (точка не входит в класс символов), поэтому скрипт работал, а картинки нет.

Решение — явный префикс с приоритетом над regex (`^~`), добавлен перед `location /`:

```
location ^~ /mascots/ {
    root /var/www/landing;
    try_files $uri =404;
    expires 7d;
    add_header Cache-Control "public";
}
```

Бэкап конфига: `/root/backups/nginx-hermes.before-mascot.20261010-201048`.
Вывод на будущее: **любая новая папка со статикой на этом домене требует `^~`-локейшна**,
иначе её проглотит Multica-роут.

## Проверка (Playwright, настоящий Chromium)

`browser_exec` в Hermes работает на **Lightpanda**, у которой нет движка рендеринга —
размеры и скриншоты оттуда недостоверны (кнопка показывалась как 5×5). Проверять вёрстку
нужно через Playwright: `/root/.cache/ms-playwright/chromium-1243`.

Результаты:

- геометрия (в потоке): 140×140, ровно по центру контейнера, между шапкой и первой секцией — верно;
  в резервном угловом режиме проверялись те же параметры (отступ 20 px);
- оба листа декодируются: **1080×1080** каждый;
- направления: **8 из 8** верны (проверено с переносом маскота в центр экрана — из угла
  курсор не может уйти вправо-вниз);
- dead zone → `50% 50%`;
- клик → `blink`, через 120 мс payoff (`heart`), через 560 мс сброс к направлениям;
- 4 клика в окне → `dizzy` (`50% 100%`), держится 1100 мс;
- мобильный viewport 390 px: **92×92**, отступ 20, трекинг выключен;
- `prefers-reduced-motion`: анимаций 0;
- ошибок в консоли — нет.

Скрипты проверки: `/root/scripts/mascot_check.py`, `mascot_check2.py`, `mascot_check3.py`,
`mascot_shots.py`.

## Как поменять персонажа

Скачать две webp с `raw.githubusercontent.com/nilbuild/page-mascot/main/public/mascots/<имя>-{directions,reactions}.webp`
в `/var/www/landing/mascots/` и заменить переменную `MASCOT` в `page-mascot.js`.

Полный список (58): afro, astronaut, bald, ballerina, bear, beard, builder, bunny, cap, cat,
chef, clockwork, crt, cube, deer, dino, drone, fox, fox-ink, fox-paper, fox-pixel, fox-riso,
fox-sketch, frog, gearbot, glasses, grandpa, granny, hamster, hedgehog, hijabi, kamran,
knight, koala, lantern, mouse, nurse, otter, owl, panda, penguin, pirate, postbot, pug,
raccoon, radio, redpanda, rocket, scientist, scout, sheep, sikh, skater, sloth, tiger,
toaster, tv, wizard.

## Оговорки

- Полный набор из 58 персонажей весит ~21 МБ (116 файлов × ~180 КБ). Мы держим **только
  выбранного** — 415 КБ.
- Скилл-часть (`npx skills add …`) **не устанавливалась**: она нужна, чтобы агент **рисовал
  нового** персонажа. Для готовой лисы не требуется.
- Репозиторий молодой (создан 14.09.2026) и с единственной датой пуша (15.09.2026) —
  в отличие от популярных инструментов, история правок короткая.
- У демо на koboyo.com есть 52–58 персонажей, из них часть — лиса в разных стилях; у
  `fox-*` вариантов спрайты разные, а не перекраска на лету.

## Источники

- 🌐 koboyo.com/page-mascot — демо-страница, инструкция установки
- 🌐 github.com/nilbuild/page-mascot — README, `src/mascot.tsx` (логика), `public/mascots/`
- 🌐 MIT © Kamran Ahmed
- 🎥 видео от AI Journal (44 с, `/root/.hermes/cache/videos/video_a561b1c9661e.mp4`)
- 📄 конфиг `/etc/nginx/sites-enabled/hermes` (regex-локейшн 3001)

## Связи

- [[tools/ai-tools-proxy-domains]] — тоже разбор присланного инструмента
- [[ops/services/server-services]] — реестр сервисов сервера
