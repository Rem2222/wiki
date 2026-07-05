---
type: concept
title: Pxpipe Context Compression
ingested_via: 'mcp:put_page'
ingested_at: '2026-07-05T09:34:43.871Z'
source_kind: 'mcp:put_page'
---

---
description: pxpipe — proxy, сжимающий токены контекста рендерингом текста в PNG (~59-70% экономии). 2.2k ⭐, npm-пакет.
tags: [tech, llm-tools]
related: [[tech/supermemory-agent-memory]] [[tech/agent-memory-research-2026]]
---

# pxpipe-context-compression

**Репозиторий:** https://github.com/teamchong/pxpipe
**NPM:** `pxpipe-proxy`
**Звёзды:** ~2.2k ⭐
**Форки:** 140
**Коммитов:** 311 (активный, последний 6 часов назад)

## Суть

Прокси, который перехватывает запросы к LLM API и конвертирует объёмные части контекста (system prompt, tool docs, старую историю, tool results) в компактные PNG-изображения перед отправкой.

Изображение стоит фиксированное число токенов (по пикселям), независимо от того, сколько текста внутри. Dense content (код, JSON, вывод) выходит ~3.1 chars/image-token против ~1 char/text-token.

## Экономия

| Метрика | Значение |
|---------|----------|
| Системный промпт + tool docs | 48k chars → 2.7k image-tokens (vs 25k text-tokens) |
| End-to-end на Claude Code | −59%…−70% токенов |
| SWE-bench Lite | 10/10 оба рукава при −65% request size |
| SWE-bench Pro | 14/19 ON vs 15/19 OFF, вердикты совпали 18/19 |

## Запуск

```bash
npx pxpipe-proxy                                # порт 47821
ANTHROPIC_BASE_URL=http://127.0.0.1:47821 claude  # или hermes
```

Дашборд: http://127.0.0.1:47821/ — токены сэкономленные, конвертации side-by-side, kill switch.

## Как работает

```
tool_result string → wrap at 1928px columns → pack ~92,000 chars/page → PNG[]
```

Прокси intercepts `/v1/messages`, переписывает bulk-блоки в изображения, сохраняя cache-friendly порядок (prefix cache работает). Потери есть: exact strings (ID, хэши, секреты) в картинках читаются хуже — надо держать их текстом.

## Бенчмарки точности

| Тест | Модель | Text | pxpipe |
|------|--------|:----:|:------:|
| Novel arithmetic | Fable 5 | 100% | **100%** |
| Novel arithmetic | Opus 4.8 | 100% | 93% |
| Gist recall (98/arm) | Fable 5 | 98/98 | **98/98** |
| State tracking | Fable 5 | 18/18 | **18/18** |
| Hex recall, dense render | Fable 5 | — | **13/15** |
| Hex recall, dense render | Opus 4.8 | 15/15 | **0/15** |

## Ограничения

- **Lossy**: exact 12-char hex strings читаются 13/15 на Fable, 0/15 на Opus
- **Byte-exact значения** (ID, хэши, секреты) должны оставаться текстом
- Для subagent на не-allowlisted моделях — pass-through (настраивается через `PXPIPE_MODELS`)
- Выгодно только на dense content (код, JSON), на разреженном прозе может проигрывать

## Статус

🔎 На рассмотрении. Может быть полезен для сжатия статичного контекста (MEMORY.md, USER.md, tool docs) при работе через Hermes, освобождая место под живой диалог.

## Ссылки

- [GitHub](https://github.com/teamchong/pxpipe)
- [NPM](https://www.npmjs.com/package/pxpipe-proxy)
