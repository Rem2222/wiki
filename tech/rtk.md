---
description: CLI-прокси на Rust, который перехватывает вывод shell-команд и сжимает его перед отправкой в контекст LLM. Экономит 60–90% токенов на типовых dev-командах.
tags: [tech]
---

# rtk

**Ссылки:** [GitHub](https://github.com/rtk-ai/rtk) | [Сайт](https://www.rtk-ai.app) | [Discord](https://discord.gg/RySmvNF5kF)

**47.9k ★ на GitHub** (на май 2026). Apache 2.0.

---

## Что это

CLI-прокси на Rust, который перехватывает вывод shell-команд и сжимает его перед отправкой в контекст LLM. Экономит **60–90% токенов** на типовых dev-командах.

Поддерживает: Claude Code, Copilot, Cursor, Codex, Gemini CLI, Windsurf, Cline, **Hermes** и др.

## Как работает

```
Без RTK: AI-агент -> git status -> shell -> ~2000 токенов (сырой вывод)
С RTK:   AI-агент -> git status -> RTK -> фильтр -> ~200 токенов
```

4 стратегии:
1. **Smart Filtering** — убирает шум (комментарии, пустые строки, boilerplate)
2. **Grouping** — группирует похожие элементы (файлы по папкам, ошибки по типу)
3. **Truncation** — оставляет релевантное, режет избыточность
4. **Deduplication** — схлопывает повторяющиеся строки с счётчиком

## Установка

```bash
## Homebrew (macOS)
brew install rtk

## Linux
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh

## Cargo
cargo install --git https://github.com/rtk-ai/rtk
```

## Подключение к Hermes

```bash
rtk init --agent hermes
```

После этого shell-вывод автоматически проходит через RTK.

## Примеры экономии (30-минутная сессия Claude Code)

| Операция | Было | Стало | Экономия |
|----------|------|-------|----------|
| `ls` / `tree` | 2000 | 400 | -80% |
| `cat` / `read` | 40000 | 12000 | -70% |
| `grep` / `rg` | 16000 | 3200 | -80% |
| `git diff` | 10000 | 2500 | -75% |
| `cargo test` / `npm test` | 25000 | 2500 | -90% |
| **Итого** | **~118,000** | **~23,900** | **-80%** |

## Аналитика

```bash
rtk gain              # статистика экономии
rtk gain --graph      # ASCII-график за 30 дней
rtk gain --history    # история команд
rtk discover          # найти упущенные возможности оптимизации
```

## Поддерживаемые команды

- **Файлы:** `rtk ls`, `rtk read`, `rtk find`, `rtk grep`, `rtk diff`
- **Git:** `rtk git status/log/diff/add/commit/push/pull`
- **GitHub CLI:** `rtk gh pr list/view`, `rtk gh issue list`
- **Тесты:** `rtk pytest/go test/cargo test/jest/vitest/playwright`
- **Линтеры:** `rtk lint/tsc/cargo clippy/ruff/golangci-lint`
- **Docker/K8s:** `rtk docker ps/logs/images`, `rtk kubectl pods/logs`
- **AWS:** `rtk aws sts/ec2/lambda/logs/s3`
- **Пакеты:** `rtk pip list/pnpm list/cargo build`
- **Данные:** `rtk json/log/curl/wget/summary`

Отдельно — `rtk err <cmd>` (показать только ошибки) и `rtk test <cmd>` (только падения тестов).