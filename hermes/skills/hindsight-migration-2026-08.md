# Переезд памяти на Hindsight: бэкфилл + архитектура (2026-08-20)

Решение Романа: **Hindsight** как замена нестабильному agentmemory. Этот файл — исполняемые
детали для реального переезда (бэкфилл, где брать сырьё, конфиг, замена GBrain). Сам выбор по
критериям/весам — `references/memory-provider-comparison-2026-08.md`.

## Ключевой факт: файлов сырых сессий НЕТ — единственный источник state.db

Проверено на VPS 20.08.2026:
- `/root/.hermes/sessions/sessions.json` — это **НЕ сессии**, а `LEGACY MIRROR of the gateway
  routing index` (внутри файла прямо написано: «This is NOT the session list. ALL sessions live in
  state.db»). Это карта «session_key → session_id».
- `request_dump_*.json` (~396 шт, `~/.hermes/sessions/`) — дампы отдельных API-запросов, не сессии.
- **Единственный полный архив истории — `~/.hermes/state.db`** (SQLite): таблицы `sessions`
  (started_at/ended_at/source/title/model/system_prompt) + `messages`
  (session_id/role/content/timestamp/reasoning/reasoning_content/tool_calls/tool_name).
  Размер ~189MB, 895 сессий, 33 956 сообщений (22k+ с полным текстом).

Для бэкфилла/миграции читать ТОЛЬКО state.db, не «файлы сессий».

## Бэкфилл истории в Hindsight через retain()

API (`hindsight_client`, pip пакет):
```python
from hindsight_client import Hindsight
client = Hindsight(base_url="http://localhost:8888")
client.retain(
    bank_id="hermes",
    content="<транша диалога/факт>",
    context="<описание контекста>",
    timestamp="2026-08-20T10:00:00Z",   # ← ключ: заливать с РЕАЛЬНЫМИ датами
)
```
- `retain()` за кулисами через LLM сам извлекает факты/сущности/связи/уроки и строит временную
  шкалу. Поэтому **не тянуть готовые факты из agentmemory**, а заливать сырые диалоги с реальным
  timestamp — Hindsight сам нарежет слои (предпочтение Романа).
- `recall(bank_id, query)` — поиск (в т.ч. temporal: «что было в июне»).
- `reflect(bank_id, query)` — LLM-синтез высшего уровня поверх памяти.
- Бэкфилл-скрипт: читать state.db → нарезать диалоги на транши → `retain()` с настоящими датами.

⚠️ **Узкое место — не эмбеддинги, а `retain()`-LLM-извлечение.** 33k сообщений через LLM =
много токенов/времени. Крутить бэкфилл асинхронно/пакетами, не блокируя боевую память. Вариант:
полный бэкфилл (вся история, долго) vs выборочный (последние 3-6 мес + важные) — решить с Романом.

## Скорость эмбеддингов bge-m3 на VPS (реальный тест, не на глаз)

- bge-m3 на Ollama (port 11434), CPU: **~790 мс на батч-вызов** (`/api/embed`, 50 рус. слов ×5).
- по 1 сообщению: 33k × 0.79с ≈ ~7 ч; **батчами по ~40 → ~11 мин**.
- Вывод: эмбеддинги НЕ проблема (Роман прав — «переиндексацию на AgentMemory делали»). Медленная
  часть — именно `retain()` с LLM-извлечением, а не вектора.
- bge-m3 совместим с Hindsight (см. ниже).

## Конфиг «Hermes + Hindsight + локальная Ollama» (кейс пользователя)

Repo `vectorize-io/hindsight-cookbook` → `applications/hermes-memory/configs/hermes-local-ollama.example.json`:
```json
{ "mode":"local", "llm_provider":"ollama", "llm_model":"gemma3:12b",
  "bank_id":"hermes", "memory_mode":"hybrid",
  "prefetch_method":"recall", "autoRecall":true, "autoRetain":true }
```
Copy → `~/.hermes/hindsight/config.json`. Ollama должна работать на той же машине (`ollama serve`).

