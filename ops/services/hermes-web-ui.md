---
description: Hermes Web UI (Hermes Studio) — веб-интерфейс Hermes Agent: сессии, чат, управление. Порт 5173.
tags:
  - ops
  - service
  - core
  - hermes
type: service
related:
  - ops/services/hermes-agent
  - ops/services/hermes-dashboard
service:
  name: hermes-web-ui
  category: core
  purpose: Веб-интерфейс Hermes (Hermes Studio) — сессии и управление агентом
  install_date: 2026-08-18
  last_verified: 2026-09-26
  health_url: "http://localhost:5173/"
  type: systemd
  ports:
    -
      port: 5173
      protocol: tcp
      bind: 0.0.0.0
      description: Web UI (Vite default port)
  systemd_units:
    - hermes-web-ui
  processes:
    -
      pattern: hermes-web-ui
  config_paths:
    - /etc/systemd/system/hermes-web-ui.service
    - /root/.hermes-web-ui/server.pid
  logs: journalctl -u hermes-web-ui
  depends_on:
    - hermes-agent
  notes: >-
    Пакет v0.6.44 в /usr/lib/node_modules/hermes-web-ui, бинарь /usr/bin/hermes-web-ui.
    Type=forking, PIDFile /root/.hermes-web-ui/server.pid, NODE_ENV=production.
    Отвечает 200 на /. Не путать с hermes-dashboard (:9119) — это отдельный дашборд.
---

# Hermes Web UI

Веб-интерфейс Hermes (также известен как Hermes Studio) — Node.js-сервер (`hermes-web-ui start --port 5173`),
systemd-юнит `hermes-web-ui.service`. Прямой доступ на `http://localhost:5173/` (0.0.0.0, вход — UFW/nginx).

## Проверка

```bash
systemctl is-active hermes-web-ui
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:5173/   # 200
journalctl -u hermes-web-ui --since "24 hours ago" --no-pager | tail
```
