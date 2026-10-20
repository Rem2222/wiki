---
description: "ink-arena (INKED arena) — Rust-сервер арены для isroleplay.fr, systemd-юнит ink-arena-s2 (Encreville/EU), поставлен 12.10.2026."
tags: [ops, service, game]
type: service
related:
  - ops/services/server-architecture
service:
  name: ink-arena
  category: game
  purpose: "Игровая арена (INKED arena) — воркеры ботов, публикуется наружу как wss://s2.isroleplay.fr (central hub play.isroleplay.fr)"
  install_date: "2026-10-12"
  last_verified: 2026-10-21
  health_url: "https://s2.isroleplay.fr/ping"
  type: systemd
  ports:
    - port: 8090
      protocol: tcp
      bind: 127.0.0.1
      description: "HTTP/WS арены (только localhost, наружу идёт через central hub)"
  systemd_units:
    - ink-arena-s2.service
  processes:
    - pattern: "ink-arena --port=8090"
  config_paths:
    - /etc/systemd/system/ink-arena-s2.service
    - /opt/ink-arena/maps/
    - /opt/ink-arena/node.key
  depends_on:
    - nginx
  notes: >-
    2026-10-13: юнит создан 12.10.2026 04:36 CEST. Бинарь /opt/ink-arena/ink-arena (~24MB,
    владелец root), maps: bijou/docks/rooftops (.inkw). Запускается от пользователя ink
    (uid 994) с жёстким sandbox (ProtectSystem=strict, MemoryMax=512M, TasksMax=64,
    CapabilityBoundingSet пустой, LoadCredential=node.key — секрет не в командной строке).
    Наружу выходит через central node play.isroleplay.fr (--node-url wss://s2.isroleplay.fr,
    --node-name Encreville, --node-region EU); наружный ping https://s2.isroleplay.fr/ping
    отвечает 204. Активной инфраструктуры на самом VPS не хранит (только бинарь + maps,
    "arena owns nothing на disk"). Порт 8090 у этого сервиса на 127.0.0.1 — НЕ путать с
    beszel hub, который внутри контейнера тоже слушает 8090.
last_verified: 2026-10-21
---
# ink-arena (INKED arena)

Игровой сервер арены на Rust, поставлен на VPS 12.10.2026 и опубликован как узел
`wss://s2.isroleplay.fr` центрального хаба `play.isroleplay.fr` (регион EU, имя узла
**Encreville**).

## Ключевые факты

| Параметр | Значение |
|---|---|
| Юнит | `ink-arena-s2.service` (systemd, enabled, Restart=always) |
| Бинарь | `/opt/ink-arena/ink-arena` (root-owned, 24MB) |
| Maps | `/opt/ink-arena/maps/{bijou,docks,rooftops}.inkw` |
| Порт | `127.0.0.1:8090` (map=bijou, max=16 players, 8 bots, teams=1) |
| Пользователь | `ink` (uid 994), sandbox: ProtectSystem=strict, MemoryMax=512M |
| Секрет | `/opt/ink-arena/node.key` через `LoadCredential` (не виден в ps) |
| Health | `https://s2.isroleplay.fr/ping` → 204 |

## Обслуживание

Специального обслуживания не требует: данных на диске не держит, обновления приходят
вместе с бинарём. Проверка: `systemctl is-active ink-arena-s2` + внешний ping.
