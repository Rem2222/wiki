---
description: "Performance Co-Pilot (PCP) — системный сборщик производительности: pmcd/pmproxy/pmie/pmlogger, метрики для внешних дашбордов."
tags:
  - ops
  - service
  - monitoring
type: service
related:
  - ops/services/beszel
  - ops/services/multi-exporter
  - ops/services/server-architecture
service:
  name: pcp
  category: monitoring
  purpose: "System-level performance metrics (PMCD + archive logger + proxy)"
  install_date: 2026-05-28
  last_verified: 2026-10-30
  health_url: "http://localhost:44322/"
  type: systemd-bundle
  ports:
    -
      port: 4330
      protocol: tcp
      bind: 127.0.0.1
      description: pmlogger control (запись архивов)
    -
      port: 44321
      protocol: tcp
      bind: 0.0.0.0
      description: pmcd (PMCD collector)
    -
      port: 44322
      protocol: tcp
      bind: 0.0.0.0
      description: pmproxy HTTP API (PMWEBAPI)
    -
      port: 44323
      protocol: tcp
      bind: 0.0.0.0
      description: pmproxy доп. listener
  systemd_units:
    - pmcd
    - pmlogger
    - pmie
    - pmproxy
    - pmlogger_farm
    - pmie_farm
  docker_containers: []
  processes:
    - pattern: pmcd
    - pattern: pmlogger
    - pattern: pmproxy
  config_paths:
    - /etc/pcp/
    - /etc/pcp.conf
    - /var/lib/pcp/
  logs:
    - /var/log/pcp/
  depends_on:
    - nginx
  data_size_hint: "/var/log/pcp ≈ 134 МБ (архивы метрик), /var/lib/pcp ≈ 1 МБ"
  notes: "Установлен пакетом pcp 6.2.0-1.1build4 (28.05.2026). Все юниты enabled от загрузки. Использования в Hermes/дашбордах не найдено — кандидат на отключение, если Роман не подключал внешний сбор."
last_verified: 2026-10-30
---

# Performance Co-Pilot (PCP)

Системный фреймворк сбора метрик производительности (аналог node_exporter, но
нативный для Linux). Ставится комплектом `pcp 6.2.0`; в системе работают шесть
юнитов, которые запускаются автоматически при загрузке.

## Архитектура

```
pmcd (44321) ──┬── pmlogger (4330) → архивы /var/log/pcp/pmlogger/
               ├── pmie (правила-алерты)
               └── pmproxy (44322/44323) → HTTP PMWEBAPI / Grafana datasource
pmlogger_farm / pmie_farm — воркеры для больших конфигураций
```

- **pmcd** — сборщик метрик (`/etc/pcp/pmcd/`), база PMDA + `pmdas/`;
- **pmlogger** — пишет архивы метрик в `/var/log/pcp/pmlogger/`;
- **pmie** — rule-based алерты (`/etc/pcp/pmie/`);
- **pmproxy** — HTTP-фасад (`http://localhost:44322/`), умеет отдавать
  PMWEBAPI и подключаться как datasource в Grafana.

## Статус на 2026-10-26

- `pmcd`, `pmlogger`, `pmie`, `pmproxy`, `pmie_farm`, `pmlogger_farm` — `active (running)`, `enabled`;
- порты 4330, 44321, 44322, 44323 слушаются;
- `curl http://localhost:44322/` → 400 (ожидаемо: API требует пути `/pmapi/...`);
- диск: `/var/log/pcp` ≈ 134 МБ — растёт архивами, чистится самим pmlogger (`/etc/pcp/pmlogger/control`).

## Обслуживание

- Ротация архивов — `pmlogger` (см. `control`/`control.d`), ручная чистка не нужна;
- Обновления — обычный `apt` (`pcp`, `pcp-conf`, `libpcp*`);
- Если сбор не нужен: `systemctl disable --now pmcd pmlogger pmie pmproxy pmlogger_farm pmie_farm`
  (раньше решения Романа — не отключать).
