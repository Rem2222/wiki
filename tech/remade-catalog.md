---
type: reference
title: Remade.wiki — каталог open-source переписей известного софта
description: Каталог независимых реализаций коммерческих программ (Photoshop → PhotoCraft, Excel → GridCraft и т.д.). Проверено 19.10.2026: проекты реальные, серия storytold/*Craft на Rust с CLI и MCP.
tags: [open-source, rust, mcp, catalog, reference]
related:
  - tech/rag-platforms
  - tech/e2e-framework
source: https://remade.wiki/explore/
github: https://github.com/replicraft/remade
license: MIT (каталог)
ingested_at: '2026-10-19'
---

# Remade.wiki — каталог переписей коммерческого софта

Каталог независимых («clean-room») реализаций известных коммерческих программ: Photoshop, Excel, AutoCAD, Premiere, MATLAB и т.д. Не плагины и не оболочки — самостоятельные реализации, часто на Rust, с открытым кодом.

- Сайт: https://remade.wiki/explore/ — сам заявляет **«123 reimplementations and 13 supporting tools»**
- Репозиторий каталога: https://github.com/replicraft/remade — MIT, создан **09.10.2026**, 86 ⭐, 16 открытых issues, пуши идут
- Фильтры на сайте: категория, язык (Rust, C++, Swift, Zig…), платформа (Linux/Windows/macOS/Web/Android/iOS), **статус — Planned / Experimental / Alpha / Beta / Stable**

## Проверка утверждений (19.10.2026)

| Утверждение | Проверка |
|---|---|
| Проекты реальные, не выдумка | ✅ подтверждено через GitHub API по 5+ именам |
| «CLI и MCP для ИИ-агентов» | ✅ у PhotoCraft архитектурно: «every action is a command», 500+ команд в одном реестре, `photocraft-cli mcp` |
| «123 проекта» | ✅ сайт заявляет ровно это; долю по всем 123 не пересчитывал |
| «68% каталога создано в октябре 2026» | ⚠️ по организации storytold сходится (22 репо из 66 — октябрь 2026), по всему каталогу не считал |
| «выросло за пару недель» | ❌ организация storytold существует с 2020 (artcraft 2022, 33.5k ⭐); свежая именно волна `*Craft` |

## Организация storytold (главный поставщик)

66 репозиториев, 213 201 ⭐ суммарно, почти всё Apache-2.0, язык Rust. Метрики на 19.10.2026:

- `photocraft` (Photoshop) — **68 403 ⭐**, 12 054 форка, 2 814 открытых issues, 49 МБ, создан 30.09.2026, пуш в день проверки
- `pdfcraft` (Acrobat) — 16 217 ⭐
- `filmcraft` (Premiere) — 15 056 ⭐
- `wordcraft` (Word) — 14 688 ⭐, создан 07.10.2026
- `lightcraft` (Lightroom) — 13 861 ⭐
- `vectorcraft` (Illustrator) — 9 984 ⭐
- `effectcraft` (After Effects) — 7 401 ⭐
- `cadcraft` (AutoCAD) — 5 965 ⭐, создан 07.10.2026
- `gridcraft` (Excel) — 5 876 ⭐, создан 07.10.2026
- `artcraft` (старый проект, 2022) — 33 574 ⭐

## Почему это интересно (главное)

**Архитектура «всё есть команда».** В PhotoCraft каждый пункт меню, инструмент и диалог — команда из единого реестра (500+). UI, CLI, JSON control channel и MCP-сервер вызывают один и тот же реестр. Агент управляет приложением не скриншотами и кликами, а командами.

Пример из README:

```bash
photocraft-cli run wave.psd
photocraft-cli batch --actions grade.json --in ./raw --out ./graded
photocraft-cli mcp      # MCP-сервер для агента
```

Это ровно тот паттерн, который нужен своим агентам (Dex): приложение как API, а не как GUI.

## Осторожно

- Форк/звёзды у photocraft — 17.6% (12 054 / 68 403). Обычно 5–10%; признак взрывного хайпа.
- 2 814 открытых issues — за вопросами не успевают.
- В самом каталоге статусы честные: у многих проектов `planned` / `experimental` / `alpha`, то есть часть ещё не написана.
- Ставить в работу ничего не стал: интерес архитектурный, а не «замена Photoshop».

## Что взять себе

1. Паттерн «реестр команд → UI / CLI / JSON / MCP как потребители» — переносить в свои инструменты (в т.ч. в 1С-обвязку и в Dex).
2. Смотреть на `gridcraft` как на пример clean-room табличного движка (Excel-совместимость — вечная боль в 1С-выгрузках).
3. Сами приложения — только когда статус дойдёт до `beta`/`stable` и появится реальная задача.
