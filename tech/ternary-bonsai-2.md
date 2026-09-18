---
description: Ternary Bonsai 2 — 27B-модель на базе Qwen3.8, трёхзначное квантование, 5.9 ГБ, Apache 2.0. 98.2% от Qwen3.8, vision + tool calling.
tags: [llm, local, quantized, qwen, bonsai, prismml, vision, tool-calling]
related:
  - hardware/xe2690-workstation
  - tech/free-llm-api-resources
---

# Ternary Bonsai 2 (PrismML)

## Что это

Ternary Bonsai 2 — компактная 27B-модель от PrismML, построенная на базе **Qwen3.8 27B**. Ключевое отличие — трёхзначное квантование (ternary quantization), которое сжимает модель до **5.9 ГБ** (~9x меньше полной версии). Открыта под **Apache 2.0**.

## Характеристики

| Параметр | Значение |
|----------|----------|
| **Базовая модель** | Qwen3.8 27B |
| **Размер (квантованная)** | ~5.9 ГБ |
| **Квантование** | Ternary (трёхзначное) |
| **Лицензия** | Apache 2.0 |
| **Vision** | ✅ Поддержка изображений |
| **Tool Calling** | ✅ Поддержка инструментов |

## Бенчмарки (vs Qwen3.8 полная)

| Метрика | Bonsai 2 | Qwen3.8 | Удержание |
|---------|----------|---------|-----------|
| **Overall** | 83.9 | 85.4 | 98.2% |
| **Math** | — | — | 99.5% |
| **Coding** | — | — | 99.3% |
| **Instruction Following** | — | — | **102%** |
| **Knowledge & Reasoning** | — | — | высокое |
| **Agentic & Tool Calling** | — | — | высокое |

Модель превосходит Qwen3.8 по Instruction Following (102%), что необычно для квантованной версии.

## Подходит для

- **CPU-only станций** (XE2690, 64 ГБ RAM) — 5.9 ГБ влезет в RAM, inference без GPU
- **Домашних серверов** — минимальные требования к железу
- **Задач кодинга и математики** — удержание 99%+ от полной модели
- **Агентных задач** — vision + tool calling в компактном формате

## Установка

Доступна на HuggingFace (поискать `PrismML/Ternary-Bonsai-2-27B` или аналогичный repo ID). Запуск через llama.cpp / Ollama / vLLM.

## Ссылки

- PrismML (разработчик)
- HuggingFace: модель доступна под Apache 2.0
