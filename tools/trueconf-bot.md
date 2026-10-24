---
title: "TrueConf ChatBot Connector — боты для TrueConf (аналог Telegram-бота)"
description: "Официальный механизм ботов в TrueConf Server (с 5.5.0): WebSocket API, библиотека python-trueconf-bot (архитектура как aiogram), токен как у TG-бота. Плюс incoming-webhook для односторонней отправки и путь встраивания TrueConf платформой в Hermes."
tags: [tool, messengers, trueconf, bot, integration, hermes]
status: разобрано, НЕ устанавливалось
created: 2026-10-10
updated: 2026-10-24
related:
  - tech/kanal-svyazi-pri-glushenii
  - tools/page-mascot
  - ops/services/server-architecture
---

# TrueConf — боты и интеграция

Задача от Романа (10.10.2026): «Нужно что-то что шлёт сообщения в труконф или из него —
как у тебя с ТГ».

## Короткий ответ

**Да, есть официальный механизм.** TrueConf Server с версии **5.5.0** содержит
**ChatBot Connector API** — боты подключаются по **WebSocket** и работают почти как
Telegram-боты: токен, получение сообщений, ответы в чат, файлы, кнопки.

Официальная Python-библиотека — `python-trueconf-bot` (PyPI, BSD-3-Clause-Clear,
репозиторий `TrueConf/python-trueconf-bot`, обновлён 06.10.2026). Она **сознательно
сделана по архитектуре aiogram** — библиотеки, на которой пишут Telegram-ботов, «чтобы
упростить миграцию ботов, созданных для Telegram».

## Как это выглядит в коде

```python
from trueconf import Bot, Dispatcher, Router, Message, F, ParseMode

router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(server="video.example.com", token=TOKEN, dispatcher=dp)

@router.message(F.text)
async def echo(msg: Message):
    await msg.answer(f"You says: **{msg.text}**", parse_mode=ParseMode.MARKDOWN)

async def main():
    await bot.run()
```

Это буквально структура aiogram: `Router`, `Dispatcher`, фильтры `F.text`,
`await msg.answer(...)`, `ParseMode.MARKDOWN`.

## Что умеет Chatbot API

Создание личных и групповых чатов и каналов; сообщения с **HTML и Markdown**; передача
файлов; опросы; пересылка и ответы на сообщения; редактирование и удаление; история чата;
список чатов и участников; добавление/удаление участника; display name пользователя.

События, на которые можно подписаться: создан чат/канал, добавлен или удалён участник,
новое сообщение, отправлен файл, отправлен опрос, сообщение отредактировано или удалено.

## Версии — критично

| TrueConf Server | Библиотека |
|:---|:---|
| < 5.5.0 | ❌ не поддерживается |
| 5.5.0 — 5.5.2 | v1.1.x |
| 5.5.3 — 5.5.5 | v1.2.1 — 1.4.x |
| ≥ 5.5.6 | v1.4.x (базово) / **v1.5.0+** полностью |

v1.5.0+ нужен для inline-кнопок, индикатора активности, голосовых сообщений,
`message.chat` и `reply_message`. На v1.4.x голосовые (тип 205) не парсятся — такие
апдейты просто отбрасываются.

**Лимит соединений:** с 5.5.3 — не более **128 одновременных WebSocket-подключений**
на сервер, то есть максимум 128 ботов.

Функциональность ботов есть в **TrueConf Server 5.5+**, **TrueConf Enterprise** и
**TrueConf Server Free**.

## Аутентификация — два пути

**1. Токен (проще).** Бот создаётся в админ-панели TrueConf Server, оттуда берётся токен
(JWT). Живёт **30 дней**, потом обновлять вручную.

**2. Логин/пароль (надёжнее для прода).** Обычный пользователь-бот на сервере:
создать учётку (например `webhook_bot`) с паролем, затем получать JWT через

```
POST https://<server>/bridge/api/client/v1/oauth/token
{"client_id":"chat_bot","grant_type":"password","username":"webhook_bot","password":"..."}
```

Сервис сам обновляет JWT примерно раз в 25 дней (сам токен живёт 30). Боту нужно право
писать в чатах — пригласить его участником заранее.

## Вариант «только отправлять» — incoming webhook

`matrozov/trueconf-webhook-bot` (1⭐, MIT-подобный, Python) — **аналог Slack/Mattermost
incoming webhook**: в любом чате команда `/webhook_create` выдаёт персональный URL,
дальше внешний сервис делает обычный `POST` — текст (и вложения по URL) попадают в чат.
Команды `/webhook_create`, `/webhook_list`, `/webhook_revoke`; в групповых чатах
обращаться надо через `@bot`; полный URL приходит автору в личку, чтобы секрет не светился
в истории чата; в списке токен показывается замаскированным (`abcd…wxyz`); есть лимит
частоты на токен и опция «только админы чата».

Если нужно просто ронять алерты и отчёты в чат — это самый дешёвый путь, без полноценного
бота.

## Репозитории

Официальная организация **`TrueConf`** на GitHub — **36 репозиториев** (с 29.06.2016):

- **`TrueConf/python-trueconf-bot`** — 21⭐, BSD-3-Clause-Clear, PyPI — обёртка Chatbot API
- **`TrueConf/trueconf-chatbot-example`** — 2⭐ — готовые примеры ботов: **Echo**, **Sick
  Leave** (сбор сообщений и пересылка в HR-чат), **Monitoring** (метрики TrueConf Server
  через API + алерты) и **GPT Bot** — работа с **локальной LLM в GGUF без интернета**
