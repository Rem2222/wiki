---
description: Jev + JevRouter — маршрутизатор browser-автоматизации для Codex/Claude Code/DSH. 5.5x скорость, 7x дешевле. Доступен через OpenRouter.
tags: [browser, automation, codex, claude-code, jev, router, ai-agent, tool-calling]
related:
  - tech/openviking
  - tech/free-llm-api-resources
---

# Jev + JevRouter

## Что это

**Jev** — модель для browser-автоматизации, которая берёт на себя клики, навигацию, прокрутку и выбор элементов, пока основной агент (Codex, Claude Code, DSH) занимается рассуждениями и вводом текста.

**JevRouter** — открытый прослойка-маршрутизатор, который подключает Jev к существующим агентам без переписывания оркестрации. Берёт на себя маршрутизацию между моделями, инструментами и субагентами. Разрешения и подтверждения остаются у основного агента.

## Как работает

Стандартный Codex на каждом шаге: прочитать DOM → рассуждение → вызов инструмента → ждать. Каждый цикл — задержка.

С Jev:
1. Codex задаёт цель
2. Jev выполняет клики, переходы, прокрутку (последовательно, без возврата к модели)
3. Когда нужно ввести текст или проверить изображение — управление возвращается Codex
4. После этого Jev продолжает

## Бенчмарки

| Метрика | Jev | DeepSeek V4.1 Flash |
|---------|-----|-------------------|
| **Tool accuracy (первые 5 шагов)** | **38%** | 24% |
| **Скорость** | **5.5x** | baseline |
| **Стоимость** | **7x дешевле** | baseline |

(Toolathlon, 10 задач)

## Установка

### JevRouter (рекомендуется)

1. Получить ключ Jev (доступен через OpenRouter)
2. Открыть http://jevrouter.co → скопировать инструкцию
3. Добавить ключ и инструкцию в Codex / Claude Code / другой агент

### Jev Browser (напрямую с Codex)

1. Codex с браузером/CUA, Node.js 22+, ключ TypeSafe API
2. `npm run install:codex -- --env-file .env`
3. Загрузить skill `jev-use`

## Поддерживаемые агенты

- **Codex** (OpenAI)
- **Claude Code** (Anthropic)
- **DSH** (DeepSeek Harness) — потенциально
- Любой агент с CUA/browser tools

## Ссылки

- http://github.com/vlad-terin/jev-use — Jev Browser skill
- http://jevrouter.co — JevRouter, инструкции по подключению
- OpenRouter — Jev доступен как модель
- http://deepwiki.com/vlad-terin/jev-browser — документация

## Статус

⏳ **Нужно попробовать** — özellikle для автоматизации браузерных задач в DSH и Hermes.
