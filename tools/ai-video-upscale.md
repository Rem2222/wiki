---
type: concept
title: Ai Video Upscale
related: tools/chatcut
description: Обзор AI-моделей для повышения разрешения видео (VHS → HD/FHD/4K)
ingested_via: "'mcp:put_page'"
ingested_at: '2026-07-16T10:24:44.866Z'
source_kind: "'mcp:put_page'"
tags:
  - video-upscale ai esrgan vhs restoration
---

# AI Video Upscaling — Апскейл Видео

## Состояние на mid-2026

Качественный скачок произошёл: Qwen-Image-Edit и NVIDIA ChronoEdit подняли планку даже для сложных real-world случаев. VHS-оцифровку с битрейтом ~2-3 MBit/s и композитным шумом можно апскейлить до **Full HD** с хорошим результатом, до **4K** — с умеренным.

## Ключевые модели (открытые)

| Модель | Размер | Фичи |
|--------|--------|------|
| Qwen-Image-Edit-2511-Upscale2K | ~8B | Лучший для real-world, H100/H200 |
| Qwen-Image-Edit-2509-Upscale2K | ~3B | Легче, быстрее |
| nvidia/ChronoEdit-14B-Diffusers | 14B | SOTA по детализации |
| Real-ESRGAN | ~4M params | Классика, лёгкий, CPU-friendly |
| Real-CUGAN | ~1M params | Очень быстрый, чистый |

## Подходы к видео

### 1. Frame-by-frame (проще)
Каждый кадр — отдельное изображение. Проблема: temporal flickering (мельтешение).

### 2. With temporal smoothing (лучше)
- **BasicSR + STDF** — учитывает соседние кадры
- **Real-ESRGAN animevideo** — temporal-aware
- **Topaz Video AI** (коммерческий) — лучший temporal smoothing

### 3. Diffusion-based (новое)
- **Stable Video Diffusion** — upscale + temporal consistency
- **Qwen-Image-Edit video mode** — native video support

## Рекомендация для VHS → Full HD

```
1. Deinterlace (QTGMC в AviSynth / ffmpeg yadif)
2. Denoise (ffmpeg hqdn3d или BM3D)
3. Апскейл 4x (Real-ESRGAN или Qwen-Image-Edit)
4. Temporal smoothing (STDF или ffmpeg minterpolate)
```

**Best open-source pipeline:** Real-ESRGAN (frame-by-frame) + ffmpeg temporal smoothing.

**Best quality (GPU):** Qwen-Image-Edit-2511-Upscale2K (HF Space [есть](https://huggingface.co/spaces) / локально через transformers).

**Best quality overall:** Topaz Video AI (коммерческий, $299/год) — temporal smoothing на уровне SOTA.

## Практические тулы

- [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) — CLI, Python API
- [Waifu2x-Extension-GUI](https://github.com/AaronFeng753/Waifu2x-Extension-GUI) — GUI Win/Linux
- [Video2X](https://github.com/k4yt3x/video2x) — Waifu2x + Real-ESRGAN для видео
- [Flowframes](https://github.com/n00mk/flowframes) — интерполяция + апскейл (Windows)

Для VHS-лент: сначала **denoise**, потом **deinterlace**, потом **upscale**. Без первого шага апскейл поднимет и шум.
