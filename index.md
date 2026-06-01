# Index — Каталог вики

_Обновлено: 2026-06-01_

## Projects
- [[projects/veritas-kanban]] — Kanban-доска для AI-агентов (Git worktree, Markdown storage)

## Концепции
- [[concepts/llm-wiki]] — паттерн персональных баз знаний с помощью LLM
- [[concepts/rag]] — Retrieval-Augmented Generation, альтернативный подход
- [[concepts/memex]] — проект Вэнивара Буша 1945, ассоциативное хранилище знаний
- [[concepts/sdd]] — Spec-Driven Development, подход к разработке через спецификации
- [[concepts/mcp]] — Model Context Protocol, открытый протокол для AI-интеграций
- [[concepts/doxygen]] — генератор документации из исходного кода (C++, Java, Python...)
- [[concepts/tradingagents]] — Multi-agent LLM фреймворк для алгоритмической торговли (UCLA + MIT)

## SDD-Orchestrator v2 (2026-05-04)
- [[tech/sdd-openspec-orchestrator-integration]] — Orchestrator Integration (что хотели для Оркестратора: QA Gate, multi-layer SDD, hybrid context)
- [[tech/sdd-openspec-sdd-developer]] — SDD Developer Agent (детали SDD Developer: RFC 2119, workflow, self-validation, QA Gate)
- [[tech/sdd-orchestrator-v2]] — Overview (старая версия, но содержит acceptance criteria)
- [[tech/sdd-openspec-precommit]] — Pre-commit hook
- [[tech/sdd-openspec-real-project]] — Real project integration

