---
description: "Orca (stablyai/orca) — ADE для параллельной работы агентов: worktrees, Design Mode, mobile companion. Electron, MIT, ★53.6k."
tags: [ade,agents,electron,parallel,worktree,ide]
related: [[tech/backpass]] [[tech/cloudflare-computer]]
---

# orca-ade

# Orca (ADE)

**Orca** (`stablyai/orca`) — ADE (Agent Development Environment): десктопная среда для параллельной работы с флотом AI-агентов. Electron, TypeScript, **MIT**, **★53.6k** за полгода (создан 17.03.2026). Разработка Stably AI (Y Combinator). Сайт: onorca.dev

## Суть
Orca бесплатна и open-source; подписка на ADE не нужна — CLI-агенты работают на аккаунтах/подписках самого пользователя (Claude Code, Codex, OpenCode, Kimi Code, MiniMax и любые другие терминальные агенты). В каталоге 35 преднастроенных конфигураций.

## Ключевые фичи
- 🌳 **Parallel Worktrees** — один промпт → несколько агентов, каждый в изолированном git worktree; сравнение результатов и merge лучшего.
- 📱 **Mobile companion** — мониторинг и руление агентами с телефона (iOS/Android), пуши о завершении, follow-up'ы отовсюду.
- 💻 **Terminal splits** — Ghostty-класс терминалы: WebGL-рендеринг, бесконечные сплиты, scrollback, переживающий рестарт.
- 🎨 **Design Mode** — клик по UI-элементу в реальном Chromium отправляет его HTML+CSS+обрезанный скриншот прямо в промпт агента (замена скриншотам).
- 🔀 **GitHub & Linear нативно** — PR, issues, project boards в приложении; worktree открывается из любой задачи.
- 🔌 **SSH Worktrees** — агенты на удалённой « beefy» машине: полный файловый доступ, git, терминалы, авто-reconnect, port forwarding.
- 💬 **Annotate diffs** — комментарии на строки диффа уходят обратно агенту; ревью/правки/коммит не выходя из Orca.
- 🖱 Drag files to agents — файлы/картинки перетаскиваются прямо в промпт агента.
- 📋 Workspace Board — канбан запущенных задач, карточки перетаскиваются между статусами.
- Платформы: macOS, Windows, Linux + VPS через SSH.

## Репо
`stablyai/orca` · TypeScript · MIT · ★53.6k / 3.7k forks · https://onorca.dev · Discord + X @orca_build

## Связь со стеком Романа
Похожая идея реализована иначе в Multica (параллельные агенты, статусы, комменты агентам) — но Multica про автономную команду, Orca про интерактивную локальную разработку. Ценные паттерны для подсматривания:
- **Design Mode** (клик по UI → контекст в промпт) — нет ни в Multica, ни в Hermes.
- **Fan-out по worktrees** (один промпт N моделям, merge лучшего) — у нас делается delegate_task'ом, но без визуального сравнения.

**Решение:** НЕ ставить (Electron-деск под Windows, не VPS). Записано в вику по правилу «новое сначала в вику» (25.08.2026).
