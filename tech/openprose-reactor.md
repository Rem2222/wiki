---
description: OpenProse — декларативный язык для AI-сессий (Markdown-контракты *.prose.md). Reactor — runtime, который удерживает мир в этом состоянии. Новая парадигма для AI-агентов: «cost scales with surprise, not wall-clock time».
tags: [tech, ai-agents, declarative, reactor, mcp]
related: [[concepts/rag]] [[concepts/mcp]] [[tech/hermes-agent-masterclass]] [[tech/openmanus]] [[tech/rag-projects-summary]]
---

# OpenProse / Reactor

**Репозиторий:** [openprose/prose](https://github.com/openprose/prose)  
**Автор:** Организация OpenProse | **Лицензия:** MIT  
**Звёзд:** 1.5k ★ | **Форков:** 110 | **Коммитов:** 240 | **Веток:** 73 | **Тегов:** 37  
**Пакеты (npm):** `@openprose/reactor` 0.3.1, `@openprose/reactor-cli` 0.2.2, `@openprose/reactor-devtools` 0.2.0

---

## Что это

Два слоя:

### OpenProse — декларативный язык
Вместо последовательности инструкций для LLM вы описываете **идеальное состояние мира** в структурированных Markdown-контрактах (`*.prose.md`). Это тот же паттерн, что SQL/Terraform/Kubernetes/React: вы декларируете желаемое состояние, а система сама приводит реальность к этому состоянию.

Файл контракта содержит:
- `### Maintains` — схема мира: какие поля этот узел держит актуальными, какие фасеты, постусловия
- `### Requires` — подписка на выходы других узлов (Forme связывает граф автоматически)
- `### Continuity` — источник пробуждения: входные данные, таймер, внешний триггер

### Reactor — runtime
Хранит и удерживает объявленное состояние. Собирает все `.prose.md` в DAG (через Forme — автоматический wiring), мемоизирует LLM-сессии на уровне узлов.

**Ключевая идея:**
> **Inference cost scales with surprise, not wall-clock time**  
> За LLM вы платите только когда что-то в мире реально изменилось, а не за время работы агента.

---

## Архитектура (React-метафора)

| React | Reactor |
|-------|---------|
| Component | **Responsibility** — объявленная цель |
| DOM | **World-model** — истина на диске |
| `render()` | **LLM-сессия**, вычисляющая новое состояние мира |
| props | Подписки на выходы других узлов |
| `React.memo` | Пропуск LLM-вызова, если входы не изменились |
| Ручной wiring | **Forme** — граф собирается автоматически из контрактов |

Intelligence заморожена на этапе компиляции (каноникализатор, Forme-диагностика, постусловия). Reconciler во время работы — намеренно детерминированный и тупой.

---

## Быстрый старт

**Keyless replay (60 секунд, без API-ключа, без трат):**
```bash
npx -p @openprose/reactor-devtools reactor-devtools --example masked-relay --describe
```

Вывод:
```
dispositions  rendered=46 · skipped=31 · failed=0
surprise-cause  external=8 · input=69
COST ROLLUP  fresh=27180 tokens · reused=12840 tokens · reuse=32%
```

**Локальный проект:**
```bash
npm install @openprose/reactor @openprose/reactor-cli @openprose/reactor-devtools
reactor init my-project
reactor doctor     # проверка окружения
reactor compile    # Forme — компиляция графа
reactor serve      # запуск
```

---

## Примеры (13 штук с keyless replay)

| Пример | Суть |
|--------|------|
| `surprise-cost` | мемоизация + пробуждение при изменении мемо-ключа |
| `renewal-risk` | переоценка только изменившихся счетов (SaaS) |
| `inbox-triage` | diamond fan-in + изоляция ошибок |
| `monorepo-ci` | fan-out + защита merge gate |
| `masked-relay` | peer-blind fan-out с маскированными проекциями |
| `tamper-forge` | атака на receipt + chain-verify ловит (или нет) |

---

## SDK

```ts
import { reactor } from "@openprose/reactor";

const { reactor: r } = await reactor("./my-project", { directory: "./state" });
console.log(r.ledger.all().length);
await r.ingest("source", { wake: { source: "external", refs: [] } });
```

Поверхность API: `.` (фасад), `/agents` (провайдеры LLM), `/adapters` (record/replay), `/internals` (ядро).

---

## Ограничения (честно от авторов)

- Receipt-ы **tamper-evident**, но не tamper-proof: нет криптографической подписи
- Нет timestamp и principal в receipt-ах — это не audit log
- Signer caveat: не привязан к артефактам world-model байт-в-байт
- Всё ещё v0.3 — молодой проект
- Зависимости: `@openai/agents`, `zod` ~99 MB / ~100 пакетов

---

## Relevance

Прямая релевантность к задачам Романа:
1. **Декларативный подход** вместо императивных агентов (как Hermes Agent / JAWL / OpenClaw) — альтернативная парадигма
2. **MCP-интеграция** — Reactor совместим с любым Prose-Complete хостом, можно подключить к Hermes
3. **Receipt-ы и аудит** — content-addressed логи решений, применимо к Multica Autopilot
4. **SDD-параллель** — как OpenSpec/SDD, но для AI runtime, не для разработки

Стоит перепроверить через неделю-две — проект быстро развивается (последний коммит 6 часов назад).
