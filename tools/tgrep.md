---
title: tgrep
type: tool
source: https://github.com/microsoft/tgrep
date: 2026-09-07
tags: [search, code, rust, microsoft, grep]
---

# tgrep

Trigram-индексированный grep с клиент-серверной архитектурой от Microsoft.

## Зачем

Обычные grep/ripgrep сканируют все файлы каждый раз — O(total bytes) на запрос. В монорепозитории на 100K+ файлов это больно. tgrep предварительно строит trigram-индекс, чтобы поиск затрагивал только потенциально подходящие файлы.

## Бенчмарки

| Репо | Файлов | macOS arm64 | Windows | Linux |
|------|--------|-------------|---------|-------|
| gecko-dev | 388K | **51.9x** быстрее rg | 38.6x | 7.36x |
| chromium | 504K | 15.8x | 17.6x | — |

## Особенности

- Написан на Rust, открытый исходный код (MIT)
- Клиент-серверный режим: запустил сервер один раз — индекс готов
- Отслеживание изменений файлов (file watcher)
- Уже интегрирован в GitHub Copilot CLI

## Установка

```bash
# Cargo
cargo install tgrep

# Или собрать из исходников
git clone https://github.com/microsoft/tgrep
cd tgrep && cargo build --release
```

## Использование

```bash
# Индексировать проект
tgrep index .

# Искать
tgrep search "pattern"

# Клиент-серверный режим
tgrep server --port 9999 &
tgrep search --server localhost:9999 "pattern"
```

## Когда использовать

- Монорепозитории >10K файлов
- Частый поиск по коду (code navigation)
- Как замена ripgrep для статических проектов

## Связано

- [[codegraph]] — граф зависимостей (tgrep для быстрого grep, codegraph для анализа)
- [[deepseek_harness]] — DSH может использовать для навигации по коду
