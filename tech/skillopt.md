---
description: Фреймворк от Microsoft Research для оптимизации skill-документов LLM-агентов через итеративный тренировочный цикл (ReflACT)
tags: [microsoft, research, llm, agents, optimization, skills]
related: [[tech/agents-best-practices]]
source: https://github.com/microsoft/SkillOpt
arxiv: https://arxiv.org/abs/2605.23904
license: MIT
created: 2026-05-27
updated: 2026-05-27
---

# SkillOpt

Фреймворк от **Microsoft Research** для оптимизации skill-документов агентов через итеративный цикл, вдохновлённый обучением нейросетей. **«Тренируй навыки агента так же, как нейросеть — с эпохами, батчами, learning rate и валидацией, но без изменения весов модели.»**

Python 3.10+, MIT.

## Архитектура

### Два типа моделей
- **Target Model** — исполняющая LLM, решает задачи с текущим skill-документом как system prompt
- **Optimizer Model** — «тренер» (обычно более мощная LLM), анализирует траектории и генерирует правки

Бэкенды: Azure OpenAI, OpenAI, Anthropic Claude, Qwen (локальный через vLLM)

### Шестистадийный пайплайн ReflACT

| Стадия | DL-аналог | Что происходит |
|--------|-----------|----------------|
| **① Rollout** | Forward pass | Target решает задачи с текущим skill |
| **② Reflect** | Backpropagation | Optimator анализирует траектории, генерирует edit-патчи |
| **③ Aggregate** | Gradient accumulation | Параллельная иерархическая склейка семантически похожих патчей |
| **④ Select** | Gradient clipping | LLM ранжирует правки, оставляет top-L (L = learning rate) |
| **⑤ Update** | Parameter update | Применяет отобранные правки к skill-документу |
| **⑥ Gate** | Validation check | Валидация кандидата, accept/reject |

### Epoch-level механизмы
- **Slow Update (Momentum)** — защита от catastrophic forgetting через продольное сравнение rollout'ов
- **Meta Skill (Meta-learning)** — память оптимизатора: стратегические заметки между эпохами

## Режимы обновления

- `patch` — классические edit-патчи (append, insert_after, replace, delete)
- `rewrite_from_suggestions` — рекомендации → переписывание скилла
- `full_rewrite_minibatch` — полная замена skill-документа

## Поддерживаемые бенчмарки

SearchQA (+23% → 35.94%), ALFWorld (+28.6% → 70.82%), DocVQA (+17.8% → 82.18%), LiveMathematicianBench (+8% → 61.5%), SpreadsheetBench (+14.1% → 43.62%), OfficeQA

## Структура репозитория

```
SkillOpt/
├── configs/          # YAML-конфиги с наследованием
├── skillopt/         # engine/, model/, envs/, gradient/, optimizer/, evaluation/
├── scripts/          # train.py, eval_only.py
├── skillopt_webui/   # Gradio мониторинг
└── docs/             # MkDocs документация
```
