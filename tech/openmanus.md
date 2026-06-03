---
description: OpenManus — open-source фреймворк-агент (MIT) от команды MetaGPT. Не LLM и не Ollama, а агент-фреймворк, аналогичный Hermes Agent.
tags: [tech]
---

# OpenManus

## Что это

OpenManus — open-source фреймворк-агент (MIT) от команды MetaGPT. **Не LLM и не Ollama**, а агент-фреймворк, аналогичный Hermes Agent.

GitHub: [FoundationAgents/OpenManus](https://github.com/FoundationAgents/OpenManus) — 56k ★

## Архитектура

```
OpenManus (фреймворк-агент)
    ├── LLM провайдеры (на выбор):
    │   ├── OpenAI API → gpt-4o, etc.
    │   ├── Anthropic API → claaude-3-7-sonnet, etc.
    │   ├── Ollama (локальный!) → llama3.2, qwen, etc.
    │   ├── Azure, Bedrock, JiekouAI...
    │
    └── Инструменты:
        ├── bash (shell-команды)
        ├── python (выполнение кода)
        ├── browser (playwright)
        └── web_search (Google/DuckDuckGo/Bing)
```

## Режимы запуска

| Файл | Режим | Описание |
|------|-------|---------|
| `main.py` | Интерактивный | CLI-терминал, печатаешь задачу → агент делает |
| `run_mcp.py` | MCP-сервер | Подключение по SSE/stdio как MCP tool provider |
| `run_flow.py` | Мультиагентный | Несколько агентов вместе на задачу |

## Установка (uv, рекомендуется)

```bash
## 1. uv
curl -LsSf https://astral.sh/uv/install.sh | sh

## 2. Клонировать
git clone https://github.com/FoundationAgents/OpenManus.git
cd OpenManus

## 3. Виртуалка
uv venv --python 3.12
source .venv/bin/activate

## 4. Зависимости
uv pip install -r requirements.txt

## 5. Конфиг
cp config/config.example.toml config/config.toml
## редактировать config.toml — добавить API ключ

## 6. Опционально (браузерная автоматизация)
playwright install

## 7. Запуск
python main.py
```

## Конфиг (config.toml)

Поддерживает множество LLM провайдеров:

```toml
## OpenAI
[llm]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."

## Anthropic
[llm]
model = "claude-3-7-sonnet-20250219"
base_url = "https://api.anthropic.com/v1/"
api_key = "sk-ant-..."

## Ollama (локально, бесплатно)
[llm]
api_type = 'ollama'
model = "llama3.2"
base_url = "http://localhost:11434/v1"
api_key = "ollama"
```

## Сравнение с Hermes Agent

| | OpenManus | Hermes Agent |
|--|-----------|--------------|
| Назначение | Агент-фреймворк | Агент-платформа |
| LLM | Любой (API/Ollama) | Настраивается |
| Инструменты | bash, python, browser, search | bash, python, browser, search, MCP, etc. |
| Память | Нет | ✅ (MemPalace, ByteRover) |
| Telegram | ❌ | ✅ |
| Cron jobs | ❌ | ✅ |
| Скиллы | ❌ | ✅ |
| MCP-режим | ✅ (run_mcp.py) | ✅ |
| Мультиагент | ✅ (run_flow.py) | ❌ (частично через delegation) |
| Графики | ✅ (DataAnalysis Agent) | ❌ |

## Вывод для Романа

Практически не нужен — Hermes Agent уже закрывает все те же задачи, плюс имеет память, Telegram, cron, скиллы.

Возможные сценарии использования:
- Эксперименты с другими LLM без переключения Hermes
- Мультиагентный режим (несколько агентов на задачу)
- DataAnalysis Agent с визуализацией данных
- Изучение архитектуры агентов

**Вердикт:** скорее "поиграться", чем практическая необходимость.

## Links

- [GitHub](https://github.com/FoundationAgents/OpenManus)
- [HuggingFace Demo](https://huggingface.co/spaces/lyh-917/OpenManusDemo)
- [OpenManus-RL](https://github.com/OpenManus/OpenManus-RL) — RL-тюнинг агентов (для разработчиков)
