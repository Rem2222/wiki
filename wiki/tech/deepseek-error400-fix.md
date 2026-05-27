---
description: Fix для DeepSeek V4 Error 400 при использовании в Claude Code
tags: [deepseek, claude-code, fix, error]
related: [[concepts/sdd]]
---

# DeepSeek V4 Error 400 Fix

**GitHub:** https://github.com/marianomelo/ccr-deepseek-thinking-fix

Исправление для ошибки 400 при использовании DeepSeek V4 моделей в Claude Code через провайдеров/прокси.

## Фишка

Позволяет использовать DeepSeek V4 (и особенно V4 Flash — самую дешёвую и достойную модель для SDD по мнению автора) без Error 400.

## Зачем

Автор статьи рекомендует DeepSeek V4 Flash как «очень достойную модель, особенно для SDD, и самую дешёвую на сегодня». Error 400 возникает при неправильной конфигурации — этот фикс решает проблему.

## Нужно ли

✅ **Да, если** используешь/планируешь использовать DeepSeek V4 в Claude Code.
