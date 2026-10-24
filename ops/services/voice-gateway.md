---
description: "Voice Gateway — голосовой шлюз Романа: PWA https://rem2222.top/rt/ ↔ realtime qwen-audio через WS (8799) + выжимка сессий Hermes /rt/brief (8798); systemd-юниты voice-gateway и voice-brief, поставлены 24.10.2026."
tags: [ops, service, voice, ai, pwa]
type: service
related:
  - ops/services/openviking
  - ops/services/nginx
  - ops/services/hermes-agent
  - ops/services/authelia
service:
  name: voice-gateway
  category: ai-voice
  purpose: "Голосовой ассистент: браузерная PWA шлёт аудио в realtime-модель qwen-audio (Aliyun MaaS), инструменты ходят в OpenViking; рядом HTTP-сервис выжимки сессий Hermes для системного промта"
  install_date: "2026-10-24"
  last_verified: 2026-10-25
  health_url: "http://127.0.0.1:8798/"
  type: systemd
  ports:
    - port: 8799
      protocol: tcp
      bind: 127.0.0.1
      description: "WebSocket realtime qwen-audio (только HTTP-проба даёт 426 — нужен Upgrade)"
    - port: 8798
      protocol: tcp
      bind: 127.0.0.1
      description: "HTTP выжимка сессий (GET / и /?days=N, кэш /tmp/daily_brief.txt 30 мин)"
  systemd_units:
    - voice-gateway.service
    - voice-brief.service
  processes:
    - pattern: "voice-gateway/gateway.py"
    - pattern: "voice-gateway/brief_server.py"
  config_paths:
    - /root/voice-gateway/gateway.py
    - /root/voice-gateway/brief_server.py
    - /root/voice-gateway/gen_brief.py
    - /etc/systemd/system/voice-gateway.service
    - /etc/systemd/system/voice-brief.service
    - /etc/nginx/sites-enabled/hermes (location = /rt/ws, = /rt/brief)
    - /var/www/landing/ (PWA-статика, manifest, /.well-known/assetlinks.json)
  logs: "journalctl -u voice-gateway -u voice-brief"
  depends_on:
    - openviking
    - nginx
    - authelia
  data_size_hint: "исходники ~18 KB; сборка Android TWA /root/twa-build ~4 MB"
  notes: >-
    Юниты созданы 2026-10-24 (enabled, Restart=always, RestartSec=5), оба живы.
    gateway.py: WS-сервер на 127.0.0.1:8799, апстрим
    wss://token-plan.ap-southeast-1.maas.aliyuncs.com/api-ws/v1/realtime?model=qwen-audio-3.0-realtime-plus,
    инструменты — поиск и чтение через OpenViking http://127.0.0.1:8900
    (API-ключ из /root/.openviking/api-key.txt). brief_server.py: 127.0.0.1:8798,
    отдаёт выжимку сессий из /root/.hermes/state.db (заголовки + user-вопросы,
    срезка до 300 символов, строки с маркерами секретов выкидываются).
    Наружу: nginx location = /rt/ws и = /rt/brief (за Authelia), статика PWA
    отдаётся публично из /var/www/landing (manifest/sw/иконки без SSO).
    Android: пакет top.rem2222.voiceassistant, TWA-сборка /root/twa-build
    (app-release-signed.apk 24.10.2026), для неё 24.10 поставлены openjdk-17 и
    /opt/android-sdk; подпись подтверждена в /.well-known/assetlinks.json.
    Health: 8798 → 200; 8799 по HTTP → 426 (норма, только WS). Докачка ключа
    alibaba/tokenplan — см. строки с маркерами в gen_brief.py.
last_verified: 2026-10-25
---
# Voice Gateway (voice-gateway + voice-brief)

Голосовой шлюз Романа, поставлен **24.10.2026**: браузерная PWA на
`https://rem2222.top/rt/` разговаривает с realtime-моделью `qwen-audio-3.0-realtime-plus`
через WebSocket, а рядом работает HTTP-сервис «выжимки» сессий Hermes для
системного промта.

## Ключевые факты

| Параметр | Значение |
|---|---|
| Юниты | `voice-gateway.service`, `voice-brief.service` (systemd, enabled, Restart=always) |
| Код | `/root/voice-gateway/{gateway,brief_server,gen_brief}.py` |
| Порты | `127.0.0.1:8799` (WS), `127.0.0.1:8798` (HTTP brief) |
| Наружу | `https://rem2222.top/rt/ws`, `https://rem2222.top/rt/brief` (за Authelia) |
| LLM upstream | `wss://token-plan.ap-southeast-1.maas.aliyuncs.com/...?model=qwen-audio-3.0-realtime-plus` |
| Инструменты | OpenViking `http://127.0.0.1:8900` (search, content/read) |
| Источник выжимки | `/root/.hermes/state.db` (последние N дней, без tool-результатов и секретов) |
| Android TWA | пакет `top.rem2222.voiceassistant`, сборка `/root/twa-build` |

## Обслуживание

- Проверка: `systemctl is-active voice-gateway voice-brief`; brief —
  `curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8798/` → 200.
- Логи: `journalctl -u voice-gateway -n 50`; на HTTP-пробу к 8799 в лог падает
  `websockets.exceptions.InvalidUpgrade: missing Connection header` — это норма.
- Платёж/ключ Aliyun MaaS — внешняя зависимость: при отказе апстрима WS
  обрывается молча (своего health-endpoint у gateway нет).
- Пересборка APK: `/root/twa-build` (gradle, keystore-пароль в `.keystore-pass`,
  mode 600), нужен `/opt/android-sdk` + openjdk-17.
