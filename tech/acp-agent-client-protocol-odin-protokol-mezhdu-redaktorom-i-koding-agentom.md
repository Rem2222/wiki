---
description: "Открытый стандарт связи редактора и кодинг-агента: JSON-RPC 2.0, сессии, апрувы, экосистема из полусотни агентов; разграничение с MCP, A2A и архивированным IBM ACP."
tags: [acp,agents,protocols,zed,hermes]
updated: 2026-11-05
source: "https://agentclientprotocol.com"
related:
  - tech/agents-anywhere-acp-rantaym-dlya-hermes-mul-10265
  - ops/services/agents-anywhere
  - tech/a2a-agent2agent-delegirovanie-zadach-mezhdu-agentami-i-stoit-li-vstavlyat-v-smithschat
---

# ACP (Agent Client Protocol): один протокол между редактором и кодинг-агентом

## Что это

**Agent Client Protocol (ACP)** — открытый стандарт связи **редактора/IDE и кодинг-агента**. Прямая аналогия: как LSP однажды убрал необходимость писать поддержку каждого языка в каждом редакторе, ACP убирает комбинаторику «каждый редактор × каждый агент».

Проблема, которую он решает: агенты и редакторы связаны, но совместимость не бесплатна. Каждый редактор писал свою интеграцию под каждого агента, каждый агент — свой API под каждый редактор. Итог — накладные расходы на интеграции, частичная совместимость и привязка разработчика к тем интерфейсам, которые есть у выбранного агента.

## Статус проекта

- Автор — Zed Industries, репозиторий переехал из `zed-industries/agent-client-protocol` в организацию **`agentclientprotocol/agent-client-protocol`**
- Лицензия **Apache-2.0**, язык Rust, создан **23.06.2025**
- На 05.11.2026: **4 585 ⭐**, 473 форка
- Актуальные релизы: crate **v1.15.1** и **schema v1.29.1** от 02.11.2026; параллельно идёт **schema v2.0.0-alpha.13** в статусе draft
- Документация: `agentclientprotocol.com`, есть `llms.txt` для агентов

## Как устроен

Транспорт — **JSON-RPC 2.0**: методы «запрос-ответ» и односторонние нотификации. Локальный агент обычно работает как подпроцесс клиента и общается через stdio; удалённый — по HTTP или WebSocket, но полная поддержка удалённых сценариев к ноябрю 2026 ещё в работе.

Поток одного хода (prompt turn):

1. `initialize` — согласование версий и возможностей
2. `authenticate` — если агент требует авторизации
3. `session/new` — новая сессия, или `session/load` — продолжение существующей (требует capability `loadSession`)
4. `session/prompt` — сообщение пользователя; агент отвечает потоком нотификаций `session/update`
5. по ходу агент может запросить `session/request_permission` (разрешение на вызов инструмента), работать с файлами (`fs/read_text_file`, `fs/write_text_file`) и терминалом (`terminal/create`, `terminal/output`, `terminal/wait_for_exit`, `terminal/kill`, `terminal/release`)
6. `session/cancel` — прерывание; ход закрывается ответом со stop reason

Дополнительно: `session/set_mode` (режимы работы агента), `session/list`, `session/delete`, план агента, слэш-команды, `elicitation/create` для структурированных уточнений, `logout`.

Текстовый формат по умолчанию — Markdown. JSON-представления частично переиспользованы из MCP, а своё добавлено там, где MCP не подходит: диффы, режимы сессии, план, слэш-команды.

## Экосистема

Агентов в официальном списке больше пятидесяти, среди них: **Hermes Agent**, Claude Agent (через адаптер Zed SDK), Codex CLI (через адаптер), Gemini CLI, GitHub Copilot (public preview), Cursor, Cline, Goose, Junie от JetBrains, Kimi CLI, Qwen Code, OpenCode, OpenHands, OpenClaw, Mercury CLI, Mistral Vibe, Poolside, Factory Droid, Augment Code, Blackbox AI.

Клиентов тоже много: Zed, JetBrains, **neovim** (CodeCompanion, `avante.nvim`, `hermes.nvim`), **Obsidian** (Agent Client, Agent Console, Copilot for Obsidian, Obsidian Harness), Emacs через `agent-shell.el`, VS Code через Exo, Chrome-расширения, Athas, necoder, Oleafly, Open Knowledge.

Есть **ACP Registry** — чтобы ставить агента в редактор одной кнопкой.

## Чем ACP не является

Термин перегружен, под «ACP» в ИИ живут четыре разные вещи:

- **Agent Client Protocol** (эта страница) — редактор ↔ агент
- **MCP** (Model Context Protocol, Anthropic) — агент ↔ инструменты и данные. Не конкурент: MCP даёт агенту руки, ACP даёт агенту место в интерфейсе, они работают вместе
- **A2A** (Agent2Agent, Google → Agentic AI Foundation) — агент ↔ агент, делегирование задач между непрозрачными агентскими системами. См. [[tech/a2a-agent2agent-delegirovanie-zadach-mezhdu-agentami-i-stoit-li-vstavlyat-v-smithschat]]
- **IBM ACP** (Agent Communication Protocol, `i-am-bee/acp`) — исторический REST-протокол для агентов, **архивирован** (последний push 25.08.2025), команда ушла в A2A. Главный источник путаницы
- **Agentic Commerce Protocol** (OpenAI + Stripe) — про покупки агентами, к разработке отношения не имеет

## Зачем это Роману

- **Hermes уже ACP-агент** и присутствует в официальном списке. У него есть headless ACP-сервер: `hermes acp` — stdio JSON-RPC с `new`, `load`, `resume`, `fork_session`, prompt со стримингом, cancel, апрувами, `set_model` и `set_mode`
- Значит Hermes можно подключить к любому ACP-клиенту без своего API: например, к Obsidian или neovim, где есть готовые плагины
- Тот же протокол использовался в работе по [[tech/agents-anywhere-acp-rantaym-dlya-hermes-mul-10265]]: универсальный ACP-рантайм вместо «hermes-специфичного»

## Статус

Разведано по документации и GitHub API 05.11.2026. Ничего не устанавливалось: подключение Hermes к ACP-клиенту (Obsidian или neovim) — отдельная задача, если понадобится.

## Источники

- `https://agentclientprotocol.com`
- `https://github.com/agentclientprotocol/agent-client-protocol`
