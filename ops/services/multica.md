---
description: "Multica — платформа управления AI-агентами. Frontend :3001, Backend :8080."
tags:
  - ops
  - service
  - core
type: service
related:
  - ops/services/nginx
  - ops/services/postgresql
service:
  name: multica
  category: core
  purpose: Платформа управления AI-агентами
  install_date: 2025-05
  last_verified: 2026-08-15
  health_url: "http://localhost:8080/health"
  type: docker-compose
  ports:
    -
      port: 3001
      protocol: tcp
      bind: 127.0.0.1
      description: Frontend
    -
      port: 8080
      protocol: tcp
      bind: 127.0.0.1
      description: Backend
    -
      port: 9092
      protocol: tcp
      bind: 127.0.0.1
      description: Backend internal web UI (host :9092 → container :9091)
    -
      port: 3002
      protocol: tcp
      bind: 0.0.0.0
      description: Grafana (host network)
    -
      port: 9093
      protocol: tcp
      bind: 0.0.0.0
      description: Prometheus (host network)
    -
      port: 9100
      protocol: tcp
      bind: 127.0.0.1
      description: Node Exporter
    -
      port: 19514
      protocol: tcp
      bind: 127.0.0.1
      description: CLI listener
  docker_containers:
    - multica-frontend-1
    - multica-backend-1
    - multica-postgres-1
    - multica-grafana
    - multica-prometheus
    - multica-node-exporter
  depends_on:
    - nginx
    - postgresql
  data_size_hint: 152 MB (PG)
  notes: v0.3.31.
---