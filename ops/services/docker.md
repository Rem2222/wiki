---
description: Docker engine — 41 образ, 16 контейнеров.
tags:
  - ops
  - service
  - system
type: service
related:
  - ops/services/unattended-upgrades
  - ops/services/multica
service:
  name: docker
  category: system
  purpose: Контейнеризация сервисов
  install_date: 2025-05
  last_verified: 2026-07-27
  health_url: 
  type: systemd
  systemd_units:
    - docker
    - containerd
  depends_on:
    []
  notes: 41 images, 16 containers, 10 GB disk.
---
