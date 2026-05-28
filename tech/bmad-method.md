---
description: SDD-фреймворк «Build More Architect Dreams» — архитектура прежде всего
tags: [sdd, framework, architecture, specification]
related: [[concepts/sdd]] [[tech/gsd]] [[tech/openspec]] [[wiki/tech/spec-kit]]
---

# BMAD-METHOD

**GitHub:** https://github.com/bmad-code-org/BMAD-METHOD

Spec-Driven Development фреймворк. Философия: **«Architecture First»**.

## Фишка

Лучшая архитектурная проработка — задаёт вопросы не только про «как», но и про «что надо сделать». Исследует тему по собственной инициативе.

## Особенности

- **Архитектура прежде всего** — exhaustive SDD до написания кода
- **Работа с неясными идеями** — задаёт вопросы, анализирует ответы, возвращается к противоречиям
- **Развитые исследовательские сценарии** — сам проводит дополнительное исследование темы
- **Phased SDD:** Context & Constraints, High-Level Architecture, Data Models, Component Design, Sequence Diagrams, API Contracts

## Минусы

- **Медленный старт** — долгий путь от описания до реализации
- **Неочевидное обновление спецификации** — не вполне внятный сценарий модификации

## Установка

```bash
claude plugin add bmad-code-org/BMAD-METHOD
```

Per-project.

## Когда выбирать

✅ **Когда пока не знаешь, как реализовать идею** — хочешь сформулировать её в архитектурных документах, прежде чем писать код.
❌ Простые/понятные задачи — оверхед не оправдан.
