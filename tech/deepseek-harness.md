---
description: DeepSeek Harness (dsh) — агентный harness от DeepSeek AI «Everything is a Plugin» на Cordis. Developer preview (13.08.2026), 94.8k⭐ за 2 дня (вирусный рост +145%/сутки). Мониторинг: Ночная рутина (шаг 5.5).
tags: [deepseek, agent-harness, cordis, plugins, acp, trend]
related: [[tech/semantica]] [[tech/agent-harness-research]]
---

# DeepSeek Harness (dsh)

## Что это

Open-source агентный harness от DeepSeek AI. Архитектура **«Everything is a Plugin»** на фреймворке [Cordis](https://github.com/cordiverse/cordis): всё — адаптеры моделей, реестр тулов, лог сессий, сам agent-loop — плагины. Нет привилегированного ядра: расширяешь монтированием плагина, регистрации откатываются при выгрузке.

- **Репозиторий:** https://github.com/deepseek-ai/deepseek-harness
- **Статус:** developer preview, compatibility-breaking changes возможны (13.08.2026); стабильного релиза нет
- **Stars:** 94 854 (15.08.2026), forks 8 743, MIT, TypeScript
- **npm:** `@deepseek-ai/dsh` 0.1.0-rc.6
- **Запуск:** `npx @deepseek-ai/dsh web` → UI на 127.0.0.1:3080; `dsh headless` — одноразовый runner; из исходников — `pnpm install && pnpm run build && pnpm dsh web`
- **Docker/deploy-гайд:** официального нет (только npm и сборка из исходников)

## Архитектура

- **Профили/бандлы** — композиция плагинов при загрузке; шаблоны `web` и `headless`; патчи слоями (`cordis.patch.yml`)
- **События** — durable session events (переживают рестарт) + live agent events (`agent/*`) + capability events
- **Turn flow** — шаг = запрос модели + тулы; всё в append-only SessionEvent логе, из него же выводится контекст для модели
- **Capability seams** — заменяемые провайдеры: fs, subprocess, shell, terminal, LSP, web, skill, compaction, subagent, workflow, plan, guard, **self-modification** (агент монтирует свои плагины), hooks (Claude Code/Codex bridge)
- **Интерфейсы** — Web UI, ACP-сервер (Agent Client Protocol), JSON-RPC SDK (TypeScript + Python)
- **Песочница** — E2B POC + landlock-run (native, Linux)

## Вирусный рост (15.08.2026)

**38 630 → 94 829 звёзд за сутки (+145%).** Причина — не новый релиз, а накрытие волной хайпа после анонса 13.08:

- **13.08.2026:** публичный запуск developer preview v0.1 + MIT-лицензия + публикация на npm (`@deepseek-ai/dsh` rc.3→rc.6 в тот же день). Репозиторий создан 13.08, за первый день 37.5k⭐, forks 2.9k.
- **HN:** тред «DeepSeek Harness developer preview» (718 pts, ~300 комментариев) + официальный сайт deepseek.com/harness.
- **Китайские медиа** (Sina, aihub.cn, jdon и др.) — «Model + Harness = Agent», позиционирование против Claude Code / OpenAI Codex.
- **Контекст:** в тот же вечер DeepSeek выпустила V4-Pro и пересмотрела API-цены (в т.ч. рост до +1114%) — день стал «тройным анонсом», что усилило внимание к harness.
- **Экосистема:** появился топик `dsh-plugin`, сторонние гайды (deepseek-code.com, dsh.so, explainx.ai), растёт комьюнити.

**Статус при этом не изменился:** стабильного релиза нет (GitHub releases пусто), README прямо предупреждает «THERE WILL BE COMPATIBILITY-BREAKING CHANGES», официального Docker-гайда нет. Рост — чисто хайповый, а не следствие нового функционала (последний коммит всё ещё 13.08).

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

**Решение по интеграции (15.08.2026):** пока НЕ подключать в локальные воркфлоу — нет стабильного релиза, README предупреждает о breaking changes, официального Docker-гайда нет, а у нас уже есть Hermes (зрелый) как основной harness. Следить дальше; сигналы для активной интеграции: выход стабильного релиза, официальный Docker/deploy-гайд, появление готовых dsh-плагинов под наши задачи. Полезное из архитектуры уже учитываем: plugin-first, self-modification, ACP-интерфейс.

## Мониторинг обновлений

Слежка вынесена в автопилот Multica **«Ночная рутина» (01:00 MSK)** — шаг 5.5 «Трендовые репозитории». Тихий watch: обычные коммиты/мелкие фиксы — одна строка в отчёте; задача с пометкой [TREND] создаётся только при прорыве:
- Выход из developer preview / первый стабильный релиз
- Рост звёзд ≥ 30% за сутки
- Крупный релиз с breaking changes (major)

Также отслеживаются: semantica, graphify, LFM2.5-VL-3B.

**15.08.2026 — [TREND] сработал критерий «рост звёзд ≥ 30% за сутки»** (+145%: 38 630 → 94 829). Разбор в секции «Вирусный рост»; вердикт: хайп, а не новая функциональность, статус прежний (preview). Трекер обновлён.

## Ссылки

- GitHub: https://github.com/deepseek-ai/deepseek-harness
- Cordis: https://github.com/cordiverse/cordis
- Discord: https://discord.gg/Ycq5dCaS4