## Технологии
- [[tech/1c-mcp]] — MCP серверы для экосистемы 1С (vibecoding1c.ru)
- [[tech/mempalace-viz]] — визуализация графа знаний для MemPalace (D3.js, MCP, Cloudflare)
- [[tech/agents-best-practices]] — best practices для проектирования агентных систем (provider-agnostic)
- [[tech/agentation]] — Enterprise-платформа для оркестрации AI-агентов (no-code, HITL, on-premise)
- [[tech/assemblyai]] — API-first распознавание речи и аудиоинтеллект (STT, LeMUR)
- [[tech/authelia]] — Self-hosted SSO (Authelia) + nginx auth_request, Docker compose
- [[tech/beszel]] — Лёгкая система мониторинга серверов (Hub + Agent)
- [[tech/cockpit]] — веб-администрирование сервера, reverse proxy, SSO, плагины
- [[tech/codex-harness]] — Codex Harness plugin для нативного Codex app-server runtime
- [[tech/codexbar-win-cookie-decryption]] — расшифровка Chromium cookies через DPAPI + AES-GCM
- [[tech/cookie-decryptor]] — извлечённые процедуры из CodexBar-Win для расшифровки cookies
- [[tech/cursor-proxy-fix]] — как починить доступ к Claude Sonnet в Cursor через прокси
- [[tech/cursor-rules-1c]] — полный набор правил и агентов для 1С в Cursor IDE
- [[tech/duc]] — визуализация дискового пространства (sunburst), фикс CGI redirect
- [[tech/heisenberg-team-gpt]] — production-ready мультиагентный шаблон для OpenClaw
- [[tech/jawl]] — Just Another Workflow Library, автономный агент (Jinx)
- [[tech/jawl-architecture]] — L0-L3 архитектура JAWL
- [[tech/jawl-config]] — Конфигурация: models.json, settings.yaml, .env
- [[tech/jawl-context]] — Context Builder: сборка промпта
- [[tech/jawl-dashboard]] — Dashboard: Flask мониторинг
- [[tech/jawl-events]] — EventBus: 22 события Pub/Sub
- [[tech/jawl-heartbeat]] — Heartbeat: driving system + periodic tick
- [[tech/jawl-howto-add-event]] — HOWTO: добавить событие EventBus
- [[tech/jawl-howto-add-interface]] — HOWTO: добавить L2 интерфейс
- [[tech/jawl-howto-add-provider]] — HOWTO: добавить LLM провайдера
- [[tech/jawl-howto-add-skill]] — HOWTO: добавить навык
- [[tech/jawl-react-loop]] — ReAct Loop: reasoning → action → observation
- [[tech/jawl-skills-registry]] — Реестр всех навыков по интерфейсам
- [[tech/landing]] — Лендинг rem2222.top с карточками сервисов
- [[tech/markitdown]] — Microsoft конвертер документов в Markdown
- [[tech/metadata-1c]] — генератор DevOps-отчётов по конфигурации 1С из XML
- [[tech/mcp-inspector]] — MCP Inspector, отладка MCP серверов
- [[tech/multica]] — Open-source managed agents platform
- [[tech/naiveproxy]] — лучший способ обхода DPI в 2026
- [[tech/obsidian-livesync]] — Self-hosted синхронизация Obsidian через CouchDB
- [[tech/obsidian-plugins]] — Рекомендованные плагины Obsidian (Dataview, Templater, MCP)
- [[tech/openai-routing]] — настройка нескольких OpenAI подписок через OmniRoute
- [[tech/openspec]] — легковесный SDD-фреймворк от Fission-AI
- [[tech/openspec-usage]] — детальное руководство по использованию OpenSpec
- [[tech/playsvideo]] — Chrome-расширение для локального воспроизведения видео
- [[tech/pre-mortem]] — Pre-Mortem анализ провала по Gary Klein
- [[tech/sdd-deep-guide]] — полное погружение в SDD для опытного программиста
- [[tech/sdd-deep-guide-ru]] — русская версия глубокого погружения в SDD
- [[tech/sdd-instruments]] — сравнение SDD-инструментов: Kiro, Spec-kit, Tessl, OpenSpec
- [[tech/smoon-docker]] — Остановка SMOON, очистка Docker, команды и структура
- [[tech/specsmaxxing]] — Spec-Driven Development с ACID tracking (Acai.sh)
- [[tech/vibe-coding-workflow]] — 5-phase structured workflow для AI-assisted development
- [[tech/skillopt]] — Microsoft Research: оптимизация skill-документов через ReflACT тренировочный цикл
- [[tech/webwright]] — Microsoft Research: веб-агенты через code-as-action (Python + Playwright)
- [[tech/cc-websearch]] — поисковый плагин для Claude Code (multi-engine: Google, Bing, SerpAPI, Tavily)
- [[tech/context7]] — MCP-сервер документации библиотек для AI-агентов
- [[tech/z-ai]] — AI-поисковик с MCP для Claude Code
- [[tech/serena-mcp]] — LSP MCP-сервер — IDE-интеллект для Claude Code
- [[tech/caveman]] — skill для Claude Code, сокращает многословие модели на ~75%
- [[tech/sequential-thinking]] — Sequential Thinking skill для Claude Code
- [[tech/go-skills-claude-code]] — набор Go-плагинов для Claude Code (modern-go-guidelines, cc-skills-golang, go-best-practices)
- [[tech/gopilot]] — Go AI coding agent для Claude Code
- [[tech/claude-plugin-dev-tools]] — три официальных инструмента Anthropic для разработки плагинов (plugin-dev, skill-creator, mcp-server-dev)
- [[tech/gsd]] — GSD (Get Shit Done) SDD-фреймворк
- [[tech/bmad-method]] — BMAD-METHOD SDD-фреймворк (Architecture First)
- [[tech/agent-skills-marketplace]] — skillsmp.com — агрегатор skills для Claude Code
- [[tech/sourcecraft]] — AI-помощник для понимания кода (sourcecraft.dev)
- [[tech/deepseek-error400-fix]] — фикс Error 400 для DeepSeek V4 в Claude Code
- [[tech/revealjs]] — HTML Presentation Framework (презентации из Markdown, 71.5k ⭐)
- [[tech/ozon-seller-api]] — Ozon Seller API: MCP, SDK, библиотеки для Python/Go/PHP/TS/C#
- [[tech/ozon-purchase-history]] — Ozon история покупок: Chrome-расширение и Python-парсер для экспорта заказов
## 1С
- [[tech/1c-mcp]] — настройка и использование MCP для 1С
- [[tech/1c-mcp]] — MCP vs Built-in Tools, анализ токенов

