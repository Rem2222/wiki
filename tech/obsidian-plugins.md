---
description: Рекомендованные плагины Obsidian: Dataview, Templater, MCP Plugin, InfraNodus AI Graph.
tags: [obsidian, plugins, dataview, templater, mcp, infranodus, ai]
related: [[wiki/tech/obsidian]], [[tech/dataview]], [[tech/obsidian-livesync]]
---

# Плагины Obsidian: рекомендованные

## Установка плагинов

Settings → Community plugins → Turn on → Browse → Install → Enable.

---

## 1. Dataview

**URL:** https://github.com/blacksmithgu/obsidian-dataview  
**Статус:** Установлен

SQL-подобные запросы по заметкам через YAML frontmatter.

```dataview
TABLE description, tags
FROM "tech"
SORT file.name ASC
```

Подробнее: [[tech/dataview]]

---

## 2. Templater

**URL:** https://github.com/SilentVoid13/Templater  
**Статус:** Рекомендован

Скриптовые шаблоны для создания заметок. Мощнее встроенного шаблонизатора.

**Возможности:**
- Переменные: `{{title}}`, `{{date}}`, `{{time}}`
- Системные: `{{cursor}}`, `{{clipboard}}`
- JavaScript: `<% tp.file.title %>`
- Запросы через всплывающее окно: `{{prompt}}`

**Пример шаблона:**
```markdown
---
title: {{title}}
date: {{date:YYYY-MM-DD}}
tags: []
---
# {{title}}
{{cursor}}
```

**Настройка:** Указать папку шаблонов, назначить горячую клавишу.

---

## 3. Obsidian MCP Plugin

**URL:** https://github.com/obsidianMCP/obsidian-mcp-plugin  
**Статус:** Рекомендован

Открывает доступ к vault через MCP — AI-агенты читают и создают заметки.

**Что даёт:**
- Hermes, Claude Code, OpenCode получают доступ к vault
- Чтение, поиск, создание заметок через MCP

**Настройка:** Установить плагин → включить MCP-сервер → добавить в конфиг MCP-клиента.

**Ограничения:** Требует запущенного Obsidian на той же машине.

---

## 4. InfraNodus AI Graph

**URL:** https://infranodus.com  
**Статус:** Внешняя надстройка

Визуализация графа знаний, поиск структурных дыр (structural holes), генерация идей. Не Obsidian-плагин, а внешний сервис. Требует платной подписки.

---

## Сводка

| Плагин | Тип | Назначение |
|--------|-----|------------|
| Dataview | Obsidian plugin | SQL-запросы |
| Templater | Obsidian plugin | Шаблоны |
| Obsidian MCP Plugin | Obsidian plugin | AI-доступ через MCP |
| InfraNodus AI Graph | Внешний сервис | Анализ графа знаний |
