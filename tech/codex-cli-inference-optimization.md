---
description: Лайфхак — скормить Codex CLI (или любой agent) детальный бенчмарк-гайд, чтобы он сам подобрал оптимальную конфигурацию инференса (quant, KV cache, batch, context) под железо и модель. Основано на статье Ахмеда про Qwen 3.5-9B на RTX 3070 8GB.
tags: [llm, inference, optimization, codex, benchmarking, llama.cpp, gguf, quantization]
related: [llm/local-gemma-4-12b-setup, hardware/xe2690-workstation]
---

# Оптимизация локального инференса LLM через Codex CLI

Лайфхак: скормить Codex CLI (или Claude Code, OpenCode, любого AI-агента) детальный бенчмарк-гайд по инференсу — и он сам подберёт оптимальную конфигурацию под твоё железо: квант KV cache, размер батча, ubatch, контекст, флаги llama.cpp.

## Исходные данные (из статьи Ахмеда)

**Сетап:**
- Модель: `QWEN3.5-9B UD-IQ3_XXS`
- Железо: VM 503, **NVIDIA RTX 3070 8GB**, драйвер 595.58.03, CUDA 13.2
- Бэкенд: `llama.cpp 0033f53`, порт 8001

### RUN SUMMARY — итерации тестов

| RUN | PHASE | STATUS | KV | CTX | BATCH/UB | PEAK MiB | TOK/S | NOTES |
|-----|-------|--------|----|-----|----------|----------|-------|-------|
| 082229Z | Initial | failed | — | — | — | — | — | Prompt overflow / 400s timeout |
| 082331Z | Broad | stable | q4_1 | 131072 | 6144/1024 | 5945 | 54.00 | First full successful sweep |
| 083206Z | Expanded | partial | q8_0 | 196608 | probe | — | — | Found q8_0 upper limit, OOM@212992 |
| 085018Z | Shortlist | stable | q8_0 | 180224 | 8192/1024 | 7825 | 54.45 | Production profile |

### FINAL SHORTLIST — все протестированные конфиги

| KV | CTX | BATCH/UB | STATUS | PEAK MiB | TOK/S | TAKEAWAY |
|----|-----|----------|--------|----------|-------|----------|
| q8_0 | 196608 | 4096/512 | stable | 7573 | 54.16 | Highest stable q8_0 context |
| q8_0 | 196608 | 4096/1024 | failed | 3567* | — | Startup failure (batch size) |
| **q8_0** | **180224** | **8192/1024** | **stable** | **7825** | **54.45** | **Selected production winner** |
| q8_0 | 180224 | 8192/1536 | failed | 3567* | — | Startup failure (ubatch oversize) |
| q4_1 | 262144 | 2048/512 | stable | 7061 | 54.15 | Max stable context for q4_1 |
| q4_1 | 262144 | 4096/512 | stable | 7061 | 53.91 | Same VRAM, slightly slower |
| q4_1 | 262144 | 4096/1024 | failed | 7837* | — | Near-limit, unstable |
| q4_1 | 262144 | 6144/1024 | failed | 7837* | — | Near-limit, unstable |
| q4_1 | 229376 | 8192/1024 | stable | 7363 | 54.20 | Larger context, lower peak VRAM |

*\* — sampled VRAM before crash, не валидно для production.*

### SELECTED PRODUCTION PROFILE

| KV | CTX | BATCH/UB | PEAK MiB | TOK/S | NOTE |
|----|-----|----------|----------|-------|------|
| **q8_0** | **180224** | **8192/1024** | **7825** | **54.45** | Thinking on, stable live |

## Суть лайфхака

Вместо того чтобы вручную перебирать все комбинации флагов llama.cpp (quant, контекст, batch, ubatch, KV cache offload, и т.д.):

1. Берёшь статью/бенчмарк с детальными цифрами (как у Ахмеда)
2. Скармливаешь её Codex CLI (или Claude Code, OpenCode, Hermes Agent) с промптом:
   > «Определи подходящий inference engine под моё железо, настрой проект через uv + venv, подбери kernels, flags, batching, KVCache, оптимизируй запуск под мою модель»
3. Агент сам анализирует железо, модель, бенчмарк-данные и подбирает оптимальную конфигурацию

## Ключевые параметры для оптимизации

| Параметр | Что даёт | Типичный диапазон |
|----------|----------|-------------------|
| `-ctk / -ctv` (KV cache type) | Качество vs VRAM | q4_1 (эконом) → q8_0 (качество) |
| `-c / --ctx-size` | Длина контекста | 131072 — 262144 |
| `-b / --batch-size` | Пропускная способность | 2048 — 8192 |
| `--ubatch-size` | Стабильность, влияет на startup | 512 — 1536 |
| `-ngl / --n-gpu-layers` | Offload слоёв на GPU | 99 (максимум) |
| `--no-kv-offload` | KV cache на GPU vs CPU | offload = быстрее, но больше VRAM |

## Выводы для RTX 3070 8GB с Qwen 3.5-9B IQ3_XXS

- **q8_0 KV cache** даёт 54 tok/s при 180K контекста — этого достаточно для большинства задач
- **q4_1 KV cache** позволяет расширить контекст до 262K, но скорость та же (~54 tok/s) или чуть ниже
- Batch 8192/1024 — оптимум для этого сетапа
- На 8GB VRAM упор в 7825/8192 MiB — запас минимальный
- Итог: **54 tok/s — это production-ready скорость** для coding agent задач
