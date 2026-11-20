---
description: "altr — CLI облачной платформы Altare (altare.gg): деплой приложений, Edge Functions, БД, storage, домены/почта, Altare AI, Go-машины. Установлен вручную в /usr/local/bin, залогинен под rem5529."
tags:
  - ops
  - service
  - dev
  - cli
  - cloud
type: service
related:
  - "[[ops/services/server-architecture]]"
service:
  name: altr
  category: dev
  purpose: "CLI Altare AI: деплой приложений из GitHub/Docker-образов, Edge Functions, managed БД (Postgres/MySQL/Valkey), KV/queues/U3 storage, домены/DNS/почта, Altare AI (ключи, usage, кредит), серверы/воркстейны/туннели и запуск Altare Go-машин"
  install_date: 2026-11-20
  last_verified: 2026-11-21
  health_url: null
  type: "standalone (CLI, статический Go-бинарь)"
  ports: []
  systemd_units: []
  docker_containers: []
  processes: []
  config_paths:
    - /usr/local/bin/altr
    - /root/.config/altr/config.json
    - /root/.config/altr/id_ed25519
  logs: []
  depends_on: []
  data_size_hint: "бинарь 13 МБ + конфиг каталог ~20 КБ"
  notes: >
    v0.8.1, ELF x86-64, статически слинкован, stripped. Установлен вручную
    (dpkg -S пути не знает, apt-пакета нет), mtime бинаря 2026-11-20 22:40.
    Залогинен под аккаунтом Altare rem5529 (rem2222@gmail.com), команда
    Default (560935bf-8fc1-4d0f-aa39-7cd545ff04e7), вход подтверждён через
    браузер (console.altare.gg) 2026-11-20 22:42. Своих портов, юнитов и
    демонов не держит — работает как клиент к api.altare.gg. Статус: требует
    подтверждения Романа, что инструмент нужен на этом сервере постоянно.
last_verified: 2026-11-21
---

# altr — CLI Altare AI

Клиент облачной платформы [Altare](https://altare.gg) (документация — `altare.gg/docs`).
Ставится одним бинарём, авторизуется через браузер (`altr login` → код → подтверждение
в консоли). Умеет поднимать облачные машины, деплоить приложения и управлять
managed-сервисами платформы из терминала.

## Что умеет

- **Машины и серверы:** `altr go` (временная Linux-машина из warm-пула, Debian 13 по
  умолчанию, до 12 ч жизни), `altr server`, `altr servers`, `altr snapshots`,
  `altr ssh`, `altr workstations` — воркстейны в Лондоне.
- **Приложения:** `altr deploy` (GitHub-репозиторий + стрим сборки), `altr docker`
  (образы), `altr apps`, `altr env`, `altr previews`, `altr functions` (Edge Functions).
- **Данные:** `altr postgres`, `altr mysql`, `altr valkey`, `altr kv`, `altr queues`,
  `altr u3` (объектное хранилище).
- **Сеть и домены:** `altr dns`, `altr domains`, `altr email`, `altr network`,
  `altr mesh` (WireGuard-сеть команды), `altr tunnel` (публичный https на локальный порт).
- **AI:** `altr ai` — Token Plan, API-ключи, usage, кредит и алерты Altare AI.
- **Для агентов:** `altr mcp` (Altare MCP-сервер по stdio), `altr skill` (печать/установка
  Altare-скилла).
- **Прочее:** `altr whoami`, `altr token` (сессионный токен для `ALTARE_TOKEN` в CI),
  `altr team`, `altr teams`, `altr update`, `altr completion`.

Полезные флаги: `--json` (машиночитаемый вывод), `--team <имя|ID>`, `--token` /
`ALTARE_TOKEN` вместо `altr login`.

## Состояние на сервере (проверено 2026-11-21)

| Что | Значение |
|---|---|
| Бинарь | `/usr/local/bin/altr`, 13 000 888 байт, ELF x86-64 static stripped |
| Версия | `altr 0.8.1` |
| SHA-256 | `0e49491a01d6d9295ddb545b0396b02ae513f99174a65d536a64558b681818b4` |
| Установка | вручную, mtime 2026-11-20 22:40 (в apt не значится, `dpkg -S` пусто) |
| Аккаунт | `rem5529` (rem2222@gmail.com), команда `Default` |
| Вход | 2026-11-20 22:42 через браузерное подтверждение кода |
| Ресурсы в аккаунте | серверов нет, приложений нет (`altr servers` / `altr apps` — пусто) |
| Порты / юниты / процессы | нет — чистый CLI-клиент к api.altare.gg |

Проверка вживую:

```bash
altr --version            # altr 0.8.1
altr whoami               # rem5529 (rem2222@gmail.com) / Team: Default
altr teams                # * Default  560935bf-8fc1-4d0f-aa39-7cd545ff04e7
altr servers              # Default has no servers yet
altr apps                 # No apps yet
```

## Ограничения и наблюдения

- `altr go` с этого сервера **не запускается**: оба пробных запуска 2026-11-20 22:42
  вернули `{"error": "Altare returned 502"}` — отвечала сторона платформы, не сеть
  сервера. Стоит перепроверить при первом реальном использовании.
- Своих портов не слушает; наружу ходит по HTTPS к api.altare.gg. Прокси/nginx не нужен.
- `altr update` — самообновление бинаря (перезапишет `/usr/local/bin/altr`), поэтому
  версию в этой странице надо сверять заново после каждого апдейта.

## Безопасность

- `~/.config/altr/config.json` (права 600) содержит сессионный токен Altare —
  в чат, заметки и коммиты не выносить.
- `~/.config/altr/id_ed25519` — ключ для SSH-доступа к машинам/серверам Altare;
  приватную часть не публиковать.
- `altr token` печатает токен в открытом виде — использовать только в CI-переменных,
  не в логах.

## Статус записи

Инструмент появился на сервере 2026-11-20 без записи в реестре (обнаружен ночной
рутиной, issue MUL-10581). Установка и вход выполнены под аккаунтом Романа
(browser-подтверждение 22:42), что указывает на намеренное действие, но явного
подтверждения от Романа пока нет — до него страница считается «новый инструмент,
требует подтверждения». Если инструмент не нужен — удалить бинарь и
`~/.config/altr/`, а страницу перенести в архив.
