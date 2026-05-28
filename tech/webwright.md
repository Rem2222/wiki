---
description: Минималистичный фреймворк от Microsoft Research для веб-агентов через code-as-action (Python + Playwright из терминала)
tags: [microsoft, research, web-agents, browser-automation, playwright, code-as-action]
related: []
source: https://github.com/microsoft/Webwright
website: https://microsoft.github.io/Webwright/
blog: https://www.microsoft.com/en-us/research/articles/webwright-a-terminal-is-all-you-need-for-web-agents/
license: MIT
created: 2026-05-27
updated: 2026-05-27
---

# Webwright

Минималистичный open-source фреймворк от **Microsoft Research** для превращения код-генерирующих LLM в state-of-the-art веб-агентов.

**Ключевая идея:** вместо предопределённого цикла «наблюдай → кликни → повтори», модель пишет произвольный Python-код с Playwright и исполняет его в терминале. **«A Terminal Is All You Need For Web Agents»**.

## Архитектура

```
webwright/
├── src/webwright/
│   ├── run/cli.py                    # CLI entrypoint
│   ├── agents/default.py             # основной цикл агента
│   ├── environments/
│   │   ├── local_workspace.py        # workspace файлов
│   │   └── local_browser.py          # Playwright browser workspace
│   ├── tools/
│   │   ├── image_qa.py               # визуальный QA по скриншотам
│   │   └── self_reflection.py        # саморефлексия/верификация
│   └── models/                       # OpenAI, Anthropic, OpenRouter
├── config/                           # YAML-конфиги
├── skills/webwright/                  # общий skill для Claude Code, Codex, Hermes
├── .claude-plugin/ + .codex-plugin/
└── tests/
```

**Ядро:** ~3 200 строк Python. Зависимости: httpx, pydantic, playwright, typer, jinja2, rich.

## Как работает цикл агента

1. Модель получает задачу + стартовый URL
2. На каждом шаге пишет одну bash-команду (обычно Python + Playwright)
3. Harness выполняет, захватывает stdout/stderr/скриншоты
4. Результат показывается модели как Observation
5. До 100 шагов
6. Финальный артефакт: `final_script.py` + логи + скриншоты

Формат ответа: JSON `{thought, bash_command, done, final_response}`

## Key Features

- **Code-as-action** — циклы, функции, условная логика, а не дискретные click/type
- **State = workspace, не browser session** — браузер disposable, состояние в файлах
- **Минимализм** — нет мультиагентных систем, графовых движков
- **Pluggable backend** — OpenAI, Anthropic, OpenRouter
- **Встроенные инструменты:** image_qa, self_reflection
- **Task Showcase** — Flask-дашборд для повторяемых задач
- **Плагины** — для Claude Code, OpenAI Codex, OpenClaw, Hermes Agent

## Результаты (SOTA)

- **Online-Mind2Web:** 86.7% (GPT-5.4), 84.7% (Claude Opus 4.7)
- **Odysseys:** 60.1% (GPT-5.4) — **+15.6 п.п.** над предыдущим SOTA

## Сравнение

| Параметр | Stagehand | browser-use | **Webwright** |
|----------|-----------|-------------|---------------|
| Парадигма | Гибрид код+NL | Автономный LLM | **Code-as-action** |
| Пространство действий | Playwright код | Индексированные click/type | **Произвольный Python** |
| State | Сессия браузера | Сессия браузера | **Workspace: файлы** |
