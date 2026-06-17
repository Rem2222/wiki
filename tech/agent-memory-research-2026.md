---
description: Исследование решений для долговременной памяти AI-агентов (2026). Сравнение 40+ проектов: mem0, agentmemory, GBrain, MemPalace, TencentDB, engram, MemOS и другие.
tags: [memory, agent-memory, ltm, research, comparison, mcp, knowledge-graph]
related: [[tech/gbrain-lossless-agent-memory]], [[tech/MemPalace-Hermes-Integration]], [[tech/agentmemory-vs-current]], [[tech/tencentdb-agent-memory]]
---

# Долговременная память для AI-агентов — Исследование 2026

Исследование проведено 27 мая 2026. Собрано 40+ проектов с GitHub, Reddit, Hacker News.

## Выводы и рекомендации

**Лучшие решения на 2026 год:**

1. **agentmemory** (18.5k ⭐) — самый популярный, 51 MCP tool, multi-харнесс. Легко подключить к Hermes Agent.
2. **engram** (3.8k ⭐) — Go single binary, SQLite+FTS5, MCP+HTTP+CLI+TUI. Работает со всеми агентами.
3. **MemOS** (9.4k ⭐) — SOTA по точности, с arXiv paper. Есть OpenClaw плагин.
4. **TencentDB Agent Memory** (4.3k ⭐) — лучший по token savings (-61%). Есть Hermes интеграция.
5. **nocturne_memory** (1.1k ⭐) — "Say goodbye to Vector RAG". Graph-like структура, SQLite/PostgreSQL.
6. **agentic-stack** (2k ⭐) — портативная .agent/ папка, работает со всеми харнессами.
7. **ClawMem** (176 ⭐) — специально для Hermes/Claude Code/OpenClaw. Hybrid RAG, hooks, MCP.

**Итоговый выбор для текущего стека:** agentmemory (MCP-память для фактов и сессий) + GBrain (индексация markdown-вики).

**Тренды 2026:**
- Отказ от чистого Vector RAG → гибридные подходы (BM25+vector+graph+rerank)
- MCP как стандартный протокол для memory
- Knowledge graphs заменяют flat vector stores
- Self-evolving memory (MemOS, EverOS)
- Spaced repetition / Ebbinghaus decay curves (Vestige, YourMemory)

---

## 1. Главные проекты (10k+ stars)

| Проект | Звёзды | Суть |
|--------|--------|------|
| **mem0ai/mem0** | ~56k | Универсальный memory layer для AI-агентов. База для многих интеграций. |
| **rohitg00/agentmemory** | 18.5k | "#1 Persistent memory для AI coding agents" — npm пакет, 51 MCP-инструмент. Работает с Claude Code, Cursor, Hermes, OpenClaw, Codex. |
| **memvid/memvid** | 15.5k | Single-file memory layer, без БД, serverless. Rust-based. |
| **NevaMind-AI/memU** | 13.7k | Фреймворк для 24/7 проактивных агентов. Существенно снижает token cost. |
| **MemTensor/MemOS** | 9.4k | "Self-evolving memory OS". arXiv paper, +43.70% accuracy vs OpenAI Memory, 35.24% token savings. |
| **EverMind-AI/EverOS** | 5.7k | Build, evaluate, integrate LTM для self-evolving агентов. |

## 2. Решения для Hermes Agent

| Проект | Звёзды | Описание |
|--------|--------|----------|
| **outsourc-e/hermes-workspace** | 5k | Native web workspace для Hermes — чат, терминал, memory, skills, inspector |
| **joeynyc/hermes-hudui** | 1.6k | Web UI consciousness monitor для Hermes с persistent memory |
| **AxDSan/mnemosyne** | 671 | Zero-dependency, sub-millisecond AI memory для Hermes. BEAM ICLR 2026. |
| **yoloshii/ClawMem** | 176 | On-device memory для Claude Code, Hermes, OpenClaw. Hooks + MCP + hybrid RAG. |
| **esaradev/icarus-plugin** | 122 | Self-memory plugin для Hermes. |
| **elkimek/honcho-self-hosted** | 267 | Self-hosted Honcho memory layer для Hermes Agent. |

## 3. MCP Memory Servers

