---
description: "Docker Skills — 11 официальных SKILL.md от Docker для кодинг-агентов (Apache-2.0, Agent Skills Spec). Что установлено у нас (3 из 11), какие пропущены и почему, локальная правка правила про имя compose-файла."
tags: [docker, skills, ai-agents, devops, claude-code, codex, habr]
updated: 2026-09-25
source: "https://github.com/docker/skills"
related:
  - "[[tech/free-llm-api-resources]]"
  - devops/selfhosted-services
  - devops/vps-disk-cleanup
---

# Docker Skills — официальные навыки Docker для агентов

**Репозиторий:** https://github.com/docker/skills · **Доки:** https://docs.docker.com/ai/skills
**Лицензия:** Apache-2.0 · **Язык:** Python · **Статус:** 169★ / 4 форка, активный (последний пуш 25.09.2026)
**Теги:** `v0.1.0` → `v0.2.0` → **`v0.3.0`** (текущий; репо создан 27.03.2026)

Docker-authored knowledge skills — портируемые каталоги `SKILL.md`, которые любой совместимый агент подхватывает по стандартным путям. Таблицы в README, `skills.sh.json` и манифесты плагинов **генерятся из `catalog.yaml`** (`task catalog`) — править нужно его, а не таблицу.

## Стандарт, а не приватный формат

