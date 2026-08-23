# Index — Каталог вики

_Обновлено: 2026-08-20_

## Projects
- [[projects/cloud-memory-external-agents]] — план облачной памяти для внешних агентов (MCP HTTP endpoints AgentMemory+GBrain), решение Rem: не разворачивать пока
- [[projects/veritas-kanban]] — Kanban-доска для AI-агентов (Git worktree, Markdown storage)
- [[projects/Оркестратор_v3_Руководство]] — руководство по Оркестратору v3, ИИ-ассистенту для распределения задач между субагентами

## GameDev
- [[gamedev/ccgs-skills-research]] — анализ Claude Code Game Studios (49 AI-агентов, 73 скилла) для геймдева
- [[tech/mengto-skills-gamedev]] — MengTo/Skills: портабельные agent skills для Three.js геймдева

## Концепции
- [[concepts/llm-wiki]] — паттерн персональных баз знаний с помощью LLM
- [[concepts/rag]] — Retrieval-Augmented Generation, альтернативный подход
- [[concepts/memex]] — проект Вэнивара Буша 1945, ассоциативное хранилище знаний
- [[concepts/sdd]] — Spec-Driven Development, подход к разработке через спецификации
- [[concepts/memory-retrieve-middleware]] — идея middleware-слоя авто-retrieve перед запросом к LLM (роутер памяти: память+вики+сессии)
- [[concepts/mcp]] — Model Context Protocol, открытый протокол для AI-интеграций
- [[concepts/doxygen]] — генератор документации из исходного кода (C++, Java, Python...)
- [[concepts/tradingagents]] — Multi-agent LLM фреймворк для алгоритмической торговли (UCLA + MIT)
- [[concepts/open-knowledge-format]] — Open Knowledge Format (OKF), открытый формат знаний от Google Cloud Platform
- [[concepts/graph-engineering]] — от последовательных агентов к графу работ
- [[concepts/hermes-knowledge-base]] — Hermes Agent как персональная БД
- [[concepts/self-improving-agent-theory]] — теория Self-Improving Agent (Schmidhuber 2026)
- [[concepts/llm-tier-strategy]] — стратегия выбора LLM для разных этапов разработки
- [[concepts/github-actions]] — GitHub Actions — CI/CD платформа от GitHub
- [[concepts/javadoc]] — генератор документации из Java-кода в HTML
- [[concepts/sphinx]] — генератор документации на Python, reStructuredText/Markdown
- [[concepts/waku-agent]] — Waku Agent: локальный AI-ассистент (Agent Harness на практике, ~95 строк Python)

## Сервисы
- [[ops/services/server-architecture]] — полная карта серверной инфраструктуры VPS
- [[ops/services/nginx]] — обратный прокси, HTTPS, Authelia SSO
- [[ops/services/docker]] — контейнеризация сервисов
- [[ops/services/postgresql]] — реляционные БД
- [[ops/services/authelia]] — SSO аутентификация, 2FA
- [[ops/services/agentmemory]] — долговременная память агента
- [[ops/services/agentmemory-exporter]] — Prometheus метрики AgentMemory
- [[ops/services/beszel]] — мониторинг CPU/RAM/диска
- [[ops/services/cgc]] — MCP-сервер для кодовой базы Multica
- [[ops/services/cockpit]] — веб-интерфейс управления сервером
- [[ops/services/codegraph]] — MCP-сервер для анализа кода
- [[ops/services/dex]] — веб-дашборд и REST API для управления агентом Dex
- [[ops/services/duc]] — визуализация использования диска
- [[ops/services/freedeepseekapi]] — DeepSeek Web Chat proxy
- [[ops/services/freellmapi]] — Unified LLM API router
- [[ops/services/gbrain]] — Graph-based knowledge brain
- [[ops/services/gemini-web2api]] — Gemini reverse proxy
- [[ops/services/hermes-agent]] — AI-агент для автоматизации, gateway сообщений
- [[ops/services/hermes-dashboard]] — веб-дашборд Hermes Agent
- [[ops/services/jawl]] — автономный Python-агент (Jinx)
- [[ops/services/mercury]] — дашборд Mercury Agent
- [[ops/services/monitor-ui]] — панель управления ntfy
- [[ops/services/multi-exporter]] — Prometheus метрики для нескольких сервисов
- [[ops/services/multica]] — платформа управления AI-агентами
- [[ops/services/multica-inbox-bridge]] — мост Multica → Telegram
- [[ops/services/ntfy]] — push-уведомления
- [[ops/services/skills-dashboard]] — веб-дашборд для approval навыков Hermes
- [[ops/services/sshd]] — SSH-доступ к серверу
- [[ops/services/tailscale]] — Mesh VPN, exit node
- [[tech/netbird]] — NetBird: mesh VPN / Zero-Trust на WireGuard, конкурент Tailscale
- [[ops/services/tor]] — анонимный SOCKS5 прокси
- [[ops/services/ufw-fail2ban]] — фаервол + защита от брутфорса
- [[ops/services/unattended-upgrades]] — автообновления безопасности
- [[ops/services/lightpanda]] — Lightpanda headless-браузер (Zig, CDP, порт 9222)

