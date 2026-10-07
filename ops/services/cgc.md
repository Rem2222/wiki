---
description: CGC (CodeGraphContext) — MCP-сервер для графа кода Multica.
tags:
  - ops
  - service
  - agent-platform
type: service
related:
  - ops/services/codegraph
service:
  name: cgc
  category: agent-platform
  purpose: MCP-сервер для кодовой базы Multica
  install_date: 2026-07-03
  last_verified: 2026-10-08
  health_url: "http://localhost:51234/"
  type: systemd
  ports:
    -
      port: 51234
      protocol: tcp
      bind: 127.0.0.1
      description: API
  systemd_units:
    - cgc-daemon
  depends_on:
    []
  notes: "Python uv tool (CodeGraphContext). ОТКЛЮЧЁН 2026-09-29 вместе с codegraph — детали в теле страницы."
  disabled_at: 2026-09-29
  status: disabled
last_verified: 2026-10-07
---

# CGC (CodeGraphContext)

Вторая реализация код-графа на сервере: Python-тул (`uv tool`), API на :51234, БД — KuzuDB/FalkorDB, индексируется через `cgc index -c <context> <path>`. Два контекста в `/root/.codegraphcontext/config.yaml`:

- `multica` → `/opt/multica` (kuzudb) — для рутины «Обнова мультика»;
- `codexbar` → репо CodexBar-Win (falkordb) — одноразовая задача, репо уже в старом workdir.

## Состояние: отключён 2026-09-29

**Решение Романа (MUL-10132): вместе с `codegraph.service` — `systemctl disable --now cgc-daemon.service` (inactive + disabled, :51234 закрыт).**

- Контекст `multica` отстаёт так же, как MCP-граф: обновление = полный re-index ~20 мин / ~3.5 GB RAM (OOM-kill демона 2026-08-07), поэтому в рутине он не обновлялся и 4 прогона подряд был неактуален.
- Прямых вызовов `cgc` из автопилотов/кронов не было — использовался только вручную; 104 захода «нужен граф» решались `grep`/`git` по `/opt/multica`.
- Данные (`contexts/`, 525 MB) не удалялись — решение за Романом.

**Возврат:** `systemctl start cgc-daemon.service`, при необходимости переиндекс `cgc index -f -c multica /opt/multica` (в окно с остановленными шлюзом и демоном Multica), после использования — снова stop+disable.

Связано: [[ops/services/codegraph]], [[ops/workflow/new-project-with-codegraph]]