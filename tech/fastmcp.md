---
title: "FastMCP — MCP фреймворк от PrefectHQ"
description: "FastMCP — стандартный Python-фреймворк для создания MCP серверов, клиентов и приложений. 25.7k ⭐, ~70% всех MCP серверов."
tags: [MCP, Python, FastMCP, Prefect, сервер, клиент, фреймворк]
related: [[1c-mcp]], [[mcp]], [[native-mcp]]
---

# FastMCP 🚀

**GitHub:** github.com/PrefectHQ/fastmcp  
**Документация:** gofastmcp.com  
**PyPI:** `fastmcp`  
**Звёзды:** 25.7k ⭐ | **Коммитов:** 3.5k+ | **Загрузок:** ~1 млн/день  

**Коротко:** Быстрый, Pythonic способ строить MCP сервера и клиенты. FastMCP 1.0 был включён в официальный MCP Python SDK (2024). На текущий момент standalone проект с 25.7k ⭐.

---

## Фишка

**70% всех MCP серверов на всех языках построены на FastMCP.** Это *de facto* стандарт для MCP в Python-экосистеме. Лучшее, что можно взять, если нужно написать свой MCP сервер.

---

## ✅ Плюсы

- **Минимум кода** — декораторы `@mcp.tool()` + type hints = готовый MCP инструмент со схемой и валидацией
- **Три компонента** в одном фреймворке: Servers, Clients, Apps
- **Apps** — интерактивные UI (чарты, дашборды, формы) прямо в диалоге с LLM
- **Из коробки:** OAuth (CIMD, Bearer, Auth0, GitHub, Google, Keycloak...), прогресс, нотификации, логирование
- **CLI** — `fastmcp install` устанавливает сервер в Claude/Cursor/Gemini
- **fastmcp-remote** — мост удалённых MCP серверов в stdio-only хосты
- **Client-only** — лёгкий пакет только для клиента без зависимостей сервера
- **FastAPI интеграция** — MCP + REST на одном порту
- **Sandboxed Agents** — изоляция MCP инструментов от агентов
- **1 млн загрузок/день** — зрелый, активно поддерживается

---

## ❌ Минусы

- Только Python (не подойдёт если нужно на Go/JS)
- Для простых интеграций может быть избыточен (если нужен 1 инструмент — проще `mcp` напрямую)
- `apps` (интерактивные UI) работают только с определёнными MCP хостами (поддержка не везде)

---

## Быстрый старт

```bash
uv pip install fastmcp
```

```python
from fastmcp import FastMCP

mcp = FastMCP("My Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

```bash
# Запуск: автоматически выбирает транспорт
python server.py

# Или явно
python server.py --transport sse --port 8000
```

**Типы транспорта:** `stdio` (по умолч.), `sse` (HTTP), `streams` (WebSocket).

---

## Три компонента

### Servers

```python
@mcp.tool           # инструменты (callable)
@mcp.resource       # данные (URI-шаблоны)
@mcp.prompt         # шаблоны промптов
```

### Clients

```python
from fastmcp import FastMCPClient

async with FastMCPClient("http://localhost:8000/mcp") as client:
    result = await client.call_tool("add", {"a": 1, "b": 2})
```

Поддерживает: OAuth 2.1, Bearer, CIMD, root directories, sampling, progress, logging, background tasks.

### Apps (интерактивные UI)

```python
from fastmcp import FastMCPApp

app = FastMCPApp(mcp)
app.run()
```

Типы UI: prefab (чарты/таблицы/формы/дашборды), generative UI (LLM создаёт UI на лету), custom HTML/JS.

---

## fastmcp-remote

Мост для подключения удалённых MCP серверов к хостам, которые поддерживают только stdio-транспорт:

```bash
uvx fastmcp-remote --url https://my-server.com/mcp
```

Полезно для: Claude Code, Cursor и других stdio-only хостов.

---

## Сравнение с альтернативами

| | FastMCP | MCP SDK (офиц.) | Написать вручную |
|---|---|---|---|
| Кода | `@decorator` | `Server()` + схема | Всё с нуля |
| Клиент | ✅ из коробки | Нужно писать | Нужно писать |
| OAuth | ✅ 10+ провайдеров | ❌ | ❌ |
| Apps/UI | ✅ | ❌ | ❌ |
| Загрузки | 1M/день | ~100k/день | — |

---

## Когда брать FastMCP

- Нужно **написать свой MCP сервер** (а не просто подключить готовый)
- Нужен **MCP клиент** для подключения к чужим серверам
- Нужны **OAuth/авторизация** для MCP
- Нужен **bridge** (fastmcp-remote) для удалённых серверов
- Проект на Python

## Когда НЕ брать

- Просто подключить готовый MCP сервер через `native-mcp` в Hermes
- Написать 1 простой инструмент на коленке