## SDD-Orchestrator v2 (2026-05-04)
- [[tech/sdd-openspec-orchestrator-integration]] — Orchestrator Integration (что хотели для Оркестратора: QA Gate, multi-layer SDD, hybrid context)
- [[tech/sdd-openspec-sdd-developer]] — SDD Developer Agent (детали SDD Developer: RFC 2119, workflow, self-validation, QA Gate)
- [[tech/sdd-orchestrator-v2]] — Overview (старая версия, но содержит acceptance criteria)
- [[tech/sdd-openspec-precommit]] — Pre-commit hook
- [[tech/sdd-openspec-real-project]] — Real project integration

## Технологии
- [[tech/qwen-mm-plugins]] — Qwen-MM-Plugins: native-мультимодальные плагины (skill + MCP) для агентных обвязок: изображения/видео/PDF, OCR, grounding, ASR
- [[tech/dpi-zapret-netfix]] — DPI, Zapret, TgWsProxy и GUI-обёртка NetFix
- [[tech/mimo-code]] — AI coding agent от Xiaomi, форк OpenCode с persistent memory
- [[tech/openprose-reactor]] — декларативный язык для AI-сессий (OpenProse) и runtime (Reactor)
- [[tech/rag-projects-summary]] — обзор RAG-проектов из Hands-On AI Engineering
- [[tech/pixelrag]] — PixelRAG: визуальный RAG-фреймворк, рендерящий документы в скриншоты вместо HTML
- [[tech/mcp-projects-summary]] — обзор MCP-проектов из Hands-On AI Engineering
- [[tech/1c-mcp]] — MCP серверы для экосистемы 1С (vibecoding1c.ru)
- [[tech/mempalace-viz]] — визуализация графа знаний для MemPalace (D3.js, MCP, Cloudflare)
- [[tech/agents-best-practices]] — best practices для проектирования агентных систем (provider-agnostic)
- [[tech/agentation]] — Enterprise-платформа для оркестрации AI-агентов (no-code, HITL, on-premise)
- [[tech/openworker]] — OpenWorker: open-source AI-коллега на десктопе от Andrew Ng (aisuite, BYOK, MCP)
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
- [[tech/zvec]] — Zvec: встраиваемая векторная БД от Alibaba (SQLite-подход для векторного поиска)
- [[tools/wiki-search-current-state]] — как сейчас ищем в вики (zvec-wiki vs GBrain, MCP для zvec)
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
- [[tech/hermes-external-integrations]] — каталоги готовых интеграций для AI-агентов (aci.dev, composio, arcade.dev)
- [[tech/mcpservers]] — каталог MCP-серверов (mcpservers.org)
- [[tech/fastmcp]] — FastMCP: MCP фреймворк от PrefectHQ (25.7k ⭐, ~70% всех MCP серверов)
- [[tech/opencode]] — установка и настройка OpenCode на VPS (anomalyco/opencode)
- [[tech/opencode-gigachat-plugin]] — плагин GigaChat для OpenCode (Сбер, OAuth, TLS РФ)
- [[tech/opencode-notifier-ntfy]] — плагин OpenCode, шлёт ntfy-уведомления о событиях (permission/complete/error/question)
- [[tech/ponytail]] — Ponytail: скилл «ленивый сеньор» для AI-агентов (80-94% меньше кода)
- [[tech/free-claude-code]] — прокси для бесплатного Claude Code через альтернативные LLM-провайдеры
- [[tech/poe-api-models]] — модели и цены Poe API
- [[tech/poe-chutes-comparison]] — сравнение Poe API и Chutes AI
- [[tech/optimizing-llm-api-calls-for-coding]] — оптимизация вызовов LLM API для кодинг-агентов
- [[tech/llm-as-a-verifier]] — LLM-as-a-Verifier: верификация ответов LLM через logprobs (Best-of-N, self-verification). Усилитель для сложных задач, пока НЕ применимо к текущему стеку (нет top-k logprobs)

