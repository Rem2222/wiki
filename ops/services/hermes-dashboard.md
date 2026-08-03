---
description: Hermes Dashboard — веб-интерфейс для Hermes Agent.
tags:
  - ops
  - service
  - core
type: service
related:
  - ops/services/hermes-agent
service:
  name: hermes-dashboard
  category: core
  purpose: Веб-дашборд Hermes Agent
  install_date: 2025-06
  last_verified: 2026-08-04
  health_url: "http://localhost:9119/"
  type: systemd
  ports:
    -
      port: 9119
      protocol: tcp
      bind: 127.0.0.1
      description: Dashboard
  systemd_units:
    - hermes-dashboard
  depends_on:
    - hermes-agent
    - nginx
  notes: Через /hermes/. SPA.
---
