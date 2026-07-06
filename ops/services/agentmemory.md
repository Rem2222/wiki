---
description: "AgentMemory / III engine — память агента. III :3111-3112, MCP :3113."
tags:
  - ops
  - service
  - agent-platform
type: service
related:
  - ops/services/hermes-agent
service:
  name: agentmemory
  category: agent-platform
  purpose: Долговременная память агента
  install_date: 2025-06
  last_verified: 2026-07-07
  health_url: "http://localhost:3113/"
  type: docker + systemd
  ports:
    -
      port: 3111
      protocol: tcp
      bind: 127.0.0.1
      description: III engine REST
    -
      port: 3112
      protocol: tcp
      bind: 127.0.0.1
      description: III streams (WS)
    -
      port: 3113
      protocol: tcp
      bind: 127.0.0.1
      description: MCP viewer
    -
      port: 9464
      protocol: tcp
      bind: 127.0.0.1
      description: Prometheus
    -
      port: 49134
      protocol: tcp
      bind: 127.0.0.1
      description: III WS engine
  systemd_units:
    - agentmemory
    - agentmemory-exporter
  docker_containers:
    - agentmemory-iii-engine-1
  processes:
    -
      pattern: iii --config
      description: III engine
    -
      pattern: @agentmemory/mcp
      description: MCP service
  config_paths:
    - /root/.hermes/config.yaml
    - /root/.agentmemory/
  depends_on:
    []
  notes: /agentmemory/health 404. REST consolidation не работает.
---
