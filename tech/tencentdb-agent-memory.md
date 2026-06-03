---
description: Полностью локальная система долговременной памяти для AI-агентов, без внешних API-зависимостей.
tags: [tech]
---

# tencentdb-agent-memory

**Репозиторий:** https://github.com/Tencent/TencentDB-Agent-Memory
**Лицензия:** MIT
**Автор:** Tencent (腾讯)
**Дата:** Май 2026 (v0.3.4, 58 коммитов, 2k звезд)

## Суть

Полностью локальная система долговременной памяти для AI-агентов, без внешних API-зависимостей.

## Архитектура

### 1. Memory Layering — семантическая пирамида L0–L3

| Уровень | Что хранит | Хранилище |
|:--|:--|:--|
| **L0 — Conversation** | Сырые диалоги | SQLite |
| **L1 — Atom** | Атомарные факты | SQLite |
| **L2 — Scenario** | Сцены/ситуации | Markdown |
| **L3 — Persona** | Профиль пользователя | Markdown |

Принцип: нижние слои = доказательства, верхние = структура. Полная цепочка: Persona → Scenario → Atom → Conversation.

### 2. Symbolic Memory — контекстная компрессия

- Тяжёлые логи выгружаются во внешние файлы (`refs/*.md`)
- В контексте остаётся Mermaid-диаграмма с `node_id`
- При необходимости агент обращается к полному тексту по `node_id`

## Бенчмарки

| Бенчмарк | Успех (до/после) | Токены (до/после) |
|:--|:--:|:--:|
| WideSearch | 33% → **50%** (+51%) | 221M → **85M** (-61%) |
| SWE-bench | 58.4% → **64.2%** (+10%) | 3474M → **2375M** (-33%) |
| PersonaMem | 48% → **76%** (+59%) | — |

## Интеграции

- **OpenClaw plugin** — `openclaw plugins install @tencentdb-agent-memory/memory-tencentdb`
- **Hermes Gateway** — есть адаптер + Docker-образ
- **Бэкенды**: SQLite + sqlite-vec (из коробки), Tencent Cloud Vector Database
- **Retrieval**: BM25 + векторный + RRF-фузия (hybrid)

## Особенности

- White-box debugging — все промежуточные данные читаемые файлы
- Контекстная компрессия: mild при 50% контекста, aggressive при 85%
- Три уровня конфигурации (базовый / продвинутый / полный)
- Полная прослеживаемость без необратимой компрессии

## Конфигурация

Базовый минимум (OpenClaw):
```json
{
  "memory-tencentdb": {
    "enabled": true
  }
}
```

## Статус

❓ На study, требуется тестирование и оценка применимости к текущему стеку (Hermes Agent + OpenClaw + MemPalace + ByteRover).

## Ссылки

- [GitHub](https://github.com/Tencent/TencentDB-Agent-Memory)
- [NPM](https://www.npmjs.com/package/@tencentdb-agent-memory/memory-tencentdb)
- [Discord](https://discord.gg/kDtHb5RW2)