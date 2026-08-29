---
description: "MCP-поиск по вики + writer-скрипт wiki-write (задача MUL-891)"
tags: [wiki,mcp,zvec,wiki-write,tasks]
---

# 10. MCP-поиск по вики (read-only) + единый writer-скрипт wiki-write

## Зачем

У нас два узких места при работе с вики (`~/Documents/wiki/`, Obsidian, markdown + YAML frontmatter):

1. **Поиск не нативный.** `zvec-wiki` — это вызов из shell, а не MCP-tool. Агент не «видит» его в списке инструментов (как раньше `mcp_gbrain_query`), приходит сырой текст.
2. **Запись не согласована.** Разные агенты (Hermes, Hermes Helper, Multica-автопилоты) пишут страницы в вики каждый по-своему → ломается YAML frontmatter / заголовки / пути, что бьёт по Obsidian и по индексу.

Решение — **две согласованные единые точки**:
- **Read:** свой лёгкий MCP-сервер поверх существующего `zvec_search.py` (read-only поиск), чтобы у Hermes был нативный tool.
- **Write:** единый writer-скрипт `wiki-write`, через который ВСЕ агенты пишут в вики → формат всегда валиден.

## Контекст (факты, проверено 21.08)

- Zvec-индекс: `/root/.zvec-wiki/index` — 1265 док, embedding completeness 100% (bge-m3 через Ollama :11434).
- Поиск: `zvec_search.py` → гибрид (вектор bge-m3 + FTS), RRF. CLI `zvec-wiki`.
- Вики: `~/Documents/wiki/` — markdown + frontmatter. Есть skill `memory-wiki-workflow` + `references/wiki-frontmatter-standard.md` (стандарт формата страниц).
- Официальный `zvec-ai/zvec-mcp-server` (⭐7) НЕ подходит: требует OpenAI-embedding + заточен на full CRUD коллекций. Нам нужен read-only поиск по готовому индексу bge-m3 (без OpenAI).

## Задачи

### A. MCP-сервер read-only (FastMCP)
1. В `~/.zvec-mcp/` создать сервер на **FastMCP** (`pip install fastmcp`), один tool:
   - `zvec_wiki_search(query: str, topk: int = 10, page_only: bool = False) -> list` — вызывает логику `zvec_search.py` (тот же bge-m3 через Ollama), возвращает JSON (page, category, title, score, snippet).
   - БЕЗ OpenAI-ключа (эмбеддинги через Ollama bge-m3).
2. Зарегистрировать в Hermes: `hermes mcp add` (stdio-транспорт) → tool `zvec_wiki_search` виден агенту.
3. Проверить: `hermes mcp test`, и что tool появляется в списке инструментов.

### B. Единый writer-скрипт `wiki-write`
1. Скрипт `wiki-write.sh` (или .py) в `~/.hermes/scripts/`, принимает:
   ```
   wiki-write --title "Название" --dir tech --description "..." \
              --tags "a,b" --related "[[x]]" --body-файл /tmp/body.md [--update path/to/existing.md]
   ```
   - `--dir`: tech|tools|projects|concepts|articles|misc (см. SCHEMA.md вики). Короткие ссылки в корень, длинные в `wiki/` (паттерн из memory-wiki-workflow).
   - Генерит корректный YAML frontmatter по стандарту.
   - Пишет файл `~/Documents/wiki/<dir>/<slug>.md`, slug из title (транслитерация/дефисы).
   - `--update` — обновляет существующую страницу (патчит frontmatter + тело), сохраняя связанные ссылки.
   - Добавляет строку в `index.md` (если новой страницы нет).
   - `git add -A && git commit -m "wiki: <title>" && git push origin master`.
   - **auto-rebuild:** после записи пересобрать zvec-индекс (вызвать `build_index.py`).
2. Проверить: создание новой страницы, обновление существующей, валидность frontmatter (`python3 /root/.hermes/scripts/wiki-health-check.py`), что Obsidian/индекс видят изменения.

### C. Интеграция с skill-ами
1. Обновить `memory-wiki-workflow` и `hindsight-mental-models`: правила «писать в вики ТОЛЬКО через `wiki-write`», искать через `zvec_wiki_search`.
2. Обновить агентов/автопилоты (Hermes Helper, Ночная рутина Шаг 9/10), которые пишут в вики, чтобы использовали `wiki-write`/`zvec_wiki_search`.

## Не делать
- НЕ удалять GBrain до cutover (MUL-881) — он остаётся бэкапом.
- НЕ менять источники правды вики — markdown-файлы остаются каноном, zvec только индекс (проекция).
- НЕ трогать официальный `zvec-ai/zvec-mcp-server` — свой лёгкий сервер, только read-only.

## Критерий готовности
- `hermes mcp test zvec` → tool `zvec_wiki_search` доступен и возвращает релевантные результаты.
- Новая страница создана и обновлена через `wiki-write`, frontmatter валиден, git закоммичен/запушен, zvec-индекс пересобран (поиск находит новую страницу).
- Скиллы обновлены, автопилоты пишут через `wiki-write`.