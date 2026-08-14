---
description: AgentMemory Prometheus Exporter — метрики памяти агента.
tags:
  - ops
  - service
  - monitoring
type: service
related:
  - ops/services/agentmemory
service:
  name: agentmemory-exporter
  category: monitoring
  purpose: Prometheus метрики AgentMemory
  install_date: 2026-07-03
  last_verified: 2026-08-15
  health_url: 
  type: systemd
  ports:
    -
      port: 8000
      protocol: tcp
      bind: 0.0.0.0
      description: Metrics endpoint
  systemd_units:
    - agentmemory-exporter
  depends_on:
    - agentmemory
  notes: Python /opt/multica-monitoring/agentmemory_exporter.py.
---