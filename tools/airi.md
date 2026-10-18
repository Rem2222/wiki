---
title: AIRI (Project AIRI) — self-hosted AI-вайфу / киберсущество (Neuro-sama своими руками)
type: tool
status: checked
tags: [ai-companion, ai-vtuber, neuro-sama, live2d, vrm, tts, stt, minecraft, factorio, self-hosted]
url: https://github.com/moeru-ai/airi
license: MIT
added: 2026-07-29
updated: 2026-10-17
---

# AIRI — «контейнер душ» AI-вайфу/VTuber (moeru-ai/airi)

Пересоздание **Neuro-sama** в open-source: «своё цифровое существо», которое живёт у тебя
и умеет говорить голосом, играть в игры и сидеть в чатах. Слоган авторов —
«self hosted, you-owned Grok Companion».

- **Стек:** TypeScript, Vue; WebGPU/WebAudio/Web Workers/Three.js; десктоп-версия
  (Electron, «stage-tamagotchi») умеет нативно **NVIDIA CUDA** и **Apple Metal**
- **Лицензия:** MIT · **⭐ 50 442**, форков 5 062, issue 237, пуш 17.10.2026
- **Релизы:** последний **v0.12.0-beta.5** (29.08.2026), стабильный v0.11.3 (18.07.2026);
  main активен — 76 коммитов за неделю
- Первое знакомство: 29.07.2026 (Роман просил инструкцию для Windows)

## Платформы и установка (Windows)

| Платформа | Как |
|---|---|
| **Windows** | `winget install MoeruAI.AIRI` · `scoop bucket add airi https://github.com/moeru-ai/airi` + `scoop install airi/airi` · или setup.exe из релизов (699 МБ, 19 470 загрузок — самый популярный ассет) |
| macOS | `brew install --cask airi`, dmg/zip (arm64/x64, ~875 МБ) |
| Linux | deb / rpm / flatpak (x64 и arm64, 565–815 МБ) |
| Web | airi.moeru.ai (браузер, PWA); мобильные — Android APK (197 МБ) и iOS .ipa |

## Что умеет (статус по roadmap, 17.10.2026)

- **Brain** ✓ — LLM через `xsai`: AIHubMix (рекомендуют), OpenRouter, vLLM, SGLang, Ollama,
  302.AI, OpenAI, Azure, Anthropic, DeepSeek, Qwen, Gemini, xAI, Groq, Mistral,
  Cloudflare Workers AI, Together, Fireworks, Novita, Zhipu, SiliconFlow, Stepfun, Baichuan,
  MiniMax, Moonshot, ModelScope, Player2, Tencent Cloud, **Xiaomi MiMo**
- **Игры:** Minecraft ✓, Factorio (WIP, есть PoC `airi-factorio`), Kerbal Space Program ✓,
  Helldivers 2 (WIP)
- **Чаты:** Telegram ✓, Discord ✓
- **Ears** ✓ — распознавание речи на клиенте, детект речи (VAD), аудио из браузера и Discord
- **Mouth** ✓ — много-провайдерный TTS: ElevenLabs, Azure Speech, OpenAI-совместимые,
  Alibaba Cloud Model Studio, локальный **Kokoro**
- **Body** ✓ — **VRM** и **Live2D** модели: анимации, автоблинк, автоповорот взгляда, idle-глаза
- **Память — ещё НЕТ** (☐ в roadmap; «Memory Alaya» — WIP). Локальная БД в браузере:
  DuckDB WASM / pglite ✓; чисто браузерная инференция на WebGPU — ☐

## Подпроекты (организация @proj-airi) — сами по себе полезны

- **`unspeech`** — универсальный прокси для `/audio/transcriptions` и `/audio/speech`
  («как LiteLLM, но для ASR и TTS») — сравнить с neuraldeep-путем
- **`mcp-launcher`** — «как Ollama для моделей», но для запуска MCP-серверов
- `webai-realtime-voice-chat` — полный пример реалтайм-голоса (VAD+STT+LLM+TTS)
- `airi-factorio` + `autorio`, `inventory` (каталог моделей), `demodel`, `xsai-transformers`,
  `drizzle-duckdb-wasm`, `hfup`

## Ограничения и предупреждения

- **Релиз — beta 0.12**, стабильная ветка 0.11.3; памяти пока нет — «характер» держится на промпте
- Размер дистрибутивов большой (0.6–0.9 ГБ — тянет рантаймы/модели)
- Авторы **прямо предупреждают: официальной крипты/токена у проекта НЕТ** (защита от скам-клонов)
- README содержит партнёрские ссылки (AIHubMix, 302.AI, SiliconFlow) — это доход проекта, не нейтральный выбор
- Windows-версия не проверялась нами; ставить — по команде
- Топик `openclaw` в репозитории есть, но явной интеграции в README не нашлось

**Статус: разобрано и записано, НЕ устанавливалось.** Кандидат на домашний ПК
(XE2690 — CPU-only Hermes; AIRI просит GPU для CUDA-режима, но есть Web/браузерный путь).