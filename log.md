# Log — Журнал вики

_Append-only. Формат: `## [дата] type | описание`_

---

## [2026-06-13] ingest | Open Knowledge Format (OKF)

- Создана страница [[concepts/open-knowledge-format]] — открытый формат знаний от GCP для людей и AI-агентов
- Добавлена секция «Идея на апгрейд wiki» — анализ того, как OKF соотносится с текущей wiki
- Источник: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md

## [2026-04-05] setup | Создание вики

- Создана структура папок (raw, assets, wiki/{people,tech,projects,concepts,books,misc})
- Создан SCHEMA.md (правила для LLM)
- Создан index.md (каталог)
- Создан этот log.md
- Источник идеи: https://gist.github.com/iAlexeyRu/84a365fe34c3f0a964888a2c09a4541b
- Инструкция добавлена в AGENTS.md

## [2026-04-05] ingest | LLM Wiki (gist)

- Создана страница [[concepts/llm-wiki]] (wiki/concepts/llm-wiki.md)
- Создана страница [[Obsidian]] (wiki/tech/obsidian.md)
- Создана страница [[RAG]] (wiki/concepts/rag.md)
- Обновлён index.md
- 3 страницы, 3 перекрёстные ссылки

## [2026-04-05] ingest | LLM Wiki (полный импорт)

- Сохранён raw-источник: raw/llm-wiki-gist.md
- Обновлена [[concepts/llm-wiki]] (полное содержимое, все связи)
- Создана [[concepts/memex]] (wiki/concepts/memex.md)
- Создан [[qmd]] (wiki/tech/qmd.md)
- Создан [[tech/obsidian-web-clipper]] (wiki/tech/obsidian-web-clipper.md)
- Создан [[tech/marp]] (wiki/tech/marp.md)
- Создан [[Dataview]] (wiki/tech/dataview.md)
- Обновлён index.md
- Итого: 9 страниц в wiki, все связаны с [[concepts/llm-wiki]]

## [2026-04-08] ingest | NaiveProxy Guide

- Источник: gist swrneko + GitHub klzgrad/naiveproxy
- Создан [[tech/naiveproxy]] (wiki/tech/naiveproxy.md) — полная инструкция по установке
- Сохранён raw-источник: raw/naiveproxy-guide-swrneko.md
- Обновлён index.md и log.md
- Добавлены клиенты: v2rayN, NekoRay, NekoBox
- Добавлены хостинг-провайдеры: RuVDS, 62yun, Zomro, Reg.ru

## [2026-04-08] ingest | Cursor Proxy Fix

- Источник: forwarded message от Дарт Вейдер
- Создан [[tech/cursor-proxy-fix]] (wiki/tech/cursor-proxy-fix.md)
- Сохранён raw-источник: raw/cursor-proxy-fix.md
- Обновлён index.md и log.md
- Добавлены: OneXRay, Hiddify, VLESS, HTTP/2 fix для Cursor

## [2026-04-09] ingest | Heisenberg Team

- Источник: https://github.com/ai-operacionka/heisenberg-team-GPT
- Создан [[tech/heisenberg-team-gpt]] (wiki/tech/heisenberg-team-gpt.md)
- 8 агентов, 34 скилла, Board-First протокол
- Обновлён index.md и log.md
- Статус: на рассмотрении

## [2026-04-09] ingest | MarkItDown

