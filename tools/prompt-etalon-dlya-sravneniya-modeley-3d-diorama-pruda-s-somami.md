---
description: "Готовая задача для бенча моделей: единый index.html с анимированной 3D-сценой японского пруда и шестью сомами на Three.js, всё процедурно. Полный текст промпта, критерии приёмки (мостик дугой, усы и плавники у сомов, рыба видна сквозь воду), порядок прогона через субагентов и результаты прогона 18.10.2026."
tags: [benchmark,llm,prompt,threejs,agents,render]
related:
  - tech/herdr
  - tech/orca-gui-orkestrator-flota-koding-agentov
updated: 2026-11-02
source: "промпт Романа (документ 3d.md), прогон 18.10.2026"
---

# Промпт-эталон для сравнения моделей: 3D-диорама пруда с сомами

## Что это

Эталонная задача для сравнения моделей: одна и та же творческая работа с объективно проверяемым результатом. Модель должна отдать единый `index.html` с анимированной 3D-сценой японского садового пруда и плавающими сомами на Three.js, всё процедурно, без моделей и текстур.

Автор формулировки — Роман (документ `3d.md`, 18.10.2026). Промпт на английском намеренно: на английском модели держат структуру требований точнее, и сравнение получается честнее.

Почему задача показательна:

- **Результат проверяем объективно** — либо `index.html` открывается и рисует сцену, либо нет
- **При этом задача творческая** — разница между моделями видна сразу, подробный «огород» её бы скрыл
- **Есть узнаваемый субъект** — сом с усами, плоской головой и плавниками. Модель, отрисовавшая каплю с хвостом, задачу не выполнила
- **Есть ловушка на деталях** — изогнутый мостик, который у многих превращается в плоскую доску

## Критерии приёмки

- Открывается в headless Chromium без ошибок, canvas живой, сцена **отрисовалась** (не чёрный экран)
- Кадр не пустой: `litPx > 0` при чтении пикселей canvas
- **Мостик читается** дугой с перилами, а не доской
- **Сомы узнаваемы**: плоская голова, широкий рот, длинные усы, отдельные плавники, тёмная спина и светлое брюхо. Один крупнее остальных
- **Рыба видна сквозь воду с начальной камеры** — отдельное требование, теряется чаще всего
- Никакого геймплея: ни кнопок, ни меню, ни карточек, ни оверлеев
- Размер файла сам по себе ничего не значит: прозаическая «словесная» модель может отдать 56 КБ описаний вместо кода. Смотреть структуру и скриншот

## Как запускать

Промпт сохранять в файл и отдавать субагенту ссылкой («прочитай `/path/prompt.md` и выполни дословно») — дети не получают контекст родителя, дублировать простыню в `goal` бессмысленно. Модель субагента задаётся через `delegation.provider` / `delegation.model` **перед** спавном: дочерняя сессия читает их в момент старта. После батча вернуть штатную дешёвую модель.

Прогонять дешёвыми→дорогими, чтобы бюджет не кончился до топ-модели. Проверять фактическую модель ребёнка не по конфигу, а запросом к `sessions` в `~/.hermes/state.db` (`created_source='subagent'`).

Скриншот для приёмки снимать с флагами `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader`, иначе WebGL в headless может не подняться.

## Прогон 18.10.2026

Сравнивались три модели через субагентов на Али-подписке:

- **deepseek-v4.1-flash** — сцена богаче всех по количеству геометрии; субагент сам прогонял её три минуты в Node и нашёл два бага с рыбами
- **glm-5.3** — 34 КБ, компактнее первой на 40%; аккуратнее и легче, мостик и каменный фонарь явно читаемее, но рыб в кадре видно меньше
- **qwen3.8-max** — 49 230 байт, 1 247 строк; 6 сомов с независимым поведением, арочный мостик с перилами и сваями, фонарь с мерцающим светом, сакура, бамбук, 60 падающих лепестков; проверена 90-секундной симуляцией — 485 мешей, 0 NaN-геометрий

Живые результаты: `https://rem2222.top/3d-soms/<модель>.html`

