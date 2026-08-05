---
description: Monitor Web UI — панель управления ntfy (компрессия и т.д.).
tags:
  - ops
  - service
  - monitoring
type: service
related:
  - ops/services/ntfy
service:
  name: monitor-ui
  category: monitoring
  purpose: Панель управления ntfy
  install_date: 2026-07-03
  last_verified: 2026-08-06
  health_url: "http://localhost:3003/"
  type: standalone (python)
  ports:
    -
      port: 3003
      protocol: tcp
      bind: 127.0.0.1
      description: Web UI
  depends_on:
    - ntfy
    - nginx
  notes: "Через /monitor/. Вкладки: компрессия, логи."
---
