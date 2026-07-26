---
type: concept
title: FreeNIMAPI
description: FreeNIMAPI — локальный прокси-мост между NVIDIA NIM (бесплатный trial) и кодинг-агентами (Hermes, Codex, Claude Code, OpenCode). Работает с GLM-5.2, DeepSeek V4, MiniMax M3, GPT-OSS-120B.
tags: [tech, llm, free, proxy, nvidia, hermes]
related:
  - tech/free-llm-api-resources
  - tech/free-claude-code
  - tech/freellmapi
ingested_via: "'mcp:put_page'"
ingested_at: '2026-07-19T00:09:24.873Z'
source_kind: "'mcp:put_page'"
---

# FreeNIMAPI

**Репозиторий:** https://github.com/ForgetMeAI/FreeNIMAPI
**Видео:** https://youtu.be/aEhQlRp3cGQ (канал ForgetMe)
**Звёзд:** 5, **Форков:** 0
**Лицензия:** MIT

## Суть

Локальный прокси, который транслирует запросы от кодинг-агентов в NVIDIA NIM (Chat Completions) и обратно в нужный каждому агенту формат.

Три wire-протокола:
| Клиент | Формат | Endpoint |
|--------|--------|----------|
| **Hermes Agent** | OpenAI Chat Completions | `POST /v1/chat/completions` |
| **Codex** | OpenAI Responses | `POST /v1/responses` |
| **Claude Code** | Anthropic Messages | `POST /v1/messages` |
| **OpenCode** | Chat/Responses | оба |

NVIDIA-ключ остаётся внутри прокси, агенты получают отдельный локальный ключ.

## Быстрый старт

**Требования:** Git, Node.js 20+, [NVIDIA API key](https://build.nvidia.com/settings/api-keys)

```bash
git clone https://github.com/ForgetMeAI/FreeNIMAPI.git
cd FreeNIMAPI
npm ci
npm run start:guided
```

Лаунчер запросит NVIDIA-ключ (скрытый ввод) и поднимет прокси на `http://127.0.0.1:3000`.

## Проверка

```bash
FREENIM_LOCAL_API_KEY=freenim-local npm run health
```

## Подключение Hermes Agent

Добавить custom provider в профиль:

```yaml
model:
  default: nim-auto
  provider: custom
  base_url: http://127.0.0.1:3000/v1
  api_key: freenim-local
  api_mode: chat_completions
```

## Модели (snapshot 2026-07-17)

| Алиас | NVIDIA upstream | Статус |
|-------|----------------|--------|
| `nim-auto` (он же `gpt-oss-120b`) | `openai/gpt-oss-120b` | default |
| `minimax-m3` | `minimaxai/minimax-m3` | candidate |
| `glm-5.2` | `z-ai/glm-5.2` | experimental |
| `deepseek-v4-flash` | `deepseek-ai/deepseek-v4-flash` | experimental |
| `deepseek-v4-pro` | `deepseek-ai/deepseek-v4-pro` | unverified |
| `kimi-k2.6` | `moonshotai/kimi-k2.6` | deprecated |

## Подключение Claude Code

```bash
export FREENIM_LOCAL_API_KEY=freenim-local
export FREENIM_MODEL=nim-auto
export ANTHROPIC_BASE_URL=http://127.0.0.1:3000
export ANTHROPIC_AUTH_TOKEN="$FREENIM_LOCAL_API_KEY"
export ANTHROPIC_MODEL="$FREENIM_MODEL"
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
claude --model "$FREENIM_MODEL"
```

## Подключение Codex

В `~/.codex/config.toml`:

```toml
model = "nim-auto"
model_provider = "freenim"

[model_providers.freenim]
name = "FreeNIMAPI"
base_url = "http://127.0.0.1:3000/v1"
env_key = "FREENIM_LOCAL_API_KEY"
wire_api = "responses"
requires_openai_auth = false
```

## Переменные окружения

| Переменная | По умолчанию | Назначение |
|-----------|:-----------:|------------|
| `HOST` | `127.0.0.1` | адрес прослушивания |
| `PORT` | `3000` | локальный порт |
| `NVIDIA_BASE_URL` | `https://integrate.api.nvidia.com/v1` | hosted upstream |
| `NIM_DEFAULT_MODEL` | `nim-auto` | алиас по умолчанию |
| `NIM_TIMEOUT_MS` | `120000` | deadline запроса |
| `FREENIM_LOCAL_API_KEY` | пусто | локальный ключ для агентов |

## Ограничения

- NVIDIA API Catalog — trial/evaluation, не «бесплатно навсегда»
- Bridge поддерживает только текст (нет изображений, thinking blocks, computer-use)
- Первый токен — только после полного upstream-ответа (SSE синтезируется)
- Не для production без коммерческого endpoint

## Ссылки

- GitHub: https://github.com/ForgetMeAI/FreeNIMAPI
- Быстрый старт (RU): https://github.com/ForgetMeAI/FreeNIMAPI/blob/main/docs/QUICKSTART.ru.md
- API docs: https://github.com/ForgetMeAI/FreeNIMAPI/blob/main/docs/API.md
- Канал: https://t.me/forgetmeai
- Бусти: https://boosty.to/forgetme
