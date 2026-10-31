---
type: tool
title: e2e (TesterArmy) — агентные e2e-тесты для web и mobile
description: "Фреймворк e2e-тестирования: шаг описывается естественным языком, агент его выполняет, а следующий прогон реплеит записанные действия без вызовов модели, пока приложение не изменилось."
tags: [e2e, testing, ai-agents, playwright, mobile-testing]
related:
  - tech/lightpanda-browser
  - tech/webwright
  - tech/cloakbrowser
  - tools/browser-skill
source: https://github.com/tester-army/e2e
license: Apache-2.0
stars: 11184
ingested_at: '2026-10-18'
---

# e2e (TesterArmy)

**e2e** — фреймворк end-to-end тестирования веб- и мобильных приложений от организации TesterArmy (сайт `tester.army`, Discord). Ключевое отличие от обычных e2e-инструментов: **шаг теста описывается естественным языком, его выполняет AI-агент, а ассершены остаются детерминированными**.

- Репозиторий: https://github.com/tester-army/e2e
- Лицензия: Apache-2.0 · язык TypeScript
- npm: `e2e` (последняя версия на 18.10.2026 — `0.21.2`)

## Ключевая идея: агент → запись → реплей

Агентский шаг фиксируется вместе с проверяющей его ассершеной. При следующем прогоне записанные действия **воспроизводятся без обращений к модели**, пока приложение не изменилось. Модель вызывается только тогда, когда UI действительно «поехал».

Практические следствия:
- тесты остаются стабильными и **дешёвыми по токенам** (нет вызова модели на каждый прогон);
- тесты без агентских шагов модели не требуют вообще;
- модель — своя: подписка, API-ключ или локальная.

## Пример

```ts
// tests/checkout.e2e.ts
import { test, expect } from 'e2e';

test('a member upgrades to Pro', async ({ app, agent, screen }) => {
  await app.open('/settings/billing');

  await agent.act('upgrade the workspace to the Pro plan');
  await agent.assert('the invoice preview shows a prorated amount');

  await expect(screen.getByRole('status')).toContainText('Pro');
});
```

Быстрый старт: `npx e2e init` — спрашивает движок (web или mobile) и провайдера модели, затем пишет конфиг и пример теста.

## Пакеты

- `e2e` — SDK, runner и CLI
- `@e2e-dev/web` — браузерный движок: Chromium, Firefox, WebKit через Playwright
- `@e2e-dev/mobile` — iOS/Android: симуляторы и эмуляторы через agent-device
- `@e2e-dev/lightpanda` — **Lightpanda** (тот же headless-браузер на Zig, что стоит у нас, см. [[tech/lightpanda-browser]]), запускается на каждый прогон
- `@e2e-dev/github` — репортер: результат прогона комментарием в pull request
- `@e2e-dev/decision` — исполнители decision-модели для ограниченных семантических действий и ассершенов
- `@e2e-dev/kernel`, `@e2e-dev/smol` — хостовые браузеры (по умолчанию — тёплые Chromium-микроВМ на попытку)
- `@e2e-dev/limrun`, `@e2e-dev/eas`, `@e2e-dev/testmu` — хостовые iOS-симуляторы и Android-эмуляторы (TestMu = бывший LambdaTest)

В репозитории есть готовые примеры под Vite, Next.js, Astro, Expo, SwiftUI, Jetpack Compose, Kotlin Multiplatform, Flutter, .NET MAUI.

## Метрики и зрелость (на 18.10.2026)

| Показатель | Значение |
|---|---|
| Звёзды GitHub | 11 184 (на присланном скриншоте было 3.9k — рост очень быстрый) |
| Форки | 566 |
| Создан | 22.07.2026 (проекту ~3 месяца) |
| Релизов | 30, последний `0.21.2` (16.10.2026) |
| Активность | пуш в `main` в день проверки |

Рейтинг «Repository of the Day #1» на бейдже в README — собственный маркетинг через `star-history`, а не награда GitHub.

## Безопасность установки

В npm-пакете **нет `preinstall`/`postinstall`** — установка сама по себе код не запускает. Зависимости вменяемые: `zod`, `commander`, `oxc-parser`, `@ai-sdk/provider`, `@modelcontextprotocol/server`, `pixelmatch`. Но отдельные движки тянут бинарники и микро-ВМ, поэтому ставить — только осознанно и в песочнице.

## Оценка

Плюсы: сильная идея «агент + реплей» (экономия токенов и стабильность), единый API для web/iOS/Android, BYO-модель, Apache-2.0, есть репортер в PR.

Риски: версия `0.21` при трёхмесячной истории — API будет меняться; быстрый рост звёзд не равен зрелости; для мобильных часть движков — платные хостовые сервисы.

Статус: **в вики, не установлен** (правило: сначала вики, потом решение). Для базовой проверки своих страниц у нас уже есть Playwright Chromium (см. [[tech/webwright]], [[tools/browser-skill]]).
