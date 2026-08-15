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
  last_verified: 2026-08-16
  health_url: "http://localhost:5002/"
  type: systemd (user)
  ports:
    -
      port: 46843
      protocol: tcp
      bind: 127.0.0.1
      description: JAWL process terminal (динамический порт, см. terminal.port)
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
    Агент ~1.3G RAM, дашборд ~150M. Доступ через /jawl/.
    Проверено 2026-08-12 (MUL-806): юнит был failed (Result: signal, KILL) с 2026-07-06;
    причина — ручной kill/OOM не подтверждена (логи за дату ротированы, признаков OOM нет).
    Перезапущен: агент активен (systemctl --user start jawl), Telegram-бот @Jawl_Jinx_bot
    авторизован, LLM OpenRouter (nvidia/nemotron-3-nano-30b-a3b:free).
    Дашборд :5002 поднят и включён (systemd jawl-dashboard enabled).
    Системный jawl.service (legacy, /etc/systemd/system) оставлен disabled — работает только user-юнит.
---
