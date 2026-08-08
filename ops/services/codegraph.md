---
description: CodeGraph — MCP-сервер для графа кода (Tree-sitter).
tags:
  - ops
  - service
  - agent-platform
type: service
related:
  - ops/services/cgc
  - ops/workflow/new-project-with-codegraph
service:
  name: codegraph
  category: agent-platform
  purpose: MCP-сервер для анализа кода
  install_date: 2025-06
  last_verified: 2026-08-09
  health_url: http://localhost:51234/health
  type: systemd
  ports:
    -
      port: 3748
      protocol: tcp
      bind: 127.0.0.1
      description: HTTP
    -
      port: 51234
      protocol: tcp
      bind: 127.0.0.1
      description: Health endpoint
  systemd_units:
    - codegraph.service
  depends_on:
    []
  notes: tree-sitter код-граф. Стандартный stdio MCP.
---