- [[tech/hermes-max-plugin]] — MAX Messenger (VK) plugin for Hermes Agent
- [[tech/chatgpt-codex-proxy-experiment]] — эксперимент ChatGPT Teacher → Hermes через Codex proxy
- [[tech/sim-agent-workflow-builder]]
- [[tech/free-llm-api-resources]]
- [[tech/paperclip]] — платформа для оркестрации команды AI-агентов (Org Chart, heartbeats)
- [[tech/ods-ai-server]] — локальный AI-сервер «всё-в-одном» (LLM, Open WebUI, RAG)
- [[tech/photosorter-state-machine]] — полный автомат состояний Photo Sorter
- [[tech/anythingllm]] — all-in-one AI app для RAG, чата с документами и агентов
- [[tech/anythingllm-rag]] — AnythingLLM RAG: настройка и сравнение моделей
- [[tech/bmad-multica-integration]] — интеграция BMAD с Multica
- [[tech/dify-agent-platform]] — open-source платформа для AI-приложений
- [[tech/freellmapi]] — Unified LLM API router (бесплатные AI-провайдеры)
- [[tech/freenimapi]] — локальный прокси-мост NVIDIA NIM → coding-агенты
- [[tech/gsd-multica-integration]] — интеграция GSD с Multica
- [[tech/hermes-mcp-setup]] — настройка MCP в Hermes Agent
- [[tech/openmanus]] — open-source универсальный AI-агент
- [[tech/sdd-openspec-orchestrator]] — интеграция OpenSpec в Оркестратор
- [[tech/supermemory-agent-memory]] — Supermemory: LTM для агентов
- [[tech/9router-vs-openrouter]] — сравнение 9Router и OpenRouter
- [[tech/GitNexus]] — веб-интерфейс для хостинга Git-репозиториев
- [[tech/forgejo]] — self-hosted Git платформа (форк Gitea)
- [[tech/gitea]] — лёгкая self-hosted Git платформа
- [[tech/graphviz]] — визуализация графов через Graphviz
- [[tech/hysteria-clients]] — клиенты Hysteria2 для обхода DPI
- [[tech/hysteria-realm]] — Hysteria2 конфигурация Realm
- [[tech/jawl-multiagent]] — мультиагентная архитектура JAWL
- [[tech/mcp-1c-setup]] — настройка MCP для 1С
- [[tech/minimax]] — Minimax AI модели и API
- [[tech/nerve-recovery-timeline]] — таймлайн восстановления нерва (health)
- [[tech/no-code-agent-autoagent]] — no-code платформа для AI-агентов
- [[tech/pxpipe-context-compression]] — контекстная компрессия для LLM
- [[tech/subquadratic]] — Subquadratic: архитектуры внимания быстрее O(n²)
- [[tech/superpowers]] — Superpowers: платформа для AI-агентов
- [[tech/ui-ux-pro-max-analysis]] — UI/UX анализ Pro Max
- [[tech/lightpanda-browser]] — Lightpanda: headless-браузер на Zig для AI-агентов (в 9× быстрее headless Chrome)
- [[tech/wello-ai-api]] — Wello: единый API для Claude, GPT, Gemini (до 90% дешевле)
- [[tech/langchain-open-agent-platform]] — LangChain Open Agent Platform: UI поверх LangGraph
## Hermes Agent
- [[tech/hermes-soulmd]] — SOUL.md: как 50 строк задают характер агента
- [[tech/hermes-agent-masterclass]] — перевод мастеркласса по архитектуре Hermes Agent, памяти и скиллам

- [[secrets/hermes-telegram-bot-token]] — Telegram Bot Token для Hermes Gateway
## 1С
- [[tech/1c-mcp]] — настройка и использование MCP для 1С
- [[tech/1c-mcp]] — MCP vs Built-in Tools, анализ токенов
- [[tech/onebase]] — open-source бизнес-платформа с 1С-подобным DSL (ERP/low-code)
- [[purchased/mcp-1c/help-search]] — MCP: поиск по справке 1С
- [[purchased/mcp-1c/ssl-search]] — MCP: поиск по БСП
- [[purchased/mcp-1c/graph-metadata-search]] — MCP: граф метаданных 1С
- [[purchased/mcp-1c/syntax-check]] — MCP: проверка синтаксиса BSL
- [[purchased/mcp-1c/1c-code-checker]] — MCP: проверка через 1С:Напарник
- [[purchased/mcp-1c/templates-search]] — MCP: шаблоны кода 1С
- [[purchased/mcp-1c/code-metadata-search]] — MCP: поиск по коду и метаданным

