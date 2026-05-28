---
description: Sequential Thinking skill для Claude Code — пошаговые рассуждения
tags: [claude-code, skill, reasoning, thinking]
related: [[tech/caveman]]
---

# Sequential Thinking

**Plugin Hub:** https://www.claudepluginhub.com/plugins/nsheaps-sequential-thinking-plugins-sequential-thinking

Skill для Claude Code, который заставляет модель делать пошаговые рассуждения перед ответом.

## Фишка

Заставляет модель думать шаг за шагом — спасает слабые модели от тупиков, на сильных почти бесполезен.

## Эффективность

- **Со слабыми моделями (GLM-4.7, 2025):** практически всегда спасает от тупика
- **С современными сильными моделями:** почти бесполезен
- **В контексте SDD:** сценарии SDD-инструментария уже содержат необходимое структурирование, так что skill избыточен

## Установка

```bash
claude plugin marketplace add nsheaps/ai-mktpl
claude plugin install sequential-thinking@ai-mktpl
```

## Зачем

Автор статьи называет его «самым сомнительным пунктом в списке» и признаётся, что на современных моделях им практически не пользуется.

## Нужно ли

❌ **Нет.** SDD-инструментарий (OpenSpec, GSD, BMAD) уже включает структурирование, делающее Sequential Thinking избыточным. На сильных современных моделях — бесполезен.
