---
description: MemPalace поставляет MCP-сервер с 29 инструментами (chroma storage, KG, diary), но протокол использования не выполнялся автоматически — агент просто не знал, когда вызывать `diary_write`, `kg_query...
tags: [tech]
related: [[tech/hermes-memory-setup-vps]] [[tech/gbrain-lossless-agent-memory]] [[tech/agentmemory-vs-current]]
---

# MemPalace × Hermes Agent: интеграция через gateway hook

## Контекст

MemPalace поставляет MCP-сервер с 29 инструментами (chroma storage, KG, diary), но **протокол использования не выполнялся автоматически** — агент просто не знал, когда вызывать `diary_write`, `kg_query` и т.д.

Цель: автоматизировать те шаги протокола, которые не требуют понимания контекста от LLM.

## Что было сделано

### 1. Gateway hook `mempalace-protocol`

**Расположение:** `~/.hermes/hooks/mempalace-protocol/`

```
mempalace-protocol/
├── HOOK.yaml     # подписка на agent:start и agent:end
└── handler.py    # бизнес-логика
```

**HOOK.yaml:**
```yaml
name: mempalace-protocol
description: Auto-execute MemPalace memory protocol - status on wake, diary on session end
events:
  - agent:start
  - agent:end
```

**handler.py** реализует два автоматических шага из 5:

| Шаг протокола | Автоматизирован? | Как |
|----------------|------------------|-----|
| 1. ON WAKE → palace_status | ✅ Да | hook: `agent:start` → `_get_status_summary()` |
| 2. ПЕРЕД ответом о людях/проектах → kg_query | ❌ Нет | Только LLM знает когда нужно |
| 3. НЕУВЕРЕН → "let me check" | ❌ Нет | Только LLM знает |
| 4. ПОСЛЕ СЕССИИ → diary_write | ✅ Да | hook: `agent:end` → `_write_diary()` |
| 5. ФАКТЫ ИЗМЕНИЛИСЬ → kg_invalidate/kg_add | ❌ Нет | Только LLM знает когда факт меняется |

### 2. Патч run.py — чтобы контекст попал в LLM

**Файл:** `/usr/local/lib/hermes-agent/gateway/run.py`
**Строка:** ~6362

Проблема: `agent:start` хук возвращает dict, но gateway по умолчанию использует `emit()` который **отбрасывает** возвращаемые значения. Агент не получает статус MemPalace в свой prompt.

**Исправление:**
```python
## БЫЛО (return value discarded):
await self.hooks.emit("agent:start", ...)

## СТАЛО (return value collected и инъектится в context):
hook_results = await self.hooks.emit_collect("agent:start", ...)
## hook_results["context"] инъектится в context_prompt
```

**Правило Романа:** этот патч **слетает при каждом обновлении Hermes**. После обновления — переприменить вручную.

Проверка после патча:
```
agent:start → _get_status_summary() → context injected into LLM prompt
```

### 3. MCP wrapper

**Путь:** `/root/.hermes/bin/mempalace-mcp`

 wrapper нужен из-за того, что env filter в hermes-agent отфильтровывает переменные окружения, которые MCP сервер наследует от OpenClaw. wrapper вызывает:
```
python3 -m mempalace.mcp_server
```

В версии 3.3.4 изменился импорт: `TOOLS` вместо старого `MCP_SERVER_TOOLS`.

## Как это работает

```
User message → Gateway
  → emit_collect("agent:start", context)
       → handler.py: _get_status_summary()
            → MCP: mempalace_status + mempalace_kg_stats
       ← returns {"context": "MemPalace: 21240 drawers [...]"}
  → context["mempalace_auto"] = hook_result["context"]
  → LLM prompt получает строку статуса
  
LLM отвечает

Gateway
  → emit("agent:end", context)
       → handler.py: _write_diary()
            → MCP: mempalace_diary_write (AAAK compressed)
```

## Результат

```
[MemPalace Auto] MemPalace: 21240 drawers [technical(13380), general(4563), architecture(2069), planning(767), problems(386)] | KG: 175 entities, 648 triples
```

Эта строка теперь **автоматически** появляется в контексте каждого агентного сеанса.

## Заметки

- **МемПелес и Wiki — разные системы.** Wiki лежит в `~/.openclaw/workspace/wiki/tech/`, MemPalace — в `~/.mempalace/`. Синхронизации между ними нет.
- **Шаги 2, 3, 5** протокола остаются ответственностью модели — только LLM понимает, когда ему нужны факты из KG перед ответом.
- **AAAK** (Agent Awesome Autobiographical Knowledge) — сжатый формат для записей в diary: `SESSION:2026-05-10|action summary|plat:telegram|sid:abc123|★★★`

## Файлы

| Файл | Назначение |
|------|------------|
| `~/.hermes/hooks/mempalace-protocol/HOOK.yaml` | Подписка на events |
| `~/.hermes/hooks/mempalace-protocol/handler.py` | Реализация auto-шагов |
| `/usr/local/lib/hermes-agent/gateway/run.py:6362` | Патч для inject контекста |
| `/root/.hermes/bin/mempalace-mcp` | Wrapper для MCP сервера |
| `~/.mempalace/` | Данные MemPalace (chroma + KG) |