---
title: "SDD: Pre-commit hook для OpenSpec"
description: "Git pre-commit hook валидирует spec.md на SHALL/MUST"
tags: [SDD, OpenSpec, git, pre-commit]
related: [[openspec]], [[openspec-usage]], [[sdd-openspec-orchestrator]]
---

# SDD: Pre-commit Hook для OpenSpec

**Sub-task:** REM-197  
**Status:** Draft  
**Author:** Romul  
**Date:** 2026-05-03

---

## 1. Why (Зачем)

Сейчас можно написать spec.md без SHALL/MUST, и `openspec validate` об этом скажет только после. Pre-commit hook позволяет поймать проблему **до** коммита — на этапе когда разработчик ещё в контексте.

Это behavioral enforcement: нельзя закоммитить невалидный spec. Аналог pre-commit hooks для линтеров (ESLint, Ruff и т.д.).

---

## 2. Scope

**Входит:**
- Git hook в `.git/hooks/pre-commit`
- Проверка изменённых spec.md на SHALL/MUST
- Сообщение об ошибке с подсказкой

**Не входит:**
- Установщик (install script) — это отдельная задача
- CI/CD integration
- Хуки для других файлов (только spec.md)

---

## 3. Requirements

### 3.1 Hook срабатывает на spec.md

When `git commit` is run, the hook SHALL check all staged `spec.md` files for RFC 2119 keywords.

```bash
# Проверяемые keywords
SHALL
MUST
SHOULD
MAY
```

Если файл `spec.md` изменён но не содержит ни одного keyword → коммит отклоняется.

### 3.2 Формат ошибки

При отклонении hook SHALL output:

```
❌ spec.md: Requirements must contain SHALL/MUST/SHOULD/MAY (RFC 2119)
  
  File: openspec/changes/my-feature/specs/my-feature/spec.md
  Fix: Add SHALL or MUST to each requirement
  
  Example:
    ### Requirement: Feature does X
    The system SHALL do X when condition Y occurs.
  
  Commit ABORTED.
```

### 3.3 Не блокирует другие файлы

The hook SHALL NOT block commits that don't touch spec.md files.

Example:
```bash
# Эти коммиты НЕ вызывают проверку
git commit -m "fix: typo in code"
git commit -m "refactor: extract method"

# Эти вызывают
git commit -m "docs: update spec"    # только если spec.md изменён
git commit -m "feat: new feature"   # только если spec.md изменён
```

### 3.4 Установка

The hook SHALL be installable via a script or manual copy.

```bash
# Manual
cp pre-commit-hook.sh /home/rem/JAWL/.git/hooks/pre-commit
chmod +x /home/rem/JAWL/.git/hooks/pre-commit

# Или через install script
./install-precommit-hook.sh /path/to/project
```

---

## 4. Implementation

### 4.1 Hook Script

```bash
#!/bin/bash
# pre-commit-hook.sh — OpenSpec RFC 2119 validator

echo "🔍 Checking spec.md files for RFC 2119 keywords..."

# Найти все staged spec.md
spec_files=$(git diff --cached --name-only | grep 'spec\.md$')

if [ -z "$spec_files" ]; then
    echo "✅ No spec.md changes, skipping validation"
    exit 0
fi

errors=0
while IFS= read -r file; do
    # Проверить наличие SHALL/MUST/SHOULD/MAY
    if ! grep -qE '\b(SHALL|MUST|SHOULD|MAY)\b' "$file"; then
        echo ""
        echo "❌ $file: Requirements must contain SHALL/MUST/SHOULD/MAY (RFC 2119)"
        echo ""
        echo "   Fix: Add SHALL or MUST to each requirement."
        echo ""
        echo "   Example:"
        echo "     ### Requirement: Feature does X"
        echo "     The system SHALL do X when condition Y occurs."
        echo ""
        errors=$((errors + 1))
    fi
done <<< "$spec_files"

if [ "$errors" -gt 0 ]; then
    echo ""
    echo "Commit ABORTED — $errors spec.md file(s) without RFC 2119 keywords."
    exit 1
fi

echo "✅ All spec.md files contain RFC 2119 keywords"
exit 0
```

### 4.2 Проверка OpenSpec validate

Alternatively, use `openspec validate` directly:

```bash
#!/bin/bash

changes=$(git diff --cached --name-only | grep 'openspec/changes/' | cut -d/ -f4 | sort -u)

if [ -z "$changes" ]; then
    exit 0
fi

echo "🔍 Validating OpenSpec changes..."
errors=0
for change in $changes; do
    result=$(openspec validate "$change" 2>&1)
    if echo "$result" | grep -q "is valid"; then
        echo "  ✅ $change"
    else
        echo "  ❌ $change"
        echo "$result" | sed 's/^/    /'
        errors=$((errors + 1))
    fi
done

if [ "$errors" -gt 0 ]; then
    echo "Commit ABORTED — $errors invalid OpenSpec change(s)."
    exit 1
fi
```

**Рекомендация:** Использовать вариант 2 (через `openspec validate`) — он полнее и использует существующий CLI.

---

## 5. Acceptance Criteria

- [ ] Hook установлен в `.git/hooks/pre-commit`
- [ ] Коммит spec.md без SHALL → отклонён
- [ ] Коммит spec.md с SHALL → принят
- [ ] Коммит без spec.md → принят без проверки
- [ ] Сообщение об ошибке содержит подсказку
- [ ] Протестировано:故意но сломанный spec → отклонён

---

## 6. Installation Notes

**Важно:** `.git/hooks/` не коммитится в репозиторий. Hook нужно:
1. Положить в workspace (напр. `.openclaw/hooks/pre-commit`)
2. Создать симлинк или скрипт-копировальщик
3. Документировать установку в README

**Для JAWL:** Hook ставить в `/home/rem/JAWL/.git/hooks/pre-commit`
**Для workspace:** Hook ставить в `~/.openclaw/workspace/.git/hooks/pre-commit`