| Проект | Звёзды | Описание |
|--------|--------|----------|
| **engram** (Gentleman-Programming) | 3.8k | MCP server + HTTP API. Лучший Go-вариант. |
| **nocturne_memory** | 1.1k | "Drop-in replacement for OpenClaw memory". SQLite/PostgreSQL, graph-like. |
| **token-savior** | 910 | -77% tokens, -76% wall time. Persistent memory + structural nav. |
| **memory-bank-mcp** | 905 | Remote memory bank management, inspired by Cline Memory Bank. |
| **vestige** (samvallad33) | 540 | Cognitive memory + FSRS-6 spaced repetition. 22MB Rust binary, MCP. |
| **alash3al/stash** | 700 | Postgres + pgvector. Один бинарник. MCP. |
| **nornicdb** | 750 | Graph+Vector, Temporal MVCC, sub-ms HNSW. MCP. |

## 4. Knowledge Graph память

| Проект | Звёзды | Описание |
|--------|--------|----------|
| **neo4j-labs/agent-memory** | 272 | Официальный Neo4j. STM + LTM + Reasoning Memos. |
| **swarmclawai/swarmvault** | 499 | Local-first LLM Wiki + knowledge graph. Obsidian-alternative. |
| **graph-memory** (adoresever) | 491 | OpenClaw memory plugin: Knowledge Graph + Memory. |
| **mnemon-dev/mnemon** | 312 | LLM-supervised persistent memory. Graph-based recall. |
| **MegaMemory** (0xK3vin) | 170 | MCP + semantic search + in-process embeddings + web explorer. |

## 5. Категоризация по типам памяти

**A. SQLite-based (простые, локальные)**
- engram (Go binary + FTS5)
- agentmemory (npm, multi-харнесс)
- mnemosyne (Python, zero-dependency)
- claude-mem-lite (FTS5+TF-IDF)

**B. Knowledge Graph-based**
- neo4j-labs/agent-memory (официальный Neo4j)
- nocturne_memory (graph-like структура)
- Dragon-Brain (FalkorDB + Qdrant + CUDA)

**C. Markdown/Wiki-based**
- gbrain (Garry Tan, YC CEO — synthesis + graph traversal)
- pi-mem (plain-markdown persistence)
- Alive (5 markdown files для Claude Code)

**D. Hybrid RAG (multi-signal retrieval)**
- ClawMem (BM25+vector+RRF+rerank+recency)
- Vestige (FSRS-6 spaced repetition, 29 brain modules)
- YourMemory (Ebbinghaus + better than Mem0)

## 6. Mem0 альтернативы

| Проект | Звёзды | Описание |
|--------|--------|----------|
| **telemem** (TeleAI-UAGI) | 461 | High-performance drop-in for Mem0. Семантическая дедупликация. |
| **YourMemory** (sachitrafa) | 231 | +16pp лучше Mem0 на LoCoMo. Ebbinghaus forgetting curve. |

## 7. Ключевые обсуждения

**Hacker News:**
- "Why do none of the major AI agents persist memory across sessions?" (2026)
- "Vector embeddings are the wrong default for AI agent memory" (2026)
- "Show HN: Engram – Memory for AI coding agents" — 2.5k installs, 80% on LOCOMO
- "Memary: Open-Source Longterm Memory for Autonomous Agents" (216 pts, 2025)
- "Give AI agents long-term memory without blowing the budget" (2026)

**Claude Code / Cursor:**
- "Show HN: Persistent memory for Claude Code sessions" — TonyStef/Grov
- "Ctx – Persistent Memory for Claude Code, Cursor, and AI Coding Tools"
- "Alive – Five Markdown files that give Claude Code a persistent memory"
- "TeamMind – persistent memory for Claude Code (no API key)"

## 8. Ключевые статьи и бенчмарки

- **MemOS paper**: https://arxiv.org/abs/2507.03724 — Self-evolving memory OS
- **ByteRover paper**: https://arxiv.org/abs/2604.01599 — Context memory framework
- **BEAM benchmark**: ICLR 2026 — Benchmark for agent memory
- **HaluMem**: https://github.com/MemTensor/HaluMem — Первый benchmark галлюцинаций в memory systems
- **LoCoMo**: Основной benchmark для LTM агентов

## 9. Awesome-листы

- https://github.com/IAAR-Shanghai/Awesome-AI-Memory (922⭐)
- https://github.com/TeleAI-UAGI/Awesome-Agent-Memory (437⭐)
- https://github.com/NirDiamant/Agent_Memory_Techniques (417⭐) — 30 ноутбуков
