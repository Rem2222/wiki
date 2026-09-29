---
description: CodeGraph — MCP-сервер для графа кода (Tree-sitter).
tags:
  - ops
  - service
  - agent-platform
type: service
related:
  - ops/services/cgc
  - ops/workflow/new-project-with-codegraph
service:
  name: codegraph
  category: agent-platform
  purpose: MCP-сервер для анализа кода
  install_date: 2025-06
  last_verified: 2026-09-29
  health_url: http://localhost:51234/health
  type: systemd
  ports:
    -
      port: 3748
      protocol: tcp
      bind: 127.0.0.1
      description: HTTP
    -
      port: 51234
      protocol: tcp
      bind: 127.0.0.1
      description: Health endpoint
  systemd_units:
    - codegraph.service
  depends_on:
    []
  notes: "Tree-sitter код-граф + MCP (SSE, :3748). ОТКЛЮЧЁН 2026-09-29 — детали в теле страницы."
  disabled_at: 2026-09-29
  status: disabled
---

# CodeGraph (npm @leanlabsinnov/codegraph, v1.1.11)

Tree-sitter код-граф + MCP-сервер (SSE) для навигации по коду: `search_symbol`, `find_callers`, `get_dependencies`, `blast_radius`, `health` и др. Индекс — один файл БД (`/root/.codegraph/graph`), сервер `codegraph serve --port 3748` с bearer-токеном из `~/.codegraph/config.json`.

## Состояние: отключён 2026-09-29

**Решение Романа (MUL-10132): в проекте «Обнова мультика» (и в целом в workspace) не нужен — отключён.**

```bash
systemctl disable --now codegraph.service cgc-daemon.service   # 2026-09-29: inactive + disabled, порты 3748/51234 закрыты
```

Почему отключили:

- **Граф устарел и не обновлялся:** индекс замёрз на ~2026-08-06 (эпоха Multica **v0.4.17**: `ApiClient` в графе — строка 437, в коде v0.6.0 — 757). 4 утренних прогона подряд пункт «анализ через CodeGraph» отрабатывал на устаревшем графе.
- **Свежий граф = стоп сервиса + ~20 мин + ~3.5 GB RAM** (Kuzu-lock держит `codegraph serve`, ~3200 файлов монорепы; OOM-kill демона 2026-08-07). Рутина не могла держать его свежим.
- **Реальную проверку всегда делал grep/git:** 104 вызова тулов за 05.08–29.09 (16 задач, 100% из проекта Routine/«Обнова мультика», 0 вызовов из GSD и других проектов) — ни одной находки, которую не дал бы `grep`/`git show` по `/opt/multica`.
- **Побочно ускорился ACP discovery моделей:** 12.4 c → 10.3 c (таймаут демона Multica 12 c — запас был нулевой).

Осталось за владельцем (конфиг шлюза агентам не трогать, MUL-696):

- удалить блок `mcp_servers.codegraph` из `/root/.hermes/config.yaml` (~строки 691–696). Мёртвая запись агентам не мешает (клиент падает быстро, discovery 10.3 c), но оставлять её грязно.
- решить судьбу данных: `/root/.codegraph/graph` (111 MB) не удалялся.

Возврат: `systemctl start codegraph.service` → восстановить запись в config.yaml → **сначала переиндекс**, иначе граф снова будет на несколько версий позади.

Проверка символов вместо графа (рабочая процедура рутины):

```bash
cd /opt/multica && grep -rn '<symbol>' packages/ server/
git show v0.6.0:<path>
git diff v0.5.3..v0.6.0 -- <path>
```

Связано: [[ops/services/cgc]], [[ops/workflow/new-project-with-codegraph]], [[tasks/mul-239-codegraph-in-gsd]]