## Инструменты
- [[tools/Win11Debloat]] — скрипт для отключения телеметрии и мусора в Windows 11
- [[tools/beads]] — Git-backed issue tracker для AI агентов (steveyegge/beads)
- [[tools/dashboards-comparison]] — сравнение Dashboard-ов для OpenClaw
- [[tools/linear-cli]] — CLI-утилита для работы с Linear
- [[tools/openclawfice]] — AI-агенты как в Sims (openclawfice.com)
- [[tools/v8std-mcp]] — стандарты разработки 1С для ИИ-помощников (v8std.ru/mcp)
- [[tools/go-enumsafety]] — Go-линтер для безопасной работы с enum (sum types)

## Память AI-агентов (Memory)
- [[tech/hermes-memory-setup-vps]] — **Актуальная настройка** памяти Hermes на VPS (agentmemory + GBrain autopilot)
- [[tech/agent-memory-research-2026]] — Исследование решений для LTM агентов (2026)
- [[tech/gbrain-lossless-agent-memory]] — GBrain + Lossless для OpenClaw и Hermes
- [[tech/MemPalace-Hermes-Integration]] — MemPalace × Hermes через gateway hook
- [[tech/agentmemory-vs-current]] — agentmemory vs текущий стек памяти
- [[tech/tencentdb-agent-memory]] — TencentDB Agent Memory
- [[tools/find-skills]] — мета-скилл для поиска agent-скиллов через CLI (npx skills, skills.sh)

## Статьи
- [[articles/adam-multiagent]] — мультиагентная система Adam
- [[articles/anthropic-claude-code]] — использование Claude Code от Anthropic
- [[articles/orchestrator-year]] — оркестрация AI-агентов, год работы

## События
- [[events/1cvibeconf-2026]] — 2-я практическая конференция по вайбкодингу в 1С (22-23 мая 2026)
- [[events/gpt5-free-announcement]] — GPT-5 стал полностью бесплатным для всех (27 мая 2026, Greg Brockman)

## Видео
- [[videos/claude-opensource-llm-openclaw-runpod]] — Claude без подписки: Opensource LLM + OpenClaw на RunPod
- [[videos/moonin-papa-crypto-pumps-scanner]] — Moonin Papa: бесплатный крипто-сканер для поиска монет после пампа

## Разное
- [[links-from-sessions]] — собранные ссылки из чатов, не добавленные в wiki
- [[misc/calendar-events]] — календарь событий 2026

## SDD-инструменты (детали)
- [[tech/kiro]] — Kiro SDD-инструмент (kiro.dev)
- [[tech/spec-kit]] — Spec-kit от GitHub
- [[tech/tessl]] — Tessl Framework (docs.tessl.io)

## Obsidian & экосистема
- [[tech/obsidian]] — приложение для заметок на основе markdown
- [[tech/obsidian-web-clipper]] — браузерное расширение для конвертации статей
- [[tech/qmd]] — локальная поисковая система для markdown
- [[tech/dataview]] — плагин для запросов к метаданным Obsidian
- [[tech/marp]] — презентации на основе markdown
- [[tech/defuddle]] — инструмент для извлечения контента из веб-страниц

## Прокси и инфраструктура
- [[tech/openclaw-billing-proxy]] — OpenClaw Billing Proxy (автор: zacdcook)
- [[tech/proxy-acpx-x]] — прокси-инструмент (автор: clonn)

## Книги
- [[books/ne-otkladyvay-na-zavtra]] — «Не откладывай на завтра» — Тимоти Пичил

## Generated
<!-- openclaw:wiki:index:start -->
- Render mode: `obsidian`
- Total pages: 10
- Claims: 0
- Sources: 0
- Entities: 0
- Concepts: 1
- Syntheses: 0
- Reports: 9

### Sources
- No sources yet.

### Entities
- No entities yet.

### Concepts
- [[concepts/tradingagents|TradingAgents]]

### Syntheses
- No syntheses yet.

### Reports
- [[reports/claim-health|Claim Health]]
- [[reports/contradictions|Contradictions]]
- [[reports/low-confidence|Low Confidence]]
- [[reports/open-questions|Open Questions]]
- [[reports/person-agent-directory|Person Agent Directory]]
- [[reports/privacy-review|Privacy Review]]
- [[reports/provenance-coverage|Provenance Coverage]]
- [[reports/relationship-graph|Relationship Graph]]
- [[reports/stale-pages|Stale Pages]]
<!-- openclaw:wiki:index:end -->