- `TrueConf/TrueConf-Server-API-examples` — примеры серверного API
- `TrueConf/python-trueconf-room`, `TrueConf/contact_center_api`
- `TrueConf/telegram-trueconf-migration` — **перенос сообщений, чатов и медиа из Telegram
  в TrueConf** (Python, июль 2026)
- `TrueConf/Telegram-Bot-for-Control-TrueConf-Server` — управление админ-панелью TrueConf
  из Telegram

Сторонние:

- `matrozov/trueconf-webhook-bot` — incoming webhooks (описан выше)
- `lexezzz/java-trueconf-bot` — Java-обёртка Chatbot Connector API
- `maxineal/golang-trueconf-bot` — Go SDK
- `Demston/TrueConf_Alert_Bot` — **Grafana → TrueConf**: алерты из Grafana в чат
- `iahoo/TrueconfBot`, `paderinandrey/true-conf` (Ruby, TrueConf Server API)

## Как встроить в Hermes (чтобы было «как с ТГ»)

У Hermes для этого есть **официальный плагинный путь** — файл
`/usr/local/lib/hermes-agent/gateway/platforms/ADDING_A_PLATFORM.md`:

> Create a plugin directory in `~/.hermes/plugins/` with a `plugin.yaml` and `adapter.py`.
> The adapter inherits from `BasePlatformAdapter` and registers via `ctx.register_platform()`
> in the `register(ctx)` entry point. **This requires zero changes to core Hermes code.**

Плагинная система сама берёт на себя: создание адаптера, разбор конфига, авторизацию
пользователей, доставку cron-задач, маршрутизацию `send_message`, подсказки в системном
промпте, отображение статуса и настройку gateway.

Хуки, которые понадобятся: `env_enablement_fn`, `apply_yaml_config_fn`,
`cron_deliver_env_var`, `standalone_sender_fn`, `requires_env` / `optional_env`.

Готовые примеры для подражания: `plugins/platforms/irc/`, `plugins/platforms/teams/`,
`plugins/platforms/google_chat/`, `plugins/platforms/line/`, `plugins/platforms/whatsapp/`.

Всего в Hermes уже 22 плагина платформ: a2a, buzz, dingtalk, discord, email, feishu,
google_chat, homeassistant, irc, line, matrix, mattermost, ntfy, photon, raft, simplex,
slack, sms, teams, telegram, wecom, whatsapp.

**Значит:** TrueConf как платформа Hermes — реализуемо официальным способом, без правок
ядра. Объём: `adapter.py` поверх WebSocket-клиента Chatbot API (можно взять
`python-trueconf-bot` как транспорт) + `plugin.yaml`.

## Контекст Романа (из памяти)

TrueConf у Романа связан с **1С**: в публикации веб-сервера (файл `.vrd`) есть HTTP-сервисы
`TrueConf_ИнтеграцияБУ`, `TrueConf_СоздатьЗаказПокупателяИзCRM`,
`Trueconf_ОперацииСПроизводственнымКалендарем`, база `Srvr=het40a.trueconf.loc` —
то есть TrueConf Server стоит в корпоративной сети и интегрирован с 1С:БУ.

**Отсюда главное ограничение:** домен `.loc` — локальная сеть. VPS Романа (Contabo,
Франция) до корпоративного TrueConf Server **не достучится напрямую**. Варианты:
бот живёт в корпоративной сети; либо связь через Tailscale/VPN; либо использовать
публичный TrueConf Server / Server Free для экспериментов.

## Что нужно, чтобы завести (чеклист)

1. **TrueConf Server версии 5.5.0+** и **админский доступ** к нему (без админки бота не
   создать и токен не получить)
2. Решить формат: **токен** (30 дней, вручную) или **учётка+пароль** (автообновление)
3. Убедиться, что хост бота **имеет сетевую доступность** до TrueConf Server
4. `pip install python-trueconf-bot` (или `uv add`)
5. Определиться: только отправка (webhook-bot, минимальный путь) или двусторонний бот
6. Для Hermes — написать плагин-адаптер (`~/.hermes/plugins/trueconf/`)

## Оговорки

- Библиотека `python-trueconf-bot` — от самого вендора, но популярность низкая
  (**21⭐**), то есть внешнего сообщества вокруг мало: баги и краевые случаи придётся
  разбирать самим
- Название задачи от Романа («труконф») — TrueConf; не путать с TrueNAS/TrueCrypt
- `TrueConf/trueconf-chatbot-example` не имеет заявленной лицензии (у библиотеки — BSD-3)
- Официальная дока: `trueconf.com/docs/chatbot-connector/en/overview/` (WebSocket-API,
  с 5.5.0)

## Источники

- 🌐 github.com/TrueConf — организация, 36 репо (GitHub API)
- 🌐 github.com/TrueConf/python-trueconf-bot — README (master), PyPI
- 🌐 github.com/TrueConf/trueconf-chatbot-example — README (описание четырёх ботов)
- 🌐 github.com/matrozov/trueconf-webhook-bot — README (incoming webhooks, схема auth)
- 🌐 trueconf.com/docs/chatbot-connector/en/overview/ — официальная документация
- 📄 `/usr/local/lib/hermes-agent/gateway/platforms/ADDING_A_PLATFORM.md` — плагинный путь
- 🧠 OpenViking: события 05.09.2026 (`.vrd`, HTTP-сервисы TrueConf_* в 1С)
- 📄 wiki `links-from-sessions.md` — след «github.com/TrueConf/... — есть в проекте»

## Связи

- [[tools/page-mascot]] — тоже разбор присланного инструмента
- [[ops/services/server-architecture]] — карта сервисов сервера
