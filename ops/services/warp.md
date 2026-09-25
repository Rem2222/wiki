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
  last_verified: 2026-09-26
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
  last_verified: 2026-09-26
  notes: >-
    2026-09-24: warp-svc/бинарь warp-cli/systemd-юнит в системе НЕ найдены — WARP полностью
    отсутствует (трекается в MUL-10035 / MUL-866). Исторически: CLI требовал --accept-tos,
    был systemd таймер auto-recovery, SOCKS5 на 127.0.0.1:40000.
---
