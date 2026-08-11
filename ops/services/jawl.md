---
description: JAWL — Just Another Workflow Library. Python-агент для автономных пайплайнов.
tags:
  - ops
  - service
  - agent-platform
type: service
related:
  - ops/services/hermes-agent
service:
  name: jawl
  category: agent-platform
  purpose: Автономный Python-агент (Jinx)
  install_date: 2025-06
  last_verified: 2026-08-12
  health_url: "http://localhost:5002/"
  type: systemd (user)
  ports:
    -
      port: 37281
      protocol: tcp
      bind: 127.0.0.1
      description: JAWL process
    -
      port: 5002
      protocol: tcp
      bind: 127.0.0.1
      description: Dashboard
  systemd_units:
    - jawl
    - jawl-dashboard
  config_paths:
    - /root/JAWL/
  logs:
    []
  depends_on:
    []
  notes: >
    Занимает 1.8G RAM. Доступ через /jawl/.
    Проверено 2026-08-12: юзер-юнит jawl.service в состоянии failed (Result: signal, KILL)
    с 2026-07-06, порты 37281/5002 не слушаются. Требуется починка/перезапуск — см. MUL-805 отчёт.
---