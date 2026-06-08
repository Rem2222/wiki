---
description: Развёртывание FreeDeepseekAPI — бесплатный DeepSeek API через web-чат на VPS
tags: [deepseek, api, proxy, selfhosted]
related: [ai-services]
---

# FreeDeepseekAPI

**FreeDeepseekAPI** — локальный OpenAI-compatible API proxy для DeepSeek Web Chat (`chat.deepseek.com`). Позволяет использовать DeepSeek через OpenAI SDK, Open WebUI, Claude Code, Hermes и другие инструменты.

Репозиторий: https://github.com/ForgetMeAI/FreeDeepseekAPI

## Деплой

- **Сервер:** `/opt/FreeDeepseekAPI`
- **Systemd:** `freedeepseekapi.service`
- **Порт:** `127.0.0.1:9655`
- **Nginx:** `https://rem2222.top/deepseek/` → `127.0.0.1:9655`
- **Статус:** `systemctl status freedeepseekapi`

## Аутентификация

Для работы сервера нужен `deepseek-auth.json` с данными авторизации от `chat.deepseek.com`.

### Вариант 1: Через Chrome (рекомендуется)

1. На ПК с Chrome/GUI:
```bash
git clone https://github.com/ForgetMeAI/FreeDeepseekAPI.git
cd FreeDeepseekAPI
npm run auth
```
2. В открывшемся Chrome войти в chat.deepseek.com и отправить сообщение "ok"
3. Вернуться в терминал, нажать Enter
4. Скопировать `deepseek-auth.json` на VPS:
```bash
scp deepseek-auth.json root@80.241.218.110:/opt/FreeDeepseekAPI/deepseek-auth.json
```

### Вариант 2: Chrome Extension

1. Установить расширение из `chrome-extension/` (chrome://extensions → Загрузить распакованное)
2. Войти в chat.deepseek.com
3. Нажать на иконку расширения → Export
4. Сохранить файл и скопировать на VPS

### После получения auth-файла

```bash
systemctl restart freedeepseekapi
```

## Использование

### Через nginx (рекомендуется)

```
POST https://rem2222.top/deepseek/v1/chat/completions
GET  https://rem2222.top/deepseek/v1/models
```

### OpenAI SDK

```python
from openai import OpenAI
client = OpenAI(
    base_url="https://rem2222.top/deepseek/v1",
    api_key="any"  # proxy не проверяет ключ
)
```

### Для Open WebUI

```
Base URL: https://rem2222.top/deepseek/v1
API Key: любой
```

### Для Claude Code

```bash
export ANTHROPIC_BASE_URL="https://rem2222.top/deepseek"
export ANTHROPIC_AUTH_TOKEN="any"
claude --model deepseek-chat
```

## Модели

| Alias | Описание |
|-------|----------|
| `deepseek-chat` | Быстрая модель (DeepSeek-V4-Flash) |
| `deepseek-reasoner` | С рассуждением (thinking) |
| `deepseek-chat-search` | С веб-поиском |
| `deepseek-reasoner-search` | Рассуждение + веб-поиск |
| `deepseek-expert` | Экспертная модель |
| `deepseek-v4-pro` | Эксперт + рассуждение |

## Управление

```bash
# Статус сервера
curl https://rem2222.top/deepseek/

# Список моделей
curl https://rem2222.top/deepseek/v1/models

# Сбросить все сессии
curl -X POST https://rem2222.top/deepseek/reset-session?agent=all

# Логи
journalctl -u freedeepseekapi -f
```
