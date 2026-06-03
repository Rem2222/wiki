---
description: "baseUrl": "https://api.example.com/v1",
created: 2026-05-01
tags: [jawl, howto, provider, llm]
parent: "[[tech/jawl]]"
---

# HOWTO: Добавить LLM провайдера в JAWL

## Шаги

### 1. Добавить в config/models.json

```json
{
  "providers": {
    "my-provider": {
      "baseUrl": "https://api.example.com/v1",
      "apiKeyEnv": "LLM_API_KEY_MY",
      "api": "openai-completions",
      "models": [
        {
          "id": "my-model-v1",
          "name": "My Model V1",
          "contextWindow": 128000,
          "maxTokens": 4096,
          "reasoning": false
        }
      ]
    }
  }
}
```

### 2. Добавить API ключ в .env

```bash
LLM_API_KEY_MY=sk-your-key-here
```

Для бесплатных провайдеров: `"apiKeyEnv": null`

### 3. Типы API

| Значение | SDK метод | Примеры |
|----------|-----------|---------|
| `openai-completions` | `session.chat.completions.create()` | MiniMax, GLM, Cerebras |
| `openai-responses` | `session.responses.create()` | gpt-5-nano (OpenCode Zen) |

### 4. Переключить модель

Dashboard → Provider dropdown → Model dropdown. Или Telegram `/models`.

## Частые проблемы

### URL с суффиксом → 404
SDK добавляет `/chat/completions` к baseUrl:
- ❌ `https://api.example.com/v1/chat/completions`
- ✅ `https://api.example.com/v1`

### Reasoning модели → пустой ответ
Если модель возвращает текст в `.reasoning`, а не `.content` — loop.py автоматически читает `.reasoning` когда `.content` is None.

### Без API ключа
```json
{"apiKeyEnv": null, "baseUrl": "https://opencode.ai/zen/v1"}
```

## Связанные статьи

- [[tech/jawl-config|Config]] — полная структура конфигурации
- [[tech/jawl-react-loop|ReAct Loop]] — как используется API
