---
description: Остановка SMOON и очистка Docker. Команды docker compose down, docker system prune, структура образов.
tags: [smoon, docker, cleanup, storage, compose]
related: [[tech/cockpit]]
---

# SMOON shutdown + Docker overview

**Дата:** 22 мая 2026  
**Проект:** `/home/rem/smoon/`

## Что это

SMOON — Telegram-бот, запущенный через Docker Compose. При остановке важно различать уровни очистки.

## Остановка SMOON

```bash
cd /home/rem/smoon/
```

### docker compose down

Останавливает и удаляет контейнеры. Образы **сохраняются**.

- ✅ Удаляет контейнеры
- ✅ Удаляет сеть compose
- ❌ Не удаляет образы
- ❌ Не удаляет тома

### docker compose down --rmi all

Полная очистка проекта: контейнеры + образы. После команды нужен `docker compose build` или `pull`.

### docker compose down --volumes

Удаляет контейнеры + volumes. ⚠️ Данные пропадают навсегда.

## Где лежат образы

```
/var/lib/docker/
├── containers/   # метаданные
├── image/        # слои образов
├── volumes/      # данные томов
├── overlay2/     # файловая система контейнеров
└── buildkit/     # кэш сборки
```

## Основные команды

```bash
docker images                                    # список образов
docker ps -a                                     # все контейнеры
docker container prune                           # удалить остановленные
docker image prune                               # удалить образы без тегов
docker system prune -a                           # удалить всё неиспользуемое
```

`docker system prune -a` удаляет: остановленные контейнеры, образы без запущенных контейнеров, неиспользуемые сети, build cache.

## Размер

SMOON занимал ~31GB. После полной очистки освободилось ~31GB.

## Структура проекта

```
/home/rem/smoon/
├── docker-compose.yml
├── Dockerfile
├── .env
├── backend/
│   ├── src/
│   └── ...
├── frontend/
│   └── ...
└── data/
```

## Ссылки

- GitHub: Rem2222/app (private)
- Локально: `/home/rem/smoon/`
