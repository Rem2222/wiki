---
description: LFM2.5-VL-3B — лёгкая vision-language модель Liquid AI (3B, SigLIP2 NaFlex): GUI-агентность, grounding, OCR, 228 tok/s на M5 Max. Проверена по HF 12.08.2026.
tags: [vlm, vision, gui-agent, grounding, ocr, liquid-ai, edge, llm]
related: [[tech/qwen-tp]] [[tech/ollama-on-vps]]
---

# LFM2.5-VL-3B (Liquid AI)

## Что это

Лёгкая зрительно-языковая модель от Liquid AI для on-device: **3B параметров** (LFM2.5-2.6B текстовый backbone + **SigLIP2 NaFlex 400M** vision-энкодер). Ориентирована на агентные задачи с интерфейсами: читает экраны (мобильные/веб/десктоп), документы, изображения; точно привязывает объекты к координатам (grounding); OCR с layout-аннотациями.

**Проверено по Hugging Face (12.08.2026):**
- Репозиторий: https://huggingface.co/LiquidAI/LFM2.5-VL-3B
- 118 likes, обновлён 2026-08-12, 10 файлов (safetensors + tokenizer + chat_template)
- Контекст: 32 768 токенов, словарь 128k
- Языки: 16, включая русский
- Нативное разрешение: большие изображения → 512×512 патчи + миниатюра целиком

## Ключевые цифры

| Метрика | Значение |
|---|---|
| ScreenSpot-v2 | 80.7 (против 51.2 у Gemma-4-E4B) — из релиз-поста Liquid |
| Скорость (M5 Max) | 228 tok/s |
| Скорость (AMD Ryzen AI Max+ 395) | 116 tok/s |
| Память | <3.3 GB |
| Телефон (Galaxy S26 Ultra) | ~20 tok/s |

## Варианты весов

| Вариант | Назначение |
|---|---|
| Native (HF Transformers / vLLM / SGLang) | Файнтюнинг, серверный инференс |
| GGUF | CPU/llama.cpp, пониженная память |
| ONNX | Edge/мобильные, аппаратное ускорение |
| MLX 8-bit | Apple Silicon (mlx-vlm) |

## Применимость к нашему стеку

**Интересно, но пока не ставим (решение 12.08.2026 — «пока в вики»):**

- **Что даёт:** локальный GUI-агент (Desktop-автоматизация без облака — аналог computer_use на локальной модели), OCR без qwen-tp (экономия API-кредитов), ScreenSpot-задачи по интерфейсам (в т.ч. 1С-конфигуратор)
- **Ограничения:** GT 1030 2GB не тянет; Xeon E5-2690 CPU-only даст ~8-15 tok/s на GGUF-кванте — медленнее телефона, но для разовых «посмотри экран и кликни» хватает
- **Сейчас vision закрывает** qwen3.7-plus через qwen-tp (vision_analyze) — облако, платно, но быстро и без установки
- **Потенциальный сценарий:** если понадобится локальный vision без сети/кредитов — `ollama pull` GGUF (~2GB) или вручную

## Ссылки

- HF: https://huggingface.co/LiquidAI/LFM2.5-VL-3B
- GGUF: https://huggingface.co/LiquidAI/LFM2.5-VL-3B-GGUF
- Релиз-пост: https://www.liquid.ai/blog/lfm2-5-vl-3b
- Space (WebGPU демо): https://huggingface.co/spaces/LiquidAI/LFM2.5-VL-3B-WebGPU
