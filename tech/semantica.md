---
description: Semantica — граф-нативная инфраструктура контекста для агентов (Context Graph + KG + provenance + decision intelligence). Сравнение с нашим стеком GBrain/codegraph/AgentMemory.
tags: [graph-rag, knowledge-graph, agent-memory, mcp, rag, trend]
related: [[tech/tencentdb-agent-memory]] [[tech/gbrain]] [[concepts/graph-rag]]
---

# Semantica (semantica-agi/semantica)

## Что это

**«Open Source Palantir для AI-агентов»** — детерминированная инфраструктура поверх LLM: Context Graph + Knowledge Graph, где каждое решение — first-class объект с каузальными цепями (CAUSED / INFLUENCED / PRECEDENT_FOR), провенансом (W3C PROV-O), конфликт-детекцией и рассуждением без LLM.

- **Stars:** ~5.5k (авг 2026), Python, MIT, активен
- **Сайт:** getsemantica.ai · **Доки:** docs.getsemantica.ai
- **Установка:** `pip install semantica`

## Архитектура

```
Sources → Ingest → Parse → Normalize → Split → Extract (NER/relations/events)
→ Conflict Detection → Deduplication → Knowledge Graph
→ [ Ontology · Reasoning · Provenance · Decisions ] → Enriched KG
→ Vector Store + Polyglot Graph Store (RDF & LPG) → Export / Visualize / REST · MCP · CLI
```

**Ключевые фичи:**
- **Decision Intelligence** — `record_decision()` создаёт узел решения; `trace_decision_chain()` каузальное родословие; `find_similar_decisions()` семантические прецеденты; `analyze_decision_impact()` карта влияния; `check_decision_rules()` policy-гейт
- **Deterministic reasoning** — forward chaining, Rete, Datalog, SPARQL (без LLM)
- **Provenance** — W3C PROV-O на каждом факте, экспорт в JSON/CSV/RDF
- **Конфликт-детекция** — противоречивые факты флагаются, а не молча перезаписываются
- **Time travel** — point-in-time снимки графа (`state_at("2024-01-01")`)
- **Entity resolution** — blocking + семантическая дедупликация
- **Polyglot storage** — RDF (Oxigraph, Jena, RDF4J) + LPG (Neo4j, FalkorDB, AGE) + vector stores
- **Визуализация** — Knowledge Explorer (React 19 + Sigma.js): граф, таймлайн, decisions, ontology hub
- **MCP-сервер** — 11 тулов: extract_entities, extract_relations, record_decision, query_decisions, find_precedents, get_causal_chain, add_entity, add_relationship, run_reasoning, get_graph_analytics, export_graph
- **REST API** — enrich, graph, decisions, reasoning, provenance, ontology, embeddings, search, export, pipeline, temporal, deduplication
- **Интеграции** — Claude Code, Cursor, Codex, Windsurf, Cline, Continue, VS Code, OpenClaw (MCP + плагины), Agno (multi-agent shared context)

## Сравнение с нашим стеком

| Шаг тренда | У нас | Статус |
|---|---|---|
| RAG по документации | GBrain (wiki, bge-m3, hybrid search) | ✅ |
| RAG по коду | codegraph MCP (29 тулов: affected_by, blast_radius, callers/callees, dead_code) | ✅ |
| Граф | GBrain wikilinks + граф страниц; codegraph — граф кода | ✅ |
| Память (Q&A) | AgentMemory (observations, lessons, slots, KG) + GBrain takes | ✅ |
| Раздача агентам | MCP: gbrain (85 тулов), agentmemory, codegraph | ✅ |
| Конфликт-детекция | GBrain find_contradictions, find_anomalies | ⚠️ v0 |
| Time-travel | GBrain get_versions / revert_version | ✅ |
| Детерминированные правила | нет (только LLM-поиск) | ❌ |

**Вывод:** наш стек уже покрывает все 5 шагов тренда (GBrain + codegraph + AgentMemory через MCP). Semantica дала бы governance/аудит (не нужно) и детерминированное рассуждение (можно добавить точечно). Основная ценность — подтверждение архитектурного направления.

## Тренд (авг 2026): Graph-RAG → память агентов

Ряд репозиториев-трендов по одной теме «граф знаний для агента»:
- **Semantica** (5.5k ⭐) — context graph + decision intelligence + provenance
- **Graphify** (105k ⭐!) — код + доки + SQL-схемы → граф через **детерминированный AST-парсинг (tree-sitter), без вектор-стора**. Точный структурный граф вместо эмбеддингов. MCP + скиллы для Claude Code/Cursor/Codex/Gemini
- **TencentDB-Agent-Memory** — память агента (см. [[tech/tencentdb-agent-memory]])

**Про 1С:** XML-ины без предобработки дают шум для эмбеддингов, но **Graphify-подход (AST вместо эмбеддингов) решает проблему**: точный парсинг структуры модулей вместо «похожести текста». vibecoding1c.ru/mcp_server#graph — GraphRAG + HybridSearch + любые embedding модели (LMStudio/облачные), визуальный интерфейс — становится основным MCP для 1С.

## Ссылки

- GitHub: https://github.com/semantica-agi/semantica
- Graphify: https://github.com/Graphify-Labs/graphify
- vibecoding1c MCP: https://vibecoding1c.ru/mcp_server#graph
