---
description: Параметры конфигурации JAWL.
created: 2026-05-01
tags: [jawl, config, models, reference]
related: [[tech/jawl]] [[tech/jawl-architecture]] [[tech/jawl-context]]
parent: "[[tech/jawl]]"
---

# JAWL Configuration

Параметры конфигурации JAWL.

## Файлы

| Файл | Назначение |
|------|-----------|
| `config/models.json` | Провайдеры и модели |
| `settings.yaml` | Системные параметры |
| `.env` | API ключи |

## models.json

```json
{
  "providers": {
    "provider-name": {
      "baseUrl": "https://api.example.com/v1",
      "apiKeyEnv": "LLM_API_KEY_X",
      "api": "openai-completions",
      "models": [
        {
          "id": "model-id",
          "name": "Display Name",
          "contextWindow": 128000,
          "maxTokens": 4096,
          "reasoning": false
        }
      ]
    }
  }
}
```

### Текущие провайдеры (6)

| Провайдер | API | Модели |
|-----------|-----|--------|
| minimax | openai-completions | MiniMax-M2.7, MiniMax-M2.5 |
| zai | openai-completions | glm-5, glm-5.1, glm-4.7 |
| xiaomi | openai-completions | mimo-v2-pro, mimo-v2-flash |
| opencode-zen | openai-responses | gpt-5-nano |
| opencode-zen-chat | openai-completions | minimax-m2.5-free, hy3-preview-free, nemotron-3-super-free |
| cerebras | openai-completions | llama3.1-8b |

### Типы API

| Значение | SDK метод |
|----------|-----------|
| `openai-completions` | `session.chat.completions.create()` |
| `openai-responses` | `session.responses.create()` |

## settings.yaml

```yaml
llm:
  model_name: gpt-5-nano
  temperature: 0.4
  max_react_steps: 15

system:
  timezone: Europe/Moscow
  heartbeat_interval: 300

sql:
  max_tasks: 10
  max_mental_states: 10

linear:
  project_id: "..."
```

## Важные правила

1. **baseUrl без суффикса** — SDK добавляет `/chat/completions` сам
2. **apiKeyEnv = null** — для бесплатных провайдеров (без ключа)
3. **reasoning модели** — loop.py читает `.reasoning` когда `.content` is None

## Как добавить провайдера

→ [[tech/jawl-howto-add-provider|HOWTO: Добавить провайдера]]
