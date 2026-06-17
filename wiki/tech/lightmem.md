---
description: LightMem — лёгкий и эффективный фреймворк управления памятью для LLM/агентов (ICLR 2026)
tags: [memory, agents, llm, mcp, iclr2026, removed]
related: [[tech/hermes-memory-setup-vps]] [[tech/agentmemory-vs-current]] [[tech/gbrain-lossless-agent-memory]]
status: removed
removed_at: 2026-05-30
removed_reason: Не даёт преимуществ перед уже установленными agentmemory + gbrain. Академическая поделка без автоматики и веб-морды.
---

# LightMem (удалён)

**GitHub:** https://github.com/zjunlp/LightMem
**Архив:** https://arxiv.org/abs/2510.18866
**Лицензия:** MIT
**Автор:** Zhejiang University (ZJU)

**LightMem** — фреймворк для управления долговременной памятью LLM/агентов, принятый на **ICLR 2026**.

## Статус: ❌ УДАЛЁН

LightMem был установлен, протестирован и **удалён 30.05.2026**.

**Причина:** LightMem делает только одно — хранит пары user↔assistant в векторной БД и ищет по ним. У Romana уже есть:
- **agentmemory** — автоматическая запись наблюдений, действий, уроков, инсайтов. Есть MCP + веб-дашборд.
- **gbrain** — вики/база знаний с автосинком, семантическим поиском, графом.

LightMem не умеет:
- Автоматически писать память — только ручной вызов `add_memory`
- Показывать что внутри — нет веб-интерфейса
- Дашборды/аналитику — только MCP инструменты

Исходный код и конфигурация удалены, пакет деинсталлирован.

## Архитектура (для справки)

LightMem — модульный фреймворк с MCP сервером на FastMCP:

```
LightMem/
├── src/lightmem/
│   ├── memory/lightmem.py    # Основной класс LightMemory
│   ├── configs/              # Конфигурации модулей
│   ├── factory/              # Фабрики компонентов
│   └── memory_toolkits/      # Инструменты для бенчмарков
├── mcp/server.py             # MCP сервер (FastMCP)
├── experiments/              # Скрипты для LoCoMo / LongMemEval
└── examples/                 # Примеры использования
```

### Модули

| Модуль | Назначение | Бэкенды |
|--------|-----------|---------|
| PreCompressor | Сжатие входных сообщений | llmlingua-2, entropy_compress |
| TopicSegmenter | Сегментация по темам | llmlingua-2 |
| MemoryManager | Генерация саммари и метаданных | openai, deepseek, ollama, vllm, transformers |
| TextEmbedder | Векторизация текста | huggingface |
| Retriever | Поиск релевантных воспоминаний | qdrant, BM25 |

### MCP инструменты

| Инструмент | Описание |
|-----------|----------|
| `add_memory` | Добавить пару user↔assistant в память |
| `retrieve_memory` | Найти релевантные воспоминания по запросу |
| `offline_update` | Обновить все записи (перезапись устаревших) |
| `get_timestamp` | Текущее время |

## Вердикт

- **Для Romana:** бесполезен. Всё что он делает — уже делают agentmemory и gbrain, но лучше и с UI.
- **Для кого может быть полезен:** команды, которые строят свою memory-систему с нуля и хотят гибкий фреймворк.
- **Известные проблемы (v0.1.0):** баг с `model_kwargs: None` в huggingface embedder, FAISS не поддерживается из коробки (только qdrant для эмбеддингов).

## Ссылки

- [[tech/hermes-memory-setup-vps]] — настройка памяти в Hermes
- [[tech/agentmemory-vs-current]] — сравнение memory провайдеров
- [[tech/context7]] — MCP сервер документации
