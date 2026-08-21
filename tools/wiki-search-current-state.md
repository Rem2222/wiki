---
description: "Текущее состояние поиска по вики (2026-08-21): zvec-wiki (индекс bge-m3+FTS) основной, GBrain запас; наличие официального MCP-сервера zvec-mcp-server и оценка текущего варианта."
tags: [wiki, zvec, gbrain, semantic-search, mcp, vector-db]
related: "[[tools/zvec]] [[concepts/memory-retrieve-middleware]] [[tasks/hindsight-memory-migration]]"
status: current
---

# Поиск по вики: текущее состояние и MCP (2026-08-21)

## Как сейчас ищем в вики (после перехода GBrain → Zvec)

**Основной слой — `zvec-wiki`** (гибридный семантический поиск по markdown-вики `~/Documents/wiki/`):

- Движок: **Zvec** (Alibaba, встраиваемая векторная БД, `pip install zvec`).
- Индекс: `/root/.zvec-wiki/index` — **1265 документов**, embedding completeness 100% (bge-m3 через Ollama :11434).
- Поиск: **гибрид** — вектор (bge-m3) + FTS (BM25-стиль), ранжирование **RRF** (Reciprocal Rank Fusion).
- Интерфейс: `/usr/local/bin/zvec-wiki "<query>" [--topk N] [--json] [--page-only]` — обёртка над `/root/.zvec-wiki/zvec_search.py`, venv `/root/.zvec-venv`.
- Возвращает: ранжированные чанки с путём/категорией/титулом/сниппетом (300 симв), полный текст — читается `read_file` из пути.

**Порядок поиска (прописан в `memory-wiki-workflow`):**
1. `zvec-wiki "<запрос>"` — семантика по вики.
2. `read_file` полного текста нужной страницы.
3. **GBrain (`mcp_gbrain_query`)** — только как **бэкап** до cutover (задача MUL-881).

## Есть ли официальный MCP-сервер для Zvec?

**ДА — `zvec-ai/zvec-mcp-server`** (⭐7, Python, «Zvec Official MCP Server», push 2026-04-15):

- Установка: `pip install zvec-mcp-server` (PyPI), запуск `python -m zvec_mcp`.
- **17 MCP-инструментов**: collection management (create/open/destroy), CRUD документов, vector search (single/multi), index management (HNSW/IVF/FLAT), hybrid search, embedding.
- Конфиг: `OPENAI_API_KEY` (обязателен для embedding), `OPENAI_BASE_URL` (опционально, можно DashScope), `OPENAI_EMBEDDING_MODEL` (default text-embedding-3-small).
- Транспорт: stdio (для Qoder/Cursor/Claude Desktop).

**Нюанс:** официальный MCP-сервер **ориентирован на OpenAI-клас embedding** и на **полное управление коллекциями** (CRUD, создание индексов). Для нашего сценария (не-менеджмент, а **read-only поиск по готовому индексу, построенному на bge-m3 из Ollama**) он далеко не идеален:
- требует OpenAI-ключ для embedding (у нас эмбеддинги локальный bge-m3);
- заточен под CRUD, а не под «просто поискать по существующей вики»;
- маленький (⭐7), точ-пик.

## Чем плох текущий вариант (`zvec-wiki` через terminal)?

**Честная оценка — минусы текущего подхода:**
1. **Не нативный MCP-tool**: `zvec-wiki` — это вызов из shell (terminal), а не отдельный MCP-инструмент. Агент видит её как команду, а не как структурированный tool.
2. **Нет автодокументации/схем**: MCP-tool несёт JSON-schema параметров, дескрипшн; shell-команда — только help в коде.
3. **Возвращает сырой текст** (не JSON по умолчанию) — агент парсит вывод вручную; хотя `--json` есть.
4. **Нет семантики «агент сам решит искать»**: у gbrain был `mcp_gbrain_query` — инструмент, который агент видит в списке. `zvec-wiki` — команда, надо вспомнить вызвать.

**НО плюсы текущего варианта:**
- Работает прямо сейчас, без OpenAI-ключа.
- Гибрид bge-m3+FTS именно под наш индекс.
- Меньше подвижной части, чем подключать MCP.

## Вывод / рекомендация

- Для полноценного «нативного» поиска можно **обернуть наш `zvec_search.py` в свой лёгкий MCP-сервер** (FastMCP, read-only: `search(query, topk)`), без OpenAI — тот же bge-m3 через Ollama. Тогда у Hermes появится tool `zvec_wiki_search` и агент будет «видеть» его как инструмент (как раньше gbrain).
- Готовый `zvec-ai/zvec-mcp-server` — не подходит напрямую (OpenAI-embedding + CRUD-ориентирован).
- Сменить на MCP — **по желанию**, текущий `zvec-wiki` уже закрывает задачу. Оформить как отдельную задачу при желании.

## Связанные материалы

- [[tools/zvec]] — сама встраиваемая векторная БД от Alibaba.
- [[concepts/memory-retrieve-middleware]] — идея middleware-роутера над памятью/вики.
- MUL-878 (GBrain→Zvec) — parent-задача в Multica.