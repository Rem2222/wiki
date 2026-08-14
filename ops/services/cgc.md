---
description: CGC (CodeGraphContext) — MCP-сервер для графа кода Multica.
tags:
  - ops
  - service
  - agent-platform
type: service
related:
  - ops/services/codegraph
service:
  name: cgc
  category: agent-platform
  purpose: MCP-сервер для кодовой базы Multica
  install_date: 2026-07-03
  last_verified: 2026-08-15
  health_url: "http://localhost:51234/"
  type: systemd
  ports:
    -
      port: 51234
      protocol: tcp
      bind: 127.0.0.1
      description: API
  systemd_units:
    - cgc-daemon
  depends_on:
    []
  notes: "Python uv tool. Документация: github.com/CodeGraphContext/CodeGraphContext."
---