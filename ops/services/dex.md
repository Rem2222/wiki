---
description: "Dex Control Center — веб-дашборд и API управления агентом Dex (proactive agent)."
tags:
  - ops
  - service
  - agent-platform
type: service
related:
  - ops/services/hermes-agent
  - ops/services/mercury
  - ops/services/jawl
service:
  name: dex
  category: agent-platform
  purpose: Веб-дашборд и REST API для управления проактивным агентом Dex
  install_date: 2026-07-08
  last_verified: 2026-07-20
  health_url: "http://localhost:3333/"
  type: systemd (user)
  ports:
    -
      port: 3333
      protocol: tcp
      bind: 127.0.0.1
      description: Dashboard UI + REST API
  systemd_units:
    - dex-control
    - dex-poller
  docker_containers: []
  processes:
    -
      pattern: dex_control.py
      description: Flask dashboard & API
    -
      pattern: dex_poller.py
      description: Telegram poller daemon
  config_paths:
    - ~/.hermes/proactive/identity.yaml
    - ~/.hermes/proactive/.env
  depends_on:
    - hermes-agent
  notes: "Proactive-агент Dex: heartbeat, poller, dashboard. Skill: dex-identity. Nginx: /dex/ (за Authelia)."
---
