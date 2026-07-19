---
type: concept
title: Self Improving Agent Theory
ingested_via: 'mcp:put_page'
ingested_at: '2026-07-18T23:24:18.322Z'
source_kind: 'mcp:put_page'
---

---
title: Self-Improving Agent — теория и фреймворк
description: Разбор survey «Self-Improvements in Modern Agentic Systems» (arXiv:2607.13104, Jul 2026, Schmidhuber et al.). Формальная модель агента, Gödel Machine, Full Scaffolding, Curiosity-driven exploration и проактивность.
tags: [ai, agents, self-improvement, theory, survey, schmidhuber, godel-machine]
related: [[tech/proactive-agent-decision]], [[concepts/llm-tier-strategy]]
---

# Self-Improving Agent — Теория и Фреймворк

**Источник:** Survey «Self-Improvements in Modern Agentic Systems» (arXiv:2607.13104, 14 Jul 2026, 97 стр., Schmidhuber в соавторах)  
**Проект:** [github.com/Self-Improving-Agents](https://github.com/Self-Improving-Agents)

---

## Формальная модель агента

Агент — это конфигурация, соединяющая foundation model со *scaffold'ом*:

```
𝒜ₜ = (θₜ, Σₜ)
      ↑     ↑
    модель   scaffold (всё остальное)
```

Где scaffold раскладывается на четыре компонента:

```
Σₜ = (pₜ, mₜ, 𝒯ₜ, gₜ)
      промпт  память  тулы  control logic
```

**Ключевой insight:** self-improvement — это **самостоятельный** оператор обновления, который может менять либо θ (параметры модели), либо Σ (scaffold).

---

## Два пути самоулучшения

| Путь | Что меняется | Скорость | Стабильность | Примеры |
|------|-------------|----------|-------------|---------|
| **Foundation Model Improvement** | θ — веса модели | медленно | стабильно (но неоткатываемо) | Fine-tune, RLHF, DPO, смена модели |
| **Scaffolding Improvement** | Σ — промпты, память, тулы, логика | быстро | обратимо (easy rollback) | Скиллы, memory, новые инструменты, GSD |

**Симметрия:** плохой промпт легко откатить. Регресс, впитанный в веса — практически не отследить.

---

## Gödel Machine — теоретический идеал

Schmidhuber (2003): **полностью самореферентная, самоулучшающаяся машина**.

Свойства:
1. **Single-life RL** — живёт одну непрерывную жизнь, не сбрасывается между эпизодами
2. **Сама генерирует кандидатов** на изменение — не ждёт внешнего сигнала
3. **Доказывает оптимальность** — применяет изменение только если есть формальное доказательство, что оно улучшит ожидаемую сумму будущих наград
4. **Полная самореференция** — может менять даже собственную систему доказательств и генератор изменений

**Ограничение:** невычислима на практике (требует формального доказательства каждого изменения).
**Практические наследники:** Gödel Agent (Yin 2025c, monkey patching), Darwin Gödel Machine (Zhang 2026c, архивная эволюция), Huxley-Gödel Machine (Wang 2026a, метрика clade-level metaproductivity).

---

## Full Scaffolding Improvement (раздел 6.4)

Самая глубокая форма изменения — агент меняет собственный код и операционную логику:

```
Σₜ₊₁ = ℐ_Σₜ(Σₜ; 𝒮ₜ)
       improver      learning signal
       (сам является   (execution traces,
        частью Σₜ!)     critiques, tests)
```

**Особенность:** improver ℐ — не внешний оптимизатор, а часть текущего scaffold'а, и он эволюционирует вместе с агентом. Формально:

```
⟨Σ̃ₜ₊₁⟩ = exec(⟨Σₜ⟩; 𝒮ₜ)
Σₜ₊₁ = Σₜ ⊕ Δₜ   (применение патча)

Финальный шаг — верификация:
Σₜ₊₁ = { Σ̃ₜ₊₁, если 𝒱(Σ̃ₜ₊₁)=1
       { Σₜ,   иначе
```

**Практические системы:**
- **Gödel Agent** (Yin 2025c) — monkey-patching своего Python-кода, self-awareness + self-modification
- **Self-Taught Optimizer** (Zelikman 2024) — LM генерирует кандидатов улучшения своего же кода, выбирает лучший
- **Live-SWE-Agent** (Xia 2025) — эволюционирует на лету в runtime
- **Darwin Gödel Machine** — открытая эволюция, архив агентов, дерево видов
- **Agent Symbolic Learning** (Ou 2025) — «символическая сеть» с natural-language backprop

---

## Curiosity-Driven Exploration (будущее направление #2)

Из раздела 9.2 (Future Directions):

> Self-improving agents should **autonomously seek out valuable experiences** rather than passively accepting human-curated tasks. In sparse feedback domains, agents can improve sample efficiency by assigning **intrinsic value to interactions with high prediction errors or verifier disagreement**.

Внутренняя мотивация — агент сам решает, что исследовать:
- «Это я плохо предсказываю → надо разобраться»
- «Этот инструмент давно не пробовал → попробую»
- «Verifier не уверен → проверю»

В этом — ключевое отличие от cron-задач:

| | Cron / расписание | Проактивный агент |
|---|---|---|
| Кто ставит цель | Человек | Агент сам (intrinsic motivation) |
| Когда запускается | По расписанию | Когда видит возможность или проблему |
| Что делает | Фиксированный скрипт | Исследует, пробует, решает |
| Механизм | Внешний планировщик | Внутренний drive (curiosity, prediction error) |
| Адаптация | Нет — всегда одно и то же | Эволюционирует со временем |

---

## Практические выводы для нашей архитектуры

**Что уже есть:**
- **Scaffolding improvement:** Hermes-скиллы + память (MEMORY.md/USER.md) + cron — это быстрый цикл Σ
- **Foundation model improvement:** стратегия тиров (Flash→Pro→Reasoning) — это выбор θ
- **Memory-based improvement:** GBrain + wiki — это mₜ

**Чего не хватает для проактивности:**
1. **Внутренний drive** — intrinsic reward mechanism, который генерирует цели, а не ждёт команды
2. **Self-referential loop** — агент, который анализирует свою эффективность и сам решает, что улучшить
3. **Full scaffolding** — возможность менять собственную control logic gₜ (сейчас gₜ = «жди человека + cron»)

---

## Источники

- Ren et al., «Self-Improvements in Modern Agentic Systems: A Survey», arXiv:2607.13104, Jul 2026
- Schmidhuber, «Gödel Machines: Fully Self-Referential Optimal Self-Improving Machines», 2003
- Yin et al., «Gödel Agent: A Self-Referential Agent Framework», 2025c
- Zhang et al., «Darwin Gödel Machine», 2026c
- Zelikman et al., «Self-Taught Optimizer», 2024
