---
type: tool
title: ODS — Osmantic Deployment System
description: Локальный AI-сервер «всё-в-одном» — LLM инференс, Open WebUI, голос, агенты, RAG, генерация изображений, одной командой
tags: [local-ai, llm, open-webui, ollama, selfhosted, agents]
related:
  - tech/paperclip
  - concepts/llm-tier-strategy
  - tech/local-gguf-serving
source: https://github.com/Osmantic/ODS
ingested_at: '2026-07-23'
---

# ODS (Osmantic Deployment System)

**Суть:** Установка одной командой полного стека локального AI-сервера. Всё что нужно для приватного AI — от инференса до веб-интерфейса, голоса, агентов и генерации изображений.

## Быстрый старт

```bash
curl -fsSL https://install.osmantic.com/ods.sh | bash
```

После установки — `http://localhost:3000` (Open WebUI).

## Что входит

| Компонент | Назначение |
|---|---|
| **Ollama / llama.cpp** | Локальный LLM инференс |
| **Open WebUI** | ChatGPT-подобный интерфейс |
| **Control Dashboard** | Управление моделями, сервисами, GPU |
| **Voice** | Голосовой ввод/вывод |
| **n8n** | Workflow automation |
| **Hermes-совместимые агенты** | Подключение через единую панель |
| **RAG + Search** | Локальные документы, приватный поиск |
| **ComfyUI** | Генерация изображений |
| **Privacy / Ops** | Auth, secrets, observability |

## Системные требования

| Платформа | Поддержка |
|---|---|
| Linux (NVIDIA + AMD + Intel Arc) | ✅ Полная |
| Windows (NVIDIA + AMD) | ✅ WSL2 / Docker Desktop |
| macOS (Apple Silicon) | ✅ Нативная Metal |

Тестировалось на: Ubuntu 24.04/22.04, Debian 12, Mint 21.3, Fedora 41+, Rocky 9, Arch, Manjaro.

## Режимы работы

**Local** — всё на своём GPU/CPU, данные не уходят.
**Cloud** — тот же стек, но инференс через OpenAI/Anthropic/Together API.
**Hybrid** — смешанный режим.

## API эндпоинт

Для OpenAI-совместимых клиентов:

- Linux Docker: `http://localhost:11434` (OLLAMA_PORT)
- macOS / Windows: `http://localhost:8080` (llama-server)
- Open WebUI: `http://localhost:3000`

## Ключевые фичи (из описания)

> *"ODS wires together everything you need to run AI locally, so you do not have to assemble Ollama, Open WebUI, n8n, ComfyUI, and privacy tools by hand."*

- Автоопределение GPU и подбор модели
- Dashboard с управлением всем стеком
- Агенты вроде Hermes подключаются через панель
- Голос, RAG, поиск, генерация картинок
- No cloud required. No subscriptions required.

## Релевантность к стеку

**На VPS (Hermes + Dex):** избыточно — всё уже есть.
**На Windows (GT 1030, XE2690):** может быть полезен для быстрого старта локального LLM без ручной сборки llama.cpp / Ollama.

Хорошая альтернатива ручной сборке `local-gguf-serving` для Windows — ODS сразу даёт Open WebUI + RAG + голос, не нужно настраивать по частям.

## Статистика (GitHub)

- Stars: 3.5k
- Forks: 512
- Коммитов: 2,916
- Branches: 385
- PRs: 185
- Лицензия: Apache 2.0
- Последний коммит: 12 минут назад (активно развивается)
