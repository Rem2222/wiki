---
description: OpenAI-совместимый прокси, агрегирующий бесплатные tier'ы от 11+ AI-провайдеров в единый `/v1/chat/completions` endpoint. Суммарно ~1.3 млрд токенов/мес.
tags: [tech]
related: [[tech/assemblyai]] [[tech/openai-routing]]
---

# freellmapi

**Репозиторий:** https://github.com/tashfeenahmed/freellmapi
**Звёзд:** ~2k, **Форков:** ~286
**Лицензия:** MIT

## Суть

OpenAI-совместимый прокси, агрегирующий бесплатные tier'ы от **11+ AI-провайдеров** в единый `/v1/chat/completions` endpoint. Суммарно ~**1.3 млрд токенов/мес**.

## Поддерживаемые провайдеры

Google (Gemini 2.5 Flash), Groq, Cerebras (Qwen3 235B), SambaNova (DeepSeek V3, Llama 4), Mistral, OpenRouter, GitHub Models (GPT-4.1, GPT-4o), Cloudflare (Kimi K2), Cohere, Z.ai / Zhipu (GLM-4.5/4.7), NVIDIA NIM

## Ключевые фичи

- Полная OpenAI-совместимость — любой SDK (Python, curl, LangChain, Hermes), меняется только `base_url`
- Streaming (SSE) + Tool calling
- Автоматический fallover при 429/5xx/timeout — перебор по цепочке провайдеров (до 20 попыток)
- Per-key rate tracking (RPM/RPD/TPM/TPD)
- Sticky sessions (30 мин разговора с той же моделью)
- Шифрование ключей AES-256-GCM, хранение в SQLite
- Единый API-ключ `freellmapi-...` для всех клиентов
- Health checks (периодические пробы ключей)
- Админ-панель: React + Vite, тёмная тема, playground
- Аналитика per-request (latency, токены, успешность)
- Работает на Raspberry Pi 4 (~40 MB RSS idle)

## Быстрый старт

```bash
git clone https://github.com/tashfeenahmed/freellmapi.git
cd freellmapi
npm install
cp .env.example .env
echo "ENCRYPTION_KEY=$(node -e "console.log(require('crypto').randomBytes(32).toString('hex'))")" >> .env
npm run dev
```

Админка: http://localhost:5173
API: http://localhost:3001/v1

## Использование

```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:3001/v1", api_key="freellmapi-...")
resp = client.chat.completions.create(model="auto", messages=[{"role": "user", "content": "hi"}])
```

## Disclaimer

Автор — только для личных экспериментов, не production-ready. Бесплатные tier'ы могут измениться.