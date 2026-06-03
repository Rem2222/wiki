---
description: | Параметр | Текущий стек | agentmemory |
tags: [tech]
---

# agentmemory-vs-current

**agentmemory** (rohitg00/agentmemory) — npm-пакет для персистентной памяти AI-агентов.

## Сравнение

| Параметр | Текущий стек | agentmemory |
|----------|-------------|-------------|
| Движок | ByteRover (Go) + MemPalace (Python) | iii engine (Node.js/TypeScript) |
| Установка | brv CLI + MemPalace MCP сервер | `npm i -g @agentmemory/agentmemory` |
| Внешние БД | Зависит от конфига | 0 внешних БД |
| MCP-инструментов | ~15-25 (MemPalace) | 51 |
| Авто-хуки | MemPalace hook | 12 встроенных |
| Recall | хороший | 95.2% R@5 (заявлено) |
| Тесты | ? | 950+ |
| Совместимость | Завязано на Hermes | Любой MCP-клиент |
| RI | real-time viewer | есть |

## Вывод

agentmemory — более универсальное и богатое по API MCP-решение, но текущий стек уже рабочий и интегрирован в Hermes. Менять смысла нет, если всё устраивает. Единственный сценарий для agentmemory — если понадобится память под другой MCP-клиент (Claude Code, Cursor, Codex) без привязки к Hermes.