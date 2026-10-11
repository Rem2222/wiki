---
description: "Open-source control plane для удалённого управления AI-агентами; наш универсальный ACP-рантайм для Hermes доведён до end-to-end на VPS, PR отложен на проверку"
tags: [agents,control-plane,acp,hermes,vps]
related:
  - tech/free-coding-agents-2026
  - tech/devin-ai-agent
---

# Agents Anywhere — ACP-рантайм для Hermes (MUL-10265)

Open-source control plane для удалённого управления AI-агентами (github.com/anywhere-labs/Agents-Anywhere): телефон/веб-консоль → сервер (Docker) → connector-демон на машине агента → локальный рантайм агента (Codex/Claude/DSH; ACP — в разработке нами).

## Что сделано на 2026-10-11

### Разведка (Фаза 0, MUL-10266 → done)
- Слот `acp` зарезервирован в `RuntimeName` (connector/connector/server/protocol.py) и capabilities.py; в реестре были только claude/, codex/, dsh/
- ACP-поддержка существовала (PR #20, multi-agent ACP) и была выкинута в v2-рефакторе — остались только зарезервированные id
- Реверс hermes acp: /usr/local/lib/hermes-agent/acp_adapter/server.py — headless ACP-сервер (stdio JSON-RPC): new/load/resume/fork_session, prompt со стримингом, cancel, permission-апрувалы, set_model, set_mode

### Дизайн и код (Фазы 1–2, MUL-10267/10268 → done)
- Универсальный ACP-рантайм (один адаптер на любой ACP-агент: Hermes, Zed, OpenCode) вместо «hermes-специфичного» — выше шанс принятия PR
- Код в форке Rem2222/Agents-Anywhere, ветка feat/acp-runtime, коммит ee9d521d: пакет connector/connector/runtimes/acp/ (11 файлов: provider, provider_config, presets, runtime, models, session_identity, client), AcpProvider в providers.py, тесты test_acp_*
- Тесты: 1109 passed / 1 failed (предсуществующий codex-тест, воспроизводится на апстрим-main) / 2 skipped; ruff clean

### Живая проверка на VPS (Фаза 3, MUL-10269 → done, вёл ассистент Hermes сам)
- Docker-стек поднят: `docker compose -f docker/docker-compose.postgres.yml up -d` (postgres + redis + server-next) → консоль на :5174
- Регистрация админа: roman@rem2222.top (пароль в /root/.agents-anywhere/server-admin.password, токен в admin.token — в чат не печатать)
- Коннектор: `anywhere-cli pair http://127.0.0.1:5174` → conn_-qPS1Ly38r9wjg «VPS-Hermes» online; проект Hermes-Test (workspacePath /root)
- Runtime-инстанс создаётся отдельно через `POST /connectors/{id}/runtimes` — обязателен `command: hermes, args: [acp]` → rti_nRAj6HxI5-uBEzlj running
- End-to-end: create-and-start → HTTP 200 → ответ «тест»; второй turn «2+2?» → «4»; финальный smoke «ок» → «ок» — три независимых подтверждения, включая чистый код после снятия debug-логов
- Баг-фикс 502 «does not match the session binding»: коннектор слал нотификации/state под самогенерированным sess_acp_* вместо серверного session_id; фикс — биндинг серверного id в _sessions при create_and_start_session + чтение из state в get_session_state; коммит b890558 запушен в форк

### Доступ с телефона
- Cloudflare quick tunnel (cloudflared на VPS, порт 5174 в ufw закрыт): https://frequent-conversion-measurements-indirect.trycloudflare.com (адрес временный — живёт, пока жив процесс cloudflared; при перезапуске меняется, просить новый)
- CORS дополнен regex на trycloudflare-домены (docker-compose override /tmp/aa-cf-override.yml, контейнер server-next пересоздан)
- Официальное мобильное приложение Agents Anywhere работает ТОЛЬКО с облаком web.agents-anywhere.com — туда Hermes не подключить до принятия PR (в облаке только codex/claude/dsh). Для телефона — браузер по туннельному адресу, «Добавить на главный экран»

## Собираем всех агентов в одном месте (вывод от 2026-10-11)

Цель Романа: один клиент/консоль для VPS Hermes + рабочего DSX + домашних Hermes/DSX/OpenClaw. **Agents Anywhere это закрывает — и наш acp-рантайм тут системный, а не «ещё один адаптер»:**

| Машина | Агент | Чем подключаем | Статус |
|---|---|---|---|
| VPS | Hermes | acp-рантайм (`hermes acp`) | ✅ проверено end-to-end |
| Работа | DSX (DeepSeek Harness) | **родной dsh-рантайм в апстриме** (не наш код!) | ⏳ нужен коннектор на рабочей машине |
| Дом | Hermes | acp-рантайм | ⏳ нужен коннектор |
| Дом | DSX | родной dsh-рантайм | ⏳ нужен коннектор |
| Дом | OpenClaw | `openclaw acp` — сам OpenClaw умеет ACP-мост к своему Gateway | ⏳ нужен коннектор + проверить совместимость |
| Дом | OpenCode | acp-рантайм (OpenCode говорит по ACP) | ⏳ нужен коннектор |

- dsh-рантайм ПРИСУТСТВУЕТ в апстрим-реестре (connector/connector/runtimes/dsh/) — DSX и OpenClaw-работа подключаются без нашего форка, только родным `anywhere-cli`
- Универсальность acp: Hermes (`hermes acp`), OpenClaw (`openclaw acp`), OpenCode, Zed — все говорят по ACP, один рантайм на всех
- В облаке (web.agents-anywhere.com) пока только codex/claude/dsh: Hermes появится там после мержа PR (#276)
- Ограничение self-hosted сейчас: коннектор на других машинах из форка (PR не влит), мобильное приложение облака не видит наш acp; решение на пару дней — веб-консоль по туннелю

## Как продолжить
1. **Проверка Романом (пара дней)** — тестировать сессии с телефона по туннельному адресу; Фаза 4 (PR) специально отложена до этого
2. **Фаза 4 (MUL-10270)**: PR в anywhere-labs «ACP runtime» (closes #276) + комментарий в issue; пока в форке Rem2222/Agents-Anywhere ветка feat/acp-runtime (ee9d521 + b890558)
3. Идеи на будущее: домашний DSX/OpenCode поднять коннектор из этого же форка (`anywhere-cli pair <server-address>`), т.к. ACP-рантайм живёт только в форке до мержа

## Ограничения / сводка
- Мобильное приложение = только облако → ждём PR для Hermes
- ACP-рантайм пока не в апстриме — на других машинах коннектор брать из форка
- Туннельный адрес временный; для постоянного — DNS aa.rem2222.top (reg.ru, вручную) + nginx
- Корневой вопрос «собрать всех агентов в одном месте» (VPS Hermes + работа DSX + дома Hermes/DSX/OpenCode) — открыт, есть кандидаты-альтернативы (см. research-страницу agents-anywhere-alternatives)

## Связанное
- [[tech/free-coding-agents-2026]]
- [[tech/devin-ai-agent]] (Devvin — бывший Devin) — конкурентный класс инструментов
