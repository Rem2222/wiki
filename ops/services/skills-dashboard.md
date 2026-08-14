---
description: Skills Approval Dashboard — веб-интерфейс для утверждения навыков Hermes.
tags:
  - ops
  - service
  - agent-platform
type: service
related:
  - ops/services/hermes-agent
service:
  name: skills-dashboard
  category: agent-platform
  purpose: Веб-дашборд для approval навыков Hermes
  install_date: 2026-07-06
  last_verified: 2026-08-15
  health_url: "http://localhost:8650/"
  type: systemd
  ports:
    -
      port: 8650
      protocol: tcp
      bind: 0.0.0.0
      description: Dashboard
  systemd_units:
    - skills-dashboard
  processes:
    -
      pattern: skills-dashboard/server.py
      description: Python HTTP server (zero deps)
  config_paths:
    - /root/.hermes/scripts/skills-dashboard/
  depends_on:
    - hermes-agent
    - nginx
  last_verified: 2026-08-14
  notes: "Через /skills/. Утверждение/отклонение pending навыков."
---