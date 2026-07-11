---
description: Multi-service Prometheus Exporter — метрики ntfy, GBrain, Hermes, FreeLLMAPI.
tags:
  - ops
  - service
  - monitoring
type: service
related:
  []
service:
  name: multi-exporter
  category: monitoring
  purpose: Prometheus метрики для нескольких сервисов
  install_date: 2026-07-03
  last_verified: 2026-07-12
  health_url: 
  type: systemd
  ports:
    -
      port: 8001
      protocol: tcp
      bind: 0.0.0.0
      description: Metrics endpoint
  systemd_units:
    - multi-exporter
  depends_on:
    []
  notes: "1.2G RAM. CPU: 16ч за 2 дня. Возможно течёт память."
---
