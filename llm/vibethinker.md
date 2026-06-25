---
description: VibeThinker — семейство компактных reasoning-моделей (1.5B и 3B) от WeiboAI. Обходят DeepSeek R1 (671B) на математике при цене обучения $7,800. Техника Spectrum-to-Signal Principle (SSP).
tags: [llm, reasoning, vibe-thinker, weiboai, qwen, small-models, math, coding, gguf]
related: [llm/local-gemma-4-12b-setup, hardware/xe2690-workstation, tech/codex-cli-inference-optimization]
---

# VibeThinker (WeiboAI)

**GitHub:** [WeiboAI/VibeThinker](https://github.com/WeiboAI/VibeThinker)
**Hugging Face:** [WeiboAI](https://huggingface.co/WeiboAI)
**Лицензия:** MIT
**Звёзды:** ⭐ 1.4k | **Форков:** 102

## Что это

VibeThinker — семейство компактных reasoning-моделей от WeiboAI (微博AI). Доказывают, что **маленькие модели могут outperfom гигантов** на verifiable reasoning (математика, олимпиадное программирование) при стоимости обучения в десятки раз ниже.

Ключевое достижение: **VibeThinker-1.5B** (1.5 млрд параметров) обходит **DeepSeek R1** (671B, в 400× больше) на AIME24 — 80.3% против 79.8%.

## Модели

### VibeThinker-1.5B

| Характеристика | Значение |
|---------------|----------|
| Параметры | 1.5B |
| База | собственная архитектура |
| Пост-тренинг | Spectrum-to-Signal Principle (SSP) |
| Стоимость | **$7,800** |
| Релиз | Ноябрь 2025 |

**Бенчмарки:**
| Бенчмарк | VibeThinker-1.5B | DeepSeek R1 (671B) | MiniMax-M1 |
|----------|:-:|:-:|:-:|
| AIME24 | **80.3** | 79.8 | 80.7 |
| AIME25 | **74.4** | 70.0 | 70.0 |
| HMMT25 | **50.4** | 41.7 | 49.7 |

### VibeThinker-3B

| Характеристика | Значение |
|---------------|----------|
| Параметры | 3B |
| База | Qwen2.5-Coder-3B |
| Пост-тренинг | SSP v2: curriculum SFT + multi-domain RL + self-distillation + Instruct RL |
| Техника | **CLR** (Claim-Level Reliability Assessment) — test-time scaling |
| Релиз | Июнь 2026 |

**Бенчмарки:**
| Бенчмарк | VibeThinker-3B | +CLR | Примечание |
|----------|:-:|:-:|-----------|
| AIME26 | 94.3 | **97.1** | |
| HMMT25 | 89.3 | **95.4** | |
| LiveCodeBench v6 | 80.2 Pass@1 | — | |
| BruMO25 | — | **99.2** | |
| LeetCode acceptance (апр-май 2026) | 96.1% | — | | 

## Размеры моделей в квантизации

| Модель | Q4_K_M | Q8_0 | FP16 |
|--------|--------|------|------|
| **VibeThinker-1.5B** | **~0.9 GB** | ~1.6 GB | ~3 GB |
| **VibeThinker-3B** | **~1.8 GB** | ~3.2 GB | ~6 GB |

## Сравнение с Gemma Coding на XE2690

Конфигурация ПК Романа: Xeon E5-2690 v3, 64 GB DDR4 @ 2133, **GT 1030 (2 GB VRAM)** — инференс идёт через CPU.

| Модель | Размер (Q4) | RAM | CPU Speed | AIME | Легенда |
|--------|:-----------:|:---:|:---------:|:----:|---------|
| **Gemma 12B Q4** | 7.2 GB | DDR4 @ 2133 | ~1-2 tok/s* | ? | Generic coding, без спец. reasoning |
| **VibeThinker-3B Q4** | **1.8 GB** | DDR4 @ 2133 | **~4-6 tok/s*** | 94-97% | SOTA reasoning, можно на CPU |
| **VibeThinker-1.5B Q4** | **0.9 GB** | DDR4 @ 2133 | **~8-10 tok/s*** | 80% | Частично в L3 кеш |

*\* — примерные оценки на DDR4 @ 2133; реальные цифры зависят от количества слоёв в CPU и размера контекста.*

**Вывод:** VibeThinker-3B Q4 в **4 раза легче** Gemma 12B Q4, при этом показывает лучшие результаты на reasoning (94% vs неизвестно у Gemma). На том же CPU будет работать **в 2-4 раза быстрее** из-за меньшего объёма данных, прогоняемых через узкую DDR4 @ 2133.

## Методология: Spectrum-to-Signal Principle (SSP)

Двухстадийный пост-тренинг:

1. **SFT-фаза** — Two-Stage Diversity-Exploring Distillation
   - Генерация максимально разнообразных решений («спектр»)
   - Синтез данных + quality filtering + curriculum learning

2. **RL-фаза** — MaxEnt-Guided Policy Optimization (MGPO)
   - Усиление правильных сигналов
   - Multi-domain RL + offline self-distillation

**Стоимость обучения:** $7,800 vs $294K (DeepSeek R1) vs $535K (MiniMax-M1) — в **30-60 раз дешевле**.

## Запуск

### Требования
- `transformers>=4.54.0`
- Рекомендуется: `vLLM==0.10.1` или `SGLang>=0.4.9.post6`

### Параметры инференса
| Параметр | Значение |
|----------|----------|
| temperature | 0.6 или 1.0 |
| top_p | 0.95 |
| top_k | -1 (None в transformers) |
| max_new_tokens | до 40960 |

Для CPU-инференса на XE2690:
```bash
# Через llama.cpp
llama-cli -m VibeThinker-3B-Q4_K_M.gguf \
  -ngl 0 \           # без GPU (GT 1030 не поможет)
  -c 16384 \          # контекст 16K
  -b 512 \            # batch под CPU
  --temp 0.6 \
  --top-p 0.95
```

### Python (transformers)
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "WeiboAI/VibeThinker-3B",
    torch_dtype="bfloat16",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(
    "WeiboAI/VibeThinker-3B",
    trust_remote_code=True
)
```

## Ссылки
- [GitHub](https://github.com/WeiboAI/VibeThinker)
- [Hugging Face](https://huggingface.co/WeiboAI)
- [ModelScope](https://modelscope.cn/organization/WeiboAI)
- [Paper VibeThinker-1.5B (arxiv)](https://arxiv.org/abs/2511.06221)
- [Paper VibeThinker-3B (arxiv)](https://arxiv.org/abs/2606.16140)
