---
description: Три официальных инструмента Anthropic для разработки плагинов под Claude Code
tags: [claude-code, plugins, mcp, development, skills]
related: [[tech/agents-best-practices]] [[concepts/mcp]]
---

# Claude Code Plugin Dev Tools

Три официальных плагина от Anthropic для разработки собственных расширений Claude Code.

## plugin-dev (MCP Server Dev)

**README:** https://github.com/anthropics/claude-plugins-official/blob/main/plugins/mcp-server-dev/README.md

Инструмент для разработки, тестирования и управления MCP-серверами. Позволяет:
- Создавать новые MCP-проекты из шаблонов
- Запускать MCP-серверы в режиме разработки
- Тестировать эндпоинты и промпты
- Инспектировать и дебажить MCP-взаимодействия

## skill-creator

**README:** https://github.com/anthropics/claude-plugins-official/blob/main/plugins/skill-creator/README.md

Плагин, который позволяет Claude Code создавать, редактировать и управлять своими skills. Skills хранятся в `~/.claude/skills/`. Позволяет:
- Генерировать новые skill-файлы из NL-инструкций
- Редактировать существующие skills
- Управлять установленными skills
- Валидировать синтаксис

## mcp-server-dev (Plugin Dev)

**README:** https://github.com/anthropics/claude-plugins-official/blob/main/plugins/plugin-dev/README.md

Инструмент для создания Claude Code plugins — MCP-серверов, расширяющих возможности Claude Code. Позволяет:
- Создавать проекты плагинов из шаблонов
- Добавлять инструменты и ресурсы
- Тестировать локально без публикации
- Управлять жизненным циклом плагина

## Нужно ли

✅ **Если планируешь писать свои MCP-серверы или skills для Claude Code** — все три стоит поставить.
❌ **Если только используешь готовые плагины** — не нужно, только skills и MCP из реестра.
