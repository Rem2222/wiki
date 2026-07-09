---
description: GBrain — графовая база знаний, семантический поиск, код-граф, MCP.
tags:
  - ops
  - service
  - core
type: service
related:
  - ops/services/postgresql
  - ops/services/nginx
service:
  name: gbrain
  category: core
  purpose: Graph-based knowledge brain
  install_date: 2025-06
  last_verified: 2026-07-10
  health_url: "http://localhost:3131/health"
  type: systemd + docker
  ports:
    -
      port: 3131
      protocol: tcp
      bind: 127.0.0.1
      description: HTTP (Admin + MCP)
  systemd_units:
    - gbrain-http
  docker_containers:
    - gbrain-postgres
  processes:
    -
      pattern: gbrain.*serve
      description: HTTP-сервер
    -
      pattern: gbrain.*autopilot
      description: Автопилот wiki
    -
      pattern: gbrain.*jobs
      description: Worker
  config_paths:
    - /root/gbrain/
    - /root/.gbrain/
  logs:
    - /root/.gbrain/autopilot.err
  depends_on:
    - postgresql
    - nginx
  data_size_hint: 42 MB (PG)
  notes: v0.41.26.0. 3 serve-процесса.
---
