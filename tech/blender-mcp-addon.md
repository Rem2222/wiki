---
description: "Blender AI MCP Addon (LiCinCan) — AI-ассистент и MCP-сервер прямо в Blender 4.2+: визуальный чат со сценой, 21 инструмент, мультиагентная команда (manager/worker/reviewer), свои провайдеры, Windows x64, MIT."
tags: [blender, mcp, ai-assistant, 3d, addon]
related: [[tech/deepseek-harness]] [[concepts/waku-agent]]
---

# Blender AI MCP Addon (mcp-for-blender-pro)

## Что это

AI-ассистент для Blender (4.2+) со встроенным MCP-сервером: смотрит сцену, строит объекты, правит материалы, ищет ассеты и выполняет многошаговые задачи — через визуальное чат-окно (Studio) рядом с Blender.

- **Репозиторий:** https://github.com/LiCinCan/blender-ai-mcp-addon
- **Лицензия:** MIT, Python. Релиз 1.0.0, Windows x64, Blender 4.2+
- **Звёзды:** 747 (18.10.2026), форки 356, создан 15.10.2026 — свежий, взлетел за неделю (топ GitHub-трендов 18.10)
- **Установка:** Releases → `mcp-for-blender-pro.zip` → Blender: Edit → Preferences → Get Extensions → Install from Disk → включить → 3D Viewport → N → MCP Pro

## Возможности

- **Blender-aware ассистент** — сначала инспектирует сцену (`get_scene_info`, `list_objects`, `get_object_info`), потом действует
- **Studio-окно** — чат, список объектов, снапшоты вьюпорта, подтверждения операций, task board
- **Свои провайдеры** — OpenAI, Anthropic Claude, Google Gemini, OpenRouter, OpenCode Zen, Ollama, свои endpoint'ы (OpenAI Chat Completions / Anthropic Messages / Ollama протоколы); несколько ключей на провайдера, рабочие и личные раздельно
- **Мультиагентная команда** — Manager (разбивает на задания и критерии приёмки) → Workers (выполняют операции) → Reviewers (проверяют и возвращают замечания); неудача = 1 попытка исправить, вторая — стоп воркфлоу
- **21 инструмент сцен** — создание (cube/sphere/cylinder/plane/light/camera), правка (move/duplicate/delete/parent/material), скрипты (`execute_code`, `bpy_api_lookup`), экспорт, ассеты
- **Ассеты** — Poly Haven, Sketchfab, Poly Pizza (ключи где надо, лицензии за собой)
- **Языки интерфейса** — EN/DE/FR/ES/中文
- **Безопасность** — подтверждение операций, отмена, именованные undo-шаги; валидация Python-инструментов, но это НЕ песочница

## Интеграция с агентами

- Встроенный MCP-сервер: Streamable HTTP, аутентифицированный — подключается OpenCode Portable из сайдбара (сам настроит connection) и другие MCP-клиенты
- Картинко-модели могут «видеть» скриншоты вьюпорта
- Нужен Blender открытым, пока работает Studio или внешний клиент

## Заметки

- Проект независимый, не от Blender Foundation; репо называет себя mcp-for-blender-pro, имена в топиках — blender-mcp
- Записал 18.10.2026 из топ-10 GitHub-трендов недели, по просьбе Романа («Давай блендер в Вики»)
- 356 форков при 747 звёздах — отношение подозрительно высокое; у свежего репо (3 дня) это может значить ботов/накрутку — качать с оглядкой