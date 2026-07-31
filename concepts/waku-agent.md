---
type: concept
title: Waku Agent — локальный AI-ассистент (Agent Harness на практике)
description: Open-source личный AI-ассистент от Shen Sean Chen. Полный цикл агента в ~95 строках Python: память → агент → инструменты → оценка → развитие навыков. SQLite, Telegram, голос.
tags: [agent, harness, loop-engineering, python, sqlite, telegram, eval]
related:
  - concepts/graph-engineering
  - concepts/hermes-knowledge-base
source: https://github.com/ShenSeanChen/waku-agent
stars: 662
ingested_at: '2026-07-29'
---

# Waku Agent

**Waku Agent** — персональный AI-ассистент, который полностью запускается на ноутбуке. Открытый исходный код от Shen Sean Chen (ex-MIT, ex-Google, основатель AutoManus.io).

Главная ценность проекта — **демонстрация Agent Harness и Loop Engineering на реальном коде**: основной цикл агента занимает ~95 строк на Python.

## Цикл агента

```
сообщение → поиск в памяти → запуск агента → вызов инструментов
    → трассировка → оценка → сохранение в память → развитие навыков
```

## Архитектура

- **Память:** один файл SQLite
- **Основной цикл:** ~95 строк Python (harness + loop)
- **Оценка:** детерминированные + LLM-as-a-judge, проверки перед релизом
- **Каналы:** Telegram-шлюз, голосовая активация
- **Инструменты:** Apple Calendar и другие
- **Навыки:** авто-развитие навыков по результатам оценок

## Демонстрация

В видео-демо ассистент:
1. Добавляет в календарь четвертьфинал чемпионата мира
2. Запоминает друзей пользователя
3. Отвечает через Telegram

## Почему интересно

Для изучения архитектуры минимального агента — это идеальный референс:
- Полный цикл agent loop без фреймворка
- Память на SQLite (как наш AgentMemory упрощённый)
- Eval-driven development (как наш Qworum/проверки)
- Telegram-шлюз (как наш Dex)

## Ссылки

- [GitHub: ShenSeanChen/waku-agent](https://github.com/ShenSeanChen/waku-agent) (662⭐)
- [Автор: @ShenSeanChen](https://github.com/ShenSeanChen)
- [X: @ShenSeanChen](https://x.com/ShenSeanChen)
- [AutoManus.io](https://automanus.io)
