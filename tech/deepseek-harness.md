---
description: DeepSeek Harness (dsh) — агентный harness от DeepSeek AI «Everything is a Plugin» на Cordis. Developer preview (13.08.2026), 37k⭐. Мониторинг обновлений: cron-задача.
tags: [deepseek, agent-harness, cordis, plugins, acp, trend]
related: [[tech/semantica]] [[tech/agent-harness-research]]
---

# DeepSeek Harness (dsh)

## Что это

Open-source агентный harness от DeepSeek AI. Архитектура **«Everything is a Plugin»** на фреймворке [Cordis](https://github.com/cordiverse/cordis): всё — адаптеры моделей, реестр тулов, лог сессий, сам agent-loop — плагины. Нет привилегированного ядра: расширяешь монтированием плагина, регистрации откатываются при выгрузке.

- **Репозиторий:** https://github.com/deepseek-ai/deepseek-harness
- **Статус:** developer preview, compatibility-breaking changes возможны (13.08.2026)
- **Stars:** 37 547 (за первый день!), forks 2 902, MIT, TypeScript
- **Запуск:** `npx @deepseek-ai/dsh web` → UI на 127.0.0.1:3080; `dsh headless` — одноразовый runner

## Архитектура

- **Профили/бандлы** — композиция плагинов при загрузке; шаблоны `web` и `headless`; патчи слоями (`cordis.patch.yml`)
- **События** — durable session events (переживают рестарт) + live agent events (`agent/*`) + capability events
- **Turn flow** — шаг = запрос модели + тулы; всё в append-only SessionEvent логе, из него же выводится контекст для модели
- **Capability seams** — заменяемые провайдеры: fs, subprocess, shell, terminal, LSP, web, skill, compaction, subagent, workflow, plan, guard, **self-modification** (агент монтирует свои плагины), hooks (Claude Code/Codex bridge)
- **Интерфейсы** — Web UI, ACP-сервер (Agent Client Protocol), JSON-RPC SDK (TypeScript + Python)
- **Песочница** — E2B POC + landlock-run (native, Linux)

## Сравнение с Hermes

| Аспект | dsh | Hermes |
|---|---|---|
| Архитектура | Всё плагины (Cordis) | Монолит + скиллы/плагины/hooks |
| Модели | Адаптер DeepSeek | 8 провайдеров, fallback-цепочки |
| Память | Session log | state.db + AgentMemory + GBrain |
| Самоизменение | self-modification пакет | скиллы + curator |
| Зрелость | Developer preview | v0.20.0 стабильный |

## Вывод

Developer preview — не ставить. Интересно как ориентир архитектуры (self-modification, plugin-first) и как возможный ACP-субагент из Hermes в будущем. DeepSeek целится в агентный рынок — у нас их модель в проде (deepseek-v4-flash).

## Мониторинг обновлений

Слежка вынесена в автопилот Multica **«Ночная рутина» (01:00 MSK)** — шаг 5.5 «Трендовые репозитории». Тихий watch: обычные коммиты/мелкие фиксы — одна строка в отчёте; задача с пометкой [TREND] создаётся только при прорыве:
- Выход из developer preview / первый стабильный релиз
- Рост звёзд ≥ 30% за сутки
- Крупный релиз с breaking changes (major)

Также отслеживаются: semantica, graphify, LFM2.5-VL-3B.

## Ссылки

- GitHub: https://github.com/deepseek-ai/deepseek-harness
- Cordis: https://github.com/cordiverse/cordis
- Discord: https://discord.gg/Ycq5dCaS4
