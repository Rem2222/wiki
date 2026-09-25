---
description: OpenViking MCP Bridge — MCP Streamable HTTP → OpenViking REST API. Порт 8901, systemd openviking-mcp.
tags:
  - ops
  - service
  - memory
  - mcp
type: service
related:
  - ops/services/openviking
  - ops/services/hermes-agent
service:
  name: openviking-mcp
  category: memory
  purpose: MCP-мост для внешних клиентов (LLaMA, OpenClaw, DSH) к OpenViking REST API
  install_date: 2026-09-06
  last_verified: 2026-09-26
  health_url: "http://localhost:8901/"
  type: systemd
  ports:
    -
      port: 8901
      protocol: tcp
      bind: 0.0.0.0
      description: MCP Streamable HTTP (SSE)
  systemd_units:
    - openviking-mcp
  processes:
    -
      pattern: openviking-mcp.py
  config_paths:
    - /etc/systemd/system/openviking-mcp.service
    - /root/scripts/openviking-mcp.py
  logs: journalctl -u openviking-mcp
  depends_on:
    - openviking
  notes: >-
    FastMCP-bridge (Python). Инструменты: viking_search, viking_read, viking_browse, viking_remember.
    Auth: Authorization: Bearer <key> через Starlette middleware — GET / без ключа отдаёт 401 (норма).
    Внешний URL: https://rem2222.top/openviking-mcp/ (nginx proxy, CORS для браузерных MCP-клиентов).
---

# OpenViking MCP Bridge

OpenViking не имеет встроенного MCP-сервера — этот systemd-сервис мостит MCP Streamable HTTP
на REST API OpenViking (`http://127.0.0.1:8900`). Скрипт: `/root/scripts/openviking-mcp.py`.

## Проверка

```bash
systemctl is-active openviking-mcp
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8901/   # 401 без ключа = жив
journalctl -u openviking-mcp --since "24 hours ago" --no-pager | tail
```

Подробнее: скилл `memory-management`, раздел «MCP Bridge для внешних клиентов».
