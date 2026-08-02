---
description: Cloudflare WARP — VPN-клиент для обхода блокировок.
tags:
  - ops
  - service
  - network
type: service
related:
  - ops/services/tor
  - ops/services/tailscale
service:
  name: warp
  category: network
  purpose: Cloudflare WARP VPN (обход блокировок)
  install_date: 2025-06
  last_verified: 2026-08-03
  health_url: 
  type: systemd
  ports:
    -
      port: 40000
      protocol: tcp
      bind: 127.0.0.1
      description: warp-svc (SOCKS5 прокси)
  systemd_units:
    - warp-svc
  depends_on:
    []
  notes: warp-svc активен. CLI требует --accept-tos. Есть systemd таймер auto-recovery.
---
