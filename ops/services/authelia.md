---
description: Authelia + Redis — SSO-аутентификация для сервисов.
tags:
  - ops
  - service
  - security
type: service
related:
  - ops/services/nginx
service:
  name: authelia
  category: security
  purpose: SSO аутентификация, 2FA
  install_date: 2025-05
  last_verified: 2026-08-07
  health_url: "http://localhost:9091/"
  type: docker
  ports:
    -
      port: 9091
      protocol: tcp
      bind: 127.0.0.1
      description: Authelia
  docker_containers:
    - authelia
    - authelia-redis
  depends_on:
    []
  notes: Nginx error_page 401/403.
---
