---
description: DUC (Disk Usage) — CGI-визуализация диска.
tags:
  - ops
  - service
  - system
type: service
related:
  []
service:
  name: duc
  category: system
  purpose: Визуализация использования диска
  install_date: 2025-05
  last_verified: 2026-07-10
  health_url: "http://localhost:8081/"
  type: standalone (python CGI)
  ports:
    -
      port: 8081
      protocol: tcp
      bind: 127.0.0.1
      description: CGI
  systemd_units:
    - duc-server
  depends_on:
    []
  notes: Через /duc/. Индекс обновляется каждые 2ч.
---
