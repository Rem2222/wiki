---
description: "Карта вариантов, если Agents Anywhere не устроит: Mission Control (6.3k⭐, OpenClaw), Kandev (ACP), Agency, Codeg, AgentMonitor; вывод — AA закрывает весь стек Романа"
tags: [agents,control-plane,research,acp,self-hosted]
related:
  - tech/agents-anywhere-acp-rantaym-dlya-hermes-mul-10265
  - tech/free-coding-agents-2026
---

# Control plane для всех агентов — обзор альтернатив (2026-10-11)

Роман собирает всех своих агентов в одном месте: VPS Hermes, рабочий DSX, домашние Hermes/DSX/OpenClaw/OpenCode. Главный трек — Agents Anywhere (своя страница tech/agents-anywhere-*), здесь — map альтернатив, если он не устроит. Критерии: self-hosted, несколько машин, телефон/браузер, поддержка наших агентов (Hermes ACP, DSX, OpenClaw, OpenCode).

## Кандидаты (по убыванию перспективности)

### Mission Control (builderz-labs) — ⭐6340
- Репо: github.com/builderz-labs/mission-control — self-hosted control plane для AI-агентов: диспатч задач, ревью, трекинг расходов, координация рантаймов, SQLite
- Адаптеры: OpenClaw, Claude Code, Codex, CrewAI, LangGraph, AutoGen, Claude SDK (OpenClaw — первый класс!)
- Интерфейсы: Web UI, CLI, MCP server, REST API, WebSocket, SSE
- Альфа: API/схемы могут меняться. Для «параноика» есть hardened compose-overlay и security-guidance
- Плюсы: большая база (6.3k ⭐), self-hosted без облака, OpenClaw нативно
- Минусы: альфа; адаптеров для Hermes/DSX-как-такового нет (но Hermes можно как Claude SDK? нет). Судя по описанию — это про задачи/запуски, а не про «чатик с агентом с телефона»; мобильного приложения не видно

### Kandev (kdlbs) — ACP-нативный control plane
- Репо: github.com/kdlbs/kandev, сайт kandev.ai — server-first UI: параллельные агенты в git worktree, **все агенты общаются по ACP** (Claude Code, Codex, Copilot, Gemini CLI, Auggie, OpenCode)
- Строит на ACP — того же протокола, что наш acp-рантайм (совместимость с Hermes/OpenCode/OpenClaw высокая по построению)
- Плюсы: ACP-экосистема, remote-рантаймы (sprites.dev, Docker), воркфлоу с гейтами
- Минусы: молодой; звёзд меньше; нюансы по self-hosted надо смотреть самому

### Agency (christag) — ⭐71
- Репо: github.com/christag/agency — «одна панель для всех твоих AI-агентов»: Claude Code, Codex, Gemini, Aider, Goose, **OpenCode**, Pi, custom scripts
- Без БД/без Docker: markdown + YAML frontmatter, Python/FastAPI
- Плюсы: лёгкий, поддерживает OpenCode, mission-control («что видят агенты, ревью, решения»)
- Минусы: маленький (71 ⭐), один разработчик, судя по описанию — про локальную панель, не про мульти-машины/телефон

### Codeg (lyhiving) — ⭐0
- Репо: github.com/lyhiving/codeg — агрегация сессий AI-кодинг-агентов: Claude Code, Codex, **OpenCode, OpenClaw**, Gemini CLI, Cline; desktop-приложение, self-hosted server, **Docker**; удалённая разработка из браузера; чат-каналы **Telegram/Lark/iLink**; MCP/Skills менеджмент; git worktree
- Плюсы: прямое покрытие нашего стека (OpenCode, OpenClaw), Telegram-канал = «рулить из телефона», web-режим
- Минусы: 0 звёзд (свежий/молодой), качество и безопасность не проверены; про мульти-машины в описании вскользь

### AgentMonitor (Ericonaldo) — ⭐34
- Dashboard для Claude Code/Codex: шаблоны задач, worktree, remote-доступ через relay (WebSocket-туннель, без открытых портов), JWT
- Плюсы: relay-туннель как у нас (с телефона было бы ок), password-protected
- Минусы: только Claude Code и Codex, OpenCLI-рантайм; Hermes/DSX/OpenClaw не поддержаны (нам не подходит целиком)

### Agent Dashboard (dustinblack) — ⭐15
- Multi-host оркестрация: hub (FastAPI+Socket.IO) + демоны-контейнеры на машинах; Claude Code, Pi, Antigravity, **OpenCode**, Bash; PTY-терминалы в браузере, токены через OpenTelemetry
- Плюсы: мульти-хост как задумано; OpenCode поддержан
- Минусы: мало звёзд; нет Hermes/DSX/OpenClaw; нужны демоны на каждой машине

### Reemoat (reemoat.com)
- Self-hosted удалённое управление для coding-агентов («твои агенты работают, ты спишь»); параллельные агенты, desktop и web
- Детали по open-source/self-hosted требуют проверки (в результатах поиска промелькнул GitHub-клон remote-coding-agents)

## Другие из Reddit (для контекста)
- Preloop — MCP-файрвол + gateway с бюджетами + запись сессий + апрувы; это про безопасность/контроль, не про «собрать всех в одном UI»
- Foundry (sathiyandrakumar) — «Kubernetes для AI dev-воркфлоу», Postgres, планировщик DAG; молодой
- «git-backed multi-machine control plane» (r/myclaw) — специфичный проект, Discord-нативный, не наш кейс

## Вывод
- **Agents Anywhere — остаётся основным**: уже поднят, закрывает весь стек (Hermes=acp, DSX=dsh из коробки, OpenClaw/OpenCode=acp), есть телефоный доступ (сейчас — веб-консоль по туннелю; после PR — и мобильное приложение облака)
- **Страховка №1 — Mission Control**: если AA не устроит по управлению/телефону — 6.3k ⭐, OpenClaw нативно, self-hosted; но Hermes/DSX-адаптеров нет
- **Страховка №2 — Kandev**: ACP-нативный (тот же протокол, что наш рантайм) — «следующий лучший» по совместимости с нашим стеком
- Если цель «просто посмотреть на все агенты с телефона, не строить своё» — Codeg с Telegram-каналом выглядит самым быстрым, но сырой (0 ⭐)
- Общее: категория «control plane для агентов» в 2026 активно формируется (r/AI_Agents, r/AIAgentsInAction, r/coolgithubprojects) — стоит перепроверять раз в месяц

## Связанное
- [[tech/agents-anywhere-acp-rantaym-dlya-hermes-mul-10265]]
- [[tech/free-coding-agents-2026]]
