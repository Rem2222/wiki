# MCP v8std — Стандарты разработки 1С для ИИ-помощников

**Сайт:** [v8std.ru/mcp](https://v8std.ru/mcp/)
**Репозиторий:** [github.com/zeegin/v8std](https://github.com/zeegin/v8std)

---

## Суть

MCP v8std — это подключение к базе стандартов v8std.ru из редактора кода с ИИ.
ИИ-помощник может сам обращаться к справочнику и находить нужный стандарт,
диагностику или связанный материал по фрагменту кода или текстовому запросу.

Сервис **не меняет код** и **не запускает проверки** — только возвращает материалы
сайта: стандарты, описания диагностик и связи между ними.

---

## Методы MCP

| Метод | Что делает |
|-------|-----------|
| `v8std_search` | Ищет стандарты, диагностики и материалы по фразе, номеру стандарта или коду диагностики |
| `v8std_get_page` | Возвращает полный текст страницы (сам стандарт или описание диагностики) |
| `v8std_get_related` | Показывает связанные страницы (стандарт ↔ диагностика) |
| `v8std_explain_snippet` | По фрагменту кода 1С подбирает применимые стандарты |
| `v8std_explain_diagnostics` | Объясняет список диагностик АПК, BSL Language Server и EDT |

### Примеры запросов

- "Найди стандарт про модальные окна в 1С"
- "Объясни диагностику bslls:UsingModalWindows"
- "Что означает acc:1245 и какой стандарт с ним связан?"
- "Какие стандарты относятся к локализации интерфейсных текстов?"
- "По этому фрагменту кода подбери применимые стандарты v8std"

---

## Подключение

### Публичный сервис (без ключа)

```
https://ai.v8std.ru/mcp
```

### Cursor

```json
// ~/.cursor/mcp.json
{
  "mcpServers": {
    "v8std": {
      "url": "https://ai.v8std.ru/mcp"
    }
  }
}
```

### Claude Code

```bash
claude mcp add --transport http v8std https://ai.v8std.ru/mcp
```

### Kiro

```json
// ~/.kiro/settings/mcp.json
{
  "mcpServers": {
    "v8std": {
      "url": "https://ai.v8std.ru/mcp"
    }
  }
}
```

### Antigravity

```json
// mcp_config.json
{
  "mcpServers": {
    "v8std": {
      "serverUrl": "https://ai.v8std.ru/mcp"
    }
  }
}
```

---

## Локальный запуск

Для закрытого кода, автономной работы или проверки изменений до публикации.

### Docker (рекомендуется)

```bash
git clone https://github.com/zeegin/v8std.git
cd v8std
docker compose -f docker-compose/docker-compose.yml up -d v8std-mcp

# Адрес MCP:
http://127.0.0.1:8765/mcp
```

### Без Docker

```bash
git clone https://github.com/zeegin/v8std.git
cd v8std

python3.12 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt -r requirements-mcp.txt
python scripts/generate_ai_artifacts.py
python scripts/generate_search_vectors.py

python scripts/v8std_mcp_server.py \
  --pages docs/ai/pages.jsonl \
  --vectors docs/ai/search-vectors.jsonl \
  --host 127.0.0.1 \
  --port 8765
```

Требования: Python 3.12, Zensical (устанавливается из PyPI).

---

## Диагностики и их коды

MCP понимает коды диагностик из трёх источников:

| Источник | Префикс | Пример |
|----------|---------|--------|
| АПК (1С) | `acc:` | `acc:1245` |
| BSL Language Server | `bslls:` | `bslls:UsingModalWindows` |
| EDT | `acc:` | `acc:1245` |

Метод `v8std_explain_diagnostics` группирует предупреждения и показывает
описание диагностики + пункт стандарта, который объясняет причину.

---

## Безопасность

Публичный MCP **видит текст запросов**. Не передавайте туда:
- закрытые фрагменты кода
- коммерческие данные
- сведения из непубличных проектов

Для таких сценариев — локальный запуск (см. выше).

---

## Интеграция с OpenClaw

Для подключения к OpenClaw нужно добавить v8std как MCP-сервер:

```json
{
  "mcpServers": {
    "v8std": {
      "url": "https://ai.v8std.ru/mcp"
    }
  }
}
```

Или локально:
```json
{
  "mcpServers": {
    "v8std-local": {
      "url": "http://127.0.0.1:8765/mcp"
    }
  }
}
```

После подключения ИИ-ассистент автоматически использует методы v8std
при работе с кодом 1С.

---

## Полезные ссылки

- [v8std.ru/mcp](https://v8std.ru/mcp/) — документация MCP
- [v8std.ru/support](https://v8std.ru/support/) — локальный запуск
- [github.com/zeegin/v8std](https://github.com/zeegin/v8std) — репозиторий
- [v8std.ru/diagnostics](https://v8std.ru/diagnostics/) — диагностики
- [v8std.ru/lang](https://v8std.ru/lang/) — стандарты

---

*Добавлено: 2026-04-29*