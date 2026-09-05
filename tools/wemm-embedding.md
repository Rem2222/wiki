---
title: WeMM-Embedding
created: 2026-09-05
status: reference
tags: [embedding, multimodal, tencent, wechat, ai]
related:
  - [[ops/services/gbrain]]
  - [[ops/services/openviking]]
---

# WeMM-Embedding

Мультимодальная модель эмбеддингов от Tencent (WeChat Vision team). Обрабатывает текст, изображения, видео и документы. Apache 2.0.

## Модели

| Размер | Матрёшка dim | MMEB-v2 | HuggingFace |
|--------|-------------|---------|-------------|
| **2B** | 64, 128, **256**, 512, 1024, 2048 | **77.9** | [tencent/WeMM-Embedding-2B](https://huggingface.co/tencent/WeMM-Embedding-2B) |
| **4B** | 64, 128, 256, 512, 1024, 2560 | 79.2 | [tencent/WeMM-Embedding-4B](https://huggingface.co/tencent/WeMM-Embedding-4B) |
| **9B** | 64, 128, 256, 512, 1024, 2048, 4096 | **80.6** (SOTA) | [tencent/WeMM-Embedding-9B](https://huggingface.co/tencent/WeMM-Embedding-9B) |

## Ключевые особенности

- **Matryoshka embeddings** — размерность 64 → 2048 без переобучения
- **Мультимодальность** — текст + изображения + видео + визуальные документы
- **256 dim = 98.7%** от полного качества (2B модель)
- **1 млрд запросов/день** внутри Weixin (production-grade)
- **Сервер:** vLLM 0.27.0 или SGLang 0.5.9

## Установка

```bash
pip install -r requirements.txt  # transformers==5.2.0
```

## Инференс

```bash
# Transformers
python examples/transformers_inference.py \
  --model tencent/WeMM-Embedding-2B \
  --image photo.jpg \
  --dimension 2048

# Sentence Transformers
python examples/sentence_transformers_inference.py \
  --model tencent/WeMM-Embedding-2B \
  --dimension 2048
```

## Сравнение с bge-m3

| | bge-m3 | WeMM-Embedding-2B |
|---|---|---|
| Размер | 1.14 GB | ~4 GB |
| Dim | 1024 | 64-2048 (настраиваемая) |
| Мультимодальность | ❌ только текст | ✅ текст + видео + изображения |
| Мультимодальный SOTA | нет | MMEB-v2 #1 (77.9) |
| Ресурсы VPS | ~0 GB RAM (on-demand) | ~4 GB RAM |
| Годен для GBrain/OpenViking | ✅ сейчас | ✅ когда появится GPU или больше RAM |

## Ссылки

- GitHub: https://github.com/Tencent/WeMM-Embedding
- Paper: https://arxiv.org/abs/2608.24053
- HuggingFace: https://huggingface.co/collections/tencent/wemm-embedding

## Статус для VPS

**Пока НЕ ставить** — bge-m3 компактнее (1.14 GB vs 4 GB) и работает на CPU. WeMM-Embedding-2B — кандидат на замену при:
- Увеличении RAM до 16+ GB
- Нужде мультимодальности (изображения, видео)
- Требовании регулируемой размерности (64 для быстрого поиска)
