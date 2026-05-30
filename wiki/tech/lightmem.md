---
description: LightMem — лёгкий и эффективный фреймворк управления памятью для LLM/агентов (ICLR 2026)
tags: [memory, agents, llm, mcp, iclr2026]
related: [[tech/hermes-memory-setup-vps]] [[tech/agentmemory-vs-current]] [[tech/tencentdb-agent-memory]] [[wiki/tech/context7]]
---

# LightMem

**GitHub:** https://github.com/zjunlp/LightMem
**Архив:** https://arxiv.org/abs/2510.18866
**Лицензия:** MIT
**Звёзды:** 886+
**Автор:** Zhejiang University (ZJU)

**LightMem** — фреймворк для управления долговременной памятью LLM/агентов, принятый на **ICLR 2026**. Лёгкий, модульный, с MCP-сервером.

## Фишка

Модульная архитектура + MCP сервер из коробки. Поддерживает OpenAI, DeepSeek, Ollama, vLLM. Использует Qdrant/FAISS для векторного поиска.

## Архитектура

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
| Retriever | Поиск релевантных воспоминаний | qdrant, FAISS, BM25 |

## MCP сервер

LightMem предоставляет MCP сервер на FastMCP. Инструменты:

| Инструмент | Описание |
|-----------|----------|
| `add_memory` | Добавить пару user↔assistant в память |
| `retrieve_memory` | Найти релевантные воспоминания по запросу |
| `offline_update` | Обновить все записи (перезапись устаревших) |
| `show_lightmem_instance` | Статус инстанса и конфигурация |
| `get_timestamp` | Текущее время |

## Установка

```bash
git clone https://github.com/zjunlp/LightMem.git
cd LightMem
pip install -e .
pip install '.[mcp]'  # для MCP сервера
```

## MCP конфиг для Hermes

```yaml
mcp_servers:
  lightmem:
    command: python
    args: ["/path/to/LightMem/mcp/server.py", "--config", "/path/to/config.json"]
```

## Бенчмарки

LightMem значительно легче аналогов:

| Метод | Токены Total (k) ↓ | Runtime total (s) ↓ | ACC (%) |
|-------|-------------------|---------------------|---------|
| **LightMem** | **~2,870** | **~24,220** | **58.25%** |
| A-MEM | 21,664 | 67,084 | 64.16% |
| Mem0 | 25,793 | 120,175 | 36.49% |
| FullText | 54,884 | 6,971 | 73.83% |

Данные: LoCoMo, backbone gpt-4o-mini, judge gpt-4o-mini.

## Поддерживаемые LLM

- OpenAI (gpt-4o-mini и др.)
- DeepSeek (deepseek-v4-flash, deepseek-v4-pro)
- Ollama (локальные модели)
- vLLM (локальный inference)
- Transformers (HuggingFace)

## Ссылки

- [[tech/hermes-memory-setup-vps]] — настройка памяти в Hermes
- [[tech/agentmemory-vs-current]] — сравнение memory провайдеров
- [[wiki/tech/context7]] — MCP сервер документации
