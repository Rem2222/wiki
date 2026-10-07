---
description: "Multi-service Prometheus exporter (ntfy, GBrain, Hermes, FreeLLMAPI) — демонтирован вместе со стеком мониторинга Prometheus/Grafana; скрипт остался в /opt."
tags:
  - ops
  - service
  - monitoring
type: service
last_verified: 2026-10-08
related:
  - ops/services/server-architecture
  - ops/services/beszel
  - ops/services/ntfy
status: decommissioned
service:
  name: multi-exporter
  category: monitoring
  purpose: "Prometheus /metrics для ntfy, GBrain, Hermes, FreeLLMAPI"
  path: /opt/multica-monitoring/multi_exporter.py
  port: 8001
  type: standalone (python)
  status: "демонтирован: systemctl disable --now multi-exporter.service (Docker Monitoring Stack Teardown)"
  notes: "Скрипт остался лежать в /opt/multica-monitoring/. GBrain-метрика захардкожена = 0 (GBrain отключён 23.08.2026). Проверено 03.10.2026: юнита и процесса нет, порт 8001 закрыт."
---

# multi-exporter — Prometheus exporter (демонтирован)

Кастомный Python Prometheus-exporter на порту `8001`, отдавал `/metrics` по четырём
сервисам:

- `ntfy` — `127.0.0.1:2586/v1/stats` (сообщения, rate, up);
- `GBrain` — после отключения GBrain (23.08.2026) возвращал всегда `gbrain_up 0`;
- `Hermes` — `127.0.0.1:8642/health`;
- `FreeLLMAPI` — `127.0.0.1:3010/v1/models` (up + число моделей).

Кэш метрик — 1800 с.

## Статус

**Сервис демонтирован** в рамках teardown стека мониторинга (Grafana + Prometheus +
node-exporter): `systemctl disable --now multi-exporter.service
agentmemory-exporter.service`. На 03.10.2026 юнита нет, процесс не запущен,
`8001/tcp` закрыт; nginx-блок `/metrics/` тоже удалён.

Скрипт-первоисточник сохранился: `/opt/multica-monitoring/multi_exporter.py`
(рядом — неиспользуемый `agentmemory_exporter.py`). Если мониторинг
понадобится снова — поднимать его оттуда, а не искать в systemd.
