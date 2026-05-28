---
description: Мета-скилл для поиска и установки agent-скиллов через CLI (npx skills) — «менеджер пакетов» для экосистемы skills.sh
tags: [skills, cli, package-manager, meta-skill, agents]
related: [[tech/agents-best-practices]]
source: https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md
author: Vercel Labs
created: 2026-05-27
updated: 2026-05-27
---

# Find Skills

Мета-скилл от **Vercel Labs** для поиска и установки agent-скиллов. Выступает как «менеджер пакетов» для экосистемы открытых agent-скиллов на [skills.sh](https://skills.sh/).

**Триггеры активации:** пользователь спрашивает «как сделать X», «найди скилл для Y», хочет расширить возможности агента.

## Как работает (6 шагов)

1. **Понять потребность** — определить домен, задачу, типовость
2. **Проверить лидерборд** (`https://skills.sh/`) — топ скиллов по установкам
3. **Поиск через CLI** — `npx skills find [query]`
4. **Верификация** — установки (1K+), репутация источника, звёзды GitHub (100+)
5. **Презентация** — название, описание, установки, команда установки
6. **Установка** — `npx skills add <owner/repo@skill> -g -y`

## Команды CLI

```bash
npx skills find [query]        # Поиск скиллов
npx skills add <package>       # Установка
npx skills check               # Проверка обновлений
npx skills update              # Обновление всех
npx skills init                # Создание своего
```

## Категории скиллов

Web Dev, Testing, DevOps, Documentation, Code Quality, Design, Productivity

## Особенности

- **Мета-скилл** — не предоставляет функциональности, только поиск
- **Явные критерии верификации** — защита от некачественных скиллов
- **Fallback** — если скилл не найден, предложить помощь вручную или создать через `npx skills init`
