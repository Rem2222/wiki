---
description: Agent Reach — CLI-инструмент, дающий AI-агентам доступ к интернету (research, format, transcribe).
tags: [tools, cli, ai, web]
related:
  - tools/yt-dlp
  - tech/agent-reach
created: 2026-08-03
---

# Agent Reach

CLI-инструмент: «Give your AI Agent eyes to see the entire internet». Используется агентами Hermes для веб-исследований (см. skill `agent-reach`).

Установлен в `/opt/agent-reach-venv/`, симлинк `/usr/local/bin/agent-reach` (2026-08-02).

## Команды

```bash
agent-reach setup      # первичная настройка
agent-reach configure  # конфигурация
agent-reach doctor     # диагностика
agent-reach skill      # установка skill для агента
agent-reach transcribe # транскрибация
agent-reach watch      # наблюдение
agent-reach check-update
```

## Связано

- Skill `agent-reach` в Hermes — основной способ вызова для веб-исследований
- `tools/yt-dlp` — используется для скачивания видео-контента
