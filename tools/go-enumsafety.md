---
description: Go-линтер для безопасной работы с enum (sum types) в Go
tags: [go, linter, enum, safety]
related: [[tech/go-skills-claude-code]]
---

# go-enumsafety

**GitHub:** https://github.com/Djarvur/go-enumsafety

Линтер для Go, который автор статьи написал с помощью Spec-Kit и AI за несколько вечеров. Задача: сделать enum-подобные типы в Go типобезопасными.

## Фишка

«Без Spec-Kit писал бы пару месяцев, а без AI не написал бы никогда» — показательный пример эффективности SDD.

## Нужно ли

✅ **Если пишешь на Go** и используешь enum-паттерны (iota) — может быть полезен.
