---
description: FreeLLMAPI — универсальный LLM-роутер (OpenAI-совместимый).
tags:
  - ops
  - service
  - llm-proxy
type: service
related:
  - ops/services/freedeepseekapi
  - ops/services/gemini-web2api
service:
  name: freellmapi
  category: llm-proxy
  purpose: Unified LLM API router
  install_date: 2025-06
  last_verified: 2026-07-22
  health_url: "http://localhost:3010/v1/models"
  type: docker
  ports:
    -
      port: 3010
      protocol: tcp
      bind: 127.0.0.1
      description: API
  docker_containers:
    - freellmapi-freellmapi-1
  depends_on:
    []
  notes: Через /v1/ и /freellmapi/.
---
