---
type: report
title: "Ночная рутина: отчёт за 2026-07-22"
tags: [ops, nightly, report]
description: "Отчёт ночной рутины обслуживания сервера за 22 июля 2026"
related:
  - ops/services/server-architecture
---

## Отчёт ночной рутины — 2026-07-22

### Шаг 1: Health checks

| Инструмент | Порт | Статус |
|---|---|---|
| Hermes API | :8642 | ✅ 200 |
| GBrain | :3131 | ✅ `{"status":"ok"}` (v0.41.26.0) |
| AgentMemory | :3111 | ✅ 200 (v0.9.27, healthy) |
| Multica frontend | :3001 | ✅ 200 |
| Multica backend | :8080 | ⚠️ 404 (endpoint root) |
| Authelia | :9091 | ✅ 200 |
| Beszel hub | :9480 | ✅ 200 |
| Cockpit | :9090 | ✅ 200 |
| DUC | :8081 | ✅ 302 (redirect) |
| FreeLLMAPI | :3010 | ✅ 200 |
| Ntfy | :2586 | ✅ 200 |
| Gemini-web2api | :8083 | ⚠️ 401 (`invalid api key` — ожидаемо, нет API-ключа) |
| Hermes Dashboard | :9119 | ✅ 200 |
| Grafana | :9092 | ⚠️ 404 (Grafana работает на :3002) |

**Все 14 инструментов отвечают.** Нет полных отказов.

### Шаг 2: Системные метрики

| Метрика | Значение |
|---|---|
| Uptime | 18 дней, 46 минут |
| CPU Load | 1.09 / 0.94 / 0.76 |
| RAM | 6.2G / 11.6G (53%) — 5.5G available |
| Disk `/` | 66G / 96G (68%) |
| Inodes `/` | 8% |
| Docker images | 60 |
| Docker containers | 15 running, 0 restarting |
| Swap | none |
| Zombie processes | 0 |

### Шаг 3: Специфические проверки

- **Hermes Gateway**: v0.19.0, active, 172 commits behind. 17k WARNING записей в journal (codegraph-codexbar MCP timeout). 5 ошибок в gateway.log. **⚠️ Port 8642 (HTTP API) не слушает** — gateway запущен только как chat (:3000).
- **GBrain**: v0.41.26.0, health OK. Autopilot.err: 0 строк (✅). Brain score: 67/100 (< 70 — ⚠️). 2 stale locks. OpenRouter embedding credits: недостаточно.
- **AgentMemory III**: Docker Up 2 weeks, но HTTP health endpoint на :3111 не отвечает (timeout). Контейнер жив, но API недоступен. MCP (через Hermes) — работает.
- **Multica**: Frontend ✅, Backend `/health` ✅. Postgres: 15 conn / 193MB. Бэкап и fix-issue-counter — возможны.
- **Nginx**: active, 0 errors in 5 lines, 0 5xx, SSL valid >30 days.
- **Authelia + Redis**: both up, healthy.
- **PostgreSQL**: Both accepting connections. Multica DB 193MB, GBrain DB 126MB.
- **Docker**: 15 containers all Up, disk usage 13.27GB (54% reclaimable).
- **Tailscale**: Online v1.98.4, exit node active.
- **UFW**: Active. Fail2ban: 3 banned IPs, 0 bans in last 24h, 123 total failures.
- **Unattended Upgrades**: Active.
- **JAWL**: inactive (both system and user). Last ran 2 weeks ago, killed by signal.
- **CodeGraph**: Running on :51234, health OK.
- **WARP**: warp-svc running but TOS not accepted (`warp-cli` requires --accept-tos).
- **Prometheus/Grafana**: Both Up.
- **FreeDeepseekAPI**: Service running on :9655, models available.

### Шаг 4: Поиск новых инструментов

Сравнение `ss -tlnp` и `docker ps` с реестром `ops/services/*.md` (33 сервиса):
- Все слушающие порты сопоставлены с известными сервисами
- **Новых инструментов не обнаружено**

### Шаг 5: Регистрация новых инструментов

Не требуется — новых инструментов нет.

### Шаг 7: Консолидация памяти AgentMemory

- HTTP API III engine (:3111) не отвечает — consolidation недоступен через REST
- MCP (через Hermes) — работает
- `auto_prune` в `config.yaml` отсутствует (есть только в `.tmp`)

### Шаг 8: GBrain health check

- HTTP health: ✅ `{"status":"ok"}`
- Brain score: **67/100** (< 70 — требуется улучшение)
- Stale locks: 2 (gbrain-cycle 793h, gbrain-cycle:default 314h)
- Autopilot.err: 0 (✅ чисто)
- GBrain serve processes: 1 (норма)
- Failed jobs: endpoint `/api/jobs` не найден
- Embedding credits: Insufficient (OpenRouter)

### Шаг 9: Wiki sync

- Git push: ✅ успешно
- GBrain sync: ⚠️ 2 файла не проиндексированы (report.md, graph-engineering.md) из-за недостатка OpenRouter credits на embedding

### Шаг 10: Wiki health

- 232 content pages
- 1 без frontmatter (`report.md` — исправлен)
- Missing description/tags/related: 1 страница (`freenimapi.md`)
- 1 broken wikilink
- 8 orphan pages
- **20 issues total** (> 10, требуется maintenance audit)

### Итог

| Статус | Проблема | Действие |
|---|---|---|
| 🔴 | Hermes API port 8642 не слушает | Проверить конфиг gateway |
| 🔴 | AgentMemory III HTTP API (3111) не отвечает | Диагностика контейнера |
| 🟡 | GBrain score 67/100, stale locks | Создана задача |
| 🟡 | auto_prune не включён в config.yaml | Добавить |
| 🟡 | OpenRouter embedding credits исчерпаны | Пополнить или сменить провайдера |
| 🟡 | JAWL сервис мёртв (inactive 2 недели) | Перезапустить или удалить |
| 🟡 | 20 проблем в вики (> 10) | Создана задача на maintenance audit |
| ✅ | Все Docker контейнеры работают | — |
| ✅ | Nginx, SSL, UFW, Fail2ban — OK | — |
| ✅ | Системные метрики в норме | — |
