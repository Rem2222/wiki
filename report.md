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
| Swap | 0B (нет swap) |
| Disk / | 64G / 96G (67%) |
| Inodes | 8% использовано |
| Zombie processes | 0 |
| Docker образы | 58 |
| Docker контейнеры | 15 running, 0 restarting |
| Docker диск | 12.97GB (образы), 957.5MB (volumes) |

### Шаг 3: Обслуживание по списку

**Hermes:**
- Gateway: ✅ active
- Ошибки в journalctl за 24ч: **🔴 29167** (ERROR/Traceback/failed) — массовые ошибки
- Gateway log ошибки: **15**
- Версия: v0.18.2 (2026.7.7.2)
- `hermes update` был прерван: **🔴 SOCKS proxy не даёт доступа к pypi.org** — требуется ручное восстановление
- `auto_prune`: ✅ true

**GBrain:**
- HTTP health: ✅ `{"status":"ok"}`
- Brain Score: **86** ✅ (выше 70, норма)
- Stale pages: **17**
- Orphan pages: **15**
- Missing embeddings: 3
- Autopilot.err: **0 строк** ✅ (было 43K, улучшение!)
- Процессов gbrain serve: **1** ✅
- DB connection: ✅ нет ошибок
- Упавших задач: **0** ✅

**AgentMemory:**
- Docker: ✅ Up 2 weeks
- Статус: ✅ healthy (v0.9.27)
- Активных сессий: **2142** — многовато
- Эпизодическая консолидация: ✅ успешно
- Семантическая консолидация: ⚠️ timeout 30s (возможно, недостаточно семплов)

**Multica:**
- frontend: ✅ Up 3 days
- backend: ✅ Up 3 days
- postgres: ✅ Up 11 days (healthy)
- Grafana: ✅ Up 2 weeks
- Prometheus: ✅ Up 2 weeks
- Node-exporter: ✅ Up 2 weeks

**PostgreSQL:**
- Multica DB: ✅ accepting, 32 connections, 189 MB
- GBrain DB: ✅ accepting, 7 connections, 43 MB

**Nginx:**
- Сервис: ✅ active
- Ошибки upstream: ✅ 0
- 5xx в access.log: ✅ 0

**SSL:**
- Сертификат: ✅ не истекает в ближайшие 30 дней

**Authelia + Redis:**
- Authelia: ✅ Up 2 days (healthy)
- Redis: ✅ Up 2 weeks

**Beszel:**
- Hub: ✅ Up 2 weeks
- Agent: ✅ Up 2 weeks

**Cockpit:**
- Сервис: ✅ active
- HTTP: ✅ 200

**DUC:**
- HTTP: ✅ 302

**Tailscale:**
- Статус: ✅ Online (v1.98.4)

**UFW:**
- Статус: ✅ active
- Правила: 80, 443, 3001, 3114, 2586, 8765, 22022

**Fail2ban (sshd):**
- Currently failed: 0
- Total failed: 67
- Currently banned: **3** (106.13.74.207, 157.7.195.26, 45.198.224.114)
- Ban/Unban за 24ч: 3

**Unattended Upgrades:**
- ✅ active, были автообновления 2026-07-21

**JAWL:**
- **🔴 INACTIVE/FAILED** — сервис не работает

**Gemini-web2api:**
- Docker: ✅ Up 2 weeks
- HTTP: 401 (ожидаемо)

**FreeLLMAPI:**
- Docker: ✅ Up 2 weeks (healthy)
- HTTP: ✅ отвечает, модель `auto`

**Ntfy:**
- Docker: ✅ Up 2 weeks

**Prometheus/Grafana:**
- Grafana: ✅ Up 2 weeks
- Prometheus: ✅ Up 2 weeks

**CodeGraph:**
- MCP process: ✅ (stdio-based, не HTTP)

**WARP:**
- Процесс warp-svc: ✅ работает (с Jul 3)
- warp-cli: недоступен (не установлен CLI)

**Hermes Dashboard:**
- Сервис: ✅ active
- HTTP: ✅ 200

**Логи сервера:**
- Journald: 1.0G на диске
- Повторяющиеся ошибки: xdg-desktop-portal (GTK) — 8 раз, systemd-networkd-wait-online timeout — 3 раза, sshd kex error — 3 раза

### Шаг 4: Поиск новых инструментов

Сравнение `ss -tlnp` + systemd + docker со списком в `~/Documents/wiki/ops/services/*.md`:

**Все 33 документированных сервиса обнаружены и работают.** Новых недокументированных инструментов не найдено.

Необычные порты проверены:
- :3003 → monitor-ui (VPS мониторинг) — ✅ в wiki
- :3333 → Dex Control Center — ✅ в wiki
- :8650 → Skills Dashboard — ✅ в wiki
- :3002 → Grafana — ✅ в wiki
- :9655 → FreeDeepseekAPI — ✅ в wiki

### Шаг 5: Регистрация нового инструмента

Новых инструментов не обнаружено. Обновлены `last_verified` на 2026-07-22 у всех 33 страниц в `ops/services/`.

### Шаг 7: Консолидация памяти AgentMemory

- Эпизодическая консолидация: ✅ успешно (результатов нет — данных мало)
- Семантическая консолидация: ⚠️ timeout 30s
- Hermes config auto_prune: ✅ true

### Шаг 8: GBrain health check

- Brain Score: **86/100** ✅
- Stale pages: 17
- Orphans: 15
- Failed jobs: 0
- Autopilot errors: 0 ✅

### Шаг 9: Синхронизация Wiki

- ✅ git add, commit, push — успешно (commit 9538bdd)
- ✅ GBrain sync job #798 отправлен
- ✅ Нет конфликтов

### Шаг 10: Wiki health check

- **16 issues found** (>10, требуется maintenance audit)
- 4 страницы без description/tags/related
- 1 битая вики-ссылка (`[[tech/proactive-agent-decision]]`)
- 6 orphan-страниц (без обратных ссылок)
- Git: ✅ чист, без конфликтов

### Проблемы, требующие внимания (🔴)

| # | Проблема | Статус |
|---|---|---|
| 1 | **Hermes Gateway**: 29167 ошибок в journalctl за 24ч | Требует расследования |
| 2 | **Hermes update**: прерван, SOCKS proxy блокирует pypi.org | Ручное восстановление |
| 3 | **JAWL**: сервис inactive/failed | Требует диагностики |
| 4 | **Wiki health**: 16 проблем | Требует maintenance audit |
| 5 | **AgentMemory**: 2142 сессии | Возможно, нужна чистка |
