---
created: 2026-05-07
type: concept
tags: [LLM, AI-research, sub-quadratic, long-context]
description: First fully sub-quadratic LLM, 12M token context, sparse attention O(n)
related: [[tech/free-claude-code]] [[tech/opencode]] [[tech/optimizing-llm-api-calls-for-coding]]
---

# Subquadratic (SubQ)

**URL:** https://subq.ai

## What is it

Первый полностью суб-квадратичный LLM. Вместо attention O(n²) как у Transformers — sparse attention O(n).

## Key specs

- **Context:** 12M tokens
- **Speed:** 150 tok/sec
- **Cost:** 1/5 от frontier-моделей
- **Reduction in attention compute:** ~1000× at 12M tokens

## Architecture

Subquadratic Sparse Attention (SSA): находит и фокусируется только на релевантных связях между токенами, не на всех парах.

## Benchmarks

- SWE-Bench Verified: **81.8%**
- RULER@128K: **95.0%**
- MRCR v2 (1M): 65.9%

## Products

- **API** — 12M context, OpenAI-compatible, streaming, tool use
- **Code** — для coding-агентов (Claude Code, Codex, Cursor), 25% дешевле, 10× быстрее exploration

## Founders

Researchers from Meta, Google, Oxford, Cambridge, BYU.

## Links

- X: @subquadratic
- Discord: Bc9Rrx2x45
- LinkedIn: subquadratic-ai
