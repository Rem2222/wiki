---
description: Unified API for hundreds of models. OpenAI-compatible.
tags: [tech]
---

# poe-chutes-comparison

**Date:** 2026-05-11
**Context:** Gist mcowger/892fb83ca3bbaf4cdc7a9f2d7c45b081 (KiloCode related), testing new providers for coding

## Poe API (poe.com/api)

Unified API for hundreds of models. OpenAI-compatible.

**API Key:** `sk-poe-gF8zqW-x7iDLO_jLCbR1eW0Ogn9llHGj3CoIN4mELQY`
**Base URL:** `https://api.poe.com/v1/chat/completions`

### Subscription Plans (yearly)

| Plan | Price | Points |
|------|-------|--------|
| Base | €4.79/mo | 10K/day (~300K/month) |
| Standard | €19.17/mo | 660K/month |
| Pro | €47.92/mo | 1.65M/month |
| Pro+ | €95.83/mo | 3.3M/month |
| Max | €239.58/mo | 8.25M/month |

### Best Coding Models

| Model | Input $/1M | Output $/1M | Context | Notes |
|-------|-----------|-------------|---------|-------|
| `gpt-5.5-pro` | $4.55 | $27.27 | 400K | Top agentic coding |
| `gpt-5.5` | $4.55 | $27.27 | 400K | Same quality |
| `claude-opus-4.7` | $4.29 | $21.46 | 1M | Enterprise, MCP |
| `seed-2.0-code` | $0.63 | $3.79 | 256K | Enterprise coding, front-end |
| `kimi-k2.6` | $0.96 | $4.04 | 262K | Multi-agent, 300 sub-agents |
| `deepseek-v4-pro-el` | $1.67 | $3.33 | 1M | 49B MoE |
| `qwen3.6-max-preview` | $1.31 | $7.88 | 256K | Vibe coding |
| `deepseek-v4-flash-el` | $0.14 | $0.28 | 1M | Fast + cheap |
| `deepseek-r1` | $0.018/request | — | 160K | Reasoning |
| `grok-4.3` | $1.26 | $2.53 | 1M | xAI, factual accuracy |

**Image:** `gpt-image-2`, `nano-banana-2` (Google)
**Video:** `happyhorse-1.0-el` (ByteDance)

---

## Chutes AI (chutes.ai)

Serverless GPU for open-source models. OpenAI-compatible API.

### Subscription Plans

| Plan | Price | Notes |
|------|-------|-------|
| Base | $3/mo | Open-source models only |
| Plus | $10/mo | Frontier models (GLM-5, Kimi K2, Qwen 3.5, MiniMax M2.5) |
| Pro | $? | Contact sales |
| Enterprise | $? | Contact sales |

**Free tier:** 200 requests/day (retiring soon)

**PAYG:** ~$0.10–$0.30 per 1M tokens

### Models for Coding

Qwen, Llama, DeepSeek Coder, CodeQwen — all available.
No proprietary models.

---

## Poe vs Chutes — Quick Comparison

| | Poe | Chutes |
|--|-----|--------|
| Proprietary models | ✅ Yes (GPT-5, Claude, Gemini...) | ❌ No |
| Open-source models | ❌ No | ✅ Yes (Qwen, Llama...) |
| Pricing model | Points (subs) or per-token | Per-token or subscription |
| Tool calling | ✅ Yes | ✅ Via liteLLM |
| Best for | Access to top models | Budget coding with open models |
| Starting price | €4.79/mo | $3/mo |

---

## Hermes Integration

Both are OpenAI-compatible — add as custom providers:

```yaml
providers:
  poe:
    api_key: "sk-poe-gF8zqW-x7iDLO_jLCbR1eW0Ogn9llHGj3CoIN4mELQY"
    base_url: "https://api.poe.com/v1"
```

---

## Related

- [Poe API Models](poe-api-models.md) — full model list with pricing
- KiloCode (mcowger) — alternative open-source coding agent