---
description: Gemini-web2api — OpenAI-совместимый прокси для Gemini Web.
tags:
  - ops
  - service
  - llm-proxy
type: service
related:
  []
service:
  name: gemini-web2api
  category: llm-proxy
  purpose: Gemini reverse proxy (OpenAI-compatible)
  install_date: 2025-06
  last_verified: 2026-07-07
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
