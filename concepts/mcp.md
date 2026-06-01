---
description: Model Context Protocol — открытый протокол для интеграции AI-агентов с внешними инструментами
tags: [mcp, protocol, integration, ai]
related: [[tech/context7]] [[tech/serena-mcp]] [[tech/claude-plugin-dev-tools]]
---

# Model Context Protocol (MCP)

Открытый протокол, стандартизирующий подключение внешних инструментов и источников данных к AI-агентам. Позволяет агенту вызывать внешние функции (tools) и получать данные (resources) через единый интерфейс.

## Как работает

- **MCP Server** — предоставляет инструменты (tools) и ресурсы
- **MCP Client** (агент) — вызывает инструменты через JSON-RPC
- **Транспорт:** stdio (локальные процессы) или HTTP/SSE (удалённые серверы)

## MCP-серверы в вики

- [[tech/context7]] — документация библиотек
- [[tech/serena-mcp]] — LSP для Claude Code
- [[tech/claude-plugin-dev-tools]] — создание своих MCP

## Skills vs MCP

Технически отличаются радикально, но для модели выглядят одинаково: краткое описание → развёрнутое по запросу → вызов тула.
