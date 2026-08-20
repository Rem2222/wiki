---
description: "Сравнение Hindsight vs MemOS (и EverOS) по критериям Романа: стабильность, сквозная память, многослойность, хуки vs нативный, бэкфилл, отзывы/форки. Решение по MUL-874: Hindsight."
tags: [memory, comparison, hindsight, memos, eeros, hermes, dsh, decision]
related: "[[tools/hermes-memory-comparison]] [[concepts/memory-retrieve-middleware]] [[tasks/hindsight-memory-migration]]"
status: decision
---

# Hindsight vs MemOS vs EverOS — решение по MUL-874

Дата: 20.08.2026. Задача: [[tasks/hindsight-memory-migration]] (MUL-874).

## Ключевая развилка

Роман рассматривал dsh (DeepSeek Harness) как **дополнительного агента на Windows**, основной — **Hermes на VPS**. Поэтому кандидат должен давать и Hermes-провайдер, и (желательно) dsh-интеграцию.

| Кандидат | Hermes-провайдер | dsh-плагин | ⭐/forks | Лицензия |
|---|---|---|---|---|
| **Hindsight** | ✅ штатный (`memory.provider: hindsight`, autoRecall/autoRetain) | ❌ нет нативного (свой плагин по EverOS-рецепту) | 20.7k/1563 | — (коммерч. behind) |
| **MemOS** | ✅ нативный адаптер (`adapters/hermes`, hooks) | ✅ нативный dsh-plugin | 10.8k/1000 | Apache-2.0 |
| **EverOS** | ❌ **нет Hermes-адаптера** | ✅ нативный (`@evermind-ai/dsh-plugin`) | 12.3k/899 | Apache-2.0 |

**EverOS отпадает** — нет Hermes-интеграции, основной агент у Романа — Hermes.

## Сравнение по 6 болям

| Боль | Hindsight | MemOS |
|---|---|---|
| 1. Стабильность | ✅ Postgres durable, без Node-в-памяти | 🟡 Node-ядро, но stdio-субпроцесс+SQLite (лучше agentmemory, но не Postgres) |
| 2. Разгрузка MD | 🟡 auto-retain, нет явного pre-compress | ✅ on_pre_compress hook (вытаскивает до компрессии) |
| 3. Единая точка | ✅ единый Postgres-центр | ✅ одно ядро для всех агентов |
| 4. Многослойность | 🔎 гибрид recall (4 стратегии) + reflect; см. отдельно | ✅ L1(traces)/L2(policies)/L3(world)+skills |
| 5. Авто-retrieve | ✅ autoRecall перед turn (штатный hook) | ✅ on_turn_start (самопальный bridge) |
| 6. Сквозная | ✅ Postgres-центр, все по сети | 🟡 локальное ядро, сквозная через MCP/HTTP |

## Хуки vs нативный инструмент

Роман отметил: самопальные хуки хуже нативного инструмента, и он прав.

- **Hindsight** — **штатный memory-провайдер Hermes**: авто через официальные pre_llm_call/post_llm_call hooks + SDK/MCP (recall/retain/reflect). Два слоя, интеграция нативная.
- **MemOS** — **самопальный bridge** (Node stdio-субпроцесс, `daemon_manager.py`), хуки жизни свои. Надёжнее agentmemory, но это собственная обвязка, а не штатный провайдер.

→ Для стабильности (вес 4) Hindsight надёжнее.

## Бэкфилл

- У обоих **готового импорта state.db нет** — пишем скрипт.
- Hindsight: `retain(bank, content, context, timestamp)` — «сам нарежет факты/уроки/таймлайн».
- MemOS: `memory.add`/`turn.end` — надо проверять авто-структуризацию.
- Сложность одинаковая.

## Отзывы / форки

- **Hindsight**: 20.7k⭐/1563 forks, max точность LongMemEval 91.4%, зрелый, push сегодня.
- **MemOS**: 10.8k⭐/1000 forks, LoCoMo 88.8 / LongMemEval 89.2, лидер OmniMemEval; бенчмарки в основном от самого проекта.

## Решение

**Hindsight** — остаётся выбором для Hermes (MUL-874):
- штатный нативный Hermes-провайдер (pre/post hooks из коробки+SDK/MCP),
- Postgres (стабильность + сквозная),
- лучшая точность,
- зрелое комьюнити (2× больше MemOS).

**Ключевое обоснование выбора — ориентация памяти (Роман, 20.08):**
- **Hindsight = семантическая память напарника** (факты → убеждения с доказательствами → mental models → knowledge pages; disposition traits = «характер» банка). Это про «кто ты для меня», модель живого собеседника/существа с историей.
- **MemOS = навыковая память** (L1 trace → L2 policy → L3 world → Skills с reward-backprop). Это про «как действовать / улучшать код».
- Для Романа навыки/процедуры уже живут в Multica-автопилотах и Hermes-skills — их не обязана давать память. Выбор → Hindsight (семантика напарника), а не MemOS (навыки).

MemOS сильнее по многослойности-поведению и встроенному dsh-плагину, но dsh у Романа вторичен; к Hindsight dsh-плагин накидывается по EverOS-рецепту (см. [[concepts/memory-retrieve-middleware]]).

## Сырые сессии при Hindsight (важно, Роман 20.08)

**Сырые сессии ≠ память провайдера.** Это разные слои:

| Слой | Где | Кто пишет |
|---|---|---|
| Сырые сессии (полный текст, tool-вызовы) | **Hermes state.db** (`~/.hermes/state.db`) + session-файлы Hermes | **Hermes всегда**, независимо от провайдера |
| Память провайдера (факты/убеждения/модели) | Hindsight → PostgreSQL | provider (retain/hooks) |

- Hindsight «focused on making agents that learn, not just remember» — `retain()` извлекает факты/сущности/связи, **не хранит дословную копию всего разговора**.
- **Точная дословная запись разговора = остаётся в Hermes state.db** навсегда. Смена провайдера НЕ влияет на это: Hermes всегда ведёт свой session-стор.
- Чтобы Hindsight имел полную историю для обучения — сырьё state.db заливается бэкфиллом (MUL-876) через `retain()` с реальными timestamp.

**ЖЁСТКИЙ запрет (hardline): state.db НЕ удалять и НЕ трогать никогда.** Это канон сырых сессий и архива. Удаление state.db = потеря точной записи всех разговоров. Только останавливать сервисы agentmemory/GBrain, данные не стирать (см. MUL-881).

## Связанные материалы

- EverOS dsh-плагин — эталон структуры dsh-плагина памяти (трёхфазный цикл Recall→Capture→Flush, Cordis patch). Открыт в `~/tmp/evos/examples/dsh`.
- MemOS Hermes-адаптер — `~/tmp/memos/apps/memos-local-plugin/adapters/hermes/`.
