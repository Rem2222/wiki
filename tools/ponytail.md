---
title: Ponytail — «ленивый старший разработчик» для AI-агентов (правила минимума кода)
description: "Плагин-правила Ponytail (DietrichGebert/ponytail, MIT): минимум работающего кода, stdlib вместо зависимостей; 20 агентов включая Hermes и OpenClaw. Не установлен — сканер Hermes дал ложный DANGEROUS."
tags: [tools, agents, rules, plugin]
updated: 2026-10-03
related:
  - tools/openclawfice
  - llm/bench-prompts
---

# Ponytail

**Статус:** ⛔ **не установлен** (решение Романа, 03.10.2026). Ссылка сохранена на будущее.

- Сайт: <https://ponytail.dev/>
- Репозиторий: <https://github.com/DietrichGebert/ponytail> (MIT, версия 4.10.3)
- Источник: пересылка от AVK, 03.10.2026 — «работает во всех агентах»

## Что это

Правила/плагин, который заставляет агента писать **минимум работающего кода**:
stdlib вместо кастомного, нативное вместо зависимостей, одна строка вместо пятидесяти.

Заявляемый результат по их же бенчу: **−54% кода** при **100%** по метрике
безопасности (примеры: date picker 404 → 23 строки, color picker 287 → 23).

## Режимы и команды

- `/ponytail lite|full|ultra|off` — интенсивность:
  - `lite` (дефолт) — строит как просили, но называет более ленивую альтернативу одной строкой
  - `full` — «лестница» принудительно: stdlib/native, кратчайший diff и объяснение
  - `ultra` — YAGNI-экстремист, оспаривает сам таск («лучший код — код, который не написан»)
- `/ponytail-review` — искать over-engineering в текущем diff
- `/ponytail-audit` — скан репозитория на раздутое
- `/ponytail-debt` — отложенные шорты в ledger, `/ponytail-gain` — таблица бенчей

## Установка (если решим вернуться)

- **Hermes:** `hermes plugins install DietrichGebert/ponytail --enable` + рестарт гейтвея
  (инжектит режим перед каждым LLM-ходом через хуки `pre_llm_call` / `pre_gateway_dispatch`,
  регистрирует скиллы `ponytail:<skill>`)
- **OpenClaw:** `clawhub install ponytail`
- Ещё Claude Code, Codex, Copilot, Gemini CLI, OpenCode, Cursor, Windsurf, Cline, Zed, Kiro, pi — всего 20 агентов

## Почему заблокировано (и это ложное срабатывание)

`hermes plugins install` → `Decision: BLOCKED (dangerous verdict, 111 findings)`,
`--force` вердикт не переопределяет (отключается только `plugins.scan_on_install` в config.yaml).

Разбор находок:

- **2 CRITICAL exfiltration** — строка документации «Commands need a skill-capable host
  (Claude Code, Codex, Devin…)» в README.md и её перевод на испанский → **ложные срабатывания**
- **27 MEDIUM supply_chain** — `git clone https://github.com/...`, `pip install pandas`,
  `npm install lodash` **в самих README и .github/workflows**
- **MEDIUM execution/traversal** — бенчмарк-харнесс `benchmarks/agentic/run.py` (subprocess)
- **62 LOW persistence** — JS-скрипты, сверяющие копии правил с AGENTS.md

**Ревью кода чистое:** `__init__.py` (247 строк) — только `json/os/re/pathlib`,
сети/subprocess/eval/exec нет; `package.json` — зависимостей и postinstall-хуков нет;
подозрительных конструкций (`curl|bash`, `rm -rf`, `chmod +x`) по репо не найдено.

## Если передумаем

1. `plugins.scan_on_install: false` в `config.yaml` → `hermes plugins install ... --enable`
2. сразу вернуть `plugins.scan_on_install: true`
3. рестарт гейтвея
