---
description: Эксперимент по подключению ChatGPT Teacher (K12) подписки к Hermes через Codex API proxy
tags: [chatgpt, teacher, codex, proxy, hermes, experiment]
related: []
date: 2026-06-17
---

# Эксперимент: ChatGPT Teacher → Hermes через Codex Proxy

## Проблема
ChatGPT Teacher (K12) подписка не предоставляет API-ключа. Нужен способ использовать подписку через Hermes.

## Исследованные варианты

### 1. 0oAstro/codex-openai-proxy (Rust)
- **Фишка:** OAuth PKCE, `login-device` для headless (VPS), автокеры
- **Попытка:** device-флоу запросил верификацию телефона — не прошёл
- **Статус:** ❌ Не взлетело

### 2. Securiteru/codex-openai-proxy (Rust, 138⭐)
- **Фишка:** Читает `~/.codex/auth.json`, Rust-бинарник
- **Попытка:** Не пробовали — нужен Codex OAuth, упрётся в ту же проблему
- **Статус:** ⏸ Отложен

### 3. Kitjesen/chatgpt-to-api (Python) ✅
- **Фишка:** Session Token из кук браузера (`__Secure-next-auth.session-token`), `curl_cffi` для обхода Cloudflare
- **Попытка:** 
  - Собрали, запустили на VPS
  - Session Token и Access Token валидны
  - Cloudflare обходится через `curl_cffi`
  - **НО:** Codex endpoint (/backend-api/codex/responses) возвращает: `"model X is not supported when using Codex with a ChatGPT account"`
- **Причина:** Teacher (K12) план не имеет доступа к Codex API
- **Статус:** ❌ Не взлетело

## Почему Codex не работает с Teacher
Из JSON сессии:
```json
{
  "planType": "k12",
  "structure": "workspace",
  "organizationId": "org-..."
}
```
K12/Workspace аккаунты не включены в Codex API. Только ChatGPT Plus/Pro или отдельный Codex subscription.

## Альтернативы

### OpenRouter (уже есть)
- Просто добавить `openai/gpt-4o` в конфиг Hermes
- Отдельная оплата, не через Teacher подписку

### platform.openai.com
- Создать отдельный API-аккаунт
- Получить `sk-...` ключ
- Прямой доступ, без посредников

### PandoraNext (предстоит исследовать)
- Использует `/backend-api/conversation`
- Нужно решение Cloudflare Turnstile
- Работает с любым аккаунтом
- Задача: MUL-??? (создать)

## Вывод
ChatGPT Teacher подписку напрямую к Hermes через API-прокси подключить не удалось — ограничение OpenAI. Рекомендуется OpenRouter или отдельный API-ключ.
