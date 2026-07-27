---
type: tool
title: Lightpanda Browser — headless браузер для AI-агентов на Zig
description: Headless браузер, написанный с нуля на Zig (не форк Chromium). В 9× быстрее и в 16× меньше памяти, чем headless Chrome. CDP-совместим.
tags: [browser, headless, zig, web-scraping, ai-agents]
related:
  - tech/hermes-agent-masterclass
  - tech/paperclip
source: https://github.com/lightpanda-io/browser
license: AGPL-3.0
stars: 32700
ingested_at: '2026-07-27'
---

# Lightpanda Browser

**Lightpanda** — headless браузер, написанный с нуля на Zig для AI-агентов и веб-скрейпинга. Не форк Chromium, не патч WebKit, а новый браузер.

## Ключевые характеристики

- **Язык:** Zig (не C++ как Chromium)
- **Размер:** ~5 MB против ~200+ MB у Chrome
- **Совместимость:** CDP (Chrome DevTools Protocol) — работает с Playwright, Puppeteer, chromedp
- **Порт по умолчанию:** 9222
- **Лицензия:** AGPL-3.0

## Бенчмарки (933 реальные веб-страницы)

| Метрика | Lightpanda | Headless Chrome | Разница |
|---|---|---|---|
| Память (peak, 100 стр) | 123 MB | 2 GB | ~16× меньше |
| Время выполнения (100 стр) | 5 сек | 46 сек | ~9× быстрее |

## Быстрый старт

```bash
# Docker
docker run lightpanda/browser

# macOS (Homebrew)
brew install lightpanda-io/browser/lightpanda

# Arch Linux
yay -S lightpanda-nightly-bin
```

## Совместимость с Hermes

Hermes использует `browser_navigate` / `browser_click` и другие browser tools через headless Chrome. Lightpanda может заменить его как более лёгкая альтернатива через CDP на порту 9222.

## Ссылки

- [GitHub: lightpanda-io/browser](https://github.com/lightpanda-io/browser) (32.7k ⭐)
- [Discord](https://discord.gg/lightpanda)
- [Документация](https://lightpanda.io/docs)
