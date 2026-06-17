---
description: Fix для DeepSeek V4 Error 400 в thinking-mode при multi-turn agentic задачах
tags: [deepseek, claude-code, fix, error, ccr, transformer]
related: [[concepts/sdd]]
---

# DeepSeek V4 Error 400 Fix

**GitHub:** https://github.com/marianomelo/ccr-deepseek-thinking-fix

Трансформер для `claude-code-router` (ccr), чинящий баг DeepSeek V4 в thinking-mode при multi-turn задачах с tool calls.

## В чём баг

При роутинге Claude Code через ccr на DeepSeek V4 в thinking-mode второй же вызов тула падает:

```
API Error: 400 The `reasoning_content` in the thinking mode must be passed back to the API.
```

## Почему

DeepSeek V4 требует: если ассистент делал `tool_calls`, его `reasoning_content` **обязательно** надо слать обратно в каждом следующем запросе. Claude Code теряет это поле при своей Anthropic↔OpenAI конвертации.

## Как работает фикс

**reasoning-injector.js** — in-memory transformer для ccr:

1. **На ответе** (SSE): перехватывает стрим, аккумулирует `reasoning_content`, сохраняет в Map под ключом из `tool_call_ids` (сортированных, через `|`)
2. **На запросе**: находит assistant-сообщения с `tool_calls`, восстанавливает ключ и вставляет `reasoning_content` обратно
3. LRU-кеш на 1000 записей, при рестарте ccr сбрасывается

## Результаты

- 0 ошибок 400 на 13+ турах
- 15/15 успешных инъекций
- Реальные reasoning_tokens сохраняются

## Установка

```bash
mkdir -p ~/.claude-code-router/transformers
curl -L https://raw.githubusercontent.com/marianomelo/ccr-deepseek-thinking-fix/main/reasoning-injector.js \
  -o ~/.claude-code-router/transformers/reasoning-injector.js
```

В `config.json` провайдера добавить `"use": ["deepseek", "reasoning-injector"]` (injector **последним**).

## Нужно ли

**Да, если** используешь DeepSeek V4 (флагман) в thinking-mode через ccr.
**Нет, если** используешь V4 Flash (бага может не быть) или не используешь DeepSeek V4.
