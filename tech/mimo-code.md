---
description: MiMo-Code — open-source AI coding agent от Xiaomi, форк OpenCode с persistent memory, goal/stop, subagent orchestration и self-improvement (dream/distill). Бесплатно (MIT), плата только за токены моделей.
tags: [tech, ai-coding, mimocode, xiaomi, opencode]
related: [[tech/opencode]] [[tech/hermes-agent-masterclass]]
---

# MiMo-Code

**Репозиторий:** [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)  
**Звёзд:** 4.4k ★ | **Форков:** 334 | **Лицензия:** MIT  
**Релиз:** 9 июня 2026 (Initial open-source)  
**Установка:** `npm install -g @mimo-ai/cli` или `curl -fsSL https://mimo.xiaomi.com/install | bash`

---

## Что это

AI coding agent от Xiaomi. Форк [OpenCode](https://github.com/anomalyco/opencode) с расширенными возможностями. Работает из терминала, поддерживает несколько LLM-провайдеров, умеет читать/писать код, запускать команды, управлять git.

---

## Цена

| Слой | Цена |
|------|------|
| **Инструмент** | Бесплатно — MIT, open source |
| **MiMo Auto** | Бесплатно на ограниченное время (встроенный канал, нулевая конфигурация) |
| **Xiaomi MiMo Platform** | OAuth-логин, та же поминутная оплата моделей |
| **Свой провайдер** | Любой OpenAI-совместимый API |

Сам инструмент **бесплатный**. Плата только за токены моделей при использовании Xiaomi MiMo API или через свой провайдер.

---

## Ключевые отличия от OpenCode

| Фича | OpenCode | MiMo-Code |
|------|----------|-----------|
| Persistent memory (cross-session) | Нет | ✅ SQLite FTS5 + checkpoints |
| `/goal` + независимый judge | Нет | ✅ Условие остановки |
| `/dream` (самоанализ → память) | Нет | ✅ |
| `/distill` (workflow → skills) | Нет | ✅ |
| Voice input | Нет | ✅ TenVAD + MiMo ASR |
| Compose mode (SDD workflow) | Нет | ✅ Plan → Code → Review → Merge |
| Subagent orchestration | Базовое | ✅ С жизненным циклом, cancel, background |

---

## Архитектура

### Агенты

| Агент | Описание |
|-------|----------|
| **build** | Default. Полный доступ к инструментам |
| **plan** | Read-only анализ кода и проектирование |
| **compose** | Specs-driven разработка (встроенный SDD-пайплайн) |

### Persistent Memory

SQLite FTS5 full-text search:
- **MEMORY.md** — знания проекта, правила, архитектурные решения
- **checkpoint.md** — слепки состояния между сессиями
- **notes.md** — временные заметки
- **tasks/`<id>`/progress.md** — прогресс по задачам

При возобновлении сессии память автоматически инжектится — агенту не нужно переучивать контекст.

### Goal / Stop Condition

Команда `/goal` задаёт условие завершения. Когда агент хочет остановиться, независимый judge-модель проверяет, действительно ли цель достигнута — предотвращает преждевременные остановки.

### Dream & Distill

- **`/dream`** — сканирует недавние сессии, извлекает persistent knowledge в MEMORY.md, удаляет устаревшие записи
- **`/distill`** — находит повторяющиеся ручные workflow и пакует их в переиспользуемые skills, subagents или команды

### Compose Mode

Встроенный SDD-like пайплайн: планирование → исполнение → код-ревью → TDD → дебаг → верификация → merge. Полный цикл от spec до зашипленного кода.

---

## Конфигурация

Файл: `.mimocode/mimocode.json` (в проекте) или `~/.config/mimocode/mimocode.json` (глобально)

Настройки: провайдер и модель, права агентов, checkpoint-и, MCP-серверы, keybindings, тема.

**Max Mode** — parallel best-of-N рассуждений с judge-выбором (через `experimental.maxMode`)

---

## Relevance

Для Романа, который уже использует Xiaomi MiMo модели через OpenCode Go:
- MiMo-Code может заменить OpenCode без изменения API-провайдера
- Persistent memory решает проблему потери контекста между сессиями
- Compose mode — аналог SDD/OpenSpec прямо в кодинг-агенте
- Бесплатно (инструмент), плата только за те же модели, что и сейчас
