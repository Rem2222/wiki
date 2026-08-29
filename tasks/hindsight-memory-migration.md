---
description: "Переезд памяти Hermes: agentmemory → Hindsight + разбор GBrain (задача)"
tags: [hindsight,migration,memory,gbrain,tasks]
---

# Переезд памяти Hermes: agentmemory → Hindsight (+ разбор GBrain)

## Контекст

Роман считает текущий стек памяти Hermes неоптимальным:
- **agentmemory** нестабилен (Node-движок iii зависает, heap растёт, приходится восстанавливать из копии; стоит костыль-таймер рестарта 4h).
- MEMORY.md / USER.md переполнены (см. MUL-713).
- **GBrain** тяжёлый, постоянно падает, фактически используется только как семантический индекс вики.
- Нет многослойности (факты/паттерны/уроки/логи раздельно) и авто-retrieve перед запросом.

## Решение (предварительное, согласовано с Романом 20.08.2026)

**Выбран провайдер: Hindsight** (vectorize-io/hindsight, 20.7k⭐, Python).
- Хранение: PostgreSQL (уже есть на VPS), локальный daemon.
- Авто-recall перед turn + авто-retain после turn (pre_llm_call / post_llm_call hooks).
- Точность recall 91.4% (LongMemEval) — лучшая.
- Совместим с локальной Ollama (bge-m3 для эмбеддингов, qwen2.5:7b / gemma3:12b для LLM) — полностью локальный режим.
- Распределённость: единый сервер на VPS, Windows-агент и внешние агенты подключаются через REST/MCP/SDK по сети.

## Объём работ

### 1. Развёртывание Hindsight на VPS
- Docker (или локальный daemon) с PostgreSQL, внешний хранилище-эндпоинт наружу (порт 8888) + защита.
- Готовый конфиг-образец: `applications/hermes-memory/configs/hermes-local-ollama.example.json` (mode: local, llm_provider: ollama, autoRecall: true, autoRetain: true, memory_mode: hybrid).
- Настройка memory.provider: hindsight в Hermes.

### 2. Бэкфилл данных из state.db
- Источник истории — только **state.db** (895 сессий, ~34k сообщений; файловых сессий нет, verified).
- Скрипт: читать state.db → нарезать на транши → `client.retain(bank_id, content, context, timestamp)` с реальными датами → Hindsight сам построит факты/сущности/связи/уроки и временную шкалу.
- НЕ тянуть старый мусор фактов из agentmemory — история через retain покроет.
- Эмбеддинги bge-m3: ~11 мин на 33k бэтчами (проверено на живом VPS).

### 3. Вики и GBrain
- Вики остаётся базой знаний на ФС (Markdown + Obsidian), НЕ переносится.
- GBrain заменить на лёгкий векторный индекс **Zvec** (Alibaba, 13.8k⭐, pip install, hybrid vec+FTS) для семантического поиска по вики.
- Скрипт очистки вики: убрать лишние слои (.openclaw-wiki, graphify-out), оставить Obsidian-структуру.

### 4. Правила памяти (после переезда)
- Обсудить и зафиксировать правила для MEMORY.md/USER.md: что писать в оперативную, авто-retrieve, консолидация.

## Не делать / Ограничения
- НЕ удалять state.db и agentmemory до полного успешного переноса и согласования.
- НЕ менять конфиг gateway напрямую ДО утверждения плана.
- Сквозная распределённая память VPS↔Windows — отдельный этап (после локального развёртывания).

## Статус
Планирование. НЕ запускать на выполнение до явного «угу» Романа.
