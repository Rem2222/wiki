---
description: "Needle 2 (Cactus Compute) — 14MB tool-calling модель для edge-устройств (смартфоны, Raspberry Pi, ~28MB RAM)."
tags: [llm,edge,on-device,tool-calling,small-model]
---

# needle-cactus

# Needle 2 (Cactus Compute)

> **Решение Романа (24.08.2026):** не ставить сейчас. Держать как кандидата **для умного дома на Raspberry Pi**, если заведёт — локально, офлайн, дешёво (14MB / ~28MB RAM). Для текущего function-calling у Романа используется локальный Qwen 2.5 7B на Ollama.

**Needle 2** — лёгкая базовую модель для tool-calling размером **14MB** для малых устройств (смартфоны, носимая электроника, Raspberry Pi $50). Дистилляция Gemini'овой инво|кации инструментов.

## Суть
Весь модельный бинарь — один файл ~14MB, полная сессия в ~28MB RAM. Фокус сугубо на tool invocation (агенты строятся на этом, крупные модели — overkill). Работает на edge: Raspberry Pi, Home Assistant, браузер (WASM).

- `pip install cactus-needle` — inference, LoRA fine-tune, экспорт.
- OpenAI-совместимая обёртка (`needle-openai`) — drop-in для любого OpenAI-клиента.
- Telemetry: на десктопе `prefill_tps` ~4300, `decode_tps` ~850, `peak_ram_mb` ~28.5, `confidence`.

## Варианты использования
- Home Assistant-агент полностью локально (`needle2-ha`)
- WASM-демо tool-calling (`needle-2-wasm-demo`)

## Репо
`iggue/cactus-compute-needle` (Python-пакет) / основная модель **Cactus Compute Needle 2**
