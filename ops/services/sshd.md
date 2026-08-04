---
description: "SSH-сервер на нестандартном порту :22022."
tags:
  - ops
  - service
  - system
type: service
related:
  - ops/services/ufw-fail2ban
service:
  name: sshd
  category: system
  purpose: SSH-доступ к серверу
  install_date: 2025-05
  last_verified: 2026-08-05
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
  last_verified: 2026-08-05
  notes: Нестандартный порт.
---
