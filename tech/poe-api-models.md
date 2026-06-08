---
description: Подписки Poe включают API-доступ. OpenAI-compatible.
tags: [tech]
related: [[tech/poe-chutes-comparison]] [[tech/free-claude-code]] [[tech/9router-vs-openrouter]]
---

# poe-api-models

**API Key:** `sk-poe-gF8zqW-x7iDLO_jLCbR1eW0Ogn9llHGj3CoIN4mELQY`

**Base URL:** `https://api.poe.com/v1/chat/completions`

**Docs:** https://poe.com/api

## Pricing Overview

Подписки Poe включают API-доступ. OpenAI-compatible.

| Plan | Monthly | Points |
|------|---------|--------|
| Base | €4.79 | 10K/day (~300K/month) |
| Standard | €19.17 | 660K/month |
| Pro | €47.92 | 1.65M/month |
| Pro+ | €95.83 | 3.3M/month |
| Max | €239.58 | 8.25M/month |

> Prices shown in EUR (billed yearly). Per-token pricing available via API for each model.

## Coding Models

### Best for Agentic Coding

| Model | Input $/1M | Output $/1M | Context | Notes |
|-------|-----------|-------------|---------|-------|
| `gpt-5.5-pro` | $4.55 | $27.27 | 400K | Top tier, SWE-Bench Pro |
| `gpt-5.5` | $4.55 | $27.27 | 400K | Same quality, lower price |
| `claude-opus-4.7` | $4.29 | $21.46 | 1M | Enterprise-grade, MCP |
| `gemini-3.1-pro` | $2.02 | $12.12 | 1M | Tool calling, video/audio |
| `kimi-k2.6` | $0.96 | $4.04 | 262K | Multi-agent, 300 sub-agents |

### Cost-Effective Coding

| Model | Input $/1M | Output $/1M | Context | Notes |
|-------|-----------|-------------|---------|-------|
| `seed-2.0-code` | $0.63 | $3.79 | 256K | Enterprise coding, front-end |
| `gpt-5.4` | $2.27 | $13.64 | 400K | Balanced price/quality |
| `deepseek-v4-pro-el` | $1.67 | $3.33 | 1M | 49B active MoE |
| `qwen3.6-max-preview` | $1.31 | $7.88 | 256K | Vibe coding |
| `deepseek-v4-flash-el` | $0.14 | $0.28 | 1M | Fast, cheap |

### Reasoning Models

| Model | Pricing | Context | Notes |
|-------|---------|---------|-------|
| `deepseek-r1` | $0.018/request | 160K | Open-source reasoning rivaling o1 |
| `grok-4.3` | $1.26/1M in, $2.53/1M out | 1M | Factual accuracy, xAI |

## Image Generation

| Model | Pricing | Notes |
|-------|---------|-------|
| `gpt-image-2` | $5.05/1K prompt | OpenAI, generation + editing |
| `nano-banana-2` | $0.51/1K prompt + $0.06/image | Google, 4K output |

## Video Generation

| Model | Pricing | Notes |
|-------|---------|-------|
| `happyhorse-1.0-el` | — | ByteDance, T2V/I2V/R2V |

## Other Notable Models

- `gpt-5.4-nano` — $0.18/1M in, fast/cheap
- `gpt-5.4-mini` — $0.68/1M in, balanced
- `minimax-m2.7-fw` — $0.0061/request, agentic
- `mimo-v2.5-pro` — $1.01/1M in, multimodal 1M context

## Integration (Hermes)

OpenAI-compatible. Add as custom provider:

```yaml
providers:
  poe:
    api_key: "sk-poe-gF8zqW-x7iDLO_jLCbR1eW0Ogn9llHGj3CoIN4mELQY"
    base_url: "https://api.poe.com/v1"
```

## Notes

- Tool calling поддерживается на большинстве моделей
- Streaming работает
- Cache read: ~50% от prompt цены

Связано: [[tech/poe-chutes-comparison]] — сравнение Poe API и Chutes AI