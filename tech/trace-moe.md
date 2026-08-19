---
description: trace.moe — движок поиска аниме-сцен по скриншоту. Поиск по изображению → название аниме, эпизод, таймкод. Бесплатный API, Telegram-бот, расширение для браузера. Open-source.
tags: [anime, search, api, image-recognition, tool]
related: [[tools/activitywatch]]
---

# trace.moe

## Что это

**Anime Scene Search Engine** — загружаешь скриншот из аниме, получаешь: какое аниме, какой эпизод и точный таймкод этой сцены.

- **Сайт:** https://trace.moe/
- **GitHub:** https://github.com/soruly/trace.moe (★ 5k+, forks 262, MIT)
- **Автор:** soruly
- **Лицензия:** MIT
- **API-документация:** https://soruly.github.io/trace.moe-api/

## Возможности

- Поиск по скриншоту или URL изображения
- Точное определение аниме, эпизода и времени сцены
- Интеграция через URL: `https://trace.moe/?url=IMAGE_URL`
- Telegram-бот: `@trace_moe_bot`
- Расширение для браузера (WebExtension)
- Бесплатный API для разработчиков

## API

Бесплатный HTTP API для автоматизации:
- Загрузка изображения или передача URL
- Результат: название аниме (AniList ID), эпизод, таймкод, similarity score
- Квота: per-IP rate limit (бесплатный тариф, без ключа)
- Подходит для ботов, плагинов, скриптов

**Пример запроса:**
```
GET https://api.trace.moe/search?url=https://example.com/screenshot.jpg
```

**Пример ответа:**
```json
{
  "result": [{
    "anilist": 101922,
    "filename": "...",
    "episode": 1,
    "from": 684.5,
    "to": 688.5,
    "similarity": 0.96738,
    "video": "...",
    "image": "..."
  }]
}
```

## Архитектура (самостоятельный хостинг)

Проект самоподдерживаемый, состоит из нескольких компонентов:

### Клиент
- `trace.moe-www` — веб-интерфейс
- `trace.moe-WebExtension` — расширение для браузера
- `trace.moe-telegram-bot` — Telegram-бот

### Сервер
- `trace.moe-api` — API-сервер (поиск + обновление БД)
- `trace.moe-media` — медиа-сервер (хранилище видео, генерация превью)
- `trace.moe-worker` — hasher, loader, watcher (интегрированы в API)
- `LireSolr` — плагин для анализа и поиска изображений через Solr

### Прочее
- `anilist-crawler` — парсинг данных AniList для хранения в БД

### Запуск自己的 хостинг (Docker Compose)

```bash
# 1. Создать директорию для видео
mkdir -p /path/to/trace.moe/video/

# 2. Положить видео по пути: /path/to/trace.moe/video/{anilist_ID}/foo.mp4

# 3. Скопировать .env.example → .env, указать VIDEO_PATH

# 4. Запустить
docker compose up -d
```

Сканирует `VIDEO_PATH` каждую минуту на новые файлы (.mp4, .mkv).

**Зависимости:** Milvus (векторный поиск), Solr.

## Связанные сервисы

- **AnimeOshi** (animeoshi.com) — трекинг аниме, рейтинги, эпизоды, сообщество (интеграция с trace.moe)
- **AniList** — база аниме-данных, используется для идентификации

## Использование

- Вставить URL скриншота в строку поиска на сайте
- Отправить скриншот боту `@trace_moe_bot` в Telegram
- Использовать API в скриптах/ботах
