---
description: "Плагин DSH → Hindsight: интеграция DeepSeek Harness с памятью (задача)"
tags: [dsh,hindsight,plugin,tasks]
---

# Плагин DSH → Hindsight (детали из EverOS-рецепта)

## Контекст / зачем

Роман хочет использовать **DeepSeek Harness (dsh)** на Windows как **дополнительного** агента,
основной агент — **Hermes на VPS**. Память обоих — **Hindsight** (выбрано в MUL-874, семантическая
память напарника). У dsh НЕТ нативного Hindsight-плагина — его надо написать, чтобы dsh мог
**recall/retain** в ту же память, куда пишет Hermes. Это соединит dsh (Windows) и Hermes (VPS)
в одну сквозную память.

## Что у нас уже есть (я нарыл при изучении EverOS)

В репозитории EverOS есть **готовый образец dsh-плагина памяти** — его можно взять как каркас
и заменить EverOS-клиент на Hindsight. EverOS уже написал всю обвязку жизненного цикла dsh.

### Где взять образец (локально, клонированный)

- `/tmp/evos/examples/dsh/README.md` — полный разбор плагина EverOS для dsh
- `/tmp/evos/examples/dsh/cordis.patch.yml` — сам патч, который подключает плагин в dsh
- `/tmp/evos/examples/dsh/src/index.ts` — код жизненного цикла (суть каркаса)
- `/tmp/evos/examples/dsh/src/recall.ts`, `capture.ts`, `memory-runtime.ts`, `everos-client.ts`
- `/tmp/evos/examples/dsh/package.json` — `dsh.bundle.patch` (как упаковать)
- `/tmp/evos/examples/dsh/test/` — тесты плагина (с моками, без провайдера)

> Примечание: эти папки — WIP-клоны из моего исследования, могут отличаться. Проверяй
> по актуальным источникам ниже.

### Ссылки на источники (сверяться при застревании)

- EverOS dsh-пример: https://github.com/EverMind-AI/EverOS/tree/main/examples/dsh
- EverOS README (память для dsh): https://github.com/EverMind-AI/EverOS
- Hindsight README (core concepts: retain/recall/reflect, banks, mental models):
  https://github.com/vectorize-io/hindsight
- Hindsight Сайт-доки: https://hindsight.vectorize.io/
- Hindsight разработка (retain/retrieval/reflect/mental-models):
  https://hindsight.vectorize.io/developer/retain
  https://hindsight.vectorize.io/developer/retrieval
  https://hindsight.vectorize.io/developer/reflect
  https://hindsight.vectorize.io/developer/mental-models
- Hindsight MCP-сервер (к какому endpoint цепляться): https://hindsight.vectorize.io/developer/mcp-server
- dsh-клиент (конфиг MCP): из клона DeepSeek Harness:
  https://github.com/deepseek-ai/deepseek-harness/tree/main/packages/mcp/mcp-client
  (docs/config-catalog.md → секция `@deepseek-ai/dsh-mcp-client` — конфиг StdioConfig/StreamableHttpConfig)

## Суть каркаса EverOS (что скопировать, заменив EverOS → Hindsight)

EverOS-плагин работает через **трёхфазный цикл**, подключаясь к событиям dsh:

1. **Recall — старт каждого turn**
   Хук `agent/pre-step` (prepend): если `step===1` (первый шаг), вызывает `recallMessage()`
   → ищет по трекам user/agent → **встраивает сообщение-воспоминание в messages перед моделью**
   (`{ kind:'enter', messages:[...decision.messages, recalled] }`).
   У нас вместо EverOS-поиска — `hindsight client.recall(bank, query)`.

2. **Capture — на каждой границе turn**
   Хук `agent/turn-stopping` → `capture()` — дурабильно дописывает user/assistant/tool-call/tool-result
   в буфер **без LLM-извлечения** (дёшево).
   У нас — `hindsight client.retain(bank, content, context, timestamp)`.

3. **Flush — пакетное извлечение**
   После idle-окна / порога токенов / смены сессии / таймаута — дорогая LLM-экстракция разом.
   `flushOnSessionSwitch` перед recall коммитит недофлашенную память прошлой сессии
   (read-after-write barrier).

Как встроено в dsh:
- Через **Cordis-патч** (`dsh.bundle.patch` + файл `cordis.patch.yml`)
- Плагин подключается: `dsh plugin --profile web add <pacakge>` (см. EverOS README)
- `inject: ['agents']`, регистрирует слушатели событий `agent/pre-step` и `agent/turn-stopping`

Правило **fail-open**: ошибки памяти логируются, но НИКОГДА не блокируют шаг/ход dsh.
Это обязательное требование надёжности.

## Что заменить на Hindsight

- EverOS-клиент (`everos-client.ts`) → Hindsight-клиент. Два пути:
  - **Вариант A (проще, рекомендую):** подключаться к Hindsight **MCP-серверу** (у Hindsight есть MCP
    endpoint `/mcp`), вызвав `hindsight_recall` / `hindsight_retain` / `hindsight_reflect`.
    Меньше кода — не пишем HTTP-клиент сами.
  - **Вариант B:** HTTP/REST-клиент к Hindsight API (порт 8888) с `retain`/`recall`/`reflect`.
- `bank_id` — используй то же, что в Hermes-настройке (обычно `hermes`).
- URL для Windows → VPS: Hindsight слушает на VPS (порт 8888 / MCP), dsh на Windows цепляется
  через streamable-HTTP / MCP по интернету (см. конфиг dsh-mcp-client: `transport: streamable-http`).
  Возможны endpoint-прокси через nginx (уже есть паттерны в нашей инфре).

## Требования

- TypeScript/Node (dsh — TS-экосистема, типа как EverOS)
- Node.js ^22 (или выше, как требует EverOS-пример)
- DeepSeek Harness 0.1.x — **plugin API ещё RC, может меняться** (EverOS это отмечает как limitation)
- Hindsight уже развёрнут на VPS (задача MUL-875)

## Критерии done

- [ ] dsh на Windows может читать память Hindsight (recall) — видит факты, которые записал Hermes
- [ ] dsh может писать в Hindsight (retain) — Hermes на VPS потом видит записи с Windows
- [ ] Авто: recall в начале turn + retain после (через хуки), fail-open
- [ ] Протестировано (одиночный smoke-сценарий: записал на Windows → прочитал на VPS и наоборот)
- [ ] Опционально: `reflect` для синтеза

## Не делать

- НЕ трогать боевую память до MUL-881 (cutover)
- НЕ ломать Hermes-настройку Hindsight (это отдельный аген-слой)
- НЕ делать сквозную сеть VPS↔Windows до MUL-882 (это отдельный этап); здесь только плагин dsh→Hindsight
