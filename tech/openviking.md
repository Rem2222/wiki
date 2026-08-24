---
description: "OpenViking (Volcengine/ByteDance) — self-evolving контекст-БД для агентов: единая память+RAG+скиллы, файловая парадигма. (AGPL-3.0, ★32.6k)."
tags: [agent-memory,rag,context-database,volcengine,skills]
related: [[tech/semantica]] [[tech/tencentdb-agent-memory]]
---

# OpenViking

**OpenViking** (Volcengine/ByteDance) — self-evolving контекст-БД для ИИ-агентов: единая память, RAG-знания и скиллы. (Python, AGPL-3.0, ★32.6k).

## Суть
Заменяет фрагментированные векторные стора и «плоские» пулы контекста на чистую файловую парадигму. Хранит память, ресурсы и навыки как один навигируемый файлzist, рекурсивно достаёт их и грузит слоями — чтобы агент всегда имел нужный контекст при минимальных токенах.

- Автоподстройка под локальные агенты: детектит OpenViking CLI, Claude Code, Codex, Cursor, Trae, OpenCode, конфигурит plugin/MCP/Hook/CLI-интеграции.
- Плагины для Claude Code, OpenClaw, DSH.

## Оценка (0.3.22)
- long-conversation user memory (LoCoMo) и multi-turn agent tasks (tau2-bench) — бенчмарк-отчёт в репо (`./benchmark`).

## Репо
`volcengine/OpenViking` · Python · AGPL-3.0 · ★32.6k · https://openviking.ai
