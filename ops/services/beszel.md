---
description: Beszel hub + agent — мониторинг ресурсов.
tags:
  - ops
  - service
  - monitoring
type: service
related:
  - ops/services/multi-exporter
service:
  name: beszel
  category: monitoring
  purpose: Мониторинг CPU/RAM/диска
  install_date: 2025-06
  last_verified: 2026-07-19
  health_url: "http://localhost:9480/"
  type: docker
  ports:
    -
      port: 9480
      protocol: tcp
      bind: 127.0.0.1
      description: Hub UI
    -
      port: 45876
      protocol: tcp
      bind: 127.0.0.1
      description: Agent
  docker_containers:
    - beszel
    - beszel-agent
  depends_on:
    []
  notes: Доступ через /beszel/.
---
