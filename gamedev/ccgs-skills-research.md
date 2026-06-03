---
description: 20.4k звёзд, 3k форков, стабильный v1.0.0. Автор: Donchitos, активно с февраля 2026.
title: "Анализ Claude Code Game Studios — скилы для геймдева"
created: 2026-05-30
tags: [gamedev, ccgs, skills, research, hermes-agent]
type: research
status: done
sources:
  - "https://github.com/Donchitos/Claude-Code-Game-Studios"
  - "Форк: https://github.com/Rem2222/Claude-Code-Game-Studios"
---

# Claude Code Game Studios — анализ скилов для адаптации

## Что такое CCGS

**Claude Code Game Studios** (49 AI-агентов, 73 skill-команды, 12 авто-хуков) — фреймворк, превращающий сессию Claude Code в полноценную игровую студию с трёхуровневой иерархией: Directors (Opus) → Department Leads (Sonnet) → Specialists (Sonnet/Haiku).

20.4k звёзд, 3k форков, стабильный v1.0.0. Автор: Donchitos, активно с февраля 2026.

**Форк:** `https://github.com/Rem2222/Claude-Code-Game-Studios` (сделан 2026-05-30).

---

## 1. Скилы дизайнера интерфейсов (UI/UX)

### 1.1 `team-ui` — полный пайплайн UI-разработки

**Что делает:** Оркестрирует команду UI из 5+ агентов через 5 фаз:
Context Gathering → UX Spec → Visual Design → Implementation → Review → Polish.

**Ключевые принципы (адаптируемые):**

- **Context Gathering до дизайна** — прочитать game-concept, player-journey, все GDD UI Requirements, interaction-patterns, accessibility-requirements. Никаких предположений «из головы».
- **UX Spec Authoring** — документирование экрана через 14 секций (Purpose, Player Context, Layout + ASCII Wireframe, Interaction Map, Data Requirements, Events, Accessibility, Localization).
- **UI ≠ game state** — UI только читает данные, не владеет ими. Все действия — события (events fired). Никакого прямого изменения game-state из UI.
- **Pattern Library** — переиспользование паттернов вместо изобретения новых. Файл `interaction-patterns.md`.
- **4 режима ревью** — full/lean/solo — уровень гейтов варьируется от полного до нулевого.

**Что адаптировать для Carrot Maze / GSD:**

1. **Шаблон UX-спецификации из 14 секций** — можно упростить до 6-8 секций для HTML5-игры, но структура остаётся: Purpose → Layout → States → Interaction → Accessibility → Acceptance Criteria.
2. **Принцип разделения UI/Game State** — уже частично реализован в нашей гибридной архитектуре (Canvas HUD + HTML-оверлеи), но стоит формализовать в RESEARCH.md/PLAN.md.
3. **Interaction Pattern Library** — для повторяющихся UI-паттернов (меню паузы, Hall of Fame, настройки) иметь документированные паттерны вместо переписывания с нуля.
4. **Accessibility-first** — проверка контраста, keyboard navigation, screen reader — закладывать в спецификацию до реализации.

### 1.2 `ux-design` — пошаговое создание UX-спецификации

**Что делает:** 14-секционный шаблон + цикл Context→Questions→Options→Decision→Draft→Approval→Write для каждой секции.

**Секции шаблона:**
1. Purpose & Player Need
2. Player Context on Arrival
3. Navigation Position
4. Entry & Exit Points
5. Layout Specification (ASCII wireframe + zone definitions + component inventory)
6. States & Variants
7. Interaction Map
8. Data Requirements
9. Events Fired
10. Transitions & Animations
11. Input Method Checklist
12. Accessibility Requirements
13. Localization Considerations
14. Acceptance Criteria

**Что адаптировать:**

- **ASCII Wireframe** — простой способ задокументировать раскладку экрана до кодинга. Для Carrot Maze пригодится при проектировании меню паузы, Hall of Fame, экрана Game Over.
- **States & Variants** — обязательная спецификация всех состояний экрана (Loading, Empty, Populated, Error, Confirmation). 90% багов в UI — непредусмотренные состояния.
- **Interaction Map** — таблица «каждый input → что делает» для keyboard/gamepad/touch. Исключает «а что должно происходить по Tab?» на этапе реализации.

