---
type: concept
title: OpenProse / Reactor
description: OpenProse — декларативный язык для AI-сессий (Markdown-контракты *.prose.md). Reactor — runtime, который удерживает мир в этом состоянии. Новая парадигма для AI-агентов: «cost scales with surprise, not wall-clock time». С примерами кода, SDK, контрактами и сценариями для своей инфраструктуры.
tags: [tech, ai-agents, declarative, reactor, mcp]
related: [[concepts/rag]], [[concepts/mcp]], [[tech/hermes-agent-masterclass]], [[tech/openmanus]], [[tech/rag-projects-summary]]
---

# OpenProse / Reactor

**Репозиторий:** [openprose/prose](https://github.com/openprose/prose)  
**Автор:** Организация OpenProse | **Лицензия:** MIT  
**Звёзд:** 1530 ★ (+30 за неделю) | **Форков:** 120 (+10) | **Коммитов:** ~250 | **Веток:** много активных | **Тегов:** 37+  
**Последний push:** 2026-06-14 (вчера)  
**Последний релиз:** skill-v0.15.0 (2026-06-04)  
**Пакеты (npm):** `@openprose/reactor` 0.3.1, `@openprose/reactor-cli` 0.2.2, `@openprose/reactor-devtools` 0.2.0  
**Открытых issues:** 31 (закрытых — 0 за всю историю)

---

## Что это

Два слоя:

### OpenProse — декларативный язык
Вместо последовательности инструкций для LLM вы описываете **идеальное состояние мира** в структурированных Markdown-контрактах (`*.prose.md`). Это тот же паттерн, что SQL/Terraform/Kubernetes/React: вы декларируете желаемое состояние, а система сама приводит реальность к этому состоянию.

### Reactor — runtime
Хранит и удерживает объявленное состояние. Собирает все `.prose.md` в DAG (через Forme — автоматический wiring), мемоизирует LLM-сессии на уровне узлов.

**Ключевая идея:**
> **Inference cost scales with surprise, not wall-clock time**  
> За LLM вы платите только когда что-то в мире реально изменилось, а не за время работы агента.

---

## Быстрый старт (CLI)

**Keyless replay (60 секунд, без API-ключа, без трат):**
```bash
npx -p @openprose/reactor-devtools reactor-devtools --example masked-relay --describe
```
```
dispositions  rendered=46 · skipped=31 · failed=0
surprise-cause  external=8 · input=69
COST ROLLUP  fresh=27180 tokens · reused=12840 tokens · reuse=32%
```

**Локальный проект:**
```bash
npm install @openprose/reactor @openprose/reactor-cli @openprose/reactor-devtools
reactor init my-project
cd my-project
reactor doctor        # проверка окружения
reactor compile       # Forme — компиляция графа
reactor serve --http 8080  # запуск с HTTP gateway
```

---

## Контракты (*.prose.md)

Это то, что вы реально пишете. Три вида узлов:

### 1. Gateway — точка входа

```markdown
---
name: signals
kind: gateway
---

# Signals

> Входные сигналы из внешнего мира. Не имеет Requires (данные приходят извне).

### Continuity: external-driven

Вебхук, poll, ручной триггер — gateway превращает это в нормализованную истину.

### Maintains
Какое поле узел держит актуальным:
- `headline`: последнее внешнее событие (строка)
- `epoch`: монотонный номер обновления (число)

Фасетов нет — весь truth экспортируется как единый ATOMIC_FACET.
Постусловия перед подписанием receipt: headline непустая, epoch > 0.
```

**Механика:** Gateway — entry point DAG. Когда вы `ingest()` в него данные, Reactor фингерпринтит новое состояние. Если байт-в-байт не изменилось — memo-skip, downstream не пробуждается.

### 2. Responsibility — узел DAG (основной тип)

```markdown
---
name: digest
kind: responsibility
---

# Digest

> Стоячая цель: пересказывать signals.headline только когда он изменился.

### Requires
- Узел `signals`, фасет `ATOMIC_FACET`

### Maintains
- `brief`: пересказ headline (строка)
- `source_epoch`: эпоха, на которой сделан пересказ (число)

Постусловия:
- brief содержит актуальный headline
- source_epoch совпадает с epoch из signals

### Continuity: input-driven

Просыпается только когда изменился subscribed input (сигнал).
Если входа нет — skip, fresh tokens = 0.

### Execution
1. Прочитать upstream signals по ссылке (headline, epoch)
2. Вызвать stateless render-digest-line(headline, epoch) через `call`
3. Записать { brief, source_epoch } как новую истину
```

### 3. Function — stateless helper

```markdown
---
name: render-digest-line
kind: function
---

# Render Digest Line

> Чистая функция, без world-model и wake-источника.

### Parameters
- `headline`: строка
- `epoch`: число

### Returns
- `brief`: `"digest: {headline}"`
- `source_epoch`: переданный epoch
```

---

## Архитектура (React-метафора)

| React | Reactor |
|-------|---------|
| Component | **Responsibility** — объявленная цель |
| DOM | **World-model** — истина на диске |
| `render()` | **LLM-сессия**, вычисляющая новое состояние мира |
| props | Подписки на выходы других узлов (Requires) |
| `React.memo` | Пропуск LLM-вызова, если входы не изменились |
| Ручной wiring | **Forme** — граф собирается автоматически из контрактов |
| useState | **Maintains** — поддерживаемое поле truth |
| prop drilling | **Facets** — подписываемые части truth-а |

Intelligence заморожена на этапе компиляции (каноникализатор, Forme-диагностика, постусловия). Reconciler во время работы — намеренно детерминированный и тупой: сравнил фингерпринты → пропустил / запустил.

---

## SDK — интеграция в свой проект

Установка:
```bash
npm install @openprose/reactor
# Для live-рендера (опционально):
npm install @openai/agents zod
```

### Фасад `reactor()` — один вызов до рабочего Reactor

```ts
import { reactor } from "@openprose/reactor";

// Компиляция + сборка + boot (cold-start рендер)
const { reactor: r } = await reactor("./my-project", {
  directory: "./state"  // world-model + receipt-ledger
});

// Читаем трейл решений
console.log(r.ledger.all().length);      // все receipt-ы
console.log(r.store.publishedFingerprints("source"));

// Инжектим внешнее событие
await r.ingest("source", {
  wake: { source: "external", refs: [] }
});

// Dry-run / keyless (без LLM)
const { reactor: r2 } = await reactor("./my-project", {
  mode: "inspect"
});
```

### Верификация receipt-ов

```ts
import { verifyReceipt, verifyReceiptChain } from "@openprose/reactor";
import {
  inspectReceiptProof,
  projectReceiptProof,
  type LedgerReceipt,
  type ReceiptProofInspection,
} from "@openprose/reactor/internals";

// Проверка одного receipt
const proof = verifyReceipt(receipt);
if (!proof.ok) throw new Error(proof.errors.join("; "));

// Верификация всей цепочки
const chainOk = verifyReceiptChain(r.ledger.all());

// Публичное доказательство (без приватных полей)
function publicEvidence(proof: ReceiptProofInspection) {
  const result = projectReceiptProof({ tier: "public", proof });
  return result.ok ? result.projection : null;
}
```

### Полный контроль — `createReactor`

```ts
import { createReactor, fileSystemSubstrate } from "@openprose/reactor";

const { reactor: r } = await createReactor({
  directory: "./state",
  substrate: fileSystemSubstrate({ directory: "./state" }),
  mounts: [
    {
      node: "signals",
      mount: { render: { model: "gpt-4o", temperature: 0 } }
    }
  ],
  asyncMounts: [
    {
      node: "digest",
      requires: ["signals"],
      render: { model: "gpt-4o", maxTurns: 3 }
    }
  ]
});
```

### Receipt — структура решения

Каждый раз, когда Reactor принимает решение (рендерить или пропустить), он пишет content-addressed receipt:

```ts
type Receipt = {
  node: string;
  status: "rendered" | "skipped" | "failed";
  cause: { source: "external" | "input"; refs: string[] };
  cost: { fresh: number; reused: number };  // токены
  priorFingerprint: string;
  fingerprint: string;
  // подпись (v1 — tamper-evident, не криптографическая)
  signature: { scheme: "none"; null_reason: string };
};
```

Reactor умеет:
- `r.ledger.all()` — все receipt-ы
- `verifyReceiptChain(ledger)` — проверка цепочки
- `reactor-devtools --describe` — cost rollup по surprise-cause

---

## Практические сценарии для твоей инфраструктуры

### 1. Вместо cron, который дёргает LLM каждый час

**Сейчас:** cronjob → Hermes Agent → LLM → ответ. LLM платит каждый час, даже если данных нет.

**OpenProse:**
```ts
import { reactor } from "@openprose/reactor";

// Gateway `disk-usage` раз в час забирает df / duc
// Responsibility `disk-summary` подписан на него
// Если диск не изменился — Reactor пропускает рендер, fresh=0
const r = await reactor("./server-monitor", {
  directory: "/opt/monitor/state"
});

// Gateway просыпается по таймеру
// Но downstream не платит, пока данные реально не изменились
await r.ingest("disk-poll", { wake: { source: "external", refs: [] } });
```

### 2. Аудит решений в Multica Autopilot

**Сейчас:** задача в agentmemory, статус, ручная проверка.

**OpenProse:**
```ts
// Каждое решение автопилота — receipt.
// Цепочка верифицируется: можно доказать, что решение было принято
// на тех данных, которые были на тот момент.
const ledger = r.ledger.all();
const ok = verifyReceiptChain(ledger); // true/false
```

### 3. Gateway для MCP-серверов

Reactor совместим с любым Prose-Complete хостом. Можно подключить MCP-сервер как gateway, и downstream responsibility будет подписан на его truth:

```markdown
---
name: github-events
kind: gateway
---

# GitHub Events

### Continuity: external-driven

Подключено к GitHub MCP серверу.
Каждый новый PR/issue — событие, которое обновляет Maintains.

### Maintains
- `event_type`: "issue" | "pr"
- `payload`: тело события
- `timestamp`
```

---

## Сравнение с текущим стеком

| Аспект | Hermes Agent + cron | OpenProse + Reactor |
|--------|-------------------|---------------------|
| Парадигма | Императивная (навыки, cron, триггеры) | Декларативная (Maintains → reconciler) |
| LLM-затраты | Каждый запуск = полная стоимость | Только при изменении входов (skip = fresh 0) |
| Состояние | agentmemory, файлы, env | World-model + content-addressed receipt-ы |
| Аудит | Логи сессий | Chain-verifiable receipt-ы |
| Wiring | Ручной (делегирование, cron-цепочки) | Forme — автоматический из Requires/Maintains |
| Входной порог | Низкий (пишешь навыки как инструкции) | Выше (надо декларативно описать мир) |

**Когда стоит попробовать:**
- Много polling-агентов, которые большую часть времени работают вхолостую
- Нужен верифицируемый аудит решений
- Есть сложная сеть зависимостей между задачами (DAG)
- Хочется платить за LLM только когда что-то изменилось

**Когда не стоит:**
- Простые одноразовые задачи
- Нужен быстрый прототип «сделай и забудь»
- Критична зрелость (проекту 0.3)

---

## Примеры (13 штук с keyless replay)

| Пример | Суть | Домен |
|--------|------|-------|
| `surprise-cost` | мемоизация + пробуждение при изменении мемо-ключа | ядро |
| `renewal-risk` | переоценка только изменившихся счетов | SaaS / finance |
| `inbox-triage` | diamond fan-in + изоляция ошибок | email / ops |
| `monorepo-ci` | fan-out + защита merge gate | dev tooling / CI |
| `research-tree` | рекурсивное распространение по дереву, branch-memoized | research |
| `masked-relay` | peer-blind fan-out с маскированными проекциями | competitive intel |
| `agent-observatory` | много дешёвых watcher → batched synthesis | agent ops |
| `tamper-forge` | атака на receipt + chain-verify ловит (или нет) | audit / security |
| `oblique-weave` | hidden-context adversarial roles | product strategy |
| `github-star-enricher` | per-entity fan-out + human gate | growth / GTM |
| `implementation-pipeline` | fixed wide fan-out с per-facet lane wake | software delivery |
| `forme-fixpoint` | топология как ответственность (сам-wiring bootstrap) | meta |
| `basic-unit-suite` | 13 микромеханик, одна за другой | substrate |

Запуск любого (ключ не нужен):
```bash
cd skills/open-prose/examples/surprise-cost
npx reactor-devtools ./replay --describe
```

---

## Структура SDK

**API поверхность:**
- `@openprose/reactor` — фасад + curated front door (45 имён)
  - `.` — `reactor()`, `createReactor()`, `verifyReceipt()`, `fileSystemSubstrate()` и т.д.
- `@openprose/reactor/agents` — полный `@openai/agents` escape hatch
- `@openprose/reactor/adapters` — substrate, record/replay, render backend
- `@openprose/reactor/run` — offline compile + run boundary
- `@openprose/reactor/run/types` — типы offline run
- `@openprose/reactor/internals` — engine room, domain shapes

---

## Ограничения (честно от авторов)

- Receipt-ы **tamper-evident**, но не tamper-proof: нет криптографической подписи (signer — `{ scheme: "none" }`)
- Нет timestamp и principal в receipt-ах — это не audit log
- Signer caveat: редактирование world-model артефактов без переподписи receipt-ов не детектится
- Нет аутентификации в gateway
- Зависимости live-рендера: `@openai/agents` + `zod` ~99 MB / ~100 пакетов
- TypeScript: нужен `moduleResolution: "nodenext"` или `"bundler"` для subpath exports

---

## Relevance

Прямая релевантность к задачам Романа:
1. **Декларативный подход** вместо императивных агентов (Hermes Agent / JAWL / OpenClaw) — альтернативная парадигма
2. **Hermes MCP-интеграция** — Reactor совместим с любым Prose-Complete хостом. MCP-серверы можно подключить как gateway
3. **Receipt-ы для Multica Autopilot** — chain-verifiable лог решений. Аналог agentmemory, но с криптографической доказуемостью
4. **SDD-параллель** — как OpenSpec/SDD, но для AI runtime, не для разработки
5. **Замена cron-дёргателям** — если сейчас задача запускается по расписанию, но данные не меняются, OpenProse пропустит LLM-вызов

---

## Changelog

- **2026-06-15:** +30 ★ (1500→1530), +10 forks (110→120), 10 commits за неделю без релиза. 0 закрытых issues. Проект жив, slow burn.
- **2026-06-08:** Страница создана.
