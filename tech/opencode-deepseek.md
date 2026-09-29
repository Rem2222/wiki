---
description: "Локальный OpenAI-совместимый мост к бесплатному веб-чату DeepSeek — эмулирует API без ключа, но tool calling парсится из прозы и запросы сериализуются."
tags: [ai,deepseek,free-api,bridge,opencode]
related: [[tech/command-code]] [[ops/services/hermes-agent]] [[tech/freellmapi]]
---

# opencode-deepseek (мост к бесплатному DeepSeek)

## Что это

Локальный **OpenAI-совместимый мост** к бесплатному веб-чату DeepSeek (chat.deepseek.com). FastAPI-сервер на `127.0.0.1:8000` принимает OpenAI-запросы и транслирует их в веб-чат через обычный аккаунт DeepSeek, решая PoW-челлендж через wasmtime. Выглядит для клиента как настоящий OpenAI API — без ключа и без оплаты.

Порт/форк проекта `sums001/Deepseek-API`. Официальной связи с DeepSeek нет — используется твой личный аккаунт, ответственность на тебе.

- 🐙 https://github.com/Tsuev/opencode-deepseek
- 33 звезды, MIT, Python, создан 2026-09-22

## Как устроено

```
клиент (opencode/Hermes) → localhost:8000/v1 (FastAPI) → внутренний протокол + PoW/WASM → chat.deepseek.com
```

- `deepseek/auth.py` — вход через настоящий Playwright-браузер, сессия в `session/`, живёт ~5 часов и обновляется автоматически
- `deepseek/pow.py` — решение proof-of-work в песочнице `wasmtime`
- Модели: `deepseek-chat` (Instant), `deepseek-expert`

## Развёртывание

```bash
git clone https://github.com/Tsuev/opencode-deepseek.git
cd opencode-deepseek
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt && playwright install chromium
python -m deepseek.auth          # одноразовый вход в аккаунт через браузер
cp .env.example .env
python app.py                    # http://127.0.0.1:8000
```

Проверка: `curl http://127.0.0.1:8000/healthz` и `curl http://127.0.0.1:8000/v1/models`.

Подключение как custom provider (base_url `http://127.0.0.1:8000/v1`, apiKey любой — мост игнорирует).

## ⚠️ Ограничения (ключевое)

- **Сериализация запросов** — вызовы строго по одному (PoW-хранилище wasmtime не реентерабельно). Параллельных агентов/сессий не будет.
- **Tool calling эмулируется** — мост буферизует ответ и парсит прозу/XML-фенсы DeepSeek в tool calls. Терпимо к фенсам, но «возможны сбои на длинных многошаговых цепочках».
- **Нет реального подсчёта токенов** — usage ≈ грубая оценка 4 символа/токен.
- **Большинство OpenAI-параметров игнорируется** — работают только `model`, `messages`, `stream`, `conversation_id`, `thinking`, `search`. temperature/top_p/max_tokens не действуют.
- **Нет vision** (изображения не принимаются).
- `conversation_id` фиксирует модель при создании потока — при продолжении `model` игнорируется.
- **Риск аккаунта** — массовые автоматические запросы могут привести к блокировке обычного аккаунта DeepSeek.

## Для кого это

- ✅ Экономия: полноценный бесплатный LLM-endpoint локально, без API-ключа.
- ❌ **Не подходит для tool-heavy агентов** (Hermes, DSH, Mercury): эмулируемый tool calling ломается на нетривиальных цепочках, а сериализация убивает параллельные задачи.
- ❌ Дублирует бесплатные пути к DeepSeek, уже имеющиеся в стеке: [[tech/freellmapi]], opencode-go free-модели, дилы Command Code на deepseek-v4.1-flash.
- 📌 Резерв: если freellmapi или free-каналы отвалятся — этот мост как запасной вариант, когда нужно разово сэкономить.

## Связи

- Родственные темы: [[ops/services/hermes-agent]], [[tech/command-code]] (дешёвый официальный endpoint), [[tech/deepseek-harness]]
