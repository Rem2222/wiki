---
description: "ArcEngine — LLM-native 3D-движок в браузере (Babylon.js, ноль npm-зависимостей): dev-server кита на :8082, наружу торчит https://rem2222.top/arcengine/"
tags:
  - ops
  - service
  - dev
  - 3d
type: service
related:
  - "[[ops/services/nginx]]"
  - "[[ops/services/hermes-agent]]"
service:
  name: arcengine
  category: dev
  purpose: "3D-игровой кит под кодинг-агентов: dev-server отдаёт статику проекта /root/arcengine (index.html + js/libs/assets)"
  install_date: 2026-10-13
  last_verified: 2026-10-29
  health_url: "http://127.0.0.1:8082/"
  type: systemd
  ports:
    -
      port: 8082
      protocol: tcp
      bind: 127.0.0.1
      description: dev-server.mjs (node) — статика проекта ArcEngine
  systemd_units:
    - arcengine-game
  docker_containers: []
  processes:
    - pattern: "node tools/dev-server.mjs --port=8082"
  config_paths:
    - /root/arcengine
    - /etc/systemd/system/arcengine-game.service
    - /etc/nginx/sites-enabled/hermes (location ^~ /arcengine/)
  logs:
    - "journalctl -u arcengine-game"
  depends_on:
    - nginx
  data_size_hint: "/root/arcengine ≈ 24 МБ (git-клон + assets)"
  notes: >
    Клон github.com/xaidan777/ArcEngine (Babylon.js, ноль npm-зависимостей и
    сборки, сидлы для агентов в claude/skills, экспорт в Unity). Поставлен
    2026-10-13 19:46, юнит arcengine-game.service создан 2026-10-13 20:02,
    enabled. Проксируется nginx по пути /arcengine/ (location ^~, без
    authelia-гейта — публично). Это dev-server, а не production-хостинг:
    отдаёт только /root/arcengine, данные игры лежат внутри клона.
    Обслуживание: обновление — `git -C /root/arcengine pull`; рестарт —
    `systemctl restart arcengine-game`.
last_verified: 2026-10-29
---

# ArcEngine (dev-server, :8082)

LLM-native 3D-движок для браузера от `xaidan777`: Babylon.js, ноль
npm-зависимостей, редактор сцены/UI и скиллы для кодинг-агентов. На сервере
крутится **не движок как сервис**, а его dev-server — статика проекта.

## Что запущено

- `arcengine-game.service` (`enabled`, `active (running)`), `WorkingDirectory=/root/arcengine`,
  `ExecStart=/usr/bin/node tools/dev-server.mjs --port=8082 --no-open`;
- слушает `127.0.0.1:8082` (наружу не открыт напрямую);
- nginx (`sites-enabled/hermes`) проксирует `https://rem2222.top/arcengine/` → `127.0.0.1:8082/`,
  `location = /arcengine` даёт 301 на `/arcengine/`;
- внешний ответ: `https://rem2222.top/arcengine/` → 200.

## Статус на 2026-10-28

- `systemctl is-active arcengine-game` → `active`, `is-enabled` → `enabled`;
- процесс живёт с 2026-10-18 20:38 (перезапуск), uptime 9+ суток;
- `curl http://127.0.0.1:8082/` → 200, `<title>ArcEngine</title>`;
- клон на коммите `16fc587 unity harness` (origin xaidan777/ArcEngine).

## Обслуживание

- Обновления: `git -C /root/arcengine pull` (upstream — публичный репозиторий автора);
- Рестарт: `systemctl restart arcengine-game`;
- Логи: `journalctl -u arcengine-game -n 50`;
- Бэкапить нечего, кроме правок в самом клоне (24 МБ, не в git-цепочке бэкапов);
- ⚠️ `/arcengine/` не закрыт Authelia — любой в интернете видит статику проекта.
  Если это станет не нужно — либо добавить `include /etc/nginx/snippets/authelia-location.conf;`,
  либо `systemctl disable --now arcengine-game`.