Hermes поставляет **встроенный Hindsight memory provider**: `pre_llm_call` hook → auto-recall
(инъекция релевантной памяти перед ответом), `post_llm_call` → auto-retain (сохранение сессии после
ответа). Мodes: `hybrid` (auto-recall + явные tools, default), `context` (только auto-recall),
`tools` (только явные tools, модель сама решает). `prefetch_method`: `recall` (быстро, сырые факты)
или `reflect` (LLM сначала синтезирует связные сводки).

## Подключение к Hindsight: агностичность

Hindsight работает с **25+ провайдеров** LLM/эмбеддингов через `HINDSIGHT_API_LLM_PROVIDER`:
hosted (openai/anthropic/gemini/groq/bedrock/vertexai/minimax/deepseek/atlas) + полностью локал
(**ollama/lmstudio/llamacpp**) + любой OpenAI-совместимый endpoint + gateways (litellm). Существующие
подписки: `openai-codex`, `claude-code`, `github-copilot` без API-ключа.
Python/Node.js/Go SDK + CLI + REST + MCP. **bge-m3 на Ollama = валидный локальный embedder для Hindsight.**

## Авто-retrieve перед turn (что реально умеет)

- **Hindsight**: `auto_recall=true` + `memory_mode=hybrid/context` + `recall_budget=low/mid/high`.
  `recall()` = 4 параллельные стратегии: Semantic (vector) + Keyword (BM25) + Graph (entity/temporal/
  causal) + Temporal. Хранилище PostgreSQL + pgvector.
- **ClawMem**: `prefetch()` — prompt-aware semantic search каждый turn (context-surfacing hook).
- **Holographic**: НЕТ нативного авто-retrieve (только инструменты probe/search; `auto_extract=false`)
  — слабое место под вес авто-retrieve=4.
- **OpenViking**: L0-абстракт (~100 ток) грузится всегда, но глубокий векторный поиск — по запросу.

## Сквозная/распределённая память (VPS ↔ Windows)

- **Hindsight/Honcho** (Postgres): сервер на VPS (Docker, порт 8888) → Windows-агент по REST/MCP/SDK
  через сеть = единый центр, удалённые клиенты. Из коробки.
- **ClawMem**: локальный SQLite-файл — VPS и Windows получили бы два ОТДЕЛЬНЫХ vault'а; нужен ручной
  мост. Для разнесённого сценария проигрывает.
- **НЕ зеркалить БД на винду активной копией** — две расходящиеся копии. Правильно: одна БД на VPS,
  все агенты подключаются к ней. Копия на винду — только бэкап/кэш, не источник правды.

## Замена GBrain для вики → Zvec (Alibaba)

Роль GBrain у пользователя = только семантический поиск по md-вики (сам GBrain тяжёлый, падает,
беспризорный). Замена: **Zvec** (`pip install zvec`, уже в вики `tech/zvec.md`):
- встраиваемая векторная БД, один файл, без серверов/Docker; гибрид вектора+FTS+скалярные фильтры;
  DiskANN (мало RAM); WAL; 13.8k⭐, Apache 2.0, активная (коммиты ежедневно); Windows поддержка.
- Роль та же (семантика по вики), геморроя сильно меньше. Вики при этом остаётся Markdown-файлами на
  ФС + Obsidian-интерфейс для чтения (пользователь заходит через Obsidian).

## YAML-frontmatter в вики — кто ввёл (для чистки)

YAML frontmatter (`--- description/tags/related ---`) внёс **сам агент** (по правилам Obsidian/OKF),
НЕ GBrain. В вики намешаны слои: `.obsidian`, `.openclaw-wiki` (GBrain), `graphify-out` (Graphify),
секции от разных систем. План чистки (согласован): оставить Obsidian-дерево + frontmatter (уже
285/296 файлов), убрать лишние слои и мусорные папки (reports/syntheses от GBrain/Graphify).

## Идея middleware авто-retrieve (записана в вики)

`concepts/memory-retrieve-middleware.md` — отдельный роутер перед каждым turn: память + вики +
state.db, сам ранжирует и встраивает топ-N. На старте НЕ плодить свой middleware — Hindsight даёт
авто-recall из коробки; роутер — вторая итерация, если одиночный провайдер не покроет вики/историю.
