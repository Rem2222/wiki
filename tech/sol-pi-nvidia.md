---
description: SoL-Pi (NVIDIA) — автоматическое улучшение обвязки ИИ-агентов через рекурсивные auto-research циклы. −50% расход токенов без потери качества. 4 механизма: Action Fusion, ObservationPack, context compression, reduced reading.
tags: [ai, agent, harness, optimization, nvidia, cost-reduction, pi, token-saving]
related:
  - tech/jev-jevrouter
  - tech/ai-guardrails
  - tech/ternary-bonsai-2
---

# SoL-Pi (NVIDIA NVlabs)

## Что это

**SoL-Pi** — система, которая **автоматически улучшает обвязку (harness) ИИ-агентов** через рекурсивные циклы автоматических исследований. Вместо ручной оптимизации — агент сам ищет и проверяет механизмы экономии токенов.

Разработана NVIDIA Research. Код: [NVlabs/SoL-Pi](https://github.com/NVlabs/SoL-Pi).

## Как работает (высокий уровень)

```
┌─────────────────────────────────────────────┐
│         Auto-Research Loop                  │
│                                             │
│  Research AI ──► Предлагает механизмы       │
│       │                                     │
│       ▼                                     │
│  Фильтрация ──► Тестирование на задачах     │
│       │                                     │
│       ▼                                     │
│  Отбор ──► Только стабильные机制 попадают   │
│       │         в итоговую версию            │
│       ▼                                     │
│  Повтор (рекурсия) ──► Ещё лучшие机制       │
└─────────────────────────────────────────────┘
```

Research AI запускает циклы: предлагает механизмы → тестирует на реальных задачах → отбирает лучшие → повторяет. Итоговая версия содержит только механизмы, стабильно прошедшие отбор.

## 4 выживших механизма

### 1. Action Fusion (объединение действий)
Вместо нескольких отдельных вызовов инструментов — один объединённый. Меньше раундов общения с LLM = меньше токенов.

### 2. ObservationPack (сжатие наблюдений)
Результаты выполнения инструментов сжимаются прямо во время работы, а не передаются целиком. Сохраняется только релевантная часть.

### 3. Context Compression (сжатие контекста)
Уменьшение replay истории контекста. Агент не перечитывает всё заново — только ключевые доказательства.

### 4. Reduced Delegated Reading
Сокращение делегированного чтения файлов/документов с сохранением важных证据. Агент не читает файл целиком, а извлекает только нужное.

## Результаты

| Модель | Без SoL-Pi | С SoL-Pi | Экономия | Качество (EdgeBench) |
|--------|-----------|----------|----------|---------------------|
| **GPT-5.6 Sol** | $1,787 | $894 | **−50%** | 42 (baseline: 44.8) |
| **Claude Opus 5** | $2,535 | $1,158 | **−54%** | comparable |

Экономия $8.75–13.50/час против Codex/Claude Code, $4.36–5.71/час против базовой обвязки.

## Установка

### Как плагин для Pi
```bash
# From pi-extensions
pi install sol-pi
# или
npx pi extensions add sol-pi
```

### Как standalone
```bash
git clone https://github.com/NVlabs/SoL-Pi
cd SoL-Pi
# following README for setup
```

## Ссылки

- https://github.com/NVlabs/SoL-Pi — исходники
- https://arxiv.org/abs/2609.20519 — статья
- https://nvlabs.github.io/SoL-Pi/ — страница проекта
- https://github.com/HerbertGao/pi-extensions/tree/master/packages/sol-pi — Pi-плагин

## Релевантность

- **Pi**:可以直接 как extension
- **DSH/Hermes**: 4 механизма универсальны — Action Fusion и Context Compression можно адаптировать
- **Стоимость**: −50% расходов на API для coding agent задач
