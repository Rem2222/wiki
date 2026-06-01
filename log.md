# Log — Журнал вики

_Append-only. Формат: `## [дата] type | описание`_

---

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
