---
description: Cockpit — веб-админка сервера (systemd, логи, сеть).
tags:
  - ops
  - service
  - system
type: service
related:
  - ops/services/duc
service:
  name: cockpit
  category: system
  purpose: Веб-интерфейс управления сервером
  install_date: 2025-06
  last_verified: 2026-07-19
  health_url: "http://localhost:9090/"
  type: systemd
  ports:
    -
      port: 9090
      protocol: tcp
      bind: 127.0.0.1
      description: Web UI
  systemd_units:
    - cockpit
    - cockpit-tcp-proxy
  depends_on:
    - nginx
  notes: Через /cockpit/.
---
