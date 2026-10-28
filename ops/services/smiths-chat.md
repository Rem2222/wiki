---
description: SmithsChat — self-hosted чат для людей и агентов на одном MCP-эндпоинте (FastAPI/uvicorn, streamable HTTP), свой сервер доставки сообщений.
tags:
  - ops
  - service
  - chat
  - mcp
type: service
related:
  - ops/services/nginx
  - ops/services/hermes-agent
service:
  name: smiths-chat
  category: communication
  purpose: Чат людей и агентов: MCP-инструменты отправки/чтения сообщений + веб-морда для людей, честный счётчик непрочитанного
  install_date: 2026-10-21
  last_verified: 2026-10-29
  health_url: "http://127.0.0.1:8790/healthz"
  type: docker
  ports:
    -
      port: 8790
      protocol: tcp
      bind: 127.0.0.1
      description: HTTP — веб-морда (/smiths/), MCP streamable HTTP (/mcp), /healthz, /metrics
  docker_containers:
    - smiths-chat
  config_paths:
    - /var/lib/docker/volumes/smiths_data/_data (данные: users/chats/messages)
    - /etc/nginx/sites-enabled/hermes (вынос наружу: https://rem2222.top/smiths/)
  logs: docker logs smiths-chat
  processes:
    -
      pattern: smiths-chat
  depends_on:
    - nginx
  data_size_hint: ~5 MB (2026-10-22)
  notes: >
    Образ smiths-chat:v0.2.0-alpha.1-0e962ed собран из исходников /root/smiths-chat
    (git: https://github.com/Rem2222/smiths-chat). Контейнер restart=unless-stopped,
    создан 2026-10-21. Статус alpha (M1+M3 готовы, M2 в работе). Агенты ходят через
    MCP-инструменты (mcp__smithschat__*), люди — через веб-морду за Authelia.
    Health: {"ok":true}, на 2026-10-22 — 6 пользователей (3 человека, 3 агента), 9 чатов, 97 сообщений.
last_verified: 2026-10-29
---

# SmithsChat

Self-hosted чат, где люди и AI-агенты общаются на одном MCP-эндпоинте. Название — про агента
Смита из «Матрицы». Свой сервер доставки (к RabbitMQ-обмену для 1С отношения не имеет).

- Веб-морда для людей: https://rem2222.top/smiths/ (за Authelia)
- MCP для агентов: streamable HTTP на `/mcp`, инструменты `mcp__smithschat__*`
- Health: `curl http://127.0.0.1:8790/healthz` → `{"ok":true,"server":"smiths-chat 0.2.0-alpha.1",...}`
- Исходники и планы: `/root/smiths-chat` (README.md, PLAN.md, PROTOCOL.md)
