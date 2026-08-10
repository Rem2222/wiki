---
description: Qwen-MM-Plugins — набор native-плагинов от QwenLM (skill + MCP), добавляющий агентным обвязкам мультимодальные инструменты: чтение изображений/видео/документов, OCR, grounding, ASR, генерация медиа, 3D/CAD.
tags: [qwen, multimodal, mcp, vision, plugins, ai]
related: [[tools/yt-dlp]] [[tech/Mercury-Agent-Skills]]
---

# Qwen-MM-Plugins

Native multimodal plugins for Qwen models. Репозиторий: https://github.com/QwenLM/Qwen-MM-Plugins (Apache-2.0).

## Что это

Каждая «капабилити» = **skill** (чтобы модель знала об инструментах) + **MCP-сервер** (сами инструменты). MCP запускается по требованию через `uvx` (Python-пакет из репозитория, ничего не висит в системе).

⚠️ **Важно:** плагины НЕ дают зрение текстовой модели. Текстовая модель остаётся текстовой — у неё появляются «инструменты зрения»: отдельные VL-модели смотрят, а результат (описание/текст) возвращается модели. «DeepSeek стал мультимодальным» из новостей — журналистское упрощение.

## Капабилити

| Капабилити | Что даёт | Install name |
|---|---|---|
| **core** | Фундаментальный vision: чтение изображений/видео/документов/3D (динамическое разрешение), OCR, grounding, сегментация, ASR, vision-chat, веб-поиск | `qwen-mm-plugins-core` |
| video-memory | Вопросы по длинным видео (иерархическая графовая память) | `qwen-mm-plugins-video-memory` |
| omni-av | ASR с таймкодами/спикерами, теги музыки, событийный счёт | `qwen-mm-plugins-omni-av` |
| video-edit | Редактирование + генерация видео/изображений/аудио | `qwen-mm-plugins-video-edit` |
| blender | Управление запущенным Blender (thin client, 22 тула) | `qwen-mm-plugins-blender` |
| freecad | Параметрический CAD в запущенном FreeCAD (14 тулов, STEP/STL, FEM) | `qwen-mm-plugins-freecad` |
| edu-agent | Учебные видео-объяснялки (skill-only, без MCP) | `qwen-mm-plugins-edu-agent` |

Поддерживаемые харнессы установщиком: Claude Code · Codex · Qoder · OpenClaw · Qwen Code · Gemini CLI. Для остальных (opencode, Hermes и т.п.) — регистрация skill + MCP вручную.

## Как работает core

Структура Python-пакета:
- `readers/` — нарезка картинок на патчи (динамическое разрешение — 4K и миниатюры одинаково детально), кадры видео, метаданные
- `renderers/` — превращение PDF/Office/CSV/кода/SVG/3D/GIS/LaTeX в картинки
- `apis/` — вызовы облачных API: vision_chat, ocr, grounding, asr, web_search, web_extractor, image_search
- `producers/` — crop, draw_bbox (рамки), save_view

## Кто распознаёт

| Инструмент | Кто распознаёт | Нужен ключ |
|---|---|---|
| `read_image` / `read_video` / `visualize` | Сама модель агента (должна иметь vision) | нет |
| `vision_chat` | qwen3.7-plus (VLM) через DashScope | DASHSCOPE_API_KEY |
| `ocr` | qwen-ocr (DashScope) | DASHSCOPE_API_KEY |
| `grounding` | qwen-vl (DashScope), возвращает bbox | DASHSCOPE_API_KEY |
| `transcribe_audio` | qwen3-asr (DashScope), SRT/текст/JSON | DASHSCOPE_API_KEY |
| `segmentation` | Самосборный SAM3 (локальный GPU-сервер, CUDA) | свой (нет GPU — не подходит) |
| `web_search` | Serper (Google API) | SERPER_API_KEY |

Есть `DASHSCOPE_BASE_URL` — override endpoint'а (прокси/шлюзы). Потенциально можно направить на свой [[tech/qwen-tp]] (TokenPlan: qwen3.7-plus, аудио-модели есть) — проверить совместимость.

## Применимость к стеку Rem

- **Hermes** — MCP можно подключить вручную (native-mcp). Но базовый vision уже есть: `vision_analyze` → auxiliary.vision → qwen3.7-plus (qwen-tp). Плагины добавили бы: видео-кадры, PDF-рендер, OCR, grounding, ASR.
- **Mercury** — тоже можно, но не критично.
- **GBrain** — не нужно (эмбеддинги).
- Ограничения: DashScope-ключ (или совместимость с qwen-tp), segmentation отпадает (нет GPU), нативное чтение требует vision-модели в агенте.

**Вывод:** полезно, но не критично — частично дублирует существующий auxiliary.vision. Реальная ценность: OCR, PDF, видео, grounding. Задачи по PDF/OCR до этого в стеке не было (разбор видео — другие инструменты, [[tools/yt-dlp]] + транскрипция).

## Проверочное видео

https://youtu.be/KnW3UII-sNU — разобрать как проверку (отложено).