### 1.3 `ux-review` — валидация UX-спецификации

**Что делает:** Проверяет завершённый UX-спек на полноту, консистентность, accessibility. Вердикт: APPROVED / NEEDS REVISION / REJECTED.

**Что адаптировать:** Идея гейта «спецификация утверждена до реализации». В GSD уже есть аналог: Research → Plan → Execute, но UX-review добавляет формальную проверку accessibility и input completeness до кодинга.

### 1.4 `quick-design` — лёгкая спецификация для малых изменений

**4 категории изменений:**
- **Tuning** — изменение чисел (таблица old→new)
- **Tweak** — малое поведенческое изменение (1-2 состояния)
- **Addition** — добавление механики в существующую систему
- **New Small System** — небольшой самостоятельный фича (< 1 недели)

**Что адаптировать:** Формат Quick Design Spec для мелких правок в Carrot Maze (добавили бонус, изменили скорость зайцев, поправили баланс). Вместо переписывания всего PLAN.md.

### 1.5 `art-bible §7: UI/HUD Visual Direction`

Секция арт-байбла про UI: diegetic vs screen-space HUD, typography direction, iconography style, animation feel. Параллельный запуск art-director + ux-designer для выявления конфликтов между эстетикой и юзабилити.

### 1.6 Шаблон HUD Design (`hud-design.md`)

**13 секций**, включая:
- HUD Philosophy (принцип «по умолчанию скрывать» vs «показывать»)
- Information Architecture (вся инфа → категоризация: Always Show / Contextual / On Demand / Hidden)
- Layout Zones (ASCII-диаграмма зон экрана)
- Visual Budget (жёсткие лимиты: макс % экрана под HUD — 12% exploration, 22% combat)
- Platform Adaptation (safe zones, resolution ranges)
- Accessibility — HUD Specific (colorblind modes, text scaling, motion sensitivity, subtitles)

**Критически важно для Carrot Maze:** Visual Budget и Information Architecture. Сейчас HUD растёт стихийно — бонусы, счётчик зайцев, сердечки, FPS... Нужен явный документ что где и почему висит.

---

## 2. Скилы дизайна игры / мира (Game/World Design)

### 2.1 `team-level` — полный пайплайн левел-дизайна

**5 шагов с параллельными и последовательными агентами:**

| Шаг | Агенты | Результат |
|-----|--------|-----------|
| 1 | narrative-director + world-builder + art-director (параллельно) | Narrative brief, lore foundation, visual direction targets |
| 2 | level-designer | Spatial layout, pacing curve, encounters, landmarks |
| 3 | systems-designer | Enemy compositions, loot tables, difficulty balance |
| 4 | art-director + accessibility-specialist (параллельно) | Production concepts, accessibility audit |
| 5 | qa-tester | Test cases, playtest checklist |

**Ключевой принцип:** Visual direction targets от art-director (Step 1) — это ВХОДНЫЕ данные для level-designer (Step 2), а не выходные. Layout строится внутри визуального направления, а не наоборот.

**Что адаптировать для Carrot Maze:**

- **Концепция «уровней»** — сейчас игра авто-генерирует уровни. Но логика «каждые 3 уровня = новый бонус + заяц» — это уже левел-дизайн. Можно формализовать прокачку сложности как «зоны» (Zone 1: 1-3 уровни, Zone 2: 4-6, ...).
- **Adjacent area dependency check** — проверка что соседние зоны задокументированы. При росте игры — полезно.
- **Системная интеграция (Step 3)** — для каждого уровня/зоны: enemy compositions (типы зайцев?), resource distribution (как часто спавнятся бонусы?), difficulty balance.

### 2.2 `design-system` — полное GDD-авторство

**8 секций GDD:** Overview → Player Fantasy → Detailed Design (Core Rules, States, Interactions) → Formulas → Edge Cases → Dependencies → Tuning Knobs → Acceptance Criteria.

