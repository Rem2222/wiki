---
description: Cloudflare WARP — VPN-клиент, ставился для обхода обрывов "incomplete chunked read" при доступе к opencode.ai. Сейчас не используется (ALL_PROXY закомментирован).
tags:
  - ops
  - service
  - network
type: service
related:
  - ops/services/tor
  - ops/services/tailscale
  - tech/free-llm-api-resources
service:
  name: warp
  category: network
  purpose: Cloudflare WARP VPN (обход обрывов chunked read у opencode.ai)
  install_date: 2026-06-03
  last_verified: 2026-08-17
  health_url: 
  type: systemd
  ports:
    -
      port: 40000
      protocol: tcp
      bind: 127.0.0.1
      description: warp-svc (SOCKS5/HTTP прокси, режим WarpProxy)
  systemd_units:
    - warp-svc
  depends_on:
    []
  notes: >
    Установлен 3 июня 2026 (apt-get install -y cloudflare-warp) из-за проблемы с opencode.ai.
    Есть systemd таймер warp-health (каждые 5 мин проверяет прокси). С 2 августа 2026
    ALL_PROXY в ~/.hermes/.env закомментирован — прокси никто не использует. Можно удалить.
    Проверено 2026-08-12: warp-svc полностью удалён с сервера (нет процесса, бинарника,
    /etc/warp, unit warp-svc.service). Запись оставлена как историческая; удалить при следующей чистке реестра.
---