---
description: mcporter — CLI-клиент для управления MCP-серверами (Model Context Protocol).
tags: [tools, cli, mcp, ai]
related:
  - concepts/mcp
created: 2026-08-03
---

# mcporter

CLI-клиент для работы с MCP-серверами (Model Context Protocol). Позволяет подключать, запускать и управлять MCP-серверами из командной строки.

Установлен через npm (v0.12.3), симлинк `/usr/local/bin/mcporter` (2026-08-02). Пакет в `/usr/local/lib/node_modules/mcporter`.

## Команды

```bash
mcporter --version
mcporter list        # список MCP-серверов
mcporter add <name>  # добавить MCP-сервер
mcporter run <name>  # запустить MCP-сервер
```

## Связано

- `concepts/mcp` — протокол Model Context Protocol
- `ops/services/codegraph` — MCP-сервер графа кода