- Источник: forwarded от Derp Learning (https://github.com/microsoft/markitdown)
- Создан [[tech/markitdown]] (wiki/tech/markitdown.md)
- Конвертер: PDF, Word, Excel, PowerPoint, Images (OCR), Audio, YouTube, HTML
- Установлен: pip install 'markitdown[all]'
- Обновлён index.md и log.md

## [2026-04-09] ingest | OpenAI Routing

- Источник: OpenClaw Lab (forwarded)
- Создан [[tech/openai-routing]] (wiki/tech/openai-routing.md)
- OmniRoute для балансировки между несколькими OpenAI подписками
- Автопереключение при исчерпании лимитов
- Обновлён index.md и log.md

## 2026-04-10

### CodexBar-Win-Enhance
- Создан проект для добавления провайдеров в CodexBar-Win
- Цель: z.ai (API token), MiniMax (cookies), OpenCode (cookies)
- Создан шаблон проекта в projects/CodexBar-Win-Enhance/
- Созданa страница wiki: [[tech/codexbar-win-cookie-decryption]] — документация по технологии расшифровки Chromium cookies

### CodexBar research
- Найден CodexBar-Win — Windows порт CodexBar
- Найдены 16+ провайдеров в macOS версии включая OpenCode и MiniMax
- Субагент исследовал архитектуру провайдеров
- OpenRouter поддерживается! Через него можно проксировать на Minimax
- [[JAWL]] — добавлена страница tech/jawl.md (2026-04-25)
- [[links-from-sessions]] — собран все ссылки из 33 session файлов в один файл (2026-04-25)
- [[tech/mcp-inspector]] — MCP Inspector страница (2026-04-25)
- [[tools/linear-cli]] — Linear CLI страница (2026-04-25)
- [[articles/adam-multiagent]] — Adam multi-agent тред (2026-04-25)
- [[articles/anthropic-claude-code]] — Anthropic Claude Code тред (2026-04-25)
- [[articles/orchestrator-year]] — Год оркестраторов статья (2026-04-25)

## [2026-05-05] ingest | TradingAgents
Создана страница [[concepts/tradingagents]] — мультиагентный LLM фреймворк для торговли. Источник: https://tradingagents-ai.github.io/. Создан raw/tradingagents.md. 5 ролей: Analysts → Researchers (Bull/Bear debate) → Trader → Risk Manager → Fund Manager. Ключевое: ReAct prompting, structured reports + natural language debate, quick/deep thinking models. Результаты: AAPL +26.6% (B&H -5.2%), Sharpe 8.21, MaxDD 0.91%.

## [2026-05-30] ingest | Moonin Papa — крипто-сканер
Создана страница [[videos/moonin-papa-crypto-pumps-scanner]] — обзор видео Aaron Dishner (Moonin Papa) про бесплатный крипто-сканер bettertrader.io для поиска монет после пампа через spread и near 24h low фильтры. Расшифровка получена через Tor.

## [2026-05-27] ingest | MemPalaceViz
Создана страница [[tech/mempalace-viz]] — визуализация графа знаний для MemPalace (D3.js force-directed graph, MCP интеграция, Crystal Palace тема). Автор: Joe Guarino / G5 Labs. Репозиторий: https://github.com/JoeDoesJits/mempalace-viz. Версия v1.5.0, 25 коммитов, MIT лицензия. Zero-build single-file SPA. Cloudflare zero-trust hosting.

## [2026-05-27] ingest | 8 источников (батч)
Созданы страницы:
- [[tech/assemblyai]] — AssemblyAI, API-first Speech-to-Text и аудиоинтеллект
- [[tech/skillopt]] — Microsoft Research SkillOpt: оптимизация агентных скиллов через ReflACT
- [[tech/webwright]] — Microsoft Research Webwright: веб-агенты через code-as-action
- [[events/gpt5-free-announcement]] — GPT-5 стал полностью бесплатным (Greg Brockman, 27 мая 2026)
- [[tech/agents-best-practices]] — provider-agnostic best practices для агентных систем (Denis Shiryaev)
- [[tech/agentation]] — Enterprise-платформа оркестрации AI-агентов
- [[tech/metadata-1c]] — генератор DevOps-отчётов по конфигурации 1С из XML
- [[tools/find-skills]] — мета-скилл для поиска agent-скиллов (Vercel Labs, skills.sh)

## [2026-05-27] ingest | Agent Memory Research
- Создана [[tech/agent-memory-research-2026]] — исследование 40+ решений для долговременной памяти агентов
- Обновлён index.md — добавлена секция "Память AI-агентов (Memory)"
- Итог: выбраны связка agentmemory + GBrain для установки

## 2026-05-27 18:00: ingest | 16 источников (статья на Habr про harness для Claude Code)

Добавлены страницы из статьи «Рабочее место не-вайбкодера: настраиваем harness» (https://habr.com/ru/companies/yadro/articles/1038084/):
- [[tech/cc-websearch]] — поисковый плагин для Claude Code
- [[tech/context7]] — MCP документации библиотек
- [[tech/z-ai]] — AI-поисковик с MCP
- [[tech/serena-mcp]] — LSP через MCP
- [[tech/caveman]] — сокращение многословия модели
- [[tech/sequential-thinking]] — пошаговые рассуждения
- [[tech/go-skills-claude-code]] — Go-плагины (3 шт.)
- [[tech/gopilot]] — Go AI coding agent
- [[tech/claude-plugin-dev-tools]] — plugin-dev, skill-creator, mcp-server-dev
- [[tech/gsd]] — Get Shit Done SDD-фреймворк
- [[tech/bmad-method]] — BMAD SDD-фреймворк
- [[tech/agent-skills-marketplace]] — skillsmp.com
- [[tech/sourcecraft]] — AI-объяснение кода
- [[tech/deepseek-error400-fix]] — фикс DeepSeek V4
- [[tools/go-enumsafety]] — Go enum linter

## 2026-05-28 18:30: ingest | reveal.js

- [[tech/revealjs]] — HTML Presentation Framework (Hakim El Hattab, 71.5k ⭐)

## 2026-06-01 16:00: maintenance | полный аудит вики

Полный аудит и обслуживание вики:
- Созданы недостающие страницы концепций: concepts/sdd, concepts/mcp, concepts/rag, concepts/llm-wiki, concepts/memex, concepts/github-actions, concepts/javadoc, concepts/sphinx
- Созданы tech/kiro и tech/tessl
- Исправлены ~20 битых вики-ссылок (wiki/ → правильный путь)
- Переименован tech/Mercury Agent Skills.md → tech/Mercury-Agent-Skills.md
- Добавлен frontmatter tech/Mercury-Agent-Skills.md
- Исправлены пути в index.md и log.md
- Обновлён SCHEMA.md (удалены template artifacts)
- Все wiki/ префиксы приведены к единому стандарту

## [2026-06-01] ingest | Ozon API инструменты (2 страницы)

- Создана [[tech/ozon-seller-api]] — MCP-серверы, SDK, библиотеки, парсеры для Ozon Seller API
- Создана [[tech/ozon-purchase-history]] — расширение Chrome + Python-парсер для скачивания покупок из ЛК
- Обновлён index.md

## 2026-06-03 maintenance | wiki audit + fixes
- Добавлен frontmatter 35 страницам (tech/)
- Добавлены description 41 странице
- Добавлены tags 7 страницам
- Исправлены множественные H1 на 46 страницах (→ H2)
- Исправлены битые вики-ссылки (30+) — редиректы, пути, созданы страницы-заглушки
- Созданы 9 новых страниц: forgejo, gitea, defuddle, mcp-1c-setup, minimax, openclaw-billing-proxy, superpowers, graphviz, hermes-mcp-setup
## [2026-07-25] maintenance audit | wiki health check fixes

- Merged double frontmatter: tech/freenimapi.md, concepts/self-improving-agent-theory.md
- Added missing related links: 7 purchased/mcp-1c/* pages → [[tech/1c-mcp]]
- Fixed broken YAML description: tech/1c-mcp.md (invalid literal block)
- Added index.md entries for 12 orphan pages (concepts, tech, tools, purchased, hosting, ops)
- Added backlinks from tech/1c-mcp.md to all purchased/mcp-1c pages
- Updated index.md date to 2026-07-25
- Health check: 25 issues → 0
## [2026-07-25] maintenance | wiki health fix
- Удалён дубликат hermes-agent-masterclass.md из корня (оставлен в tech/)
- Добавлены 4 концепции в index.md (llm-tier-strategy, github-actions, javadoc, sphinx)
- Добавлен раздел «Сервисы» с 33 ops/services/* страницами
- Добавлены 15+ tech-страниц в index.md
- Добавлены страницы в Obsidian & экосистема (cli-printing-press, lightmem)
- Добавлено видео (claude-tradingview-connection)
- Обновлена дата index.md
## [2026-08-02] update | tech/tencentdb-agent-memory

- Исправлен URL репозитория: Tencent → TencentCloud
- Обновлена дата/статус (Backlog, MUL-715), добавлена секция Hermes-интеграции (provider memory_tencentdb, Gateway :8420, Docker, Windows-скрипт, безопасность)
- Обновлены ссылки (Discord, related: agent-memory-research-2026, gbrain-lossless-agent-memory, supermemory-agent-memory)
## [2026-08-03] nightly routine | реестр: last_verified обновлён (33 стр.), cockpit +port 3114; новые tools: yt-dlp, agent-reach, mcporter
## [2026-08-05] update | ops/services/warp, ops/services/multi-exporter (MUL-746)
- warp.md: задокументирована причина установки WARP (обрывы "incomplete chunked read" у opencode.ai), решение через WarpProxy :40000, и текущий статус — ALL_PROXY закомментирован, можно удалять
- multi-exporter.md: CACHE_DURATION 30с → 1800с (30 мин) — раньше каждые 30с гонял gbrain doctor (bun-процесс), cgroup ~1.1-1.9G; теперь раз в 30 мин
## [2026-08-06] maintenance | wiki health audit (MUL-752)

- Health check: 19 → 0 issues
- Исправлен frontmatter (description содержал `tags: [...]` вместо описания, отсутствовали tags): tech/ui-ux-pro-max-analysis, tech/agentmemory-vs-current, concepts/doxygen, tools/dashboards-comparison
- Добавлен frontmatter (description/tags/related) оффлайн-копиям Habr: archive/habr-vpn/habr-1036100-proxy-vpn-part1, habr-1065064-proxy-vpn-part2
- 10 orphan-страниц получали ссылки (related + index.md): tech/mengto-skills-gamedev, tech/lightpanda-browser, tech/wello-ai-api, tech/langchain-open-agent-platform, concepts/waku-agent, tools/rtk, tools/openminis, ops/services/lightpanda, 2× archive/habr-vpn
- Связанные пары: lightpanda-browser ↔ ops/services/lightpanda, tech/rtk ↔ tools/rtk, mengto-skills-gamedev ↔ ccgs-skills-research, wello-ai-api ↔ freellmapi, langchain-open-agent-platform ↔ dify-agent-platform, waku-agent/openminis → hermes-knowledge-base

- [2026-08-04] ingest | tech/openworker — OpenWorker от Andrew Ng (aisuite, десктопный AI-коллега, BYOK, MCP, approval-gated)
- [2026-08-10] ingest | tech/qwen-mm-plugins — Qwen-MM-Plugins: мультимодальные плагины (skill+MCP) для агентных обвязок (core: изображения/видео/PDF, OCR, grounding, ASR)
## [2026-08-11] ingest | tech/semantica (граф-тренд для агентов)
## [2026-08-13] ingest | tech/lfm25-vl-3b (VLM Liquid AI для GUI-агентов)
## [2026-08-13] ingest | tech/deepseek-harness (агентный harness DeepSeek, слежка за обновами)
## [2026-08-15] update | tech/deepseek-harness (MUL-832 TREND: вирусный рост +145%)
- Звёзды 38 630 → 94 854 (+145%/сутки), forks 8 743, npm 0.1.0-rc.6
- Причина скачка: хайп-волна после анонса 13.08 (preview v0.1 + MIT + npm, HN 718pts, китайские медиа, «тройной анонс» с V4-Pro и пересмотром цен)
- Статус НЕ изменился: стабильного релиза нет, Docker-гайда нет, README предупреждает о breaking changes
- Решение: не подключать в воркфлоу, следить дальше (критерии активации: stable release / Docker-гайд / готовые dsh-плагины)
## [2026-08-15] ingest | tech/buzz (Nostr-workspace от Block/Дорси, люди + агенты)
- Видео от Rem (43 сек): GitHub block/buzz, «Agents are members, not bots»
- Self-hostable workspace на Nostr: люди и ИИ-агенты в одних комнатах; агент = участник с ключами и аудитом
- Rust 91%, Apache-2.0, 27.5k⭐, Buzz Runtime v0.4.16 (15.08.2026), создан 06.03.2026
- Решение: в вики, не разворачивать (по правилу новых инструментов)
## [2026-08-15] update | ops/services/lightpanda (новый образ + таймер рестарта)
- Причина OOM: старый образ 27.07 без mem-фиксов (ArenaPool/blob/_proto, 30-31.07) + лик #2460 (Frame.removeNode)
- Образ обновлён до nightly.8662 (15.08), лимит 4GiB, CDP ок
- Таймер lightpanda-restart.timer: рестарт каждые 6ч (страховка от лика #2460)
- MUL-831 закрыт (done)
## [2026-08-15] ingest | tech/youtube-relay-setup (инструкция от Rem)
- Схема: телефон → релей в стране (nginx маскировка → xray mux.cool → sing-box маршрутизация)
- Google/YouTube → direct через zapret (локальный кэш Google), остальное → заграничный VLESS
- Ключевое: домены плеера разделять нельзя (ip= в URL, иначе 403); mux ~40% экономии; connbytes 1:100 для слабых серверов
- Замеры: TLS-соединение ~146 мс через туннель; старт 13.5 с → 8.1 с с mux
## [2026-08-15] ingest | tech/ru-marketplace-mcp (12 MCP-серверов для маркетплейсов РФ + Taobao)
- Оценено по прямой ссылке от Rem: качественный проект, 1182 теста, CI 3 ОС, честная ANTI_BOT.md
- С VPS (Франция) анонимно: WB, Яндекс Маркет, Детский мир; Ozon через Chrome; Авито/Taobao/Мегамаркет — только домашний IP
- v1.5.0 — бандл DeepSeek Harness (13 Agent Skills); v1.5.1 (16.08.2026)
- Решение: в вики, не ставить (по правилу новых инструментов)
## [2026-08-18] ingest | tools/diagram-design (27 редакционных диаграмм HTML/SVG для AI)
- Ссылка от Rem: cathrynlavery/diagram-design, 21k⭐, MIT
- 27 типов: block, flow, timeline, matrix, sankey, chord и др.; чистый HTML/SVG, без Mermaid
- Полезная ссылка, не must have (у нас visual-design скилл для кастомных SVG)
## [2026-08-18] ingest | tools/activitywatch (open-source трекер времени)
- Ссылка от Rem: activitywatch.net, 18.6k⭐, MPL-2.0, Python
- Автоматический трекер времени: приложения, окна, браузер. Приватно, self-hosted, localhost:5600
- Релиз v0.13.2 (05.10.2024): Windows installer 81MB
## [2026-08-20] ingest | projects/cloud-memory-external-agents (план облачной памяти для внешних агентов)
- Контекст: clarify-опрос Rem о том, что разворачивать по облачной памяти для внешних агентов (MCP HTTP endpoints за bearer — AgentMemory + GBrain)
- 4 варианта: 1=A+B сразу, 2=только Tailscale, 3=только публичный MCP на nginx, 4=не разворачивать, починить state.db и оставить план
- Решение Rem (20.08.2026): вариант 4 — ничего не разворачивать пока, приоритет = починка state.db, план сохранён

## [2026-08-20] ingest | +1 страница
- [[articles/1c-autonomous-ai-development]] — паттерн автономной разработки 1С с ИИ-агентами
## [2026-08-20] ingest | +1 страница

- Добавлена страница [[tech/llm-as-a-verifier]] — LLM-as-a-Verifier: верификация ответов LLM через logprobs (Best-of-N, self-verification). Проверено на opencode-go: топ-k logprobs не отдаёт → пока НЕ применимо к текущему стеку; перспективный усилитель на больших/сложных задачах.
- Источник: https://github.com/llm-as-a-verifier

## [2026-08-20] ingest | +1 страница

- Добавлена страница [[tools/hermes-memory-comparison]] — сравнение систем памяти для Hermes по 6 болям (стабильность, разгрузка MD, единая точка, многослойность, авто-retrieve, сквозная память). Рекомендация: Holographic (стабильность) / Hindsight, ClawMem (максимум болей). HTML-версия: /var/www/landing/hermes-memory.html → https://rem2222.top/hermes-memory.html


- Добавлена страница [[tech/opencode-notifier-ntfy]] — плагин OpenCode (TypeScript, MIT) для ntfy-уведомлений о событиях: permission/complete/error/question. GitHub: ongyishen/opencode-notifier-ntfy (2★). Только в вику, НЕ ставился.

- Добавлена страница [[tech/netbird]] — mesh VPN / Zero-Trust на WireGuard (Go, 28.6k★, BSD-3+AGPLv3), конкурент Tailscale. GitHub: netbirdio/netbird. Только в вику, НЕ ставился.

- Ingest | 4 новых страниц (топ-5 GitHub недели): [[tech/cloudflare-computer]] (Cloudflare Computer), [[tech/openviking]] (self-evolving контекст-БД), [[tech/needle-cactus]] (Needle 2, 14MB модель), [[tech/omarchy]] (Linux от DHH). [[tech/semantica]] уже была (Ночная рутина). Только в вику, НЕ ставились.

- Добавлена страница [[tech/backpass]] — gradient descent для памяти агента: читает транскрипты сессий (7 харнессов, incl. hermes state.db) и предлагает evidence-обоснованные правки. GitHub: kunchenguid/backpass (188★, JS, MIT). Только в вику, НЕ ставился.

- Добавлена [[tech/orca-ade]] — Orca (stablyai/orca): ADE для параллельной работы агентов, ★53.6k за полгода, MIT. Источник: Habr news 1074212 (ссылка от Романа). НЕ ставить — только в вике.
## [2026-08-29] ingest | Qwen3.8-27B local GPU case
## [2026-09-12] ingest | AX (tech/ax.md)

## [2026-09-23] ingest | Qwen3.8-Flash-Next 176B на GTX 1080 Ti

- Добавлена [[tech/qwen38-flash-next-176b-1080ti]] — разбор статьи Habr 1085544 (@SkalolazOther): запуск 176B-класса (125B main + 51B n-gram, ~6B активных) на 11 GB VRAM. Рецепт: Unsloth UD-Q4_K_XL (111 GB) -> llama.cpp (`qwen4exp`, PR #27742, стабильно с 0.4.1) -> llama-server -> DSH-плагин dsh-local-llm-controller. Ключевое: НЕ ставить -ngl 999, авто-размещение + --n-cpu-moe. Результат 11 tok/s decode / 19 prefill, VRAM 9.5 GB. Грабли: плагин ищет llama-server.exe (симлинк), chat_template_kwargs enable_thinking deprecated, --no-reasoning-preserve НЕ выключает reasoning. Для нашего железа не подходит напрямую (111 GB > 64 GB RAM, GT 1030 2GB) — кандидат сборка X99-TF + E5-2696 v4 + GPU 1080 Ti-класса.

## [2026-09-23] update | free-llm-api-resources +6 сервисов

- Дополнена [[tech/free-llm-api-resources]] по Habr 1085352 (@Ungated): новая секция «Обзор @Ungated» — 6 сервисов, которых нет в cheahjs-списке. Atria (100M токенов на реге, Atria-Dawn-Preview = 744B MoE GLM-5.2, 3 API: Chat/Responses/Anthropic — все 200, x-rpm-limit: 50), Vireonix (БЕЗ ключа и регистрации, маршрут auto, 20M in/200K out токенов в час по IP, temporary: false), ShareLLM (120 req/5ч, 600/нед, 39 моделей, имя маршрута != реальная модель: gpt-5.6-luna -> codex-auto-review), OdiRouter (пул free-*, нестабильно: 502/503/504), Selora (Nova 14 дней, $5/4ч + $30/нед, 10/10 моделей включая claude-opus-5 и gpt-6-astra, тест = $0.000804), Routeway (5 RPM, 200/сут, при балансе $0, deepseek-v4-flash:free даёт 502, НЕУДАЧНЫЕ запросы едят квоту). Плюс секция «Ловушки»: HTTP 200 + пустой content = съеденный reasoning-токенами max_tokens (283 из 299 токенов ушли в reasoning), формат reasoning у каждого провайдера свой. Frontmatter: tags + habr, updated 2026-09-23, description переписан, в шапке два источника.

## [2026-09-25] ingest + install | Docker Skills

- Добавлена [[tech/docker-agent-skills]] — github.com/docker/skills (Apache-2.0, 169★, тег v0.3.0). 11 SKILL.md в 5 группах: Build(2), Compose(1), Sandboxes(4), Docker Agent(3), cross-product destructive-guardrails(1). Формат — Agent Skills Specification (agentskills.io), валидатор skills-ref, НЕ приватный формат Docker. Таблицы генерятся из catalog.yaml.
- УСТАНОВЛЕНО 3 из 11 в ~/.hermes/skills/devops/ (по согласованию Романа «ставь без подтверждения»): docker-destructive-guardrails (Tier1/Tier2 подтверждения — дополняет vps-disk-cleanup), docker-build-strategies (Multica собирает образы), docker-compose-patterns (healthchecks/depends_on для новых сервисов). Проверены skills_list — видны.
- Локальная правка: в docker-compose-patterns перед File naming вставлен блок [!IMPORTANT] — правило «compose.yaml канон, docker-compose.yml legacy» на нашем хосте НЕ применяется, всё на docker-compose.* (Multica: -f selfhost -f override), переименовывать нельзя (selfhosted-services и скрипты обновления Multica разыменовывают имена явно). Без правки был бы конфликт.
- Не ставили 8: sandboxes(4, у не используются), docker-agent(3, у нас Hermes), project-foundations(редко). Скрипты verify-*.sh прочитаны: только docker compose config --quiet и docker build - безопасно.

## [2026-09-26] ingest | Бесплатные AI coding agents 2026

- Добавлена [[tech/free-coding-agents-2026]] — Habr 1086812 (MihaDeev, данные 25.09.2026): 10 coding-агентов, что в них реально бесплатно. Ключевой тезис: бесплатный клиент != бесплатный inference, деньги всегда идут на inference. Типология автора: (1) агент+бесплатные модели = OpenCode/Freebuff, (2) агент+свой inference = Cline/Kilo/CodeGPT, (3) квота = Cursor/Codex/Antigravity/TRAE, (4) trial = ZCode 5 дней.
- Freebuff разобран детально: два режима НЕ смешивать. Full 100 Freebucks/день (GLM 5.3 Flash до 20ч, MiMo 2.6 Flash до 10ч, DeepSeek V4.1 Flash до 6ч — не складываются). Limited fallback для регионов без Full: DeepSeek V4 Flash 6 сессий x 1ч.
- Вердикт по нашему стеку: 8 из 10 уже закрыты (opencode-go основной+оплачен, qwen-tp, openrouter, freellmapi, FreeQwenApi:9656, FreeDeepseekAPI:9655, Ollama). Не закрыты: Freebuff и ZCode.
- Исправлена ошибка статьи: в Codex два раза Pro — по факту Pro 5x $100 / Pro 20x $200.
- Цены, которых в статье НЕТ (дознакомил отдельно): GLM Coding Lite $18/мес (промо -30

## [2026-09-26] ingest | Бесплатные AI coding agents 2026

- Добавлена [[tech/free-coding-agents-2026]] — Habr 1086812 (MihaDeev, данные 25.09.2026): 10 coding-агентов, что в них реально бесплатно. Ключевой тезис: бесплатный клиент != бесплатный inference, деньги всегда идут на inference. Типология автора: (1) агент+бесплатные модели = OpenCode/Freebuff, (2) агент+свой inference = Cline/Kilo/CodeGPT, (3) квота = Cursor/Codex/Antigravity/TRAE, (4) trial = ZCode 5 дней.
- Freebuff разобран детально: два режима НЕ смешивать. Full 100 Freebucks/день (GLM 5.3 Flash до 20ч, MiMo 2.6 Flash до 10ч, DeepSeek V4.1 Flash до 6ч — не складываются). Limited fallback для регионов без Full: DeepSeek V4 Flash, 6 сессий x 1ч.
- Вердикт по нашему стеку: 8 из 10 уже закрыты (opencode-go основной+оплачен, qwen-tp, openrouter, freellmapi, FreeQwenApi:9656, FreeDeepseekAPI:9655, Ollama). Не закрыты: Freebuff и ZCode.
- Исправлена ошибка статьи: в Codex два раза «Pro» — по факту Pro 5x = $100 / Pro 20x = $200.
- Цены, которых в статье НЕТ (дознакомил отдельно): GLM Coding Lite $18/мес (промо -30% = $12.60), Pro $72-80, Max $160-168; лимиты Lite ~80 prompts/5h + ~400/нед + контекст 1M. Google AI Pro $19.99/мес. ChatGPT Go $8.
- Antigravity: квота привязана к Google AI подписке, отдельно не продаётся; на форуме Google жалобы, что лимит Claude Opus сбрасывается каждые 5ч, но бывает уезжает на 2 дня.
- Рекомендации: бесплатно — Freebuff + ZCode триал; платно только GLM Coding Lite после триала; опционально Google AI Pro (ради Gemini, прокси 127.0.0.1:8083 ненадёжен) и ChatGPT Go $8 (только если ставить Codex CLI). Не брать: ClinePass $9.99, Kilo Pass $19, Cursor Pro $20, CodeGPT $10, TRAE Lite $3, GLM Pro/Max, ChatGPT Plus/Pro.
- Перекрёстная ссылка добавлена в tech/free-llm-api-resources.


## [2026-09-26] ingest | YouTube-транскрипт с заблокированного VPS

- Добавлена [[tools/youtube-transcript]] — рабочий способ снять расшифровку ролика, когда IP VPS (80.241.218.110) заблокирован YouTube. Проверено на плейлисте Vizuara 'Build DeepSeek from Scratch' (30 видео).
- РАБОЧЕЕ: `curl -sL https://youtube-transcript.ai/transcript/{VIDEO_ID}.txt` — открытый endpoint, они сами просят LLM-агентов им пользоваться (см. их llms.txt). Без ключей и rate limit. Отдаёт markdown с таймкодами [m:ss]. Реально: 42 КБ на ролик 15:13 / 7708 слов. Выбор языка `?lang=XX`.
- АРТЕФАКТ ASR: автосубтитры повторяют каждую фразу ТРОЕкратно. Очистка — скользящий поиск 4/3/2-кратного повтора, порядок от большего к меньшему (иначе двойной съест середину тройного). 42085 -> 14287 символов.
- ДВЕ ЛОВУШКИ ОЧИСТКИ: (1) таймкод [0:36] — первый токен строки, без его отдельного выкидывания сравнение перекрытий всегда проваливается; (2) ASR дублирует хвост предыдущего сегмента началом следующего — лечится сравнением toks[:L] == prev_tail[-L:] (L до ~14).
- НЕ РАБОТАЕТ (15 путей, все проверены): youtube-transcript-api (RequestBlocked, cloud IP), yt-dlp --write-sub (Sign in to confirm you're not a bot), Tor socks5:9050 (таймаут, YouTube блокирует exit-ноды), video.google.com/timedtext (200 но 0 байт), 9 инстансов Invidious (все 502/503/500), pipedapi.kavin.rocks (502), youtubetotranscript.com (403), их серверный прокси server_vid2 (отвечает 'YouTube is currently blocking us'), kome.ai (429), tactiq (401), youtranscripts/tubetranscript/downloadyoutubesubtitles (429/404/404).
- КЛЮЧЕВОЙ ДИАГНОЗ: страница YouTube отдаёт 200, но playabilityStatus=LOGIN_REQUIRED -> 'Sign in to confirm you're not a bot', блока captions нет. Поэтому curl 200 ничего не доказывает — смотреть playabilityStatus.
- РАБОТАЕТ при заблокированном IP: oembed (заголовок/автор/превью) и yt-dlp --flat-playlist (30 ID плейлиста за ~2 сек).
- Перекрёстная ссылка + предупреждение добавлены в tools/yt-dlp (там секции про субтитры не было вовсе).


## [2026-09-26] ingest | browser-use/jev-ultrafast — первый прод-кейс Jev

- Добавлена [[tech/jev-ultrafast]] — браузерный агент от организации Browser Use, построенный на Jev (TypeSafe System One). MIT, Python >=3.12, всего 2 зависимости (browser-harness==0.1.13, httpx[http2]).
- 20 646 звёзд / 1 419 форков, создан 16.09.2026. Рост ~2000 звёзд/день.
- ВАЖНО: во всём репозитории ВСЕГО 3 коммита, код написан за два дня (17-18.09), дальше только docs. Это вирусный демо-репозиторий, а не вылизанная библиотека.
- Механизм: каждая страница -> таблица индексированных элементов [1] button / [2] combobox ... Один запрос к Jev возвращает И операцию, И цель (CLICK/TYPE_TEXT/SELECT/SCROLL/WAIT/DONE/BLOCKED). Вопросы про цель СПЕКУЛЯТИВНЫЕ: click_target и type_text_target спрашиваются параллельно, исполняется только совпавший -> 2 решения за 1 сетевой раунд. Маленький LLM включается ТОЛЬКО при TYPE_TEXT и обязан вернуть JSON с одним полем text.
- ЦИФРЫ (6 чередующихся прогонов, одна задача, один профиль Chrome, TypeSafe jev-1.13.0, inception/mercury-2.5): медиана 9.450с -> 7.092с (-25%), Jev-запросов 22 -> 17, browser protocol calls 1092 -> 101, верификация 3/3. Задача: Google Flights Zürich -> London one-way -> 7.073с при 1x. Медианная латентность Jev 178мс.
- ИХ СОБСТВЕННЫЕ ОГОВОРКИ: p = 0.25 (3 пары), сами пишут 'too few for a strong statistical claim'; 'two websites do not establish broad reliability'; это НЕ общий бенчмарк; DONE не доказательство успеха.
- ОШИБКА В ПЕРВОЙ ВЕРСИИ СТРАНИЦЫ: я написал 'переполнение per-question context до 46.7%' - этой цифры НЕТ в источниках. Убрал после чтения docs/performance.md. Проверять каждую цифру по первоисточнику, даже если она 'кажется правдоподобной'.
- ОГОВОРКА ПО СТОИМОСТИ: $0.00006272 - это ТОЛЬКО плата за 2 текст-вызова через OpenRouter, НЕ полная стоимость задачи. У TypeSafe есть счётчики токенов, но НЕ сумма в долларах.
- ОГРАНИЧЕНИЯ: не поддерживаются shadow roots, frames, canvas, загрузка файлов, новые вкладки, вложенный скроллинг, произвольные keyboard-виджеты. Лимиты рана: 60 действий, 120 decision-запросов, до 250 кандидатов. Сервис loopback-only.
- ПРИГОДНОСТЬ У НАС: Python 3.12.3 + uv 0.11.16 на VPS - подходят. Узкое место ТОЛЬКО браузер: на 9222 стоит Lightpanda/1.0 (nightly.8662) в Docker-контейнере, а browser-harness требует настоящий Chrome + галочку chrome://inspect/#remote-debugging. Ставить на ДОМАШНИЙ ПК.
- ЦЕНА: $0.042/MTok вход, вывод бесплатно. Но typesafe.ai/pricing отдаёт 404 - официальной страницы цен НЕТ, ключ только через waitlist (console.typesafe.ai). Цифра подтверждается лишь сторонними обзорами.
- Правки: в tech/jev-jevrouter обновлён раздел Статус (был 'нужно попробовать' -> теперь есть конкретный кандидат) + добавлены оговорки про цену.
- ПРОБЕЛ ИСПРАВЛЕН: tech/jev-jevrouter вообще отсутствовала в index.md, хотя страница была создана раньше. Добавлены обе записи рядом с webwright.

## [2026-09-28] health | wiki-health: 63 → 0 проблем

- Еженедельный аудит wiki-health-check.py: 63 проблемы на 322 страницах → все исправлены, финальный прогон "Wiki health: OK".
- Frontmatter: +description (9 страниц), +tags (1), +related (26), frontmatter целиком для openviking-task-description.md.
- Битые wikilinks (21 реальный): исправлены на существующие пути ([[deepseek_harness]] → [[tech/deepseek-harness]], [[tools/zvec]] → [[tech/zvec]], [[tech/ollama-on-vps]] → [[ops/services/ollama]], [[hindsight]] → [[ops/services/hindsight]], [[tech/gbrain]] → [[tech/gbrain-lossless-agent-memory]], [[tech/llm-tier-strategy]] → [[concepts/llm-tier-strategy]] и др.); для [[cognee]] и [[tech/qwen-tp]] созданы новые страницы через wiki-write.
- tech/ax.md: demote второго H1. Сироты (33): все прописаны в index.md (новая секция ## Паттерны + Сервисы/Технологии/LLM/1С/Инструменты/GameDev/Память/Tasks/Hermes Agent/Разное), дата индекса → 2026-09-28.
- wiki-health-check.py: аудит ссылок игнорирует [[...]] внутри ```code``` и `code` — 48 «битых» ссылок-примеров в скилле были ложными (Obsidian не линкует код). Скилл memory-wiki-workflow: убран [[wiki-links]] из description, wiki-копия синхронизирована с источником + tags/related.
- Zvec: полный rebuild (1582 чанка, ~35 мин) держит эксклюзивный LOCK — zvec-wiki временно падает с "Can't lock read-only collection" (норма). tech/qwen-tp создан после старта walk rebuild'а — добавлен в индекс точечным insert.
- git: коммиты "wiki: Cognee", "wiki: qwen-tp", "wiki-health 2026-09-28" — push OK, рабочее дерево чистое.

## [2026-09-28] ingest | deepseek-4-1 — Assistant Operating Specification

- Источник: https://github.com/togg53192-cmd/jailbreaks/blob/main/deepseek-4-1.md — репо описывает себя как «LIST OF ALL MY JAILBREAKS», публичное, 1 475⭐ / 225 форков, 25 файлов по одному на модель, без лицензии. Последний пуш 24.09.2026.
- Создана страница [[prompts/deepseek-4-1-assistant-spec]] — разбор: структура (10 разделов), 8 приёмов механики (перенос линии из категории в вред, замыкание списка из 5 запретов, over-refusal как дефект, блок переоценки §7, заряженные слова = параметры, защита от дрейфа §10, снятие аудитории, мимикрия под продуктовую спецификацию), ограничения.
- Оригинал сохранён как [[raw/deepseek-4-1]] — 14 788 байт, 120 строк, sha256 6b6d56797e68c10e0ffb4274fe0cf8aca1b55b8f74c9b2d89e0089d972dff7ed (совпадает с выкачанным из raw.githubusercontent). Лежит в raw/, а не в prompts/: SCHEMA определяет raw как «исходники, не менять», и wiki-health-check.py его не сканирует — так оригиналу не добавляют YAML-фронтматтер и портят sha256.
- index.md: +2 записи в секцию «Промпты».
- Проверено, что credentials.json токена Qwen в публичном репо github.com/Staks-sor/qwen_free_api НЕ утёк — в дереве только .gitignore и credentials.example.json.

## [2026-09-28] ingest | harvard-ai-tutor-rct — Гарвард: ИИ-тьютор против профессоров

- Источник: https://www.nature.com/articles/s41598-025-97652-6 — «AI tutoring outperforms in-class active learning: an RCT introducing a novel research-based design in an authentic educational setting», Scientific Reports. 213k просмотров, 202 цитирования.
- Создана [[tech/harvard-ai-tutor-rct]] с тегом `ииобучение` — материал к проекту-«обучалке» Романа.
- ВСЕ цифры сверены с первоисточником (curl полной страницы, 355 КБ, разбор скриптом), а не по пересказу:
  - PS2, Fall 2023, зачислено 233 → в анализе 194 ✓
  - crossover: неделя 1 одни группы с ИИ / другие в классе, неделя 2 условия меняются ✓
  - медианный пост-тест: ИИ M=4.5 (N=142) vs класс M=3.5 (N=174) ✓
  - базовая линия pre-test M=2.75 (N=316), прирост в ИИ-группе «over double» ✓ (Mann–Whitney z=−5.6)
  - 70% в ИИ-группе <60 мин, медиана 49 мин (класс — 60 мин из 75-минутного занятия) ✓
  - вовлечённость 4.1 vs 3.6 (t(311)=−4.5, p<0.0001), мотивация 3.4 vs 3.1 (t(311)=−3.4, p<0.001) ✓
  - enjoyment и growth mindset — значимой разницы НЕТ
  - 83% сочли объяснения ИИ не хуже/лучше человеческих
- 7 педагогических принципов подтверждены дословной цитатой статьи: (i) active learning, (ii) cognitive load, (iii) growth mindset, (iv) scaffolding, (v) accuracy of information/feedback, (vi) targeted & timely feedback, (vii) self-pacing. Отмечено, что (vi)–(vii) физически недоступны одному преподавателю на потоке.
- Анти-галлюцинационный приём подтверждён: «we avoided relying solely on GPT-4 ... enriched our prompts with comprehensive, step-by-step answers».
- **Не подтверждено первоисточником** (на странице помечено отдельно): термин «угодничество»/sycophancy в статье отсутствует (0 совпадений по sycophan/people-pleas/agreeable) — есть только тезис «designed to be helpful, not to promote learning»; упоминаний Musk/Grok Educational/Сальвадор/PISA/Sweden в статье нет вообще (0 совпадений) — это авторская параллель Романа, помечена как таковая.
- index.md: +1 запись в секцию «Статьи».
- Ошибочно созданная ранее страница tech/free-proxy-auth-diagnostics.md удалена по решению Романа (я принял «закинь в Вики» за речь про диагностику прокси, тогда как оно относилось к тексту про Гарвард). В вики не попадала: index/log не трогались, коммита не было.

## [2026-09-28] fix | harvard-ai-tutor-rct — поправки после сверки с Fig. 1

- Роман прислал скриншот Fig. 1 из статьи — по нему вышли три уточнения, страница обновлена и запушена.
- **Исправлена своя же неточность**: было «z = −5.6, p < 0.0001», в статье — `p < 10⁻⁸` (значимость сильно выше, чем я написал).
- **Mean vs median**: головные цифры (4.5 / 3.5 / 2.75) — медианы, а Fig. 1 показывает средние (`Figure 1 shows mean aggregate results (weeks 1 and 2 combined)`). Столбец AI на рисунке ≈4.2–4.3, не 4.5. Точных средних пост-тестов в тексте статьи нет вообще: `Mean = X.X` встречается только для вовлечённости (4.1/3.6) и мотивации (3.4/3.1). На странице вынесено предупреждением — легко перепутать при цитировании.
- **Размеры групп**: N=142 + N=174 = 316 = N базовой линии; студентов 194, каждый проходит оба условия → это счётчики наблюдений по урокам, а не «студентов в группе».
- **Добавлена робастность** (не было): подгруппы FCI <40% и >40% обе значимо лучше с ИИ (p<0.001), то же для порога 65% CLASS; регрессия p<10⁻⁸, effect size 0.63 — с оговоркой статьи, что это занижение из-за ceiling-эффекта; рандомизация шла по группам пиран-инструкции (2–3 чел.), модель с кластеризацией на уровне группы дала те же результаты (p<0.001).
- Command Code (Provider API, 88 моделей) и opencode-deepseek (мост к бесплатному DeepSeek, резерв) — 2 новые страницы в tech/, записи в index.md.
- B.AI (api.b.ai, мульти-модельный API с дилами на MiMo/DeepSeek) — страница tech/bai.md + запись в index.md.

## [2026-09-29] update | CodeGraph отключён на сервере (MUL-10132) — записи вики дополнены

- Решение Романа: CodeGraph в проекте «Обнова мультика» не нужен → отключён. `systemctl disable --now codegraph.service cgc-daemon.service` (порты 3748/51234 закрыты); ACP discovery моделей после отключения 10.3 c (было 12.4 c при таймауте демона 12 c).
- Данные для решения: 104 вызова codegraph-тулов за 05.08–29.09 = 16 задач, все из проекта Routine («Обнова мультика»), из GSD и других проектов — 0; граф устарел до ~v0.4.17 (индекс от 2026-08-06), свежий = стоп сервиса + ~20 мин + ~3.5 GB RAM (OOM 2026-08-07); реальную проверку символов в рутине всегда делал grep/git.
- Дополнено в вики: [[ops/services/codegraph]] (первое тело страницы: состояние, почему отключили, возврат, замена grep/git), [[ops/services/cgc]] (тело: контексты multica/codexbar, отключение), [[ops/workflow/new-project-with-codegraph]] (предупреждение о статусе), [[tasks/mul-239-codegraph-in-gsd]] (статус: внедрение в GSD не состоялось), index.md (метки «отключён 2026-09-29» у codegraph и cgc).
- Осталось за владельцем: удалить блок `mcp_servers.codegraph` из /root/.hermes/config.yaml (агентам не трогать, MUL-696); данные графа (111 MB + 525 MB) не удалялись.
- Также обновлены: автопилоты «Обнова мультика» (шаг 4) и «Ночная рутина» (health-check → «ожидается inactive, не алертить»), скилл multica-workflow.

## [2026-09-30] audit | Wiki maintenance audit MUL-10087 — health-check 9 → 0

- Битые wikilinks (5 целей): `[[software/freellmapi]]` → `[[tech/freellmapi]]`; `[[software/dsh]]` (3 страницы) → `[[tech/deepseek-harness]]`; `[[software/opencode-go]]` → `[[tech/opencode-go]]`; `[[tools/hermes]]` (7 вхождений в tech/opencode-deepseek, tech/bai, tech/command-code) → `[[ops/services/hermes-agent]]`.
- Множественные H1 (3): в tech/opencode-deepseek, tech/bai, tech/command-code убран дублирующий голый `# Название`, оставлен описательный H1.
- Новая страница: [[tech/opencode-go]] — основной inference-провайдер Hermes (подписка OpenCode Go, `opencode.ai/zen/go/v1`, fallback-цепочка, лимиты, `*-free` ≠ go); + запись в index.md.
- Итог: `python3 /root/.hermes/scripts/wiki-health-check.py` → `Wiki health: OK` (330 контент-страниц), порог ночного правила >10 не достигнут. Закрыты как дубли старые audit-задачи.

## [2026-09-30] tech | Dex: разбор внутреннего устройства + внедрение ①②③ и векторной памяти

- **Новая страница [[tech/dex-internals]]** (17 КБ) — полный разбор по исходникам: три процесса (dex-poller / dex-control / dex-heartbeat), два «мозга» (чат stateless против тика с одним словом решения), луп из 7 шагов, честная таблица исполнителей (2 из 7 — заглушки), драйвы, память, панель управления, слабые места, конфигурация, бэкапы.
- **Обновлён [[ops/services/dex]]**: запись была устаревшей («юниты inactive, dex-poller НЕ запущен») — теперь оба `enabled+active`, добавлены config_paths, `depends_on: gemini-web2api`, векторная память, ссылка на tech-страницу.
- **Происхождение Dex**: создан 19.07.2026 Hermes'ом по просьбе Рома, первый коммит `df3dbe2` в 19:31 (через минуту после «Сделай dex и его контролу бэкап на гит»). Бот `@Jawl_Moishe_bot` переиспользован из свёрнутого JAWL.
- **① Отчёт по тику**: в Telegram уходит каждое действие, не только аномалии; кулдаун на идентичный текст держит поток в ~14–15 сообщений/сутки (49 тиков/сутки до дедупликации).
- **② Чтение состояния**: блок «тик/фокус/драйвы/5 тиков» в system prompt, команда `/status`, окно истории 10 → 30, правила честности (без них Dex выдумывал «искал по индексам» и «песочницу»).
- **③ Драйвы по модели «дефицит → растёт, насыщение → падает»** (утверждена Ромом): прежняя логика была перевёрнута — драйв рос ПОСЛЕ действия и не убывал, оба упёрлись в 1.0. Разовый сброс `migrate_drives()` → 0.4/0.4, маркер `drives_v2`.
- **④ Векторная память**: `vec0.so` из wheel `sqlite_vec 0.1.9` в `~/.hermes/proactive/lib/` (pip под PEP 668 отказывается), `vec_ticks` float[1024], эмбеддинги `bge-m3` через Ollama. **Ключевой приём — дедупликация: 1362 тика = 69 уникальных строк `action: result`**, экономия ×25, минуты вместо двух часов.
- **Диагностика потери контекста — три причины, и НЕ размер контекста** (промпт ~800 токенов): (1) провайдерная ошибка Google «параметры Gmail отключены» — воспроизведена чистым запросом, прокси инструменты не подключает, ошибка идёт извне; (2) конфабуляция про sqlite_vec — фраза лежит в его же system prompt (`identity.yaml:32`, `README.md:53` «Целевая», этап 5 🔜); (3) отсутствие ground truth → противоречия между соседними ответами.
- **Найден и починен битый git-remote**: в URL был вшит протухший PAT, push падал `Invalid username or token` — токен убран, авторизация через `credential.helper = store`.
- **Бэкапы**: `github.com/Rem2222/dex-agent` (запушено `ef3030b`), архив `/root/backups/dex-proactive-20260930_*.tgz`.

- MAPS (pavrus117/ai-os-maps-guide): 2 страницы tech/ai-os-maps и tech/maps-ideas (slug: maps-ai-operating-system, idei-iz-maps-dlya-steka-rem), записи в index.md. Попутно: related в 5 свежих страницах переведён в эталонный многострочный формат, убраны дубли H1, исправлены битые [[tools/hermes]]/[[wiki/tech/sdd]]/[[software/zvec]].
- Идеи MAPS: вердикт Rem — (1) один дом на факт в работу и расписан по файлам, (2) пробки на cron отложены, (3) граф вики и (4) профиль-ограничение отклонены (Obsidian graph view).

## [2026-09-30] tech | Dex вечером: инструменты с песочницей, скилы, задачи, команды ТГ

- **1. Тулзы.** Новый модуль `dex_tools.py` (399 стр.): allowlist-песочница (только чтение, 6 каталогов, запрет секретов, обрезка 4000 символов) + 8 схем `tools` в запрос к gemini-web2api + `chat_with_tools()` — цикл до 4 раундов «выполнил → дописал → переспросил», на лимите последний запрос уже без инструментов. Живые тесты: `run_check(disk)` → «34G свободно», `read_file(/etc/hostname)` → `vmi3329315`, `/etc/shadow` → отказ песочницы.
- **2. Остатки п.12.** Три заглушки заменены рабочими: `check_tools` — снимок 97 скриптов + diff (раньше 6 раз за день возвращал «пропускаю этот тик»); `check_services` — разбор `systemd_units` из **всех 41 страниц** реестра, проверка **30 юнитов** (было 1) + `docker ps -a`; `explore_interest` — реальный вызов LLM + история 20 наблюдений, круговой выбор тем.
- **3. Переиндекс** — `vec_build.py` оказался уже инкрементальным: 1362 → 1404 тика, догон 6 штук за 5,5 с.
- **4. Скилы.** Каталог `skills/<имя>/SKILL.md` (фронтматтер `name/description/when`), 3 процедуры: `service-diagnostics`, `disk-pressure`, `what-changed`. Короткий индекс в промпте, полный текст — через `read_skill`. Живой тест: «упал сервис, что делать?» → сам вызвал `read_skill(service-diagnostics)` → ответ по шагам из скила (37 с, 1 вызов).
- **Задачи.** Таблица `tasks` была создана, но не использовалась (0 строк). Появились `task_add/task_list/task_done/task_stats`, автосоздание из чеков через `maybe_file_task()`, инструмент `tasks`, влияние на промпт и на драйв `diligence` (просрочка старше суток). **Ловушка:** первая версия клала в `what` список юнитов — он меняется каждый тик, и одна проблема дала задачи #2 и #7; решение — стабильная фраза в `what`, детали в `result`.
- **Команды ТГ** (были `/start` и `/status`, остальное — заглушки): `/tasks /task /done /drives /last /memory /check /skills /skill /tick /pause [мин] /resume /restart /help`. **Белый список в двух местах** (`process_message` и `handle_command` — первого оказалось мало), **подтверждение `/yes|/no` с TTL 120 с** для `/pause`, `/restart`, `/tick`. `DISABLED` теперь понимает `until=<ISO>` и снимается сам.
- **`/restart` имеет смысл** — не из-за промпта (он собирается заново на каждое сообщение), а из-за `sessions.db`: 30 последних реплик подгружаются в каждый запрос. Очищает только строки своего `chat_id`.
- **Две ошибки дня, найдены и починены:** (1) в `call_hermes()` попал `Authorization` без `Bearer` — строка скопирована из вывода `read_file`, который редактирует `Bearer <ключ>` в `***`; провайдер отвечал `invalid api key`. (2) `check_services` звал `systemctl is-active` **без `--user`** — `dex-*` живут в менеджере сеанса, отчёт врал «inactive» для работающих сервисов (было 20/10, стало 23/7).
- **Коммиты:** `36e0e37` (тулзы) → `0997f6d` (остатки п.12) → `0cde484` (скилы) → `8fc8964` (задачи + команды). Бэкапы `dex-proactive-20260930_18*.tgz` и `_192100.tgz`.
- **Страница [[tech/dex-internals]] переписана** (18 → 28 КБ): раньше там было «нет tool-calling, нет скилов» — теперь инструменты, песочница, скилы, задачи, команды, обе ошибки дня; из слабых мест закрыты #3 #4 #6 #7 #9 #10, остался только роадмап 4–7.

## [2026-09-30] tech | Dex поздно вечером: командная строка, уровни доступа, интернет для интереса

- **`run_cmd` — 14 именованных шаблонов команд** (вариант А вместо произвольной строки): journalctl, systemctl (отдельный шаблон под `--user`), docker logs/inspect/stats, git log/status, ss, free, uptime, ps, df. Каждый слот проходит regex, значение с ведущим `-` отклоняется, `argv` списком, `shell=False`. **14/14 попыток инъекции отклонены** (`; rm`, `--help`, `0;cat /etc/shadow`, `../../`, `$(whoami)`, отсутствующий шаблон).
- **Три дыры закрыты тестами**: слот-путь режется на `DENY_SUBSTRINGS` (раньше `git-log /root/.hermes/.env` проходил); имена systemd-юнитов из вики валидируются regex **до** попадания в `argv systemctl` (в `_registry_units` + повторно в `_unit_states`); `systemctl --user` получает `XDG_RUNTIME_DIR` явно — без него «Failed to connect to bus» и молча пустой результат.
- **Уровни доступа 3/2/1** в `agent.db` (`state.access_level`, по умолчанию 3): 3 — только чтение (10 схем), 2 — песочница (запись в `sandbox/`+`skills/`, запуск от nobody без сети, лимиты CPU 20с/1ГБ/10МБ), 1 — root (запись по `/root/.hermes`, запуск от root). `active_tools()` фильтрует схемы, поэтому на уровне 3 модель **не видит** `write_file`/`run_script` вовсе. Переключение: `/access [1|2|3]` — показ без подтверждения, снижение через `/yes`, переход на 3 сразу; то же в `GET /api/status`.
- **`nobody` не пройдёт через `/root` (0700)** — поэтому на уровне 2 скрипт и входы копируются в одноразовый `/tmp` 0777, а созданные файлы забираются обратно в `sandbox`; tmp удаляется. Проверено: uid 65534, сеть отрезана (`unshare --net` → OSError), артефакт `report.txt` вернулся, `dexrun_*` не осталось.
- **`fetch_url` — интернет для драйва любопытства** (доступен на всех уровнях): 15 с / 400 КБ, редиректы обрабатываем сами (до 5) с проверкой **каждого шага**. SSRF-защита: только http/https, блок localhost/metadata, литералы IP и **все адреса из DNS** на публичность — `localtest.me → 127.0.0.1` отсекается, как и `169.254.169.254`. Тесты: example.com 0,1с, GitHub API 0,3с, Wikipedia 0,5с; **12/12 SSRF отклонены**.
- **`explore_interest` читает страницу, а не только мнение**: в промпт просим ОДИН URL отдельной строкой, извлекаем **до** обрезки (иначе адрес, стоящий последним, отрезался), прибавляем фрагмент к наблюдению, ошибки сети тик не роняют. Возврат 200 → 700 символов, history → 600. Живые прогоны: sqlite-vec GitHub и DeepSeek API Docs прочитаны, несуществующий репозиторий честно отдал `HTTP 404`.
- **Найдено и исправлено в собственном коде**: `_public_ip()` глотал `ValueError`, из-за чего `except` в `_check_url` не срабатывал и **любой** хост считался приватным (все URL блокировались); `KeyError` в подсказке подтверждения для новой команды `/access`; URL извлекался после обрезки.
- **Страница [[tech/dex-internals]] обновлена**: цифры файлов (946/974/1060/381), таблица инструментов 8 → 12 схем, новые разделы «Шаблоны команд», «Чтение сайтов», «Уровни доступа», `/access` в списке команд; из слабых мест закрыты #11 #12, **#13 отмечен как частично открытый** — автоприменение самопатчей сознательно не вводилось, нужен сторож.
- **Коммиты:** `12c0f96` (run_cmd) → `65269ea` (уровни) → `6e89dd3` (fetch_url + развязка интереса). Бэкапы `dex-proactive-20260930_200500.tgz`, `_221500.tgz`.
## [2026-10-03] wiki-health: frontmatter (description/related) для 5 страниц llm/+tools/llm-usage, +2 страницы ops/services (multi-exporter — демонтирован, skills-dashboard — не запущен), +6 записей в index.md