## Полный текст промпта

```
Create a beautiful animated 3D scene of a Japanese-style garden pond with swimming catfish, using Three.js and low-poly graphics.

Deliver the complete scene in a single `index.html` file containing all HTML, CSS, and JavaScript. Load Three.js and OrbitControls from a CDN using matching versions. Generate all objects procedurally, without external models, textures, or images.

The experience is purely visual: the viewer can rotate the camera, zoom in, and watch the fish swim and occasionally splash. Do not add fishing mechanics, feeding, inventory, information cards, menus, or gameplay.

VISUAL STYLE

Use a cohesive low-poly style with deliberate polygonal shapes, flat-shaded surfaces, and a peaceful Japanese garden atmosphere.

Use jade-green water, warm gray stones, moss-green vegetation, dark wooden elements, and soft pink cherry blossoms. Make the scene feel like a carefully crafted miniature diorama.

POND

Create an irregular rounded pond surrounded by natural angular stones and patches of moss.

Include:
- A visible underwater basin with sand, pebbles, and a few submerged rocks.
- Shallow edges and a deeper central area.
- A few lily pads and reeds along the shoreline.
- Translucent blue-green water with gentle animated ripples.
- A sculpted earth base beneath the garden.

Keep the central water area open so the fish are easy to see. The water must reveal the catfish beneath its surface from the initial camera view.

CATFISH

Create six recognizable low-poly catfish of different sizes.

Each fish must have:
- A broad, flattened head.
- A wide mouth.
- Small eyes.
- Clearly visible long barbels around the mouth.
- A thick body tapering toward the tail.
- Separate pectoral fins, a small dorsal fin, and an elongated anal fin.
- A distinct tail fin.
- A dark gray, olive, or brown back and a lighter belly.

Make one catfish larger than the others. Avoid koi-like shapes or bright orange coloring.

Animate the fish with smooth, independent swimming:
- Gentle side-to-side movement through the rear body and tail.
- Subtle fin movement.
- Different speeds, depths, and swimming paths.
- Smooth turns and occasional brief pauses.
- Natural avoidance of the pond edges, bottom, rocks, and other fish.

Most fish should swim beneath the surface. Occasionally, one should approach the surface, briefly reveal its back or tail, and produce a small splash with expanding ripples before descending again. Keep splashes subtle and infrequent.

JAPANESE GARDEN

Add a few carefully arranged elements around the pond:
- A small curved wooden bridge over a narrow section.
- A traditional stone lantern.
- A cherry blossom tree with an angular trunk and clustered pink foliage.
- A small group of bamboo stalks.
- A short stepping-stone path.

Keep the garden secondary to the pond. Do not let the bridge or vegetation obscure the fish.

Add a few slowly falling cherry blossom petals for atmosphere.

CAMERA AND LIGHTING

Use OrbitControls for smooth camera rotation and zoom. Set sensible limits so viewers can inspect the pond without moving beneath the ground.

Start with an attractive elevated three-quarter view showing the entire pond, visible fish, and surrounding garden.

Use warm daylight, soft ambient illumination, gentle shadows, and a simple complementary background. Ensure underwater fish remain clearly readable.

TECHNICAL REQUIREMENTS

- One complete `index.html` file.
- Full-screen responsive canvas.
- Procedural geometry and materials.
- Delta-time-based animation.
- Reasonable pixel-ratio limits and smooth performance.
- Correct transparency rendering for the water.
- No interface overlays or buttons.
- No unfinished features or placeholders.

Prioritize a beautiful composition, recognizable catfish, convincing swimming, gentle splashes, and enjoyable camera exploration.

Return only the complete code for `index.html`.
```

## Где лежит

- `/root/Documents/bench-3d-soms-prompt.md` — рабочий файл
- `~/.hermes/skills/mlops/llm-model-benchmarking/templates/3d-pond-catfish.md` — копия в скилле бенчмаркинга
- Раздел «Эталонная задача: 3D-диорама» в самом скилле — с чек-листом приёмки и порядком прогона
