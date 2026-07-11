---
description: Cloudflare WARP — VPN-клиент для обхода блокировок.
tags:
  - ops
  - service
  - network
type: service
related:
  []
service:
  name: warp
  category: network
  purpose: Cloudflare WARP VPN (обход блокировок)
  install_date: 2025-06
  last_verified: 2026-07-12
  health_url: 
  type: standalone
  ports:
    -
      port: 40000
      protocol: tcp
      bind: 127.0.0.1
      description: warp-svc
  depends_on:
    []
  last_verified: 2026-07-12
  notes: warp-svc активен. CLI требует --accept-tos. Есть systemd таймер auto-recovery.
---
