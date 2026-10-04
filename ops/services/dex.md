---
description: "Dex Control Center — веб-дашборд и API управления агентом Dex (proactive agent)."
tags:
  - ops
  - service
  - agent-platform
type: service
related:
  - ops/services/hermes-agent
  - ops/services/mercury
  - ops/services/jawl
service:
  name: dex
  category: agent-platform
  purpose: Веб-дашборд и REST API для управления проактивным агентом Dex
  install_date: 2026-07-08
  last_verified: 2026-10-04
  health_url: "http://localhost:3333/"
  type: systemd (user)
  ports:
    -
      port: 3333
      protocol: tcp
      bind: 127.0.0.1
      description: Dashboard UI + REST API
  systemd_units:
    - dex-control
    - dex-poller
  docker_containers: []
  processes:
    -
      pattern: dex_control.py
      description: Flask dashboard & API
    -
      pattern: dex_poller.py
      description: Telegram poller daemon
  config_paths:
    - ~/.hermes/proactive/identity.yaml
    - ~/.hermes/proactive/.env
    - ~/.hermes/proactive/heartbeat.py
    - ~/.hermes/proactive/dex_poller.py
    - ~/.hermes/proactive/dex_control.py
    - ~/.hermes/proactive/vec_build.py
    - ~/.hermes/proactive/lib/vec0.so
  depends_on:
    - gemini-web2api
  notes: >-
    Проактивный агент: три процесса — dex-poller (Telegram, 3 с), dex-control
    (Flask :3333), dex-heartbeat (cron каждые 10 мин, no-agent). Красная кнопка:
    touch ~/.hermes/proactive/DISABLED. LLM — gemini-web2api :8083 (env
    DEX_API_URL/DEX_API_KEY/DEX_MODEL в .env, сейчас gemini-3.5-flash).
    Nginx: /dex/ за Authelia. Свой venv ~/.hermes/proactive/venv (flask 3.1.3) —
    в venv Hermes flask НЕТ, ставить туда не надо. Векторная память:
    sqlite-vec (vec0.so из wheel, без pip из-за PEP 668) + bge-m3 через Ollama,
    сборка vec_build.py (дедупликация: 1362 тика = 69 уникальных текстов).
    Проверено 2026-09-30: оба юнита enabled+active, NRestarts=0 (был crash-loop
    из-за отсутствия flask, счётчик дошёл до 290 794). Git: Rem2222/dex-agent.
    Подробное устройство: [[tech/dex-internals]].
last_verified: 2026-10-05
---