---
title: Craft-аналоги Office (WordCraft / GridCraft / DeckCraft) от storytold
type: tool
status: new
tags: [office, rust, mcp, cli, reverse-engineering, open-source]
url: https://github.com/storytold/wordcraft
license: Apache-2.0
added: 2026-10-15
---

# Craft — аналоги Microsoft Office на Rust (storytold / Danny)

Тот же автор, что сделал **PhotoCraft** (реверс Photoshop, 64k★) и всю серию Craft-приложений
(ArtCraft, LightCraft, FilmCraft, PdfCraft, VectorCraft) — «человек, который зареверсил Adobe».
Теперь взялся за Office: **WordCraft, GridCraft, DeckCraft** — чистые (clean-room) пересоздания
Word / Excel / PowerPoint на **Rust**.

- **Автор:** Danny, GitHub `storytold` (ArtCraft-экосистема)
- **Лицензии:** Apache-2.0 у всех трёх
- **Релизы:** v0.7.0 от 14.10.2026 — свежие, пуши ежедневные (16.10.2026)
- **Статус:** альфа. По оценке автора — «примерно на полпути» к замене Office

| Проект | Аналог | ⭐ | Модель |
|---|---|---|---|
| **wordcraft** | Word | 13 428 | .docx, track changes, комментарии, mail merge, сравнение |
| **gridcraft** | Excel | 5 290 | электронные таблицы, чистый Rust |
| **deckcraft** | PowerPoint | 3 510 | презентации и слайды |

## MCP и CLI (для агентов)

У каждого приложения отдельные бинарники: GUI-приложение + `*-cli` (головной) + `*-web`.
CLI имеет режим MCP-сервера:

```
claude mcp add wordcraft -- ~/.local/bin/wordcraft-cli mcp
# ограничить папки агента:
wordcraft-cli mcp --automation-read-root DIR --automation-write-root DIR
# при запущенном GUI: mcp --connect 127.0.0.1:7981 — доп. инструменты screenshot/click/key
```

Инструменты MCP: `render_page`, `save_document`, `inspect_document` (агент проверяет свою
работу без скриншотов), `convert` (docx→pdf/odt/rtf/html/md/tex/txt/png), `text`, `inspect`.

Промпт из новости рассчитан на **Claude Code** (`claude mcp add --scope user`),
но это обычные stdio MCP-серверы — подключаются и к Hermes (native MCP).

## Проверка (15.10.2026)

- Скриншот из новости разобран: демо WordCraft в живую с **Track Changes: On** — вставки
  цветом, зачёркивания, комментарии «WordCraft User» в боковой панели — трек-ченджес работает.
- GitHub API: аккаунт и все три репо реальные, фолков море (wordcraft 3 466), issue открыто много (1 186) — проект массовый.
- Ассеты релизов: linux-x86_64.tar.gz / AppImage / deb, Windows (msi/portable), macOS — CLI есть под все платформы.

**Статус: записано в вики, НЕ устанавливалось** (правило «новое — сначала в вики»).
Кандидат: VPS-мониторы/отчёты в .docx или подключение на Windows-десктоп Hermes.