**Фишки:**
- **Context Gathering (2a-2d):** Чтение game-concept, systems-index, entity registry, dependency GDDs, reflexion log (consistency failures) — до первого вопроса пользователю.
- **Technical Feasibility Pre-Check:** Маппинг категории системы → engine domain → чтение engine-reference docs → feasibility brief.
- **Registry conflict check:** После записи каждой секции — сравнение с `entities.yaml`. Конфликты всплывают сразу.
- **Mandatory agent delegation:** Для Player Fantasy — creative-director, для Detailed Design — domain specialists.

**Что адаптировать:**

- **Секция Formulas** со структурой: `formula_name = expression` + таблица переменных (Symbol, Type, Range, Description) + Output Range. Идеально для документирования механик Carrot Maze (скорость питона от уровня, scaling зайцев, дроп-рейт бонусов).
- **Edge Cases** — обязательная секция. «Что если питон длиной 1 съест бонус lengthen?», «Что если бонус wall_reverse активен а стены уже wrap-around?»
- **Tuning Knobs** — все настраиваемые параметры с диапазонами. Не хардкодить, выносить в конфиг.

### 2.3 `art-bible` — арт-байбл (9 секций)

Визуальная идентичность игры: Visual Identity Statement → Mood & Atmosphere → Shape Language → Color System → Character Design → Environment Design → UI Visual Direction → Asset Standards → Style Prohibitions.

**Для пиксель-арт игр вроде Carrot Maze — адаптируемо:**
- Color System (секция 4): Primary palette с семантикой цветов, colorblind safety.
- Shape Language (секция 3): Character silhouette rules, environment geometry.
- Asset Standards (секция 8): Форматы, размеры спрайтов, naming conventions.

### 2.4 `map-systems` — декомпозиция концепта на системы

Создаёт `systems-index.md` — приоритизированный список всех игровых систем с зависимостями и слоями (Foundation → Systems → Features → Content).

**Что адаптировать:** Для Carrot Maze v3 с растущим количеством систем (бонусы, жизни, зайцы, звук, меню, стены) — нужен явный systems-index для понимания зависимостей. Сейчас это имплицитно в RESEARCH.md.

---

## 3. Скилы дизайна предметов / врагов (Items / Enemies)

### 3.1 `asset-spec` — спецификация визуальных ассетов

**Ключевые фичи:**
- **Entity & Screen Inventory:** Автоматический сбор всех визуальных сущностей из GDD, левел-доков, narrative — в единый инвентарь `entity-inventory.md`.
- **Категоризация:** Characters, Enemies, Buildings, Environment, Items/Props, VFX, UI Screens, HUD Elements, Audio.
- **Per-asset spec:** Для каждого ассета — Dimensions, Format, Naming, Visual Description (2-3 предложения), Art Bible Anchors, AI Generation Prompt.
- **Asset Manifest:** Мастер-файл `asset-manifest.md` с прогрессом (Needed → In Progress → Done → Approved).
- **Shared Asset Protocol:** Проверка существующих ассетов перед созданием дубликатов.

**Что адаптировать для Carrot Maze:**
- **Entity Inventory** — вместо стихийного «нам нужен спрайт морковки» иметь формальный список: морковка, питон (3 сегмента), заяц (4+), 9 типов бонусов (иконки), сердечки.
- **Per-asset AI generation prompts** — для генерации 8-bit спрайтов через ComfyUI/Stable Diffusion.
- **Asset Manifest** с прогрессом — видно что готово, что в работе, что ещё нужно.

### 3.2 `balance-check` — проверка игрового баланса

**4 домена анализа:**
1. **Combat:** DPS, time-to-kill, доминирующие стратегии, unkillable states
2. **Economy:** Resource faucets/sinks, flow rates, infinite loops
3. **Progression:** XP/power curves, dead zones, power spikes
4. **Loot:** Rarity distribution, pity timers, inventory pressure

**Отчёт включает:** Health Summary, Outliers (таблица expected vs actual), Degenerate Strategies, Recommendations (priority + suggested fix + impact).

