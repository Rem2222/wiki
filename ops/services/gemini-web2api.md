---
description: Gemini-web2api — OpenAI-совместимый прокси для Gemini Web.
tags:
  - ops
  - service
  - llm-proxy
type: service
related:
  - ops/services/freellmapi
  - ops/services/freedeepseekapi
service:
  name: gemini-web2api
  category: llm-proxy
  purpose: Gemini reverse proxy (OpenAI-compatible)
  install_date: 2025-06
  last_verified: 2026-08-01
  health_url: "http://localhost:8083/v1/models"
  type: docker
  ports:
    -
      port: 8083
      protocol: tcp
      bind: 0.0.0.0
      description: API
  docker_containers:
    - gemini-web2api
  depends_on:
    []
  notes: 401 Unauthorized — invalid API key.
---