## Hardware
- [[hardware/xe2690-workstation]] — домашняя рабочая станция XE2690
## Tasks
- [[tasks/mul-239-codegraph-in-gsd]] — MUL-239: добавить CodeGraph в GSD squad
- [[tasks/hindsight-vs-memos-decision]] — решение MUL-874: Hindsight vs MemOS vs EverOS (стабильность, многослойность, хуки)
- [[ops/workflow/new-project-with-codegraph]] — рабочий процесс: CodeGraph для новых проектов
## Инструменты
- [[tools/Win11Debloat]] — скрипт для отключения телеметрии и мусора в Windows 11
- [[tech/make-interfaces-feel-better]] — UI-рекомендации (Jakub Krehel, 30K+ установок)
- [[tools/beads]] — Git-backed issue tracker для AI агентов (steveyegge/beads)
- [[tools/dashboards-comparison]] — сравнение Dashboard-ов для OpenClaw
- [[tools/linear-cli]] — CLI-утилита для работы с Linear
- [[tools/openclawfice]] — AI-агенты как в Sims (openclawfice.com)
- [[tools/v8std-mcp]] — стандарты разработки 1С для ИИ-помощников (v8std.ru/mcp)
- [[tools/go-enumsafety]] — Go-линтер для безопасной работы с enum (sum types)
- [[tools/diagram-design]] — 27 редакционных диаграмм (HTML/SVG) для AI-агентов (21k⭐)
- [[tools/activitywatch]] — open-source трекер времени, приватный self-hosted (18.6k⭐)
- [[tools/hermes-memory-comparison]] — сравнение систем памяти для Hermes по 6 болям + HTML-версия (rem2222.top/hermes-memory.html)
- [[tools/yt-dlp]] — CLI-утилита для скачивания видео/аудио (YouTube и др.)
- [[tools/agent-reach]] — веб-доступ для AI-агентов («глаза в интернет»)
- [[tools/mcporter]] — CLI-клиент для управления MCP-серверами
- [[tools/chatcut]] — нарезка и обработка чатов/диалогов
- [[tools/ai-video-upscale]] — AI-модели для повышения разрешения видео
- [[tools/officecli]] — CLI для создания Office-документов
- [[tools/rtk]] — RTK: Rust CLI-прокси для сжатия вывода команд перед LLM (60–90% токенов)
- [[tools/openminis]] — OpenMinis: мобильный AI-агент с Linux shell
- [[tech/devin-ai-agent]] — AI Software Engineer от Cognition Labs (Windsurf → Devin). Включает GLM-5.2 в Pro

## LLM
- [[llm/local-gemma-4-12b-setup]] — локальный запуск Gemma 4 12B coder на XE2690
- [[tech/codex-cli-inference-optimization]] — Лайфхак: Codex CLI сам подбирает оптимум инференса под железо (Qwen 3.5-9B, 54 tok/s)
- [[llm/vibethinker]] — VibeThinker 1.5B/3B: SOTA reasoning от WeiboAI. Обходит DeepSeek R1 на AIME, 1.8 GB в Q4
- [[chinese-ai-pricing-research]] — Исследование цен на подписки китайских AI-провайдеров (Qwen, GLM, Kimi, MiniMax)
## Память AI-агентов (Memory)
- [[tech/hermes-memory-setup-vps]] — **Актуальная настройка** памяти Hermes на VPS (agentmemory + GBrain autopilot)
- [[tech/agent-memory-research-2026]] — Исследование решений для LTM агентов (2026)
- [[tech/gbrain-lossless-agent-memory]] — GBrain + Lossless для OpenClaw и Hermes
- [[tech/MemPalace-Hermes-Integration]] — MemPalace × Hermes через gateway hook
- [[tech/agentmemory-vs-current]] — agentmemory vs текущий стек памяти
- [[tech/deepseek-harness]] — DeepSeek Harness: агентный harness «всё — плагин» (Cordis)
- [[tech/lfm25-vl-3b]] — LFM2.5-VL-3B: лёгкая VLM для GUI-агентов (Liquid AI)
- [[tech/semantica]] — Semantica: граф-нативная память для агентов (тренд Graph-RAG)
- [[tech/buzz]] — Buzz: Nostr-workspace от Block (Дорси), люди + агенты в одних каналах
- [[tech/tencentdb-agent-memory]] — TencentDB Agent Memory
- [[tools/find-skills]] — мета-скилл для поиска agent-скиллов через CLI (npx skills, skills.sh)
- [[tech/Mercury-Agent-Skills]] — библиотека скиллов Mercury Agent, совместимая с Hermes

