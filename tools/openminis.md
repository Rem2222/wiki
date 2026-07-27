---
type: tool
title: OpenMinis — мобильный AI-агент с Linux shell
description: Open-source iOS/Android приложение для AI-агента с Linux shell, браузерной автоматизацией, Skills, памятью и доступом к возможностям смартфона.
tags: [mobile, ai-agent, ios, android, linux, sandbox, skills]
related:
  - concepts/hermes-knowledge-base
  - concepts/self-improving-agent-theory
source: https://github.com/OpenMinis/OpenMinis
stars: 2200
ingested_at: '2026-07-27'
---

# OpenMinis

**OpenMinis** — мобильное приложение (iOS/Android) для AI-агента с полным Linux shell на устройстве. Ранее закрытая разработка, открыта 25 июля 2026.

## Архитектура

Это не просто «чат с ИИ на телефоне». OpenMinis — это **агентная платформа**:

- **Ядро:** свой agent runtime (не Hermes), написан на Swift/Kotlin
- **LLM:** BYO-модели через API (Claude, GPT, Gemini, OpenRouter, любой OpenAI-совместимый)
- **Shell:** встроенный Alpine Linux в песочнице — полноценная среда для скриптов
- **Device API:** Native-мост к датчикам и функциям телефона
- **Browser:** встроенный веб-браузер с CDP
- **Skills:** совместимые с форматом SKILL.md
- **MCP:** поддержка HTTP и STDIO MCP-серверов
- **Память:** persistent memory между сессиями

## Варианты применения (из README + AwesomeMinis)

### 📸 Food Tracking
Minis определяет блюдо по фото, считает калории и макросы, записывает в Apple Health.

### ☀️ Morning Routine
Shortcuts → Minis загружает ленту X, суммирует, синтезирует речь → играет как будильник.

### 🐛 Bug Triage
Вытягивает сообщения из Telegram, извлекает баги и action items, дедуплицирует, заводит в Apple Reminders.

### 📝 Research + Obsidian
Исследует тему, пишет Markdown-заметки прямо в Obsidian vault.

### 📅 Event Creation
Через iOS Share Sheet → Minis создаёт событие в календаре с временем и местом.

### 🤖 Android Automation (эксклюзив)
- **Accessibility Service** — нажимает кнопки в любых приложениях
- **Shizuku** — adb-level привилегии: установка/удаление пакетов, управление разрешениями, настройки
- **Floating Overlay** — плавающее окно поверх других приложений
- **Scheduled Tasks** — запланированные задачи

## Интерес для твоего проекта

1. **Мобильный носитель для агента** — идеально ложится на концепцию «андроидное тело»
2. **SKILL.md совместимость** — можно перенести часть скиллов из Hermes
3. **MCP поддержка** — можно подключить те же MCP-серверы, что и в Hermes
4. **Shizuku** — даёт агенту контроль над устройством на уровне ADB (root-like без root)
5. **Открыт под GPLv3** — можно форкнуть и доработать

## Отзывы

Проект открыт 2 дня назад (25 июля 2026). Ранних отзывов пока немного. Репозиторий — 2.2k⭐ за 2 дня, что говорит о высоком интересе. Раньше существовал как закрытое приложение с «десятками тысяч пользователей».

## Возможности

- **BYO model** — Claude, GPT, Gemini и другие провайдеры через свои API-ключи
- **Linux shell** — sandboxed Alpine Linux на устройстве: установка пакетов, скрипты, файлы
- **Device integration** — Health, Calendar, Reminders, Contacts, HomeKit, Bluetooth, Clipboard, Media, Alarms
- **Browser automation** — веб-скрейпинг и взаимодействие
- **Skills & memory** — расширяемые скиллы, постоянная память между сессиями
- **Workspaces** — ${ minis://workspace/ } адресация контекстов
- **Native offloads** — тяжёлые задачи на нативном коде
- **iCloud sync** — синхронизация между устройствами

## Ссылки

- [GitHub: OpenMinis/OpenMinis](https://github.com/OpenMinis/OpenMinis) (2.2k ⭐)
- [Сайт: openminis.app](https://openminis.app)
- [Awesome Minis — сообщество use cases](https://github.com/OpenMinis/AwesomeMinis)
- [iOS App Store](https://apps.apple.com/app/openminis)
-
