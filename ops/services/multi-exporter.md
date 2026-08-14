---
description: Multi-service Prometheus Exporter — метрики ntfy, GBrain, Hermes, FreeLLMAPI.
tags:
  - ops
  - service
  - monitoring
type: service
related:
  - ops/services/beszel
  - ops/services/ntfy
service:
  name: multi-exporter
  category: monitoring
  purpose: Prometheus метрики для нескольких сервисов
  install_date: 2026-07-03
  last_verified: 2026-08-15
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
  notes: "CACHE_DURATION поднят 30с → 1800с (30 мин) 2026-08-05: раньше каждые 30с гонял gbrain doctor (bun-процесс), из-за чего cgroup весила ~1.1-1.9G. Теперь doctor раз в 30 мин."
---