Каждый скилл следует [Agent Skills Specification](https://agentskills.io/specification) и проходит их валидатор [`skills-ref`](https://github.com/agentskills/agentskills/tree/main/skills-ref). Это не формат Docker — он валиден для Claude Code, Codex, Cursor, Copilot, Gemini CLI, OpenCode, Windsurf, Cline, Kiro.

Дополнительно репо содержит `skill.yaml`, `agents/openai.yaml`, `checks/`, `evals/` — это их собственные конвенции качества сверх спецификации.

## Каталог: 11 скиллов в 5 группах

| Группа | Скилл | Размер | Что делает |
|---|---|---|---|
| **Dockerfile & Build** | `docker-project-foundations` | 19K / 9 файлов | Инициализация и структура Dockerized-проекта |
| | `docker-build-strategies` | 32K / 11 файлов | Multi-stage, layer-caching, `.dockerignore`, non-root |
| **Docker Compose** | `docker-compose-patterns` | 25K / 10 файлов | Service wiring, healthchecks, volumes, networks, dev-overrides |
| **Docker Sandboxes** | `docker-sandboxes-lifecycle` | 24K | Жизненный цикл `sbx`: create/reattach/tear-down |
| | `docker-sandboxes-network-credentials` | 24K | Egress-политика, безопасная выдача кредов через proxy-injection |
| | `docker-sandboxes-env` \* | 34K | Декларативные `sbxenv.yaml` окружения |
| | `docker-sandboxes-kits` \* | 52K | Авторизация, подпись и композиция sandbox-kit'ов |
| **Docker Agent** | `docker-agent-config` | 20K | Авторинг `agent.yaml` (cagent): агенты, модели, toolsets, команды |
| | `docker-agent-run` | 16K | Запуск Docker Agent локально: approval-режимы, sandbox, worktrees |
| | `docker-agent-deploy` | 17K | Как сервер, OCI-дистрибуция, регрессионные eval'ы в CI |
| **Cross-product** | `docker-destructive-guardrails` | 37K | Политика подтверждения необратимых операций |

\* — *experimental*, схемы могут измениться.

Правило триггинга: **у каждой секции есть собственный description**, входной «родительский» скилл не нужен. Порядок загрузки при меж-скилловой задаче: `project-foundations` → `build-strategies` / `compose-patterns`, `sandboxes-lifecycle` → `network-credentials` → `-env` / `-kits`, `agent-config` → `agent-run` → `agent-deploy`.

## Проверка качества (прочитаны на живца)

### `docker-compose-patterns` (9.2K SKILL.md)
Канон `compose.yaml`, запрет `latest`-тегов, `restart: unless-stopped`, `depends_on` с `condition: service_healthy` **плюс обязательный** `healthcheck` на каждый такой сервис, нативные клиенты проверок (`pg_isready`, `redis-cli ping`, `mysqladmin ping`), стартовые значения `interval: 5s / timeout: 3s / retries: 3 / start_period: 10s`. Есть секции «When to use» / «Do not use» — триггеры отсекают ложные срабатывания.

### `docker-destructive-guardrails` (10.3K SKILL.md)
Триггерится даже без названия команды: «почисти», «снеси всё», «начни с чистого листа», «nuke it», «wipe everything».

- **Tier 1** (узкая очистка контейнера) — сам, без подтверждения
- **Tier 2** — `docker kill`, `docker container prune` (всегда сносит **все** остановленные контейнеры хоста), `docker rm -f` на чужом/бегущем контейнере, любые unscoped-свипы → назвать ровно, что потеряется, и ждать явного ответа
- `docker stop` — вне модели removal: ничего не удаляет, но теряет непersisted-состояние в памяти

### `docker-build-strategies`
Multi-stage builds, layer-caching, `.dockerignore`, non-root, размер образа.

## Скрипты-проверяльщики — безопасные

Оба прочитаны целиком, ничего опасного:
- `verify-compose.sh` → `docker compose config --quiet` (валидация, вывода не печатает)
- `verify-build.sh` → `docker build -t verify-build-test .` + `docker images` + `docker inspect --format '{{.Config.User}}'`

## Установка

### `skills` CLI (кросс-клиентный)
```bash
npx skills add docker/skills --list                      # посмотреть без установки
npx skills add docker/skills --skill docker-compose-patterns --yes
npx skills add docker/skills --skill '*' --agent codex --yes
npx skills add docker/skills --all                       # всё во все обнаруженные агенты
npx skills update                                        # обновить
npx skills add https://github.com/docker/skills/tree/v0.3.0 \
  --skill docker-compose-patterns --yes                  # пин на релиз
```

### Плагины (обновления идут через агента, не через `npx skills update`)
```text
Claude Code / Copilot CLI:  /plugin marketplace add docker/skills
                            /plugin install docker-skills@docker
```
```bash
Codex:      codex plugin marketplace add docker/skills
            codex plugin add docker-skills@docker         # + новая сессия
Gemini CLI: gemini extensions install https://github.com/docker/skills  # + рестарт
Cursor:     `docker-skills` из маркетплейса, либо `skills add --agent cursor`
Sandbox:    sbx skills add docker/skills --skill docker-compose-patterns   # experimental
```

### Ручное копирование (путь для Hermes)
Таблица путей в README **нас не содержит**, но формат идентичен нашим скиллам (`name` + `description` в frontmatter), поэтому обычное копирование папки работает:
```bash
git clone --branch v0.3.0 --depth 1 https://github.com/docker/skills.git
cp -R docker-skills/skills/docker-compose-patterns ~/.hermes/skills/devops/
```
> `main` — rolling-канал. Для воспроизводимости они прямо рекомендуют пиниться на тег релиза.

## Что установлено у нас (3 из 11)

**Дата:** 25.09.2026 · **Куда:** `~/.hermes/skills/devops/` · **Тег:** `v0.3.0`

| Скилл | Причина |
|---|---|
| `docker-destructive-guardrails` | Работает вместе с `vps-disk-cleanup` — тот уже требует ранжированного списка и подтверждения, guardrails даёт формализованную шкалу Tier1/Tier2 |
| `docker-build-strategies` | Multica и `multica-frontend-patching` собирают образы; multi-stage и layer-caching напрямую экономят время |
| `docker-compose-patterns` | `selfhosted-services` покрывает наш стек, но даёт здоровые дефолты для healthchecks/depends_on при заведении новых сервисов |

### Локальная правка в `docker-compose-patterns`

В `## Core guidance` перед `### File naming` вставлен блок `[!IMPORTANT]`:

> Правило «`compose.yaml` — канон, `docker-compose.yml` — legacy» **на этом хосте не применяется**. Вся инфраструктура уже на `docker-compose.yml` / `docker-compose.selfhost.yml` / `docker-compose.override.yml` (Multica разворачивается через `docker compose -f docker-compose.selfhost.yml -f docker-compose.override.yml up -d`; `/opt/FreeQwenApi`, `/opt/freellmapi` — на `docker-compose.yml`). **Переименовывать существующие файлы нельзя** — `selfhosted-services` и скрипты обновления Multica разыменовывают эти имена явно. Каноническое имя — только для новых проектов с нуля, и там сохранять шаблон проекта.

Без этой правки скилл конфликтовал бы с `selfhosted-services` (там 7 упоминаний `docker-compose.selfhost.yml`, 4 `docker-compose.override.yml`) и мог бы спровоцировать переименование, ломающее обновления Multica.

**Конфликта по prune нет:** `vps-disk-cleanup` уже написан в том же духе — «ранжированный список, executes only after they approve», плюс пункт «`docker system prune -a` deletes far more than intended».

## Что НЕ ставили (8 из 11) и почему

| Скилл | Причина пропуска |
|---|---|
| `docker-sandboxes-*` (4 шт.) | Docker Sandboxes у нас не используются. Два из четырёх ещё и experimental |
| `docker-agent-*` (3 шт.) | Docker Agent (cagent) — отдельный рантайм агентов, у нас Hermes |
| `docker-project-foundations` | Новые проекты заводим редко; `compose-patterns` + `build-strategies` покрывают бо́льшую часть |

Все восемь остаются в репо — если появится нужда, ставятся одной командой:
```bash
cp -R /tmp/docker-skills/skills/docker-sandboxes-lifecycle ~/.hermes/skills/devops/
```

## Источники

- 🌐 https://github.com/docker/skills — репозиторий, README, каталог
- 🌐 https://docs.docker.com/ai/skills — официальные доки по установке
- 🌐 https://agentskills.io/specification — стандарт Agent Skills
- 🌐 https://skills.sh/docker/skills — индекс для `skills` CLI
- 📄 devops/selfhosted-services — наши compose-правила (override, teardown)
- 📄 devops/vps-disk-cleanup — существующие правила подтверждения при чистке
