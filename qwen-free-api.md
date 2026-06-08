---
description: Развёртывание FreeQwenApi — бесплатный Qwen API через web-чат на VPS
tags: [qwen, api, proxy, selfhosted]
related: [free-api-deepseek-qwen]
---

# FreeQwenApi

**FreeQwenApi** — локальный OpenAI-compatible API proxy для Qwen Web Chat (`chat.qwen.ai`). Позволяет использовать Qwen 3.7 Max и другие модели через OpenAI SDK, Open WebUI, Hermes и другие инструменты.

Репозиторий: https://github.com/ForgetMeAI/FreeQwenApi

## Деплой

- **Сервер:** `/opt/FreeQwenApi`
- **Systemd:** `freeqwenapi.service`
- **Порт:** `127.0.0.1:9656`
- **Nginx:** `https://rem2222.top/qwen/` → `127.0.0.1:9656`
- **Статус:** `systemctl status freeqwenapi`
- **Node.js:** v22.22.3 (`/root/.local/bin/node`)

## Аутентификация

Для работы сервера нужна авторизация в `chat.qwen.ai`. Процесс требует браузера на ПК с GUI.

### На ПК с Chrome/GUI

```bash
git clone https://github.com/ForgetMeAI/FreeQwenApi.git
cd FreeQwenApi
npm install
npm run auth       # Откроется Chrome, войдите в chat.qwen.ai
# После успешного входа — скопировать папку session на VPS
```

### Перенос сессии на VPS

```bash
scp -r session/ root@80.241.218.110:/opt/FreeQwenApi/session/
```

### Запуск сервера

```bash
systemctl daemon-reload
systemctl start freeqwenapi
systemctl status freeqwenapi
```

После этого сервер будет доступен по `https://rem2222.top/qwen/v1`.

## Использование

### OpenAI SDK

```python
from openai import OpenAI
client = OpenAI(
    base_url="https://rem2222.top/qwen/v1",
    api_key="any"
)
```

### Для Open WebUI

```
Base URL: https://rem2222.top/qwen/v1
API Key: любой
```

## Модели

| Alias | Описание |
|-------|----------|
| `qwen3.7-max` | Флагманская модель Qwen 3.7 |
| `qwen3.7-plus` | Быстрая версия Qwen 3.7 |
| `qwen3.6-plus` | Qwen 3.6 Plus |
| `qwen3.5-plus` | Qwen 3.5 Plus |
| `qwen3.5-flash` | Qwen 3.5 Flash |
| `qwen3-max` | Qwen 3 Max |
| `qwen3-vl-plus` | Мультимодальная (vision) |
| `qwen3-coder-plus` | Кодинг |
| `qwen3-omni-flash` | Omni модель |
| `qwq-32b` | Reasoning-модель |
| `qwen2.5-vl-32b-instruct` | Vision (older) |
| `qwen2.5-coder-32b-instruct` | Coder (older) |

Полный список: `/opt/FreeQwenApi/src/AvailableModels.txt`

## Управление

```bash
# Статус сервера
systemctl status freeqwenapi

# Список моделей
curl https://rem2222.top/qwen/v1/models

# Логи
journalctl -u freeqwenapi -f
```

## Hermes Provider

- **Провайдер:** `freeqwenapi`
- **Base URL:** `https://rem2222.top/qwen/v1`
- **API Key:** `any`
- **Модель по умолчанию:** `qwen3.7-max`
- **Зарегистрирован:** `_PROVIDER_MODELS` и `CANONICAL_PROVIDERS` в `models.py`
- **Агент Multica:** FreeQwenApi
