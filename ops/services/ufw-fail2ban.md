---
description: UFW + Fail2ban — фаервол и защита.
tags:
  - ops
  - service
  - security
type: service
related:
  - ops/services/sshd
service:
  name: ufw-fail2ban
  category: security
  purpose: Фаервол + защита от брутфорса
  install_date: 2025-05
  last_verified: 2026-08-17
  health_url: 
  type: systemd
  systemd_units:
    - fail2ban
  depends_on:
    []
  last_verified: 2026-08-17
  notes: "UFW: active. Fail2ban: 4 banned IP."
---