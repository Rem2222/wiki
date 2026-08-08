---
description: Unattended Upgrades — автоматические обновления безопасности.
tags:
  - ops
  - service
  - system
type: service
related:
  - ops/services/docker
service:
  name: unattended-upgrades
  category: system
  purpose: Автообновления безопасности
  install_date: 2025-05
  last_verified: 2026-08-09
  health_url: 
  type: systemd
  systemd_units:
    - unattended-upgrades
  depends_on:
    []
  last_verified: 2026-08-09
  notes: "Active. Последние обновления: vim, ncurses, libnghttp2."
---
