---
description: "Open-source AI-коллега на десктопе от Andrew Ng (aisuite): делает готовую работу — документы, ответы в Slack, календарь. Desktop-first (macOS/Windows), BYOK, 25+ коннекторов, MCP."
tags: [tech, agent, ai, desktop, open-source]
related: "[[tech/agentation]] [[tech/agent-memory-research-2026]] [[tech/Mercury-Agent-Skills]] [[tech/multica]]"
source: "https://github.com/andrewyng/openworker"
---

# OpenWorker — AI-коллега на десктопе (Andrew Ng)

_Записано: 2026-08-04_

## Суть

**OpenWorker** — open-source AI-агент (open beta), который живёт на десктопе и отдаёт **готовую работу**, а не чат: готовый документ, ответ в Slack с цифрами, обновлённый календарь, разобранный инбокс.

Автор — **Andrew Ng** (тот же, что aisuite и DeepLearning.AI). Репозиторий: [github.com/andrewyng/openworker](https://github.com/andrewyng/openworker) (MIT), openworker.com.

## Как работает

1. Говоришь желаемый результат («подготовь бриф клиенту», «разбери календарь»)
2. Агент разбивает задачу на шаги и работает по десктопу, файлам и подключённым приложениям
3. Перед любым существенным действием (отправка сообщения, изменение календаря, команда в терминале) — **спрашивает подтверждение**
4. Отдаёт готовый результат, а не TODO-список

Архитектура:

```text
┌────────────────────────────────────────────────┐
│              OpenWorker desktop app            │  native shell + GUI
├────────────────────────────────────────────────┤
│           local agent server (Python)          │  engine · tools · connectors — на aisuite
├───────────────┬────────────────┬───────────────┤
│  files/терминал│  25+ коннекторы│  любая модель  │  BYOK, всё локально
└───────────────┴────────────────┴───────────────┘
```

## Возможности

- **Реальные результаты** — документы, таблицы, отчёты, веб-страницы как файлы
- **Slack-интеграция** — упомяни `@OpenWorker` в канале, ответ придёт в тред
- **25+ интеграций** — GitHub, Slack, Jira, Notion, Linear, HubSpot, Outlook, monday.com, Gmail, Google Calendar + терминал и локальные файлы. Любой инструмент через **MCP** подключается
- **Автоматизации по расписанию** — утренний бриф, еженедельный отчёт, постоянный мониторинг канала
- **Approval-gated** — запись, отправка и shell-команды требуют подтверждения; автономные прогоны паркуют вопросы в инбокс

## Модели (BYOK)

OpenAI · Anthropic · Google Gemini · Inkling (Thinking Machines) · GLM (Z.ai) · DeepSeek · Kimi (Moonshot) · Qwen · MiniMax · Mistral · Grok (xAI) + open-weight через Together и Fireworks, локально через Ollama.

## Приватность

Local-first: агент-цикл, разговоры, токены коннекторов и ключи моделей — всё в локальном хранилище приложения. Единственное облако — сервис OAuth-рукопожатий для коннекторов.

## Запуск из исходников

Требования: Python 3.10+, Node 20+, Rust (для desktop shell).

```bash
git clone https://github.com/andrewyng/openworker && cd openworker
bash packaging/setup_dev_env.sh          # создаёт .venv
.venv/bin/openworker-server --cwd ~/proj --port 8765   # агент-сервер
cd surfaces/gui && npm install && npm run dev          # браузерный UI
# полный desktop: npm run tauri dev
```

Бинарники: macOS (Apple Silicon, подписан) и Windows 10/11 x64 (пока не подписан — SmartScreen предупредит).

## Репозиторий

| Каталог | Содержимое |
|---|---|
| `coworker/` | Python backend — движок агента, провайдеры, коннекторы, MCP-клиент, память, автоматизации |
| `surfaces/gui/` | React UI + Tauri shell |
| `stt/` | Speech-to-text sidecar (Rust) |
| `packaging/` | Инсталляторы, auto-update, dev bootstrap |
| `docs/` | Дизайн-спеки и decision logs |
| `tests/` | Тесты backend |

## Связь со стеком Rem

- Построен на **aisuite** — единый chat-completions API через провайдеров + агентский слой с инструментами/MCP. aisuite — самостоятельная библиотека, подходит как основа для своих харнессов
- По сути — **open-source конкурент Hermes Desktop** (только desktop, macOS/Windows; на VPS не запускается)
- MCP-совместим → теоретически подключаются наши MCP-серверы (gbrain, agentmemory)
- Пока **beta**: рабочий, самообновляется, но «шероховатости полируются»