**Что адаптировать для Carrot Maze:**
- **Анализ бонус-системы:** Не слишком ли силён «озверин»? Не доминирует ли «замедление» над остальными?
- **Progression analysis:** Кривая сложности — не слишком ли резкий скачок на уровне 6 (2 зайца + новый бонус)?
- **Loot/spawn rates:** Частота спавна бонусов (раз в 10 сек) + редкость (common/uncommon/rare) — ожидаемое время получения каждого типа.

### 3.3 `team-combat` — боевая система

**6 фаз:** Design → Architecture → Implementation → Integration → Validation → Sign-off.

**Команда:** game-designer, gameplay-programmer, ai-programmer, technical-artist, sound-designer, engine specialist, qa-tester.

**Что адаптировать для врагов в Carrot Maze:**
- **AI Programmer** — логика поведения зайцев (патрулирование? преследование? avoidance?). Сейчас зайцы просто двигаются — можно добавить состояний (idle/wander/chase/flee).
- **Game Designer** — документирование врагов как системы: типы зайцев (обычный, быстрый, большой?), их параметры (скорость, размер, поведение), scaling от уровня.
- **Sound Designer** — звуки для зайцев (шаги, съедение, смерть).

### 3.4 `content-audit` — аудит контента

Проверяет весь игровой контент на консистентность, полноту и соответствие GDD. Выявляет: отсутствующие ассеты, несогласованные названия, дублирующийся контент, незавершённые элементы.

---

## 4. Игровые движки и библиотеки

### 4.1 Engine Reference Docs

CCGS включает актуальную документацию по трём движкам в `docs/engine-reference/`:

| Движок | Специалист | Суб-специалисты | Модули |
|--------|-----------|----------------|--------|
| **Godot 4** | godot-specialist | GDScript, Shaders, GDExtension | animation, audio, input, navigation, networking, physics, rendering, ui |
| **Unity** | unity-specialist | DOTS/ECS, Shaders/VFX, Addressables, UI Toolkit | то же + plugins (Addressables, Cinemachine, DOTS/Entities) |
| **Unreal Engine 5** | unreal-specialist | GAS, Blueprints, Replication, UMG/CommonUI | то же + plugins (CommonUI, GAS, GameplayCamera, PCG) |

**Для каждого модуля — VERSION.md с verified capabilities под конкретную версию движка, breaking-changes.md, deprecated-apis.md, current-best-practices.md.**

### 4.2 `setup-engine` — конфигурация движка

Настраивает engine, язык, билд-систему, asset pipeline. Заполняет `technical-preferences.md`.

**Что адаптировать для HTML5 Canvas:**

Можно создать аналог engine-reference для **Web Canvas API + сопутствующих библиотек**:

- **2D Rendering:** Canvas 2D API, OffscreenCanvas, WebGL (PixiJS)
- **Audio:** Web Audio API, Tone.js, ZzFX
- **Input:** Keyboard, Gamepad API, Touch Events
- **Physics:** Matter.js, Planck.js, кастомная
- **Asset Pipeline:** Sprite sheets, texture atlases, Tile maps
- **Performance:** requestAnimationFrame, delta-time, object pooling

### 4.3 `prototype` — прототипирование

**3 пути (--path):**
- **HTML** — для концептов, UI, 2D-игр. Быстрый прототип в одном HTML-файле.
- **Engine** — полноценный прототип на выбранном движке.
- **Paper** — дизайн-воркшоп без кода (для нарратива, механик, баланса).

**Falsifiable hypothesis:** «Если игрок делает X, он почувствует Y — мы узнаем что это правда если Z.»

**Что адаптировать:** HTML-путь прототипа — ровно то, как мы уже делаем Carrot Maze. Можно формализовать как скилл `/prototype carousel-maze --path html`.

---

## 5. Шаблоны и паттерны (templates/patterns)

### 5.1 Система шаблонов (41 шаблон)

