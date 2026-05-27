---
description: SDD-фреймворк «Get Shit Done» — интервью-ориентированный подход к SDD
tags: [sdd, framework, specification, claude-code]
related: [[concepts/sdd]] [[tech/bmad-method]] [[tech/openspec]] [[wiki/tech/spec-kit]]
---

# GSD — Get Shit Done

**GitHub (Redux/активный):** https://github.com/open-gsd/get-shit-done-redux
**GitHub (оригинал):** https://github.com/gsd-build/get-shit-done

Spec-Driven Development фреймворк. Философия: **«сложность в системе, а не в твоём workflow»**.

## Фишка

Самый внятный процесс интервью: GSD задаёт вопросы → ты отвечаешь → на выходе готовая спецификация.

## Особенности

- **Интервью для прояснения задачи** — задаёт вопросы, вы отвечаете → получается точное описание
- **Лучшая декомпозиция** — разбиение на этапы практически не требует правок
- **Проверка спецификации** на внутреннюю непротиворечивость и полноту

## Минусы

- **Утомительное интервью** — робот задаёт «тупые» вопросы, процесс длинный
- **Сложно читать документы** — специфический формат и система перекрёстных ссылок
- **Требует постоянного внимания** — GSD может встать в ожидании ответа в любой момент

## Оригинал vs Redux

| | Оригинал (gsd-build) | Redux (open-gsd) |
|---|---|---|
| Язык | Bash | TypeScript/Node.js |
| AI-таргет | Claude (Anthropic) | AI-agnostic |
| Архитектура | Монолитные промпты | Федеративные агенты (Explorer, Designer, Developer, Reviewer) |
| Состояние | Эфемерно | Persistent `.sdd/` с build cache |
| Лицензия | Restrictive | Open-source |

## Установка

Per-project. Для нового проекта — через `claude plugin`:

```bash
claude plugin add open-gsd/get-shit-done-redux
```

## Когда выбирать

✅ **Большая и технически сложная задача**, которую надо доформулировать и доформализовать в процессе.
❌ Простые задачи — интервью будет too much.
