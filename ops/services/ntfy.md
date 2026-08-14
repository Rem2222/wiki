---
description: Ntfy — push-уведомления (Telegram-подобные, self-hosted).
tags:
  - ops
  - service
  - monitoring
type: service
related:
  - ops/services/monitor-ui
service:
  name: ntfy
  category: monitoring
  purpose: Push-уведомления
  install_date: 2025-06
  last_verified: 2026-08-15
  health_url: "http://localhost:2586/"
  type: docker
  ports:
    -
      port: 2586
      protocol: tcp
      bind: 0.0.0.0
      description: HTTP
  docker_containers:
    - ntfy
  depends_on:
    []
  notes: Вспомогательный канал (основной — Telegram).
---