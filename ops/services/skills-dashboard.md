---
description: "Skills Approval Dashboard — локальный Python-сервер для веб-одобрения pending-изменений скилов Hermes: approve / deny / LLM-объяснение diff'а."
tags:
  - ops
  - service
  - hermes
type: service
last_verified: 2026-10-04
related:
  - ops/services/server-architecture
  - ops/services/hermes-agent
  - tools/find-skills
service:
  name: skills-dashboard
  category: hermes
  purpose: "Веб-одобрение pending skill-изменений (approve/deny/explain)"
  path: /root/.hermes/scripts/skills-dashboard/
  url: "https://rem2222.top/skills/"
  port: 8650
  bind: 127.0.0.1
  type: standalone (python, zero deps)
  status: "не запущен: systemd-юнит не найден, порт 8650 закрыт (проверено 03.10.2026); nginx-location /skills/ на месте"
  depends_on:
    - nginx
  notes: "LLM-вызовы идут через hermes -z (bridge-скрипты apply_bridge.py, explain_bridge.py)."
---

# Skills Approval Dashboard

Веб-интерфейс управления **pending-изменениями скилов** Hermes: список изменений,
diff, кнопки «применить» / «отклонить» и LLM-объяснение, что делает правка.

## Архитектура

```
Browser → Nginx (:443) /skills/ → server.py (127.0.0.1:8650)
                                → applies skills → hermes -z (LLM explain)
```

- `server.py` — `SimpleHTTPRequestHandler`, API: `GET /api/pending`,
  `GET /api/pending/{id}/detail`, `POST .../approve|deny|explain`;
- `index.html` — фронтенд (`API = '/skills'`);
- `apply_bridge.py` / `explain_bridge.py` — «тяжёлые» операции в отдельных
  процессах (venv Python, изоляция импортов Hermes);
- LLM-вызовы — только через `hermes -z` (дефолтная модель, без дублирования ключей);
- nginx: `location ^~ /skills/` → `proxy_pass http://127.0.0.1:8650/`
  (trailing slash обязателен — иначе префикс удваивается).

## Статус на 03.10.2026

Код на месте (`/root/.hermes/scripts/skills-dashboard/`), nginx-блок на месте, но
**сервис не поднят**: systemd-юнит `skills-dashboard.service` не найден, порт
`8650` не слушается → `/skills/` сейчас отдаёт 502. Для запуска нужен unit
(см. скилл `selfhosted-services` → `skills-dashboard-deployment.md`) с
`ExecStart=/usr/bin/python3 server.py 8650`.
