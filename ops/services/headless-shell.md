---
description: "Chrome Headless Shell — CDP-браузер на :9222 (рендер/скриншоты) для Hermes browser tools; systemd headless-shell.service."
tags:
  - ops
  - service
  - browser
type: service
related:
  - ops/services/lightpanda
  - ops/services/hermes-agent
service:
  name: headless-shell
  category: proxies
  purpose: "Настоящий рендеринг и скриншоты через CDP (Playwright chromium_headless_shell). Появился как основной CDP-браузер для Hermes browser tools; lightpanda остаётся лёгкой альтернативой без реального рендера."
  install_date: 2026-09-28
  last_verified: 2026-10-07
  health_url: http://127.0.0.1:9222/json/version
  type: systemd
  ports:
    - port: 9222
      protocol: tcp
      bind: 127.0.0.1
      description: "CDP endpoint (remote debugging)"
  systemd_units:
    - headless-shell.service
  docker_containers: []
  processes:
    - pattern: "headless_shell --remote-debugging-port=9222"
      description: "chromium headless shell из Playwright-бандла"
  config_paths:
    - /etc/systemd/system/headless-shell.service
    - /var/lib/headless-shell
    - /root/.cache/ms-playwright/chromium_headless_shell-1187/
  logs:
    - "journalctl -u headless-shell"
  depends_on: []
  data_size_hint: "~300MB (профиль /var/lib/headless-shell)"
  notes: >-
    Юнит создан 2026-09-28 11:39, Restart=always, запущен как root с --no-sandbox и
    --remote-allow-origins=*. Порт 9222 на хосте занимает именно этот сервис
    (127.0.0.1:9222); у контейнера lightpanda маппинга портов нет (bridge, 9222 слушает
    только внутри контейнера) — запись lightpanda.md про "0.0.0.0:9222" устарела.
    Обслуживание: профиль переживает рестарты, при утечке памяти — systemctl restart
    headless-shell. Регистрация: ночная рутина 2026-09-29 (MUL-10126).
last_verified: 2026-10-07
---
# Chrome Headless Shell (headless-shell)

CDP-браузер, который реально рендерит страницы и делает скриншоты — в отличие от
lightpanda (Zig, без полноценного JS-рендера). Бинарник взят из Playwright-бандла.

## Проверка

```bash
systemctl is-active headless-shell
curl -s http://127.0.0.1:9222/json/version
```

## Управление

```bash
systemctl restart headless-shell
journalctl -u headless-shell -n 50 --no-pager
```