| Категория | Шаблоны |
|-----------|---------|
| **Game Design** | game-concept.md, game-pillars.md, game-design-document.md, systems-index.md, difficulty-curve.md, economy-model.md, faction-design.md |
| **UX/UI** | ux-spec.md, hud-design.md, interaction-pattern-library.md, accessibility-requirements.md |
| **Level Design** | level-design-document.md |
| **Narrative** | narrative-character-sheet.md, player-journey.md |
| **Art** | art-bible.md, sound-bible.md |
| **Architecture** | architecture-decision-record.md, architecture-doc-from-code.md, architecture-traceability.md, technical-design-document.md |
| **Production** | sprint-plan.md, milestone-definition.md, risk-register-entry.md, incident-response.md |
| **QA** | test-plan.md, test-evidence.md |
| **Release** | release-notes.md, changelog-template.md, release-checklist-template.md |
| **Other** | prototype-report.md, vertical-slice-report.md, post-mortem.md |

**Что уже можно использовать:**
- `ux-spec.md` (упрощённый) — для UI задач в GSD
- `game-design-document.md` (упрощённый) — как база для RESEARCH.md v2
- `accessibility-requirements.md` — для Carrot Maze
- `interaction-pattern-library.md` — для переиспользуемых UI-паттернов

### 5.2 Collaborative Design Principle

**Базовый цикл:** Question → Options → Decision → Draft → Approval → Write

Каждый шаг — интерактивный, с явным запросом подтверждения у человека. Агенты предлагают варианты, человек выбирает.

**В GSD это уже работает неявно** (Researcher предлагает → Planner выбирает → Executor реализует), но можно усилить явными decision points в критических местах.

### 5.3 Decision Points (AskUserQuestion pattern)

CCGS использует `AskUserQuestion` везде где есть выбор дизайна. Агент обязан:
1. Показать анализ
2. Предложить 2-4 варианта с pros/cons
3. Дождаться выбора пользователя
4. Только потом действовать

**В GSD:** Research уже делает «предлагаю варианты», но approval-gate перед переходом к Plan отсутствует.

### 5.4 Agent Delegation

Каждый team-skill оркестрирует sub-агентов через Task tool:
- Параллельный запуск где возможно
- Полный контекст в каждом промите
- Сбор результатов → компиляция

**Аналог в GSD:** Параллельные execute-таски (MUL-59/60/61). Но без формальных ролей (ux-designer, art-director, etc.).

### 5.5 Review Modes (full / lean / solo)

Гибкое управление глубиной проверок:
- **full** — все director gates активны (макс качество, макс время)
- **lean** — только PHASE-GATE проверки (баланс)
- **solo** — без agent gates (макс скорость)

**Что адаптировать:** Для GSD сделать опциональные уровни ревью в зависимости от критичности задачи.

---

## 6. Что НЕ трогаем (воркфлоу)

Пользователь явно указал: **воркфлоу не менять**. GSD-воркфлоу (Research → Plan → Execute → Verify → Code Review → Deliver) универсален и полностью устраивает.

**Что это значит:**
- **Не переносим** CCGS-воркфлоу (brainstorm → map-systems → design-system → create-epics → create-stories → dev-story → story-done).
- **Не меняем** последовательность фаз GSD.
- **Не вводим** роли Director/Department Lead/Specialist в GSD.
- **Адаптируем только** инструменты дизайна, шаблоны документов и принципы принятия решений — т.е. КАК агент делает свою работу внутри существующей фазы, а не КАКИЕ фазы есть.

---

## 7. Рекомендации по адаптации

### Приоритет 1 — Внедрить сейчас (для Carrot Maze)

1. **Шаблон UX-спецификации (упрощённый ux-spec.md)**
   - 6-8 секций вместо 14: Purpose, Layout (ASCII), States, Interaction Map, Accessibility, Acceptance Criteria
   - Использовать при проектировании меню паузы, Hall of Fame, HUD
   - Хранить в `design/ux/` (репозиторий carrot-maze)

