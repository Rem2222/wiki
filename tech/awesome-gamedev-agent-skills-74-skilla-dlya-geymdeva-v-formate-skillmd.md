---
description: "Библиотека gamedev-skills/awesome-gamedev-agent-skills (3 896 звёзд, Apache-2.0): 74 скилла для Godot/Unity/Unreal/Bevy/Phaser/three.js, роутер-диспетчер, workflows steam-publish/itch. Формат SKILL.md совместим с Hermes. Проверено 24.10.2026; не подключено."
tags: [skills, gamedev, agents, godot, unity, unreal, steam, ccgs, arcengine]
related: [[tech/harness-google-research-rekursivnyy-harnessing-agentov-bez-obucheniya-vesov]] [[tech/scenario-3d-collection-1342-ai-modeli-s-cc-by-40-hugging-face]]
---

# awesome-gamedev-agent-skills — 74 скилла для геймдева в формате SKILL.md

**awesome-gamedev-agent-skills** — открытая библиотека скиллов для геймдева под AI-агентов: 74 специализированных навыка в формате `SKILL.md` (Agent Skills, формат Anthropic). Проверено 24.10.2026 по GitHub API и исходникам.

- Репозиторий: https://github.com/gamedev-skills/awesome-gamedev-agent-skills
- **3 896 ⭐**, 354 форка, лицензия **Apache-2.0**, язык Python, создан 24.06.2026, последний push 24.10.2026
- 242 файла, из них **77 `SKILL.md`** (74 скилла + `router` + служебные)

**Статус: не подключено.** Записано по факту проверки; в наш профиль скиллы не устанавливались.

## Состав

- `skills/disciplines` — **15**: game-feel, level-design, game-ui-ux, game-ai, ai-behavior-trees-utility-ai, shader-programming, performance-optimization, physics-tuning, save-systems, dialogue-systems, camera-systems, audio-design, input-systems, procedural-gen, create-game-assets
- `skills/genres` — **9**: **card-game**, roguelike, platformer, puzzle, rpg, fps-shooter, tower-defense, survival-crafting, visual-novel
- `skills/godot` — **16** (gdscript, csharp, nodes-scenes, resources, signals-groups, animation, audio, physics, shaders, tilemap, ui-control, multiplayer, export, 2d-movement, 3d-essentials, gdscript-headless-testing)
- `skills/unity` — **8** (csharp-scripting, animation, physics, navmesh, input-system, scriptableobjects, tilemap-2d, build-pipeline)
- `skills/unreal` — **6** (blueprints, cpp-gameplay, enhanced-input, niagara, behavior-trees, packaging)
- `skills/other-engines` — **11** (Bevy, Defold, LÖVE, pygame, Roblox ×6)
- `skills/web-engines` — **6** (Phaser ×2, PixiJS, three.js ×3)
- `skills/ebitengine` — **1**
- `skills/workflows` — **4**: **prototype-fast**, game-jam, itch-publish, **steam-publish**

## Как устроен «автоматический подбор»

Это не магия и не сервис, а отдельный скилл-диспетчер `router/SKILL.md`. Он:

1. Определяет движок по отпечатку проекта (godot, unity, unreal, ebitengine, bevy, phaser, pixijs, three.js, defold, LÖVE, pygame, roblox) — максимум один набор;
2. Классифицирует задачу по формулировке → дисциплины + максимум один жанр + workflow;
3. Называет **минимальный** набор скиллов и требует прочитать их до действий.

Сам он ничего не переучивает: «dispatches and composes». Повторно роутить нужно только при смене движка или задачи.

## Совместимость с Hermes

Формат совпадает с нашим: `SKILL.md` с YAML-frontmatter `name` + `description` и телом. Переносятся **без переделки**, кладутся в `skills/` с категорией. Заявленная поддержка Claude Code и Codex подтверждена файлами: `.claude-plugin/marketplace.json` и `router/agents/openai.yaml`.

## Качество (примеры)

- `genres/card-game` (138 строк): `description` сразу с триггером («Use for a deckbuilder, TCG/CCG…»), разделы **When to use** и **When NOT to use** со ссылками на смежные скиллы вместо дублирования, модель зон deck/hand/discard, разрешение эффектов.
- `workflows/steam-publish` (247 строк): depot/package, `app_build_*.vdf`, `steamcmd`, beta-ветки, релизные чек-листы; глубокие детали вынесены в `references/steampipe-build-scripts.md`, то есть тяжёлое — по требованию, а не в always-on.

## Что взять нам (если понадобится)

- `genres/card-game` — под **ccgs**: зоны deck/hand/discard, draw/shuffle, разрешение эффектов
- `web-engines/phaser-core`, `phaser-arcade-physics`, `threejs-scene-setup`, `threejs-gltf-loading` — под HTML5 и загрузку GLB (в связке с [[tech/scenario-3d-collection-1342-ai-modeli-s-cc-by-40-hugging-face]])
- `disciplines/create-game-assets`, `shader-programming`, `performance-optimization` — под **arcengine**
- `workflows/prototype-fast` — быстрые прототипы

**Ограничение:** подключать все 77 сразу не нужно. По логике [[tech/harness-google-research-rekursivnyy-harnessing-agentov-bez-obucheniya-vesov]] список скиллов висит в контексте каждого прогона, поэтому берутся только скиллы под конкретную задачу.

## Вывод

Готовая, живая библиотека доменных скиллов, совместимая с нашим форматом и сделанная по правильной схеме: триггер в `description`, явное «когда не применять», тяжёлые детали — в `references/`. Ценность точечная: под ccgs, arcengine и веб-игры; ставить всё целиком — вредно.
