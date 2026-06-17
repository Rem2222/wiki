---
description: Flask-мониторинг на порту 5000. 15 API маршрутов, 1709 строк кода.
created: 2026-05-01
tags: [jawl, dashboard, api, reference]
parent: "[[tech/jawl]]"
related: [[tech/landing]] [[tech/nexus-dashboard]]
---

# JAWL Dashboard

Flask-мониторинг на порту 5000. 15 API маршрутов, 1709 строк кода.

## Маршруты

### Status & Info
| Endpoint | Метод | Описание |
|----------|-------|----------|
| `/` | GET | HTML Dashboard |
| `/api/status` | GET | Статус, uptime, heartbeat, CPU, RAM |
| `/api/uptime` | GET | JAWL uptime в секундах |
| `/api/logs` | GET | Последние строки system.log |
| `/api/thoughts` | GET | Последние мысли агента |

### Provider & Model
| Endpoint | Метод | Описание |
|----------|-------|----------|
| `/api/providers` | GET | Список провайдеров + текущая модель |
| `/api/switch` | POST | Переключить модель, перезапустить JAWL |

### Tasks
| Endpoint | Метод | Описание |
|----------|-------|----------|
| `/api/issues` | GET | Задачи из Linear |
| `/api/issues/sessions` | POST | Привязка сессии к задаче |

### System
| Endpoint | Метод | Описание |
|----------|-------|----------|
| `/api/spawn` | GET/POST | Спавн сессий |
| `/api/command` | GET | Выполнение shell команд |

## UI Elements

### Bottom Bar
```
[● ONLINE] [♥ 300s] [16d 29м] [CPU 31%] [RAM 32%] [Jinx: ♥ 4м 10с]
```

- `bb-status` — ONLINE/OFFLINE
- `bb-heartbeat` — heartbeat интервал
- `bb-uptime` — серверный uptime
- `bb-cpu`, `bb-ram` — загрузка
- `bb-jawl-uptime` — JAWL uptime (справа)

### Provider/Model Dropdown
Два dropdown: провайдер → модель. Выбор → `api/switch` → pkill JAWL → restart.

### Tool Choice Toggle
Кнопка `🔧 Tools: ON/OFF`. Управляет forced tool_choice.

## Uptime Sources

- **Server uptime:** `subprocess.run(["uptime"])` — 4 regex формата
- **JAWL uptime:** `ps -o etimes= -p <PID>` из `/tmp/jawl.pid`

## Связанные статьи

- [[tech/jawl-config|Config]] — models.json
- [[tech/jawl-architecture|Architecture]] — общий контекст
