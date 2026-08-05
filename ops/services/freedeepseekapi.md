---
description: FreeDeepseekAPI — OpenAI-совместимый прокси для DeepSeek Web Chat.
tags:
  - ops
  - service
  - llm-proxy
type: service
related:
  - ops/services/freellmapi
  - ops/services/gemini-web2api
service:
  name: freedeepseekapi
  category: llm-proxy
  purpose: DeepSeek Web Chat proxy
  install_date: 2026-07-03
  last_verified: 2026-08-06
  health_url: "http://localhost:9655/"
  type: systemd
  ports:
    -
      port: 9655
      protocol: tcp
      bind: 127.0.0.1
      description: API
  systemd_units:
    - freedeepseekapi
  depends_on:
    []
  notes: "Через /deepseek/. Модель: deepseek-chat."
---
