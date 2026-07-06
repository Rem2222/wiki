---
description: "SSH-сервер на нестандартном порту :22022."
tags:
  - ops
  - service
  - system
type: service
related:
  []
service:
  name: sshd
  category: system
  purpose: SSH-доступ к серверу
  install_date: 2025-05
  last_verified: 2026-07-07
  health_url: 
  type: systemd
  ports:
    -
      port: 22022
      protocol: tcp
      bind: 0.0.0.0
      description: SSH
  systemd_units:
    []
  depends_on:
    []
  notes: Нестандартный порт.
---
