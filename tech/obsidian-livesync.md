---
description: Self-hosted синхронизация Obsidian через CouchDB за nginx reverse proxy с HTTPS. Установка CouchDB в Docker, настройка nginx, подключение LiveSync plugin.
tags: [obsidian, livesync, couchdb, sync, docker, self-hosted, nginx, https]
related: [[tech/obsidian-plugins]], [[tech/obsidian-plugins]], couchdb
---

# Obsidian LiveSync

**URL:** https://github.com/vrtmrz/obsidian-livesync  
**Статус:** Настроен (22 мая 2026)

## Что это

Плагин синхронизации заметок между устройствами через self-hosted CouchDB. Плагин требует HTTPS, поэтому CouchDB проксируется через nginx с SSL.

## Архитектура

```
Obsidian (десктоп/телефон) → HTTPS (rem2222.top:443) → nginx → CouchDB (:5984)
```

## Подключение к Obsidian LiveSync

**Рабочий URL (HTTPS):** `https://rem2222.top/couchdb/`

Параметры плагина:
- **Remote type:** CouchDB
- **CouchDB URL:** `https://rem2222.top/couchdb/`
- **Username:** `admin`
- **Password:** `OpenClaw2024!`
- **Database name:** `obsidian-vault`
- **Sync mode:** LiveSync

> ⚠️ Плагин не принимает HTTP. Используй только HTTPS через nginx.

## CouchDB: установка (Docker)

CouchDB на VPS 81.17.100.103:

```yaml
services:
  couchdb:
    image: couchdb:latest
    container_name: couchdb
    restart: unless-stopped
    ports:
      - 5984:5984
    volumes:
      - ./couchdb_data:/opt/couchdb/data
    environment:
      - COUCHDB_USER=admin
      - COUCHDB_PASSWORD=OpenClaw2024!
```

**Проверка:**
```bash
curl -u admin:OpenClaw2024! http://localhost:5984/
```

## nginx reverse proxy (HTTPS)

Добавлено в `/etc/nginx/sites-enabled/rem2222` в HTTPS server block:

```nginx
location /couchdb/ {
    proxy_pass http://127.0.0.1:5984/;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_buffering off;
    proxy_read_timeout 120;
    client_max_body_size 100m;
}
```

Без Authelia — LiveSync использует Basic Auth от CouchDB.

## CORS

Включен для работы плагина:

```bash
curl -X PUT http://admin:OpenClaw2024!@localhost:5984/_node/nonode@nohost/_config/cors/origins -d '"*"'
curl -X PUT http://admin:OpenClaw2024!@localhost:5984/_node/nonode@nohost/_config/cors/credentials -d '"true"'
curl -X PUT http://admin:OpenClaw2024!@localhost:5984/_node/nonode@nohost/_config/cors/methods -d '"GET, PUT, POST, DELETE, HEAD, OPTIONS"'
curl -X PUT http://admin:OpenClaw2024!@localhost:5984/_node/nonode@nohost/_config/cors/headers -d '"accept, authorization, content-type, origin, referer, x-csrf-token"'
```

## База данных

Создана: `obsidian-vault`

```bash
curl -X PUT http://admin:OpenClaw2024!@localhost:5984/obsidian-vault
```

## Скрипт синхронизации .md → CouchDB

Агенты пишут статьи напрямую в `~/.openclaw/workspace/wiki/` как .md файлы. CouchDB не знает о файлах — чтобы статьи появились на телефоне через LiveSync, нужен скрипт, который пушит их в базу.

**Скрипт:** `/root/sync-wiki-to-couchdb.py`

### Формат документов в CouchDB (LiveSync-compatible)

```json
// Note-документ (запись о файле)
{
  "_id": "tech/authelia.md",
  "type": "plain",
  "path": "tech/authelia.md",
  "ctime": 1745452800000,
  "mtime": 1745452800000,
  "size": 4958,
  "children": ["h:<sha256-content>"],
  "eden": {}
}

// Chunk-документ (содержимое файла)
{
  "_id": "h:<sha256-content>",
  "type": "leaf",
  "data": "---\\ndescription: ...\\ntags: [...]\\n---\\n\\n# Full markdown content..."
}
```

**Ключевые моменты:**
- `_id` = относительный путь от корня вики (напр. `tech/authelia.md`)
- `type: "plain"` для markdown, `"leaf"` для чанков с контентом
- chunk ID = `h:` + SHA-256 содержимого (дедупликация по контенту)
- Используется `_bulk_docs` API — CouchDB за nginx неправильно обрабатывает `/` в doc ID через PUT URL

### Использование

```bash
## Разовый импорт всех статей
python3 /root/sync-wiki-to-couchdb.py

## Просмотр без импорта
python3 /root/sync-wiki-to-couchdb.py --dry-run
```

Скрипт:
1. Проходит всю папку `~/.openclaw/workspace/wiki/`
2. Находит все .md файлы (кроме AGENTS.md, SCHEMA.md, WIKI.md)
3. Вычисляет SHA-256 контента → chunk ID
4. Создаёт note + chunk документы в CouchDB через `_bulk_docs`
5. Если чанк уже существует (такой же контент), использует существующий

**Важно:** Скрипт синхронизирует ТОЛЬКО в сторону CouchDB. Изменения, сделанные на телефоне, обратно в файлы не попадают. Для двухсторонней синхронизации нужен daemon-режим LiveSync CLI.

## Подключение с телефона

Установить Obsidian + LiveSync плагин, ввести те же параметры (URL с HTTPS).

## Возможные проблемы

- **Плагин ругается на HTTP:** Используй `https://rem2222.top/couchdb/` а не прямые IP:порт
- **БД не создаётся:** Создать вручную через Fauxton (`/_utils/`) или curl
- **Конфликты:** LiveSync авторазрешает (last write wins)
- **Медленная синхронизация:** Уменьшить частоту или переключиться на Batch-режим

## Ссылки

- HTTPS: `https://rem2222.top/couchdb/`
- Fauxton: `https://rem2222.top/couchdb/_utils/`
- Прямой CouchDB: `http://81.17.100.103:5984` (локально)
- Логин: admin / OpenClaw2024!
- Скрипт: `/root/sync-wiki-to-couchdb.py`
