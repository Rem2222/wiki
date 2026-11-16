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
  last_verified: 2026-11-09
  health_url: "http://127.0.0.1:8799/health"
  type: systemd
  ports:
    - port: 8799
      protocol: tcp
      bind: 127.0.0.1
      description: "WebSocket realtime qwen-audio; GET /health → JSON 200/503 (с 25.10), прочие HTTP-пути → 426 (нужен Upgrade)"
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
    Health: 8799/health → 200 (JSON: апстрим Али, OpenViking, клиенты/сессии),
    при проблемах 503; 8798 → 200; корень 8799 → 426 (норма, только WS).
    Исходники с 25.10 в git: https://github.com/Rem2222/voice-gateway (публичный),
    автокоммит+push — секция VOICE-GATEWAY GIT PUSH в /root/scripts/pg-backup.sh
    (ночная рутина, MUL-10397). Докачка ключа
    alibaba/tokenplan — см. строки с маркерами в gen_brief.py; ротация ключа
    Aliyun и keystore TWA зарегистрирована (см. MUL-10140).
last_verified: 2026-11-09
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

## Провайдеры realtime-голоса

Клиент (`/rt/`, настройки → «Провайдер голоса») выбирает бэкенд, шлюз принимает
`start.provider`:

| Провайдер | Модель | Состояние |
|---|---|---|
| `ali` (по умолчанию) | `qwen-audio-3.0-realtime-plus` через token-plan | квота месячная, при 429 шлюз отдаёт `Апстрим Aliyun недоступен` |
| `gemini` | `gemini-3.8-live` (`gemini_session.py`) | работает, бесплатный ключ `GEMINI_FREE_API_KEY` |

Особенности Gemini-пути (выяснено живыми пробами 16.11.2026, коммит `3325fc9`):

- Вход — `realtime_input.audio` (объект, **один блоб на сообщение**); в gemini-3.x
  `media_chunks` объявлен deprecated, пачка 2+ → close `1007`.
- Встроенный VAD отключён (`automatic_activity_detection.disabled`), границы хода
  задаёт шлюз: `activity_start` → аудио → `activity_end`. Пустой
  `client_content.turns` работал только на первом ходу, дальше `turnComplete` без
  `modelTurn` (аудио не приходило).
- `thought:true` парты — внутренние размышления модели (по-английски). В клиент не
  отдаются: раньше из-за них в пузыре был трактат вместо ответа.
- `output_audio_transcription` → сообщение `type:"text"` клиенту (в пузыре ровно
  то, что озвучено); `input_audio_transcription` → `/debug`.
- Живой замер через шлюз, 4 фразы подряд: first_audio 0,91–1,25 с, аудио везде.
  Старая `gemini-2.5-flash-native-audio-preview-09-2025` на речи давала 2,8–4,5 с
  и теряла аудио на 3-м ходу — не использовать.
- `GET http://127.0.0.1:8799/debug` — кольцевой журнал (120 событий), только
  localhost.


### Выбор голоса и расшифровка пользователя (16.11.2026, BUILD 0.5.5)
- Селектор «Голос» в настройках PWA, отдельное значение для каждого провайдера в localStorage; смена переподключает сессию.
- Али, `qwen-audio-3.0-realtime-plus`: системные голоса `longanqian` (по умолчанию), `longanlingxin`, `longanlingxi`, `longanxiaoxin`, `longanlufeng`. По документации voice задаётся **только в первом** `session.update` — шлюз делает именно так. Источник: `raw/model-api-reference/realtime-api-directory/audio-realtime-api-directory/fun-audiochat-client-events.md`, строка 45 (скилл bailian-docs-llm-wiki).
- Gemini 3.8 Live: голоса Aoede, Kore, Fenrir, Puck, Charon, Leda, Orus через `generation_config.speech_config.voice_config.prebuilt_voice_config.voice_name`; пустое значение = голос модели. Все семь проверены живо.
- `serverContent.inputTranscription.text` → сообщение `type:"user_text"` клиенту: в «Расшифровке» вместо «Голосовая фраза · N с» появляется распознанный текст. До этого текст был только в локальном `/debug`. У Али входная расшифровка не включена.

## Обслуживание

- Проверка: `systemctl is-active voice-gateway voice-brief`;
  `curl -sf http://127.0.0.1:8799/health` → 200 = ok, 503 = degraded (JSON:
  `upstream.reachable`/`state` — апстрим Али, `openviking.healthy`,
  `clients`/`sessions`, `tool_calls`, `problems`);
  brief — `curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8798/` → 200.
- Логи: `journalctl -u voice-gateway -n 50`; на HTTP-пробу к 8799 в лог падает
  `websockets.exceptions.InvalidUpgrade: missing Connection header` — это норма.
- Платёж/ключ Aliyun MaaS — внешняя зависимость: при отказе апстрима WS
  обрывается молча; теперь обрыв виден в `/health` (`upstream.state: error`,
  `reachable: false`, текст в `last_error`/`problems`).
- Исходники: `/root/voice-gateway` — git-репозиторий
  https://github.com/Rem2222/voice-gateway (создан 25.10.2026, MUL-10397),
  коммит+push при каждом ночном `pg-backup.sh`. Секреты в репозиторий не кладутся:
  ключ Aliyun читается из `/root/.hermes/.env`, пароль keystore лежит рядом со
  сборкой; ротация обоих — в реестре секретов (см. MUL-10140).
- Пересборка APK: `/root/twa-build` (gradle, keystore-пароль в `.keystore-pass`,
  mode 600), нужен `/opt/android-sdk` + openjdk-17.