## Статьи
- [[articles/1c-autonomous-ai-development]] — паттерн автономной разработки 1С с ИИ-агентами (два проекта, координатор + разработчик)
- [[articles/hands-on-ai-engineering]] — обзор коллекции AI-проектов (RAG, MCP, агенты)
- [[articles/adam-multiagent]] — мультиагентная система Adam
- [[articles/anthropic-claude-code]] — использование Claude Code от Anthropic
- [[articles/orchestrator-year]] — оркестрация AI-агентов, год работы

## События
- [[events/1cvibeconf-2026]] — 2-я практическая конференция по вайбкодингу в 1С (22-23 мая 2026)
- [[events/gpt5-free-announcement]] — GPT-5 стал полностью бесплатным для всех (27 мая 2026, Greg Brockman)

## Видео
- [[videos/claude-opensource-llm-openclaw-runpod]] — Claude без подписки: Opensource LLM + OpenClaw на RunPod
- [[videos/moonin-papa-crypto-pumps-scanner]] — Moonin Papa: бесплатный крипто-сканер для поиска монет после пампа
- [[videos/trading/claude-tradingview-connection]] — Claude + TradingView: подключение и настройка

## Разное
- [[links-from-sessions]] — собранные ссылки из чатов, не добавленные в wiki
- [[misc/calendar-events]] — календарь событий 2026
- [[hosting/rdp-monster]] — дешёвый RDP/VDS хостинг в криптовалюте
- [[archive/habr-vpn/habr-1036100-proxy-vpn-part1]] — оффлайн-копия: извращения из мира прокси и VPN (часть 1)
- [[archive/habr-vpn/habr-1065064-proxy-vpn-part2]] — оффлайн-копия: извращения из мира прокси и VPN (часть 2)
- [[archive/habr-planning-4gen/index]] — оффлайн-копия: планирование 4-го поколения (Кови + GTD), шаблон промпта для агента

- [[flag_rebuild]] — флаг пересборки для инфраструктурных пайплайнов

## Промпты
- [[prompts/human-like-text]] — промт для LLM: текст как человек, прохождение AI-детекции

## SDD-инструменты (детали)
- [[tech/kiro]] — Kiro SDD-инструмент (kiro.dev)
- [[tech/spec-kit]] — Spec-kit от GitHub
- [[tech/tessl]] — Tessl Framework (docs.tessl.io)

## Obsidian & экосистема
- [[tech/obsidian-plugins]] — приложение для заметок на основе markdown
- [[tech/obsidian-plugins]] — плагин для запросов к метаданным Obsidian
- [[tech/marp]] — презентации на основе markdown
- [[tech/defuddle]] — инструмент для извлечения контента из веб-страниц
- [[wiki/tech/cli-printing-press]] — генератор CLI/MCP-серверов для любых API
- [[wiki/tech/lightmem]] — лёгкий фреймворк управления памятью для LLM

## Прокси и инфраструктура
- [[tech/youtube-relay-setup]] — YouTube через собственный релей внутри страны (nginx+xray+sing-box+zapret)
- [[tech/ru-marketplace-mcp]] — MCP-серверы для 9 российских маркетплейсов + Taobao (цены/отзывы, сравнение)
- [[tech/openclaw-billing-proxy]] — OpenClaw Billing Proxy (автор: zacdcook)
- [[tech/proxy-acpx-x]] — прокси-инструмент (автор: clonn)
- [[free-api-deepseek-qwen]] — обзор Free API прокси (DeepSeek / Qwen)
- [[qwen-free-api]] — развёртывание FreeQwenApi
- [[deepseek-free-api]] — развёртывание FreeDeepseekAPI

## Книги
- [[books/ne-otkladyvay-na-zavtra]] — «Не откладывай на завтра» — Тимоти Пичил
