---
description: _Записано: 2026-05-03_
tags: [tech]
---

# Codex Harness — OpenClaw Plugin

_Записано: 2026-05-03_

## Суть

Плагин `codex` позволяет OpenClaw запускать встроенные агентские обороты через нативный Codex app-server вместо встроенного PI harness.

OpenClaw продолжает владеть: каналами чата, файлами сессий, выбором модели, инструментами, подтверждениями, доставкой медиа и зеркальным транскриптом.

## Быстрый старт

**1. Авторизация через Codex OAuth:**
```bash
openclaw models auth login --provider openai-codex
```

**2. Конфигурация:**
```json5
{
  plugins: {
    entries: {
      codex: { enabled: true },
    },
  },
  agents: {
    defaults: {
      model: "openai/gpt-5.5",
      agentRuntime: { id: "codex" },
    },
  },
}
```

## Модель vs Runtime — в чём разница

| Вопрос | Ответ |
|--------|-------|
| `openai-codex/gpt-*` | Какой провайдер/авторизацию использовать PI? |
| `agentRuntime.id: "codex"` | Какой цикл выполняет встроенный оборот? |
| `/codex ...` | К какой нативной Codex-конversation привязать чат? |
| ACP | Какой внешний harness-процесс запустить? |

## Важные правила

- **`openai/gpt-5.5` + `agentRuntime.id: "codex"`** = Codex subscription + нативный Codex runtime
- **`openai-codex/gpt-5.5`** = Codex OAuth через PI (старый путь)
- **`openai/gpt-*` без Codex runtime** = прямой OpenAI API через OpenClaw

## Команды

| Команда | Что делает |
|---------|-----------|
| `/codex bind` | Привязать чат к Codex |
| `/codex resume <id>` | Возобновить Codex thread |
| `/codex threads` | Показать Codex threads |
| `/codex steer` | Управлять Codex thread |
| `/codex stop` | Остановить Codex thread |
| `/diagnostics [note]` | Отправить отчёт о проблеме |
| `/codex diagnostics [note]` | Feedback для конкретного thread |

## Status

`/status` показывает effective runtime:
- `Runtime: OpenClaw Pi Default` — обычный PI harness
- `Runtime: OpenAI Codex` — нативный Codex app-server

## Troubleshooting

**`openclaw doctor` предупреждает когда:**
- плагин `codex` включен
- модель `openai-codex/*`
- но runtime НЕ `codex`

Это не ошибка — если вы хотели именно ChatGPT/Codex OAuth через PI, всё норм.

**Если хотели нативный Codex runtime:**
```bash
## Изменить модель на openai/gpt-* и поставить agentRuntime.id: "codex"
## Затем /new или /reset для новой сессии
```

## Требования

- OpenClaw с bundled плагином `codex`
- Codex app-server `0.125.0` или новее
- Codex auth (Codex CLI account или OpenClaw `openai-codex` auth profile)

## Workspace bootstrap

Codex обрабатывает `AGENTS.md` сам через нативное обнаружение проектов. OpenClaw НЕ пишет синтетические файлы.

Для паритета с OpenClaw workspace, Codex harness резолвит `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md`, `BOOTSTRAP.md`, `MEMORY.md` и пробрасывает их через Codex config instructions на `thread/start` и `thread/resume`.

## Источник

https://docs.openclaw.ai/plugins/codex-harness