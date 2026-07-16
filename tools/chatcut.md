---
type: concept
title: Chatcut
related: tools/ai-video-upscale
description: >-
  Agent-orchestrated video-editing studio — talking-head pipeline via Claude
  Code / Codex
ingested_via: 'mcp:put_page'
ingested_at: '2026-07-16T10:22:40.543Z'
source_kind: 'mcp:put_page'
tags:
  - video-editing ffmpeg ai-agent open-source talking-head
---

# chatcut — AI Video Editing Agent

**Репозиторий:** [ArtCog/chatcut](https://github.com/ArtCog/chatcut)
**Лицензия:** MIT
**Статус:** v0.1 (building in the open)

## Что это

chatcut — extensible, agent-orchestrated video-editing studio для **talking-head** контента (влоги, туториалы, обзоры). Сырой материал → одна команда → готовое видео через Claude Code или Codex.

## Pipeline

```
raw footage
  → normalize (clean CFR) — без desync
  → transcribe (word-level) — faster-whisper локально / ElevenLabs опционально
  → detect stumbles & pauses
  → cut-plan (человек утверждает)
  → cut (EDL, padded by cut type)
  → subtitles (SRT build+burn)
  → motion graphics (hyperframes)
  → color (LUT3D)
  → render (NVENC/libx264/VideoToolbox/QSV)
```

## Фичи

- **Без API-ключей** — локальный faster-whisper по умолчанию
- **Плагинная система** — tool registry, новые инструменты без правки ядра
- **Проверка результата** — не тупо склеивает, а проверяет корректность (no frozen frames, no A/V desync)
- **Cross-platform encode** — NVENC при наличии, fallback на CPU

## Установка

```bash
git clone https://github.com/ArtCog/chatcut && cd chatcut
./setup.sh              # Linux/macOS
./setup.ps1             # Windows
chatcut tools           # список возможностей
chatcut edit raw.mp4    # запуск pipeline
```

## Зависимости

- [video-use](https://github.com/browser-use/video-use)
- [hyperframes](https://github.com/heygen-com/hyperframes)
- [auto-editor](https://github.com/WyattBlue/auto-editor)
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- ffmpeg

## Требования

- Python 3.10+
- ffmpeg
- 8+ GB RAM для faster-whisper large
- GPU опционально (NVENC для encode)
