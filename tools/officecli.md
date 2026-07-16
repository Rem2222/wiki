---
type: concept
title: Officecli
related: tools/chatcut
description: >-
  CLI for AI agents to read, edit, create Word/Excel/PowerPoint — single binary,
  no Office required
ingested_via: 'mcp:put_page'
ingested_at: '2026-07-16T16:17:42.765Z'
source_kind: 'mcp:put_page'
tags:
  - office automation ai-agent open-source docx xlsx pptx
---

# OfficeCLI — Office Suite для AI-Агентов

**Репозиторий:** [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)
**Сайт:** https://officecli.ai
**Лицензия:** Apache 2.0
**Звёзды:** ~18k ⭐
**Язык:** C# (.NET)

## Что это

OfficeCLI — первая и лучшая Office-тулза, заточенная под AI-агентов. Один бинарник, не требует установленного Microsoft Office, кросс-платформенный.

**Ключевая фича:** встроенный HTML-рендеринг конвертирует .docx/.xlsx/.pptx в HTML или PNG — агент может "увидеть" документ глазами.

## Установка

```bash
# Linux/macOS
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash

# Windows PowerShell
irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex

# Или через менеджеры
brew install officecli
npm install -g @officecli/officecli
```

## Использование

```bash
# Создать презентацию
officecli create deck.pptx

# Live preview — http://localhost:26315
officecli watch deck.pptx

# Добавить слайд
officecli add deck.pptx / --type slide --prop title="Q4 Report"

# Конвертировать документ в текст для LLM
officecli view document.docx outline

# Конвертировать в PNG (агент видит глазами)
officecli render document.docx document.png
```

## Для Hermes Agent

OfficeCLI можно вызывать через terminal tool. Особенно полезно для:
- Чтения .docx отчётов (клиенты присылают в Word)
- Создания .pptx презентаций (замена PowerPoint skill)
- Редактирования .xlsx таблиц
- Конвертации Office документов в Markdown для контекста LLM

Совместимость: Claude Code, Cursor, Windsurf, Copilot, Hermes Agent.

## Ссылки

- [SKILL.md для агентов](https://officecli.ai/SKILL.md)
- [GUI (AionUi)](https://github.com/iOfficeAI/AionUi)
