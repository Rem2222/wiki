---
description: "План развёртывания облачной памяти (AgentMemory + GBrain) для внешних агентов через MCP HTTP endpoints. Решение Rem от 20.08.2026 — не разворачивать пока, починить state.db, план сохранить."
tags: [plan, memory, agentmemory, gbrain, mcp, tailscale, nginx, external-agents]
type: plan
related:
  - ops/services/agentmemory
  - ops/services/gbrain
  - ops/services/tailscale
  - ops/services/nginx
  - concepts/mcp
  - tech/agent-memory-research-2026
  - tech/mempalace-viz
  - ops/services/server-architecture
created: 2026-08-20
updated: 2026-08-20
---

# Облачная память для внешних агентов — план

## Суть

У Rem на VPS уже работает собственная память для самого Hermes:
- **AgentMemory** — долговременная память фактов/сессий (iii-engine, MCP stdio, порты 3111-3113, bind 127.0.0.1);
- **GBrain** — графовая база знаний по markdown-вики (семантический поиск, MCP, порт 3131, bind 127.0.0.1);
- **MEMORY.md / USER.md** — встроенная память Hermes (файлы на диске).

Оба сервиса сейчас слушают **только loopback (127.0.0.1)** и доступны **только локальному Hermes** через MCP **stdio** (внутри процесса gateway). Внешние агенты (Mercury, JAWL, Cursor/OpenCode на Windows 3а, другие субагенты и хосты) этими хранилищами памяти **не пользуются** — у каждого своя изолированная память.

**План**: выставить AgentMemory и GBrain наружу как **MCP HTTP endpoints за bearer-токеном**, чтобы внешние агенты могли читать/писать в общую память (общая база знаний + общая память фактов). Это ответ на изоляцию памяти между агентами (см. также [[tech/agent-memory-research-2026]] и обсуждение «Совместная память Hermes между VPS и Windows»).

## Предыстория / контекст

- AgentMemory (rohitg00/agentmemory, ~18.5k⭐) — внедрён и работает. Доступен Hermes через MCP stdio. REST-консолидация не работает (`/agentmemory/health` → 404), MCP viewer на 3113.
- GBrain — внедрён + autopilot (система sync→extract→embed→orphans каждые 5 мин), работает на PostgresEngine (PostgreSQL 17 + pgvector, gbrain-postgres :5433). HTTP-сервер `gbrain serve --http`, systemd-сервис `gbrain-http.service`, порт 3131, bind 127.0.0.1, включён suppress-bootstrap-token. Admin можно открыть через nginx + Authelia.
- Известный MCP Streamable HTTP-паттерн (как в [[tech/mempalace-viz]]): подключение к удалённому серверу памяти через bearer token, работает из любой точки.

## Рассмотренные варианты (clarify-опрос Rem, 20.08.2026)

Rem выбрал из четырёх вариантов:

- **1️⃣ A+B (Recommended):** MCP HTTP endpoints за bearer (AgentMemory + GBrain) сразу **плюс** инструкция по Tailscale — самый полный вариант, доступ и из дома, и из любой точки.
- **2️⃣ Сначала A (Tailscale):** настроить доступ из дома к памяти по мешу (mesh VPN), **без** публичных endpoint. Только локальная сеть Tailscale, ничего не выставлять наружу.
- **3️⃣ Сначала B:** публичный MCP с bearer на nginx (работает из любой точки интернета, защита только токеном + Authelia при желании).
- **4️⃣ Пока не разворачивать** — только починить state.db и оставить план.

### ✅ Решение Rem: вариант 4

> **«Пока не разворачивать — только починить state.db и оставить план»**

То есть на 20.08.2026 никакие MCP HTTP endpoints для внешних агентов **не разворачиваются**. Приоритет — починка повреждённого `state.db` (базы сессий Hermes), которая на тот момент уже восстанавливалась (замена битой базы на здоровую через systemd transient-юнит, см. заметку «State.db recovery completed»). План записан и откладывается до следующего шага.

## Статус

- **status:** 🟡 отложено (backlog-like, «не запускай» = не разворачивать)
- **decision date:** 2026-08-20
- **blocker выполнения:** разворачивание отложено Rem до последующих решений; приоритет — здоровье state.db.

## Что понадобится, если решат разворачивать (черновик)

### Вариант A — через Tailscale (mesh, из дома)
- Tailscale уже стоит на VPS как exit node ([[ops/services/tailscale]]).
- Добавить VPS в tailnet (если ещё не), получить адрес `100.x.y.z`.
- Внешние агенты (Windows-машина Rem через Tailscale) подключаются к MCP-endpoint по tailnet-IP, не выставляя сервис в публичный интернет.
- Плюс: безопасно, ничего наружу, нет SSO-настроек.
- Минус: работает только там, где есть Tailscale.

### Вариант B — публичный MCP с bearer на nginx
- Прокинуть `/mcp/agentmemory` и `/mcp/gbrain` через nginx (см. [[ops/services/nginx]], конфиг `/etc/nginx/sites-enabled/hermes`).
- Закрыть bearer-токеном (и, при желании, Authelia one_factor, как у gbrain admin).
- Плюс: работает из любой точки интернета.
- Минус: сервисы памяти открыты наружу — нужен строгий токен/аутентификация, иначе это RCE-поверхность для чужих агентов.

### Вариант A+B (полный)
- MCP HTTP endpoints за bearer **и** инструкция по Tailscale — чтобы и дома, и из любой точки.

## Смежные страницы

- [[ops/services/agentmemory]] — долговременная память агента (iii-engine, cio.mcp)
- [[ops/services/gbrain]] — графовая база знаний, семантический поиск, MCP
- [[ops/services/tailscale]] — mesh VPN (exit node)
- [[ops/services/nginx]] — reverse proxy + SSL
- [[concepts/mcp]] — протокол подключения инструментов к AI-агентам
- [[tech/agent-memory-research-2026]] — исследование решений долговременной памяти
- [[tech/mempalace-viz]] — пример MCP Streamable HTTP + bearer для удалённой памяти
- [[ops/services/server-architecture]] — полная карта серверной инфраструктуры
