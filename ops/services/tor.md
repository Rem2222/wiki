---
description: "Tor SOCKS5 прокси — анонимный доступ к .onion сайтам и обход блокировок через DuckDuckGo Onion"
tags:
  - ops
  - service
  - proxies
type: service
related:
  - ops/services/warp
  - ops/services/tailscale
service:
  name: tor
  category: proxies
  purpose: Анонимный SOCKS5 прокси для обхода блокировок и поиска через DuckDuckGo Onion
  install_date: "2024"
  last_verified: 2026-08-12
  health_url: ""
  type: systemd
  ports:
    -
      port: 9050
      protocol: tcp
      bind: 127.0.0.1
      description: SOCKS5 прокси
    -
      port: 9053
      protocol: tcp
      bind: 127.0.0.1
      description: DNS резолвер (DNSPort)
  systemd_units:
    - tor@default
  docker_containers: []
  processes:
    -
      pattern: /usr/bin/tor
      description: Tor daemon
  config_paths:
    - /etc/tor/torrc
  logs:
    - journalctl -u tor@default
  depends_on: []
  data_size_hint: "~135MB RAM"
  notes: |
    Используется Hermes для поиска в интернете через DuckDuckGo Onion (curl через SOCKS5 127.0.0.1:9050).
    Установлен как systemd сервис tor@default.service.
    ALL_PROXY=socks5://127.0.0.1:40000 — основной прокси, Tor на :9050 для специальных случаев.
    В конфиге torrc настроен ExitNodes {ru}, StrictNodes 1 для российских выходных нод.
---