2. **HUD Design Document (упрощённый hud-design.md)**
   - Information Architecture: что Always Show / Contextual / On Demand
   - Visual Budget: макс % экрана, макс элементов
   - Для Carrot Maze: здоровье (всегда), счёт (всегда), бонусы (контекстно), FPS (скрыть в продакшене)

3. **Entity Inventory для спрайтов**
   - Формальный список всех визуальных сущностей
   - Per-asset AI generation prompts для 8-bit стиля
   - Статус каждого спрайта (Needed / In Progress / Done)

4. **Formulas & Tuning Knobs для механик**
   - Документировать формулы (scaling зайцев, спавн-рейт бонусов, скорость питона)
   - Tuning Knobs со значениями по умолчанию и диапазонами
   - Всё в `assets/data/` JSON, не хардкодить

### Приоритет 2 — Внедрить позже (при росте сложности)

5. **Interaction Pattern Library**
   - Документировать повторяющиеся UI-паттерны (canvas HUD, HTML overlay, пауза)
   - Переиспользовать вместо переписывания

6. **Quick Design Spec для мелких изменений**
   - Формат для tuning/tweak/addition без переписывания PLAN.md
   - Файлы в `design/quick-specs/`

7. **Balance Check для бонусов и зайцев**
   - Анализ доминирования одних бонусов над другими
   - Проверка кривой сложности

8. **Accessibility Requirements**
   - Contrast ratios, keyboard navigation, reduced motion
   - Для Carrot Maze: проверка всех текстов на контраст с фоном, motion sensitivity toggle

### Приоритет 3 — Долгосрочно

9. **HTML5 Canvas Engine Reference**
   - Создать аналог engine-reference для Web Canvas API
   - Модули: rendering, audio, input, physics, performance
   - Best practices, gotchas, performance budget

10. **Art Bible Lite для пиксель-арта**
    - Color palette, shape language, style prohibitions
    - Для 8-bit ретро-стиля Carrot Maze

---

## 8. Конкретные файлы из CCGS — что адаптировать

| Файл CCGS | Что взять | Куда положить | Приоритет |
|-----------|-----------|---------------|-----------|
| `templates/ux-spec.md` | Упрощённая версия (8 секций) | `carrot-maze/design/ux/` | P1 |
| `templates/hud-design.md` | Information Architecture + Visual Budget | `carrot-maze/design/ux/hud.md` | P1 |
| `templates/game-design-document.md` | Секция Formulas + Tuning Knobs | Использовать в RESEARCH.md / PLAN.md | P1 |
| `skills/asset-spec/SKILL.md` | Entity inventory формат | `carrot-maze/design/assets/entity-inventory.md` | P1 |
| `templates/interaction-pattern-library.md` | Формат каталога паттернов | `carrot-maze/design/ux/interaction-patterns.md` | P2 |
| `skills/balance-check/SKILL.md` | Структура balance-отчёта | Использовать при балансировке бонусов | P2 |
| `skills/quick-design/SKILL.md` | Формат Quick Design Spec | `carrot-maze/design/quick-specs/` | P2 |
| `templates/accessibility-requirements.md` | Чеклист accessibility | `carrot-maze/design/accessibility.md` | P2 |
| `templates/art-bible.md` | Color System + Shape Language | `carrot-maze/design/art/art-bible.md` | P3 |
| `docs/engine-reference/` | Структура engine reference | Создать для Web Canvas API | P3 |

---

## 9. Источники

- CCGS GitHub: https://github.com/Donchitos/Claude-Code-Game-Studios
- Форк: https://github.com/Rem2222/Claude-Code-Game-Studios (2026-05-30)
- CCGS README: 49 agents, 73 skills, 41 templates, 12 hooks
- CCGS CLAUDE.md: Studio hierarchy, coordination rules
- CCGS skills: `.claude/skills/` (73 SKILL.md файлов)
- CCGS templates: `.claude/docs/templates/` (41 шаблон)
- CCGS engine reference: `docs/engine-reference/` (Godot, Unity, Unreal)

---

*Статья создана 2026-05-30 в рамках исследования MUL-54.*
*Автор: GSD Researcher (Hermes Agent)*
