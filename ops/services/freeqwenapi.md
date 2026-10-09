---
description: FreeQwenApi — OpenAI-совместимый прокси для Qwen Web Chat (qwen3.7-max).
tags:
  - ops
  - service
  - llm-proxy
type: service
related:
  - ops/services/freedeepseekapi
  - ops/services/freellmapi
  - qwen-free-api
  - free-api-deepseek-qwen
service:
  name: freeqwenapi
  category: llm-proxy
  purpose: Бесплатный Qwen API через Qwen Web Chat (chat.qwen.ai)
  install_date: 2026-09-28
  last_verified: 2026-10-10
  health_url: "http://localhost:9656/api"
  type: systemd
  ports:
    -
      port: 9656
      protocol: tcp
      bind: 127.0.0.1
      description: API
  systemd_units:
    - freeqwenapi
  processes:
    -
      pattern: FreeQwenApi/index.js
  config_paths:
    - /opt/FreeQwenApi
    - /etc/systemd/system/freeqwenapi.service
  logs:
    - journalctl -u freeqwenapi
  depends_on: []
  data_size_hint: ~300MB (node + Playwright headless chromium, +swap ~225MB)
  notes: >-
    30.09 (днём) — СЕРВИС ОСТАНОВЛЕН по решению Рома: completion-эндпоинт упирался в Aliyun WAF
    (FAIL_SYS_USER_VALIDATE / RGV587_ERROR), а Playwright-браузер юнита съедал 54% CPU и 475 МБ RSS.
    Юнит inactive, MainPID=0. Включить обратно: systemctl start freeqwenapi.
    2026-09-30: страница создана ночной рутиной (MUL-10138) — сервис работал, но не был в реестре.
    Nginx: https://rem2222.top/qwen/ → 127.0.0.1:9656 (за Authelia). Модель qwen3.7-max используется
    Multica-агентом «FreeQwenApi» (freeqwenapi:qwen3.7-max). Требует живой сессии chat.qwen.ai —
    детали деплоя и авторизации в wiki:qwen-free-api; хелперы /usr/local/bin/qwen-inject-cookies и
    qwen-prep-tokens. 29.09 юнит 4 раза падал на старте (16:01–16:30, инъекция кук), с 16:37 работает
    стабильно. Живость: GET /api → 200 (/ и /v1/models отдают JSON «Эндпоинт не найден» — это норма).
    Бэкап дистрибутива: /root/backups/FreeQwenApi-20260928_142745.tgz.
last_verified: 2026-10-09
---
