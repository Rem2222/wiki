---
description: LSP MCP-сервер — IDE-интеллект для Claude Code
tags: [mcp, lsp, claude-code, ide]
related: [[concepts/mcp]]
---

# Serena MCP

**GitHub:** https://github.com/oraios/serena

MCP-сервер, который подключает Language Server Protocol (LSP) к Claude Code. Позволяет модели использовать IDE-функции: go to definition, find references, hover, диагностика.

## Фишка

Мост между LSP и MCP: Claude Code получает IDE-level навигацию по коду, не имея IDE.

## Возможности

- **lsp_definition** — переход к определению символа
- **lsp_references** — поиск всех использований
- **lsp_hover** — получение документации и типов
- **lsp_diagnostics** — ошибки и предупреждения
- **lsp_completions** — автодополнение

## Отличие от стандартных LSP-плагинов

Стандартные LSP-плагины — пассивные, реагируют на курсор. Serena — агентная: модель *сама решает*, когда вызвать `lsp_definition` или `lsp_hover`.

## Установка

```bash
pip install serena-mcp
# или
uvx serena-mcp
```

Конфиг в `.mcp.json`:
```json
{
  "mcpServers": {
    "serena": {
      "command": "uvx",
      "args": ["serena-mcp", "--lsp-command", "typescript-language-server", "--stdio"]
    }
  }
}
```

## Зачем

Автор статьи не смог точно понять, имеет ли смысл Serena вместе или вместо стандартных LSP. Советует поэкспериментировать.

## Нужно ли

❌ **Скорее нет.** Стандартные LSP-плагины Claude Code покрывают базовые нужды. Serena — если хочешь более агентный подход. Per-project установка.
