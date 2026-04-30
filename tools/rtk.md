# RTK — Rust Token Killer

> CLI-прокси для оптимизации вывода команд перед отправкой в LLM. Снижает потребление токенов на 60-90% на типичных dev-командах.

## Описание

RTK перехватывает вывод популярных команд (git, ls, cat, grep, cargo, npm и 100+ других) и обрезает всё лишнее — blank lines, excessive formatting, служебную информацию. Результат: вместо 2000 токенов → 200 токенов.

**Написано на Rust** — single binary, zero dependencies, <10ms overhead.

## Экономия токенов

| Команда             | Обычно | RTK   | Экономия |
|---------------------|--------|-------|----------|
| `git status`        | 3,000  | 600   | -80%     |
| `git add/commit/push` | 1,600 | 120   | **-92%** |
| `ls` / `tree`       | 2,000  | 400   | -80%     |
| `grep` / `rg`       | 16,000 | 3,200 | -80%     |
| `cat` / `read`      | 40,000 | 12,000| -70%     |
| `cargo test` / `npm test` | 25,000 | 5,000 | -80% |

## Установка

**Linux/macOS:**
```bash
curl -fsSL https://rtk.sh | bash
```

**Homebrew:**
```bash
brew install rtk
```

**Проверка:**
```bash
rtk --version
```

## Использование

Оборачиваем команды в `rtk`:
```bash
rtk git status
rtk git diff
rtk ls -la
rtk grep -r "pattern" .
```

Или через `rtkit` (alias):
```bash
rtkit git log --oneline -10
```

## Как работает

1. Команда выполняется как обычно
2. RTK перехватывает raw output
3. Применяет фильтры — убирает blank lines, краткое форматирование
4. Возвращает только essential info

## Принцип

Идея схожа с RLM (Remote Language Model) — популярные команды оборачиваются в оболочку, которая убирает всё лишнее из вывода. То что нужно человеку ИИ нафиг не сдалось.

## Статус

**Установить себе** — в очереди на установку (2026-04-30)

## Ссылки

- GitHub: https://github.com/rtk-ai/rtk
- Website: https://www.rtk-ai.app
- Discord: https://discord.gg/RySmvNF5kF
