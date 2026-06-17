---
description: Обзор MCP-проектов из репозитория Sumanth077/Hands-On-AI-Engineering — 4 проекта с интеграцией Model Context Protocol через разные транспорты и библиотеки.
tags: [tech, mcp, ai-agents]
related: [[tech/hermes-memory-setup-vps]] [[tech/rag-projects-summary]] [[tech/openmanus]]
---

# MCP-проекты: Hands-On AI Engineering

Репозиторий: [Sumanth077/Hands-On-AI-Engineering](https://github.com/Sumanth077/Hands-On-AI-Engineering). Найдено 4 проекта, использующих MCP.

## Сводная таблица

| Проект | MCP-сервер | Транспорт | MCP-библиотека | LLM |
|--------|-----------|-----------|---------------|-----|
| GitHub Intelligence Agent | GitHub MCP (api.githubcopilot.com/mcp) | Streamable HTTP | mcp-haystack (MCPToolset) | Gemini 3 Flash |
| Hotel Finder Agent | Trivago MCP (mcp.trivago.com/mcp) | Streamable HTTP | mcp Python SDK / google.adk.tools.mcp_tool | qwen3.6-flash (Orq.ai) |
| Eagle Eye | GitHub MCP (локально, @modelcontextprotocol/server-github) | stdio (npx) | OpenClaw (встроенная) | MiniMax M2.7 |
| Agent Discovery Agent | Registry Broker API (не прямое MCP) | REST | нет | Gemini 3 Flash |

---

## 1. GitHub Intelligence Agent

**Путь:** `ai_agents/github_intelligence_agent/`

**MCP-интеграция:**
- `mcp-haystack` — компонент `MCPToolset` + `StreamableHttpServerInfo`
- GitHub PAT через `Secret.from_env_var("GITHUB_PAT")`
- Streamable HTTP транспорт к `api.githubcopilot.com/mcp/`

**Ключевое архитектурное решение:** `SearchableToolset` оборачивает `MCPToolset`. Когда пользователь задаёт вопрос, Gemini сначала вызывает `search_tools` с ключевыми словами, Haystack находит 2-3 релевантных MCP-инструмента и загружает только их схемы в контекст. Это предотвращает перегрузку контекста (40+ инструментов GitHub API)

**Фреймворк:** Haystack Agent | **UI:** Streamlit

---

## 2. Hotel Finder Agent

**Путь:** `ai_agents/hotel_finder_agent/`

**MCP-сервер:** Trivago MCP — три инструмента:
- `trivago-search-suggestions` — резолвит локацию в ID/координаты
- `trivago-accommodation-search` — поиск отелей по локации и датам
- `trivago-accommodation-radius-search` — поиск по GPS-координатам

**Две реализации:**
1. **Streamlit (`app.py`):** нативная `mcp` библиотека — `streamablehttp_client`, `ClientSession`, ручная загрузка инструментов, конвертация в OpenAI-формат
2. **ADK (`hotel_finder_agent/agent.py`):** `google.adk.tools.mcp_tool.McpToolset` с `StreamableHTTPConnectionParams`

**Архитектурные решения:**
- LLM в отдельном потоке (`ThreadPoolExecutor`) — избегает конфликтов с event loop Streamlit
- `terminate_on_close=False` — обход ошибки 501 при закрытии сессии с Trivago
- Перехват `anyio.ClosedResourceError`

---

## 3. Eagle Eye — GitHub PR Review Agent

**Путь:** `ai_agents/eagle_eye/`

**MCP-интеграция:** Локальный stdio MCP-сервер через `npx -y @modelcontextprotocol/server-github`
- `openclaw.example.json` — декларация MCP-сервера в конфиге платформы
- OpenClaw gateway управляет подключением к stdio-процессу
- GitHub PAT в env переменной

**Архитектурные решения:**
- **Telegram-триггер + двухшаговый workflow:** PR URL → ревью в Telegram → команда `post` → публикация на GitHub через MCP. Ничего не постится без approval пользователя
- **SOUL.md:** вся логика агента в prompt-файле (identity, критерии, workflow) — не в Python
- **Pass-through безопасность:** агент не использует REST API GitHub напрямую и не вызывает shell — только MCP
- **Модель:** MiniMax M2.7

---

## 4. Agent Discovery Agent

**Путь:** `ai_agents/agent_discovery_agent/`

**MCP-связь:** Не прямое MCP-подключение. Использует Registry Broker API (`https://hol.org/registry/api/v1`), который индексирует MCP-серверы и 4 других протокола (NANDA, Virtuals Protocol, A2A, ERC-8004)

**Фишка:** Агент-поисковик, который находит MCP-серверы и другие AI-агенты через единый интерфейс

---

## Выводы по MCP

1. **Три подхода к MCP-интеграции:**
   - **Streamable HTTP** (удалённый сервер): GitHub Intelligence, Hotel Finder — современный протокол, не требует локального процесса
   - **stdio** (локальный процесс): Eagle Eye — для изолированных/приватных данных
   - **REST API поверх MCP-индекса**: Agent Discovery — когда MCP не используется как runtime, а только как каталог

2. **MCP-библиотеки:**
   - `mcp-haystack` — для интеграции с Haystack Agent framework
   - `google.adk.tools.mcp_tool` — для Google ADK
   - Нативная `mcp` Python SDK — для ручного управления
   - OpenClaw — встроенная поддержка (stdio)

3. **Применимо к моей инфраструктуре:**
   - Hermes Agent уже поддерживает MCP (native-mcp skill + `hermes mcp` команды)
   - Можно аналогично подключать GitHub MCP, Trivago MCP и др.
   - Streamable HTTP транспорт — предпочтителен для удалённых серверов
