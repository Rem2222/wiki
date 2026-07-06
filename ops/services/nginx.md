---
description: Nginx + SSL (Let's Encrypt) — обратный прокси, Authelia SSO.
tags:
  - ops
  - service
  - core
type: service
related:
  - ops/services/authelia
  - ops/services/multica
  - ops/services/gbrain
service:
  name: nginx
  category: core
  purpose: Обратный прокси, HTTPS, Authelia SSO
  install_date: 2025-05
  last_verified: 2026-07-07
  health_url: "http://localhost:80/"
  type: systemd
  ports:
    -
      port: 80
      protocol: tcp
      bind: 0.0.0.0
      description: HTTP redirect
    -
      port: 443
      protocol: tcp
      bind: 0.0.0.0
      description: HTTPS
  systemd_units:
    - nginx
  config_paths:
    - /etc/nginx/sites-enabled/hermes
  logs:
    - /var/log/nginx/error.log
    - /var/log/nginx/access.log
  depends_on:
    - authelia
  notes: 20+ location блоков.
---
