---
title: "Claude без подписки — Opensource LLM + OpenClaw на RunPod"
description: ""
tags: [OpenClaw, RunPod, open source, LLM, self-hosted]
related: 
---

# Claude без подписки — Opensource LLM + свой агент OpenClaw на RunPod

**Видео:** [YouTube](https://www.youtube.com/watch?v=mUB2gbenbUg) | [RuTube](https://rutube.ru/video/1480b2a7bc69d8f0f4566e5e6125c225/)

**Автор:** [Егор Смышников | IT](https://www.youtube.com/@itsmyshnikov) (9.13K подписчиков)
**Дата:** 23 апреля 2026
**Длительность:** 47:09
**Просмотры:** ~136K

---

## О видео

**Краткое описание:**
Claude ввёл верификацию телефона и паспорта — и $100 в месяц за подписку. Показываю как запустить opensource LLM через OpenClaw на RunPod: плачу только когда использую.

## Темы видео

- Почему opensource уже норм: смотрим бенчмарки на [artificialanalysis.ai](https://artificialanalysis.ai/models)
- Термины без воды: квантизация, VRAM, CTX, KV Cache, TPS, Runtime — что это и зачем
- Как выбрать модель на [a2go.run](https://a2go.run): ctx, VRAM, vision, reasoning
- **GuildClaw** — Docker-образ: OpenClaw + llama.cpp + Model Hub в одном контейнере
- Model Hub: переключение моделей, настройка ctx, text+image без командной строки
- Vision: кидаем картинку — модель составляет промпт, разбирает скриншот
- Скиллы: создаём свой или берём на [clawhub.ai/skills](https://clawhub.ai/skills)
- TG-бот: работаем с агентом с телефона
- Stop vs Terminate — как не слить деньги

## Timestamps

| Время | Тема |
|-------|------|
| 00:00:00 | Введение |
| 00:01:11 | Почему Open Source модели это нормально |
| 00:02:00 | Что такое LLM, Size, Quant, Weight, TPS, VRAM, KV Cache, CTX, Runtime |
| 00:09:12 | Что такое Llama.cpp, Ollama + LM Studio |
| 00:11:37 | AI Агенты их подписки |
| 00:12:39 | Что такое OpenClaw |
| 00:14:30 | Как арендовать видеокарту на RunPod и Vast: OpenClaw Template Smyshnikov |
| 00:20:23 | llama.cpp |
| 00:21:35 | ModelHub: как увеличить ctx и скачивать модели из HuggingFace |
| 00:28:21 | Аренда видеокарты для GLM5.1, Kimi K2.6 и других мощных моделей |
| 00:30:16 | Telegram botfather и HuggingFace API Token |
| 00:32:43 | OpenClaw + Web UI |
| 00:37:11 | Из чего состоит OpenClaw AI Агент: soul, identity, user, agents, tools, heartbeat |
| 00:40:01 | Telegram чатинг в OpenClaw |
| 00:43:50 | OpenClaw скиллы |
| 00:45:00 | Stop VS Terminate Pod |

## Ресурсы из видео

**RunPod Template:** [runpod.io?ref=1ryeb8om](https://runpod.io?ref=1ryeb8om)
**Vast Template:** [cloud.vast.ai/?ref_id=248159&creator_id=248159&name=OpenClaw%20LLM%20Smyshnikov](https://cloud.vast.ai/?ref_id=248159&creator_id=248159&name=OpenClaw%20LLM%20Smyshnikov)

## GuildClaw — Docker-образ

**Репозиторий:** [github.com/Smyshnikof/guildclaw](https://github.com/Smyshnikof/guildclaw)

> Проект Guildclaw — Docker-образ: OpenClaw + llama.cpp (llama-server, GGUF) + Model Hub (веб на :8080: пресеты, своя ссылка на .gguf, активация, удаление). NVIDIA GPU, локально или RunPod.

**Структура репозитория:**
- `model_hub/` — веб-интерфейс для управления моделями
- `pairing_dashboard/` — дашборд для подключения
- `scripts/` — вспомогательные скрипты
- `workspace/` — рабочее пространство
- `Dockerfile` — образ с OpenClaw + llama.cpp
- `DEPLOY.md` — инструкции по деплою
- `RUNPOD-TEMPLATE.md` — текст для RunPod template

**Образ:** `<user>/guildclaw:<тег>`

## Ключевые концепции

### LLM термины
- **Size** — размер модели (параметры)
- **Quant (квантизация)** — способ уменьшения модели для экономии памяти
- **Weight** — веса модели
- **TPS** (Tokens Per Second) — скорость генерации
- **VRAM** — видеопамять для хранения модели
- **KV Cache** — кэш для ускорения генерации
- **CTX (Context)** — окно контекста
- **Runtime** — среда выполнения

### OpenClaw компоненты
- **Soul** — личность агента
- **Identity** — идентичность
- **User** — пользовательские настройки
- **Agents** — конфигурация агентов
- **Tools** — инструменты агента
- **Heartbeat** — механизм периодических проверок

## Ссылки

- [Бенчмарки моделей](https://artificialanalysis.ai/models)
- [Выбор модели](https://a2go.run)
- [ClawHub Skills](https://clawhub.ai/skills)
- [Telegram канал Егора](https://t.me/smyshnikov)
- [Бесплатный PDF + сообщество](https://aiguild.ru/ai-generative)

---

*Добавлено: 2026-04-29*