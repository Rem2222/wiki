---
description: Набор Go-плагинов для расширения Claude Code в экосистеме Go
tags: [go, claude-code, skills, guidelines]
related: [[tech/gopilot]] [[tools/go-enumsafety]]
---

# Go Skill Set для Claude Code

Набор плагинов, которые автор статьи использует для работы с Go. Он ещё не определился, какой лучше, поэтому пробует все.

## modern-go-guidelines

**GitHub:** https://github.com/JetBrains/go-modern-guidelines

Go-рекомендации от JetBrains — стиль, идиомы, best practices современного Go.

## cc-skills-golang

**GitHub:** https://github.com/samber/cc-skills-golang

Набор skills для Claude Code с Go-специфичными знаниями: типы, паттерны, stdlib особенности.

## go-best-practices

**GitHub:** https://github.com/danicat/skills/tree/main/go-best-practices

Go best practices (создан для Gemini, ставится руками).

## Установка

```bash
# modern-go-guidelines — стандартный claude plugin
claude plugin install modern-go-guidelines

# cc-skills-golang
claude plugin install cc-skills-golang

# go-best-practices — руками в .claude/skills/
```

## Нужно ли

✅ **Если ты пишешь на Go** — хотя бы один из них стоит попробовать. Автор пока не выбрал, какой лучше.
