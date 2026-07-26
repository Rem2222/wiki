---
type: reference
title: MengTo/Skills — Agent Skills для Three.js геймдева
description: Коллекция портабельных agent skills для разработки игр на Three.js — изометрические RPG, VFX, боевые системы, камера, звук, ассеты
tags: [gamedev, threejs, skills, agents, codex, claude]
related:
  - concepts/graph-engineering
  - concepts/hermes-knowledge-base
source: https://github.com/MengTo/Skills
author: Meng To (Design+Code)
license: MIT
stars: 3200
ingested_at: '2026-07-25'
---

# MengTo/Skills — Three.js GameDev Agent Skills

**Автор:** Meng To (известен по Design+Code курсам)
**Репозиторий:** https://github.com/MengTo/Skills
**Демо игры:** https://vesperfall.mengto.chatgpt.site
**Каталог ассетов:** https://vesperfall.mengto.chatgpt.site/asset-catalog

Коллекция портабельных agent skills для Codex, Claude, Cursor и других AI-кодинг агентов. Позволяет собрать изометрическую action RPG с нуля.

## Структура

```
agent-skills/
├── three-game/           # Основные геймдев скиллы
│   ├── three-isometric-camera/    # Изометрическая камера
│   ├── three-vfx/                 # Визуальные эффекты
│   ├── three-sound/               # Звуковая система
│   ├── three-combat/              # Боевая система
│   ├── three-monster-assets/      # Ассеты монстров
│   └── three-fog-of-war/          # Туман войны
├── web-design/           # Веб-дизайн скиллы  
├── assets/               # Игровые ассеты
└── scripts/              # Скрипты
```

## Что включено

| Скилл | Описание |
|---|---|
| **Three.js Isometric Camera** | Изометрическая камера, управление, зуум, панорамирование |
| **Three.js VFX** | Визуальные эффекты — партиклы, вспышки, анимации |
| **Three.js Sound** | Звуковая система для игр |
| **Three.js Combat** | Боевая система — атаки, здоровье, damage |
| **Three.js Monster Assets** | Импорт и управление ассетами монстров |
| **Three.js Fog of War** | Туман войны для изометрических игр |

## Демо-игра Vesperfall

Изометрическая action RPG, построенная на этих скиллах:
- Управление камерой
- VFX эффекты
- Звуковое сопровождение
- Монстры и боевая система

## Применимость к проектам

**«Обучалка» (CCGS):** скиллы напрямую релевантны — изометрическая камера, спрайты монстров, боевая система. Могут использоваться как reference при генерации кода через Codex/Claude.

**Формат:** каждый скилл — папка со SKILL.md (как в Hermes), что делает их совместимыми с Hermes agent workflow.

## Ссылки

- [GitHub: MengTo/Skills](https://github.com/MengTo/Skills)
- [Демо Vesperfall](https://vesperfall.mengto.chatgpt.site)
- [Каталог ассетов](https://vesperfall.mengto.chatgpt.site/asset-catalog)
- [Автор — Meng To](https://mengto.com)
