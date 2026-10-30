---
description: "Agents Anywhere — self-hosted open-source agent workbench (форк anywhere-labs), доступ к агентам с телефона/Web; интеграция Hermes через ACP-адаптер. Порт 5174."
tags:
  - ops
  - service
  - agents
  - acp
type: service
related:
  - "[[ops/services/hermes-agent]]"
  - "[[ops/services/docker]]"
service:
  name: agents-anywhere
  category: agents
  purpose: Self-hosted рабочий стол для AI-агентов (Codex / Claude Code / DeepSeek Harness / Hermes): сессии, файлы, терминал с телефона или Web
  install_date: 2026-10-11
  last_verified: 2026-10-31
  health_url: "http://localhost:5174/"
  type: docker
  ports:
    -
      port: 5174
      protocol: tcp
      bind: 0.0.0.0
      description: Web UI сервера (docker-proxy → контейнер :8000)
  systemd_units:
    - agents-anywhere-connector
  docker_containers:
    - agents-anywhere-server-next-1
    - agents-anywhere-postgres-next-1
    - agents-anywhere-redis-next-1
  config_paths:
    - /root/agents-anywhere/docker/docker-compose.local.yml
    - /root/agents-anywhere/.env.local
  logs:
    - "docker logs agents-anywhere-server-next-1"
  depends_on:
    - docker
  data_size_hint: "~1 ГБ образы + volume agents-anywhere_agents-anywhere-pg-next (PG 17)"
  notes: >
    Поставлен Романом 2026-10-11 (клон github.com/Rem2222/Agents-Anywhere, форк
    anywhere-labs/Agents-Anywhere v2.0.3). Стек: server (uv, python -m
    agent_server.main) + postgres:17-alpine + redis:8-alpine, compose-файл
    docker/docker-compose.local.yml, запуск через local-up.sh / docker compose.
    Кастомные коммиты Романа: «feat(con): add ACP agent runtime adapter (Hermes
    via hermes acp)» — Hermes подключается как ACP-runtime (бинарь hermes-acp
    в /usr/local/bin). 2026-10-11 19:03 запущен cloudflared quick-tunnel
    (`cloudflared tunnel --url http://127.0.0.1:5174`) — эфемерный публичный
    URL, меняется при рестарте; сам процесс не в автозапуске. Миграции БД —
    контейнер agents-anywhere-migrate-next-1 (одноразовый, Exited 0 — норма).
    Обслуживание: рестарт через docker compose в /root/agents-anywhere/docker;
    обновления — git pull + пересборка образа. Рядом крутится отдельный
    юнит agents-anywhere-connector.service (создан 2026-10-20 20:08,
    enabled, active): `uv run anywhere-cli start --config
    /root/.agents-anywhere/connector.json`, WorkingDirectory
    /root/agents-anywhere/connector — коннектор, который держит связь с
    удалённым сервером Agents Anywhere (см. MUL-10274).
last_verified: 2026-10-31
---
