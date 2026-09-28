---
description: "qwen-tp — токен-план провайдер Alibaba (Aliyun MaaS TokenPlan) в стеке Hermes: vision qwen3.7-plus, дефолт deepseek-v4-flash, ~14 моделей."
tags: [llm,provider,qwen,alibaba,token-plan,inference]
related: [[tech/qwen-mm-plugins]] [[tech/free-coding-agents-2026]] [[ops/services/freellmapi]]
---

# qwen-tp

## Что это

**qwen-tp** — inference-провайдер в стеке Hermes: токен-план Alibaba (Aliyun MaaS, регион ap-southeast-1). Дополнение и fallback к основному opencode-go, не главный канал.

- **Base URL:** `token-plan.ap-southeast-1.maas.aliyuncs.com`
- **Моделей в плане:** ~14
- **Vision:** `qwen3.7-plus` — им Hermes делает `vision_analyze`
- **Дефолт:** `deepseek-v4-flash-0731` (голой `deepseek-v4-flash` в плане нет)

## Роль в стеке

- Основной канал: opencode-go (mimo-v2.6-flash). Цепочка fallback: `deepseek-v4-flash` → `qwen-tp` → `openrouter`.
- Локальный слой: Ollama (`bge-m3`, `qwen2.5:7b`) — см. [[ops/services/ollama]].

## Где упоминается

- [[tech/qwen-mm-plugins]] — `DASHSCOPE_BASE_URL` можно направить на этот endpoint (аудио-модели в qwen-tp есть)
- [[tech/free-coding-agents-2026]] — вердикт: наш inference уже закрывает задачу (opencode-go + qwen-tp + openrouter + freellmapi + self-hosted)
- [[tech/jev-jevrouter]] — JevRouter может маршрутизировать между opencode-go, qwen-tp и deepseek по сложности запроса
- [[tech/lfm25-vl-3b]] — vision LFM2.5-VL-3B как локальная альтернатива платному qwen3.7-plus через qwen-tp
