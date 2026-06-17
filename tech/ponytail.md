---
description: Ponytail — скилл/плагин для AI coding-агентов, заменяющий многословие моделей на подход «ленивый сеньор-разработчик». 80-94% меньше кода, 3-6x быстрее, 47-77% дешевле.
tags: [tech, ai-coding, plugin, skill, opencode, claude-code, codex, cursor]
related: [tech/opencode, tech/mimo-code, tech/caveman]
---

# Ponytail

**Репозиторий:** [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
**Звёзд:** 1.7k ★ | **Форков:** 80 | **Лицензия:** MIT
**Релиз:** v4.2.0

---

## Что это

Плагин/скилл для AI coding-агентов, который учит модель писать код как **ленивый сеньор-разработчик**. Вместо того чтобы генерировать 50 строк обвязки, агент останавливается и думает — а нужно ли это вообще, нет ли готового решения в stdlib/браузере/уже установленных зависимостях?

Девиз: *«He says nothing. He writes one line. It works.»*

## Принцип работы

Перед тем как писать код, срабатывает чеклист:

1. **Это вообще нужно?** (YAGNI) → нет? пропускаем
2. **Стандартная библиотека делает?** → используем
3. **Нативная платформа?** (браузер, ОС) → используем
4. **Уже установленная зависимость?** → используем
5. **Можно одной строкой?** → одной строкой
6. **Только тогда** — минимум который работает

Каждый shortcut помечен комментарием `ponytail:` с указанием upgrade path.

Защита: trust-boundary validation, data-loss handling, безопасность и accessibility никогда не срезаются.

## Цифры (бенчмарки)

| Метрика | vs без скилла | vs Caveman |
|---------|:---:|:---:|
| Строк кода | **80-94% меньше** | 20-30% меньше |
| Скорость | **3-6× быстрее** | 1.5-2× быстрее |
| Стоимость | **47-77% дешевле** | 25-40% дешевле |

Тестировалось: email validator, debounce, CSV sum, countdown timer, rate limiter — на Haiku, Sonnet, Opus. 10 прогонов на ячейку, median.

## Поддерживаемые агенты

| Агент | Способ подключения |
|-------|-------------------|
| **Claude Code** | `/plugin marketplace add DietrichGebert/ponytail` |
| **Codex** | `codex plugin marketplace add DietrichGebert/ponytail` |
| **OpenCode** | `plugin: ["./.opencode/plugins/ponytail.mjs"]` + AGENTS.md |
| **Cursor** | `.cursor/rules/ponytail.mdc` |
| **Windsurf** | `.windsurf/rules/` |
| **Cline** | `.clinerules/` |
| **Copilot** | `.github/copilot-instructions.md` |
| **Aider** | `AGENTS.md` |
| **Kiro** | `.kiro/steering/ponytail.md` |
| **Pi agent** | `pi install git:github.com/DietrichGebert/ponytail` |

## Установка для OpenCode

```json
{
  "plugin": ["./.opencode/plugins/ponytail.mjs"]
}
```

Run OpenCode из чекаута репозитория (плагин использует `hooks/` и `skills/` оттуда). AGENTS.md подгружается автоматически.

Команды:
- `/ponytail` — активировать (lite/full/ultra/off)
- `/ponytail-review` — найти что удалить в diff
- `/ponytail-help` — справка

## Команды и уровни

- **lite** — стандартный режим
- **full** — агрессивный режим
- **ultra** — «когда кодовая база тебя обидела»
- **off** — отключить

## FAQ

**Нужен конфиг?** Нет.

**Не сломает ли это код?** Безопасность, обработка ошибок и доступность не срезаются. Каждый shortcut явно помечен.

**В чём разница с Caveman?** [Caveman](https://github.com/JuliusBrussee/caveman) — похожий скилл (~75% сокращение болтовни модели). Ponytail более агрессивный по коду (не только текст, но и генерация), плюс бенчмарки показывают лучшие цифры.

## Ссылки

- [Бенчмарки](https://github.com/DietrichGebert/ponytail/tree/main/benchmarks)
- [Примеры](https://github.com/DietrichGebert/ponytail/tree/main/examples)
- [Agent portability](https://github.com/DietrichGebert/ponytail/tree/main/docs/agent-portability.md)
