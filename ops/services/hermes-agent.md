---
description: "Hermes Agent — основной AI-агент. API :8642, Dashboard :9119, Chat :3000."
tags:
  - ops
  - service
  - core
type: service
related:
  - ops/services/gbrain
  - ops/services/nginx
  - ops/services/agentmemory
service:
  name: hermes-agent
  category: core
  purpose: AI-агент для автоматизации, gateway сообщений
  install_date: 2025-05-27
  last_verified: 2026-07-20
  health_url: "http://localhost:8642/health"
  type: standalone (python)
  ports:
    -
      port: 8642
      protocol: tcp
      bind: 0.0.0.0
      description: Hermes API
    -
      port: 3000
      protocol: tcp
      bind: 0.0.0.0
      description: Hermes Chat UI
    -
      port: 9119
      protocol: tcp
      bind: 127.0.0.1
      description: Dashboard
  systemd_units:
    - hermes-dashboard
  processes:
    -
      pattern: hermes_cli.main gateway
      description: Gateway
    -
      pattern: hermes_cli.main dashboard
      description: Dashboard
  config_paths:
    - /root/.hermes/config.yaml
    - /usr/local/lib/hermes-agent/
  logs:
    - /root/.hermes/logs/gateway.log
    - /root/.hermes/logs/agent.log
    - /root/.hermes/logs/mcp-stderr.log
  depends_on:
    - nginx
  notes: v0.18.0. SOCKS proxy блокирует pip.
---
