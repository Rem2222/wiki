---
description: GBrain — графовая база знаний, семантический поиск, код-граф, MCP. УДАЛЁН 2026-10-03.
tags:
  - ops
  - service
  - archived
type: service
status: removed
related:
  - ops/services/zvec-wiki
service:
  name: gbrain
  category: core
  purpose: Graph-based knowledge brain
  install_date: 2025-06
  removed_date: 2026-10-03
  removed_reason: Полная замена на zvec-wiki (поиск) + wiki-health-check.py (аудит); удалены systemd-юнит, контейнер, том, /root/gbrain
  last_verified: 2026-10-08
  type: systemd + docker
  ports: []
  systemd_units: []
  docker_containers: []
  processes: []
  config_paths: []
  logs: []
  depends_on: []
  data_size_hint: "0 B (удалён)"
  notes: Удалён полностью 2026-10-03 по решению Романа. Не использовать, не поднимать заново. Поиск по вики — zvec-wiki, аудит — wiki-health-check.py (см. ops/services/zvec-wiki).
last_verified: 2026-10-09
---