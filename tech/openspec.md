---
title: "OpenSpec — Spec-Driven Development"
description: "Spec-driven workflow для AI-агентов: proposal → specs → design → tasks → validate → archive"
tags: [SDD, OpenSpec, spec-first, AI coding]
related: [[openspec-usage]], [[superpowers]], [[tech/sdd-orchestrator-v2]]
---

# OpenSpec

**Status:** Интегрирован в workspace | **Date:** 2026-05-03  
**Репозиторий:** [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)  
**NPM:** `npm install -g openspec`

## Концепция

Spec-driven development для AI-агентов. Вместо "пишу код как придётся" — сначала фиксируем требования, затем реализуем по чеклисту, в конце архивируем с мержащей specs.

Отличается от Specsmaxxing (Acai.sh) тем, что:
- Не требует нумерованных ACID-требований
- Валидация через RFC 2119 keywords (SHALL/MUST)
- Artifact-based workflow с явными dependencies
- Поддержка OpenCode, Claude Code, Cursor и др.

## Быстрый старт

```bash
# Инициализация
openspec init --tools opencode

# Создать change
openspec new change my-feature

# Генерация артефактов (в порядке зависимостей)
openspec instructions proposal --change my-feature   # template для proposal.md
openspec instructions specs --change my-feature     # template для spec.md
openspec instructions design --change my-feature     # template для design.md
openspec instructions tasks --change my-feature      # template для tasks.md

# Статус
openspec status --change my-feature

# Валидация
openspec validate my-feature

# Архивация (мерджит specs)
openspec archive my-feature --yes
```

## Artifact Pipeline

```
proposal ──► specs ──► design ──► tasks
   │           │          │          │
   ▼           ▼          ▼          ▼
Зачем?     Что?       Как?      Чеклист
```

- **proposal.md** — зачем это нужно, мотивация
- **spec.md** — что конкретно должно быть (RFC 2119: SHALL/MUST)
- **design.md** — как это будет устроено
- **tasks.md** — чеклист для выполнения

## Структура workspace

```
openspec/
├── config.yaml
├── specs/                        # мердженные specs из archive
│   └── <spec-name>/
│       └── spec.md
└── changes/
    ├── <active-change>/
    │   ├── .openspec.yaml
    │   ├── proposal.md
    │   ├── specs/<name>/spec.md
    │   ├── design.md
    │   └── tasks.md
    └── archive/
        └── <yyyy-mm-dd>-<change-name>/

.opencode/
├── commands/                     # 4 slash-команды
│   ├── opsx-apply.md
│   ├── opsx-archive.md
│   ├── opsx-explore.md
│   └── opsx-propose.md
└── skills/                      # 4 скилла
    ├── openspec-apply-change/
    ├── openspec-archive-change/
    ├── openspec-explore/
    └── openspec-propose/
```

## Команды

| Команда | Описание |
|---------|---------|
| `openspec init --tools opencode` | Инициализация |
| `openspec new change <name>` | Новый change |
| `openspec status --change <name>` | Прогресс артефактов |
| `openspec list` | Список active changes |
| `openspec instructions <artifact> --change <name>` | Template + deps |
| `openspec validate <name>` | Валидация (SHALL/MUST) |
| `openspec archive <name> --yes` | Архивировать + смерджить specs |
| `openspec show <name>` | Показать change |
| `openspec specs` | Все specs |

## ⚠️ Known Issues

### Валидация требует английского SHALL/MUST

Requirements в `spec.md` должны содержать **английские** ключевые слова `SHALL` или `MUST` (RFC 2119). Русские "ДОЛЖЕН" **НЕ** проходят валидацию.

❌ **Неправильно:**
```markdown
### Requirement: OpenSpec структура создаётся в workspace
OpenSpec CLI ДОЛЖЕН создавать директорию `openspec/`.
```

✅ **Правильно:**
```markdown
### Requirement: OpenSpec структура создаётся в workspace
The system SHALL create an `openspec/` directory with `config.yaml`.
```

### Scenario-формат

Scenario-часть можно оставлять на русском:
```markdown
#### Scenario: Успешная инициализация
- **WHEN** выполнена команда `openspec init --tools opencode`
- **THEN** создана директория `openspec/` с файлом `config.yaml`
```

## Интеграция с Оркестратором

OpenSpec можно использовать как spec-first этап:

1. Оркестратор: `openspec new change <project>-<task>`
2. Пишет proposal и specs с требованиями
3. Subagent-ы реализуют по tasks.md (через `/opsx-apply <name>`)
4. После завершения: `openspec archive <name> --yes`

## Links

- [GitHub](https://github.com/Fission-AI/OpenSpec)
- [Docs](https://fission-ai.github.io/OpenSpec)
- Specsmaxxing (вдохновение): [acai.sh](https://acai.sh/blog/specsmaxxing)
- Детальное руководство: [[openspec-usage]]
