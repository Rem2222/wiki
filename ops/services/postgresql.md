---
description: "PostgreSQL x2 — Multica (:5432) + GBrain (:5433)."
tags:
  - ops
  - service
  - storage
type: service
related:
  - ops/services/multica
  - ops/services/gbrain
service:
  name: postgresql
  category: storage
  purpose: Реляционные БД
  install_date: 2025-05
  last_verified: 2026-08-17
  health_url: 
  type: docker
  ports:
    - port: 5432
      protocol: tcp
      bind: 0.0.0.0
      description: "Multica PostgreSQL"
    - port: 5433
      protocol: tcp
      bind: 127.0.0.1
      description: "GBrain PostgreSQL"
  docker_containers:
    - multica-postgres-1
    - gbrain-postgres
  depends_on:
    []
  notes: "Multica: 12 conn, 152 MB. GBrain: 9 conn, 42 MB."
---