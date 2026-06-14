---
description: Free API прокси на базе web-чатов DeepSeek и Qwen
tags: [free-api, proxy, deepseek, qwen, deployment]
related: []
---

# Free API прокси (DeepSeek / Qwen)

Оба проекта — OpenAI-совместимые API-прокси, которые используют **сессию web-чата** вместо API-ключа.

---

## FreeDeepseekAPI

Подробнее: [[deepseek-free-api]] — развёртывание и настройка.

- **Репозиторий:** <https://github.com/ForgetMeAI/FreeDeepseekAPI>
- **Возраст:** июнь 2026 (2 дня)
- **Язык:** Node.js 18+
- **Зависимости:** Zero npm dependencies (один `client.js`)
- **Звёзды:** ~90

**Для чего:** Авторизация в chat.deepseek.com через Chrome-профиль → запуск OpenAI-совместимого API на localhost.

**Поддерживает:**
- OpenAI Chat Completions API
- Anthropic Messages API shim
- OpenAI Responses API shim
- Tool calling (парсит OpenAI tools / Anthropic tools)
- Reasoning с `reasoning_content`
- Multi-account pool (round-robin)
- Chrome-авторизация

**Models:**
- `deepseek-chat` — DeepSeek V4 (fast)
- `deepseek-reasoner` — DeepSeek R1 (reasoning)

**Ограничения:** Работает пока не меняется внутренний web-интерфейс DeepSeek.

---

## FreeQwenApi

Подробнее: [[qwen-free-api]] — развёртывание и настройка.

- **Репозиторий:** <https://github.com/ForgetMeAI/FreeQwenApi>
- **Форк:** y13sint/FreeQwenApi
- **Звёзды:** ~117

**Для чего:** То же самое, но для chat.qwen.ai.

**Поддерживает:**
- 28+ моделей (qwen3.7-max, qwen3.7-plus, qwen3.6-plus и т.д.)
- Генерация изображений — `POST /api/images/generations`
- Генерация видео — `POST /api/videos/generations` + polling
- Мультиаккаунты с round-robin и авто-ротацией
- Загрузка файлов

---

## Сравнение

| | FreeDeepseekAPI | FreeQwenApi |
|---|---|---|
| Web-чат | DeepSeek | Qwen |
| Возраст | 2 дня | ~4 мес. |
| Tool calling | ✅ | ❓ |
| Image gen | ❌ | ✅ |
| Video gen | ❌ | ✅ |
| Зависимости | 0 | есть |
| Модели | deepseek-chat / deepseek-reasoner | qwen3.7-max и др. |

**Суть:** Бесплатный API-доступ к топовым моделям через web-сессию вместо API-ключа. Не для production, работает пока не меняется web-интерфейс.
