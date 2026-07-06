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
  last_verified: 2026-07-07
  health_url: 
  type: docker
  docker_containers:
    - multica-postgres-1
    - gbrain-postgres
  depends_on:
    []
  notes: "Multica: 12 conn, 152 MB. GBrain: 9 conn, 42 MB."
---
