# Настройка памяти Hermes Agent на VPS (80.241.218.110)

**Дата настройки:** 27-28 мая 2026
**Сервер:** Contabo VPS, IP 80.241.218.110
**OS:** Linux (6.8.0-106-generic)

## Обзор

На VPS настроены две системы долговременной памяти для Hermes Agent:

1. **[agentmemory](https://github.com/rohitg00/agentmemory)** (rohitg00/agentmemory, 18.5k⭐) — MCP-сервер на Node.js/TypeScript, 7-53 MCP-инструментов, 0 внешних БД.
2. **[GBrain](https://github.com/garrytan/gbrain)** (Garry Tan / YC CEO) — граф знаний, индексирует markdown-репозитории, синтезирует факты.

---

## 1. agentmemory (через iii-engine)

### Архитектура

```
agentmemory (npm) → MCP Server (@agentmemory/mcp) → iii-engine (демон localhost:3111)
```

- **Движок:** iii-engine (бинарник `/root/.local/bin/iii`, 33MB)
- **MCP-сервер:** `@agentmemory/mcp` (npx, 7 инструментов по умолчанию, 53 при `AGENTMEMORY_TOOLS=all`)
- **Хранилище:** File-based SQLite через StateModule (`data/state_store.db`)
- **Порт:** 3111 (HTTP)
- **Herram-конфиг:** `~/.hermes/config.yaml`

### MCP-инструменты (7 по умолчанию)

| Инструмент | Назначение |
|-----------|-----------|
| `memory_recall` | Поиск по сохранённым наблюдениям |
| `memory_save` | Сохранить важный факт вручную |
| `memory_sessions` | Список сессий |
| `memory_smart_search` | Гибридный семантический + keyword поиск |
| `memory_export` | Экспорт всей памяти JSON |
| `memory_audit` | Аудит операций памяти |
| `memory_governance_delete` | Удаление с аудит-трейлом |

### Установка

```bash
# iii-engine (установился через MCP сервер, Option 1)
# Бинарник: ~/.local/bin/iii

# MCP-сервер в config.yaml:
npx -y @agentmemory/mcp
```

### Статус

- ✅ iii-engine daemon работает (process iii)
- ✅ MCP-сервер подключён (hermes mcp list: agentmemory enabled)
- ❌ `agentmemory status`: Not running — это нормально, т.к. MCP-сервер использует iii-engine напрямую.

---

## 2. GBrain (граф знаний)

### Архитектура

```
gbrain (Bun/TypeScript) → PGLite (встроенная БД) → Embbeddings (OpenRouter)
```

- **Движок:** Bun / TypeScript (клон `/root/gbrain`)
- **Хранилище:** PGLite (встроенный PostgreSQL-совместимый движок, 0 внешних зависимостей)
- **Эмбеддинги:** `openrouter:openai/text-embedding-3-small` (через OPENROUTER_API_KEY)
- **Источник:** `~/Documents/wiki` (130 страниц, ~395 chunks)

### Что внутри

```bash
# После импорта:
gbrain status
#   Sync: default  130 pages  embed=100%
```

130 страниц wiki, все с эмбеддингами (100%).

### Режимы работы

**Ручной:**
```bash
gbrain search "запрос"                    # семантический поиск
gbrain dream                              # полный цикл синтеза
gbrain dream --source default             # синтез по одному источнику
gbrain graph-query --entity "UFW"         # запрос графа
gbrain pages list --all                   # все страницы
```

**Автоматический:**
```bash
gbrain autopilot --install               # установка systemd-сервиса
```

Autopilot запускает полный цикл: lint + backlinks + sync + extract + embed + orphans.
Интервал: 300 секунд (5 минут).

### systemd-сервис

```
gbrain-autopilot.service
  Status: active (running), enabled
  Лог: journalctl --user -u gbrain-autopilot.service
  Репозиторий: /root/Documents/wiki
```

---

## 3. Сравнение agentmemory vs GBrain

| Параметр | agentmemory | GBrain |
|---------|------------|--------|
| Тип | Ключ-значение + семантика | Граф знаний |
| Движок | iii-engine (Go-like бинарник) | PGLite (Bun/TypeScript) |
| Источник | Факты от агента | Markdown wiki |
| Автоматизация | Только вручную через MCP | Autopilot daemon |
| Поиск | Гибридный (keyword + semantic) | Semantic + Graph traversal |
| Инструментов | 7-53 MCP | 1 MCP (gbrain mcp) |
| Объём | Пока пусто | 130 страниц wiki |

---

## 4. Триггеры и автоматизация

### Что работает автоматически

| Компонент | Триггер | Описание |
|-----------|---------|----------|
| **MEMORY.md / USER.md** | Каждый turn | Читается в каждом моём ответе, пишется через `memory()` tool |
| **GBrain autopilot** | systemd timer (5 мин) | Sync → embed → extract → cleanup |
| **session_search** | По запросу агента | FTS5 по 32 сессиям (нужен явный вызов) |

### Что делается вручную (и можно автоматизировать)

| Операция | Ручная команда | Автоматизация |
|----------|---------------|---------------|
| Сохранить факт в agentmemory | agentmemory save / MCP tool | Авто-хуки (есть 12 встроенных) |
| Запустить dream cycle | `gbrain dream` | ✅ Autopilot уже работает |
| Поиск в agentmemory | `memory_recall` (MCP) | Встроено в MCP |
| Поиск в GBrain | `gbrain search` | Через MCP-сервер |
| Просмотр памяти | `cat ~/.hermes/memories/*` | Встроено в ответы агента |

### Когда что использовать

1. **MEMORY.md** — для конфигурации сервера, предпочтений пользователя, критических правил (никогда не ребутить сервер)
2. **agentmemory** — для фактов из диалогов, заметок о проектах, ссылок (семантический поиск)
3. **GBrain** — для структурированных знаний из wiki (граф связей, синтез, тренды)
4. **session_search** — когда нужно вспомнить детали конкретного разговора

---

## Связанные страницы

- [[tech/agent-memory-research-2026]] — Исследование решений для LTM агентов
- [[tech/gbrain-lossless-agent-memory]] — Обзор GBrain
- [[tech/agentmemory-vs-current]] — agentmemory vs старый стек
- [[tech/tencentdb-agent-memory]] — TencentDB Agent Memory
- [[tech/MemPalace-Hermes-Integration]] — MemPalace × Hermes (legacy)
