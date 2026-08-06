---
description: Tailscale — mesh VPN, exit node.
tags:
  - ops
  - service
  - network
type: service
related:
  - ops/services/warp
  - ops/services/tor
service:
  name: tailscale
  category: network
  purpose: Mesh VPN, exit node
  install_date: 2025-05
  last_verified: 2026-08-07
  health_url: 
  type: systemd
  systemd_units:
    - tailscaled
  depends_on:
    []
  notes: v1.98.4. Online.
---
