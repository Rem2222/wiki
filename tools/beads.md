---
description: Beads — это git-backed база данных для задач (issues). Хранит данные в JSONL файлах в директории `.beads/`. Создан для AI агентов, не для людей.
tags: [tools]
related: [[projects/veritas-kanban]] [[tech/jawl]]
---

# beads

**Автор:** Steve Yegge (steveyegge)  
**Репозиторий:** https://github.com/gastownhall/beads  
**Тип:** CLI-first issue tracker для AI агентов

## Что это

Beads — это git-backed база данных для задач (issues). Хранит данные в JSONL файлах в директории `.beads/`. Создан для AI агентов, не для людей.

> "Behaviours is a git-backed database (JSONL files in .beads/ directory), a dependency-aware graph (tasks block other tasks), a CLI tool (bd command), designed for AI agents first, humans second."

## Ключевые особенности

- **Git-backed** — задачи хранятся в `.beads/` как JSONL файлы
- **Dependency-aware** — задачи могут блокировать друг друга
- **CLI-first** — команда `bd` для всего
- **Collision resolution** — встроенные инструменты для разрешения конфликтов
- **Легковесный** — быстрый, high-performance
- **AI-native** — создан для AI агентов с учётом их ограничений (context window)

## Установка

```bash
npm install -g @steve-yegge/beads
```

## Команды

```bash
bd new <title>              # создать задачу
bd list                     # список задач
bd update <id> --status done  # завершить задачу
bd update <id> --claim      # забрать в работу
bd get <id>                 # посмотреть задачу
```

## Статусы задач

- `pending` — ожидает
- `in-progress` — в работе
- `done` — завершена
- `blocked` — заблокирована другой задачей

## Сравнение с другими системами

| | Beads | Linear | Multica |
|---|---|---|---|
| Таски | ✅ | ✅ | ✅ |
| AI-first | ✅ | ❌ | ✅ |
| Git-backed | ✅ | ❌ | ❌ (сервер на VPS) |
| Автозапуск агентов | ❌ | ❌ | ✅ |
| Веб-интерфейс | ❌ (CLI) | ✅ | ✅ |
| CLI для агентов | ✅ (`bd`) | ⚠️ (API) | ⚠️ (API) |

## Beads vs Multica

**Beads** — это "git для тасков". Идеален если хочешь:
- CLI-first подход для агентов
- Git-based workflow (коммиты, ветки, PR)
- Локальное хранение без сервера

**Multica** — orchestration + runtime management. Идеален если хочешь:
- Веб-интерфейс
- Автоматический запуск агентов на задачи
- Multi-agent runtime discovery
- Browser + Tailscale для доступа

## Текущий статус у Романа

**Beads НЕ установлен.** Команда `bd` отсутствует. Проект "Beads внедрить в Superpowers (Оркестр)" в Linear (REM-97, REM-98) в статусе Backlog с 2026-04-26, дальше не двигался.

**Решение:** Остаёмся на Multica. Beads рассматривался как альтернатива, но не приоритет.

## Ресурсы

- [GitHub](https://github.com/gastownhall/beads)
- [Agent Workflow Guidelines](https://deepwiki.com/steveyegge/beads/8.2-agent-workflow-guidelines)
- [Статья на Medium](https://steve-yegge.medium.com/the-beads-revolution-how-i-built-the-todo-system-that-ai-agents-actually-want-to-use-228a5f9be2a9)
- [Better Stack Guide](https://betterstack.com/community/guides/ai/beads-issue-tracker-ai-agents/)

---

_Добавлено: 2026-05-04_