---
description: https://www.youtube.com/watch?v=2LvuxpXNNw8
tags: [video]
related: [[concepts/tradingagents]]
---

# claude-tradingview-connection

**Тег:** #AIтрейдинг #TradingView #Claude #automation

## Видео
https://www.youtube.com/watch?v=2LvuxpXNNw8
Автор: arden | Дата: Apr 19, 2026 | 63K просмотров

## Суть
Как подключить Claude Code к TradingView для автоматизированной торговли. Называют "Game Changer" — Claude читает графики и автоматически исправляет код.

## Что даёт подключение

1. **Claude видит графики** — анализирует TradingView в реальном времени
2. **Автоматически пишет/правит код** — читает экран, находит ошибки, фиксит
3. **Исполняет сделки** — через BitGet (или другие биржи)
4. **Полный цикл** — анализ → код → исполнение без ручного вмешательства

## Архитектура

```
Claude Code ←→ TradingView Desktop (CDP port 9222)
                    ↓
              BitGet API
                    ↓
              Авто-трейдинг
```

## Как работает

Claude подключается к TradingView Desktop через **Chrome DevTools Protocol (CDP)** на порту 9222. TradingView запускается со специальным флагом:

```bash
--remote-debugging-port=9222
```

Через CDP Claude:
- Читает данные с графика (индикаторы, TPO, объёмы)
- Определяет паттерны
- Генерирует сигналы
- Отправляет ордера на биржу

## Репозиторий

https://github.com/jackson-video-resources/claude-tradingview-mcp-trading

One-shot prompt → Claude сам настраивает всю систему:
- Клонирует репозиторий
- Подключает BitGet
- Настраивает TradingView
- Коннектит всё вместе

## Поддерживаемые биржи

- **BitGet** — основная (рекомендуемая в видео)
- Coinbase
- (и другие через MCP-адаптеры)

## Фичи

- Чтение TradingView chart в реальном времени
- Автоматическое исполнение ордеров
- Настройка торговых предпочтений
- Поддержка Forex, Futures, Stocks, Crypto

## Limitations (April 2026)

- Built-in TPO indicator имеет ограничения в текущем MCP
- Нужно запускать TradingView Desktop (не веб-версия)
- Требуется авторизация на бирже

## Канал автора

https://t.me/arden_YT — бесплатный канал о крипте и финансах