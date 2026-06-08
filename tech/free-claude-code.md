---
description: Прокси для Claude Code, который перенаправляет запросы с Anthropic API на бесплатные LLM-провайдеры.
tags: [tech]
related: [[tech/opencode]] [[tech/poe-api-models]] [[tech/subquadratic]]
---

# Free Claude Code (fcc-server)

Прокси для Claude Code, который перенаправляет запросы с Anthropic API на бесплатные LLM-провайдеры.

**Репозиторий:** https://github.com/Alishahryar1/free-claude-code
**Развёрнут на:** VPS 81.17.100.103:8082
**Провайдер:** OpenCode Zen (через [[tech/opencode]])

---

## Быстрый старт

### Вариант 1: На VPS через SSH (рекомендуется)

Claude Code уже установлен на VPS. Просто заходи по SSH:

```bash
ssh root@81.17.100.103
```

Скрипт `claude-free` установлен в `/usr/local/bin/`:

```bash
## На VPS:
claude-free
```

Подставляет переменные для локального прокси (http://127.0.0.1:8082) и запускает Claude Code. Работает из любой папки.

### Вариант 2: Установка Claude Code локально

```bash
npm install -g @anthropic-ai/claude-code
```

### Вариант 3: На Windows

Claude Code — это Node.js CLI, работает на Windows через **npm** или через **VSCode Extension**.

**Через npm (если есть Node.js):**
```bash
npm install -g @anthropic-ai/claude-code
```

Затем запускать из терминала (cmd/powershell):
```bash
set ANTHROPIC_BASE_URL=http://81.17.100.103:8082
set ANTHROPIC_AUTH_TOKEN=freecc
set CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1
claude
```

**Через VSCode Extension (проще):**
Установи расширение "Claude Code" из маркетплейса VSCode. В настройках (`settings.json`):
```json
"claude-code.environmentVariables": [
  { "name": "ANTHROPIC_BASE_URL", "value": "http://81.17.100.103:8082" },
  { "name": "ANTHROPIC_AUTH_TOKEN", "value": "freecc" },
  { "name": "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY", "value": "1" }
]
```

**Через WSL (Windows Subsystem for Linux, рекомендую):**
```bash
## В терминале WSL (Ubuntu):
npm install -g @anthropic-ai/claude-code
ANTHROPIC_BASE_URL="http://81.17.100.103:8082" ANTHROPIC_AUTH_TOKEN="freecc" CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1 claude
```

### VSCode Extension

В `settings.json`:

```json
"claude-code.environmentVariables": [
  { "name": "ANTHROPIC_BASE_URL", "value": "http://81.17.100.103:8082" },
  { "name": "ANTHROPIC_AUTH_TOKEN", "value": "freecc" },
  { "name": "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY", "value": "1" }
]
```

После настройки перезагрузить окно. Если появится экран логина — выбрать "Anthropic Console", авторизоваться. Расширение начнёт работать через прокси, игнорируя биллинг Anthropic.

### JetBrains ACP

Файл `~/.jetbrains/acp.json`:

```json
"env": {
  "ANTHROPIC_BASE_URL": "http://81.17.100.103:8082",
  "ANTHROPIC_AUTH_TOKEN": "freecc",
  "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY": "1"
}
```

---

## Админка (смена модели/провайдера)

Админка работает только через loopback. Открыть через SSH-туннель:

```bash
ssh -L 8082:127.0.0.1:8082 root@81.17.100.103
```

Затем открыть http://127.0.0.1:8082/admin

Там можно:
- Сменить провайдера (NVIDIA NIM, OpenRouter, Kimi, Wafer, DeepSeek, LM Studio, llama.cpp, Ollama, OpenCode Zen, Z.ai)
- Поменять модель для каждого тира (Opus/Sonnet/Haiku)
- Ввести API-ключи
- Настроить rate limits

---

## Поддерживаемые провайдеры

| Провайдер | Бесплатно? | Лимиты |
|-----------|-----------|--------|
| OpenCode Zen | Есть free модели | По ключу |
| NVIDIA NIM | 40 req/min | 40/мин |
| OpenRouter | Free модели | По модели |
| Kimi (Moonshot) | Нет | Платный |
| Wafer | Нет | Платный |
| DeepSeek | Нет | Платный |
| LM Studio | Да (локально) | Без лимитов |
| llama.cpp | Да (локально) | Без лимитов |
| Ollama | Да (локально) | Без лимитов |
| Z.ai | Нет | Платный |

---

## Текущая конфигурация

- **Модель:** `opencode/deepseek-v4-flash-free` (бесплатно)
- **Auth token:** `freecc`
- **Порт:** 8082
- **systemd:** `fcc-server.service` (автозапуск, авторестарт)
- **iptables:** порт 8082 открыт, правила сохраняются в `/etc/iptables.rules`, восстанавливаются через `/etc/network/if-pre-up.d/iptables-restore`

---

## Обновление

```bash
ssh root@81.17.100.103
source ~/.local/bin/env
uv tool install --force git+https://github.com/Alishahryar1/free-claude-code.git
systemctl restart fcc-server
```

---

## Управление сервисом

```bash
systemctl status fcc-server    # статус
systemctl restart fcc-server   # перезапуск
systemctl stop fcc-server      # остановка
journalctl -u fcc-server -f    # логи в реальном времени
```

## Альтернативные провайдеры

- [[tech/poe-api-models]] — подписки Poe включают API-доступ, OpenAI-compatible (альтернатива бесплатному прокси)
- [[tech/subquadratic]] — SubQ: first fully sub-quadratic LLM, 12M token context (ещё один альтернативный провайдер)
