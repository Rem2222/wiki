---
description: Mercury Agent Dashboard — дашборд для Mercury Agent.
tags:
  - ops
  - service
  - monitoring
type: service
related:
  []
service:
  name: mercury
  category: monitoring
  purpose: Дашборд Mercury Agent
  install_date: 2026-07-03
  last_verified: 2026-07-10
  health_url: "http://localhost:6174/"
  type: standalone
  ports:
    -
      port: 6174
      protocol: tcp
      bind: 127.0.0.1
      description: Dashboard
  depends_on:
    - nginx
  notes: "Через /mercury/. Уже есть страница в wiki: tech/Mercury-Agent-Skills.md."
---
