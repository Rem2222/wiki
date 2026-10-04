---
description: "Lightpanda — headless-браузер на Zig (CDP-совместим) для AI-агентов, порт 9222."
tags:
  - ops
  - service
  - browser
type: service
related:
  - "[[ops/services/hermes-agent]]"
  - "[[ops/services/headless-shell]]"
  - "[[tech/lightpanda-browser]]"
service:
  name: lightpanda
  category: system
  purpose: Headless-браузер для AI-агентов и веб-скрейпинга (не форк Chromium, на Zig)
  install_date: 2026-07-27
  last_verified: 2026-10-04
  health_url: "http://localhost:9222/"
  type: docker
  ports:
    -
      port: 9222
      protocol: tcp
      bind: 0.0.0.0
      description: CDP endpoint (headless browser)
  docker_containers:
    - lightpanda
  depends_on:
    []
  data_size_hint: ~50 MB image
  notes: "docker run lightpanda/browser (plain run, no compose). Используется Hermes browser tools как лёгкая альтернатива headless Chrome. Лимит памяти: 4GiB (поднят 2026-08-15 с 2GiB, MUL-831 — OOM-kill при пиковой конкуренции сессий на тяжёлых JS-сайтах). Образ обновлён 15.08 до nightly.8662 (mem-фиксы ArenaPool/blob/_proto, вышли 30-31.07; лик #2460 Frame.removeNode не освобождает память). Таймер lightpanda-restart.timer — рестарт каждые 6ч. 2026-09-29: на хосте 127.0.0.1:9222 слушает headless-shell.service (у контейнера lightpanda маппинга портов нет, слушает только внутри bridge-сети) — см. ops/services/headless-shell."
  memory_limit: 4GiB
last_verified: 2026-10-05
---