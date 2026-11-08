---
description: "Orca (stablyai/orca): приложение для работы с несколькими кодинг-агентами разом — каждый в своём git-worktree, мобильный компаньон, SSH-worktrees, Design Mode с отправкой HTML и CSS элемента в промпт. 113 135 звёзд, MIT, официально поддерживает Hermes Agent и DeepSeek Harness."
tags: [agents,orchestration,worktrees,desktop,gui,hermes-agent,terraform]
related:
  - tech/herdr
  - tech/ax
  - tech/control-plane-dlya-vseh-agentov-obzor-alternativ
  - tech/agent-desktop-ot-vercel-labs-computer-use-cherez-derevo-dostupnosti
  - tools/unslop-skill-ubirayuschiy-ii-vid-iz-interfeysa
  - tech/cherry-studio
updated: 2026-11-02
source: "https://github.com/stablyai/orca"
---

# Orca — GUI-оркестратор флота кодинг-агентов

## Что это

Orca (`stablyai/orca`) — GUI-приложение для работы с **флотом кодинг-агентов**: несколько агентов бок о бок, каждый в своём git-worktree, всё в одном окне. Девиз авторов — «The AI Orchestrator for 100x builders». Написано на TypeScript, лицензия **MIT**, сайт orca.dev, есть Discord и X, есть русский README среди девяти языков.

Ключевая формула: **«works with any CLI agent — if it runs in a terminal, it runs in Orca»**.

## Факты по репозиторию (проверено 02.11.2026)

- **113 135 ⭐**, 7 157 форков, **7 894 открытых issue**, TypeScript, MIT
- Создан 17.03.2026, последний push 02.11.2026, релиз **v1.4.246** от 02.11.2026
- Сборки: macOS (x64 и arm64, zip 265–275 МБ), Linux (rpm, deb, AppImage — x86_64 и arm64, 148–240 МБ), Windows (подпись от SignPath.io)
- Topic `yc-backed` — заявка на участие в YC, встречается в описании репозитория
- Мобильная часть: iOS в App Store (id6766130217) и Android APK; relay, который связывает телефон с десктопом, лежит в этом же репозитории в каталоге `cloud/` отдельным pnpm-workspace

## Поддерживаемые агенты

Список в README длинный, и в нём **оба наших агента**:

- **Hermes Agent** (ссылка на нашу документацию)
- **DeepSeek Harness** — тот самый «китаец»
- Claude Code, Codex, Grok, Cursor, GitHub Copilot, Muse, ZCode, OpenCode, MiMo Code, Amp, OpenClaude, Antigravity, Pi, oh-my-pi

## Что умеет

- **Parallel worktrees** — один промпт разложить на пять агентов, каждый в изолированном git-worktree, потом сравнить результаты и слить победителя
- **Terminal splits** — терминалы класса Ghostty с WebGL-рендерингом, бесконечные сплиты, scrollback, который выживает после перезапуска
- **Design Mode** — клик по любому элементу в реальном окне Chromium отправляет его HTML, CSS и обрезанный скриншот прямо в промпт агента
- **SSH worktrees** — агенты работают на мощной удалённой машине с полным редактированием файлов, git и терминалами; автопереподключение и проброс портов включены
- **GitHub и Linear нативно** — PR, issues и проектные доски внутри приложения, worktree открывается прямо из задачи
- **Annotate AI diffs** — комментарий к любой строке диффа уходит обратно агенту
- **Computer Use** — агент может управлять десктоп-приложениями и видимым интерфейсом, когда рабочему процессу нужна настоящая интерактивность
- **Account switcher и usage tracking** — расход и лимиты Claude и Codex, момент сброса, горячая смена аккаунтов без повторного логина
- **Quick open** — поиск по worktrees, файлам, агентам, командам и контексту репозитория
- **Уведомления и unread** — видно, когда агент закончил или ждёт внимания

## Где это в ряду того, что мы уже смотрели

- **Herdr** (`tech/herdr`) — терминальный рантайм и мультиплексор на Rust, Apache-2.0, 46 852 ⭐: tmux, переосмысленный под агентов, без GUI, с CLI и socket API. Orca — его GUI-противоположность: Electron-приложение на 150–275 МБ, зато с worktrees, мобильным компаньоном и Design Mode. Оба распознают одни и те же терминальные агенты, но Herdr про лёгкий рантайм на сервере, а Orca про рабочее место человека
- **agent-desktop** (`tech/agent-desktop-ot-vercel-labs-computer-use-cherez-derevo-dostupnosti`) — управление приложениями через дерево доступности ОС. У Orca есть свой Computer Use, но это дополнительная возможность, а не основа продукта. Зато **Design Mode** у Orca решает кусок задачи точнее: не «весь экран», а конкретный элемент с его HTML и CSS
- **AX от Google** (`tech/ax`) — облачный оркестратор с YAML-декларацией задач, «Kubernetes для агентов». Orca живёт на машине пользователя и не требует описывать задачи декларативно
- **Обзор control plane** (`tech/control-plane-dlya-vseh-agentov-obzor-alternativ`, от 11.10.2026) — там собраны кандидаты на роль панели управления агентами, крупнейший был Mission Control с 6 340 ⭐. **Orca в тот обзор не попал, хотя он на порядок крупнее любого кандидата из списка**: 113 135 ⭐ против 6 340
- **unslop** (`tools/unslop-skill-ubirayuschiy-ii-vid-iz-interfeysa`) — скилл, который правит «ИИ-вид» интерфейса. Связка очевидная: Design Mode в Orca даёт агенту точный элемент и его стили, а unslop знает, что с ними делать

## Применимость к нашему стеку

**Что подходит.** Оба наших агента в официальном списке поддержки. SSH worktrees — это ровно наш случай: Orca на рабочем ПК Романа, агенты работают на VPS по SSH. Мобильный компаньон отвечает на его привычку управлять всем с телефона: уведомление о завершении агента и follow-up прямо из приложения.

**Что ограничивает.** GUI-приложение требует графической сессии, поэтому на нашем VPS его не поставить (`DISPLAY` и `WAYLAND_DISPLAY` пустые) — VPS остаётся целью для SSH, а не хостом. Вес немалый: Electron-сборка 150–275 МБ против лёгкого Herdr на Rust.

**Что настораживает.** **7 894 открытых issue** — очень много даже для проекта со 113 тысячами звёзд; авторы пишут «we ship daily, so this list is perpetually behind», то есть темп сборки выше темпа разбора. Перед рабочим использованием стоит прочитать issue про работу с Hermes Agent и SSH.

**Статус: записано, НЕ устанавливалось.** Решение об установке — за Романом; ставится как обычное приложение на ПК.

## Плагины (обновление 08.11.2026)

У Orca есть каталог плагинов, включая community-раздел, который ставится из `Settings → Plugins`. Плагины объявляют манифест `orca-plugin.json` (manifestVersion 2, pluginApi 1) с полями `execution`, `capabilities` и `contributes.customEditors` — то есть видно, какие права запрашивает плагин, до установки.

Разобранный пример — [[tools/xlsx-editor-dlya-orca-pravka-knig-excel-s-sohraneniem-netronutyh-chastey-zip]]: редактор Excel-книг, который при сохранении переписывает только изменённые XML, а остальные части ZIP оставляет исходными байтами.

## Источники

- Репозиторий: https://github.com/stablyai/orca (113 135 ⭐, MIT, TypeScript, релиз v1.4.246 от 02.11.2026)
- Сайт и документация: https://orca.dev, https://www.onorca.dev/docs/
- README проекта (раздел Supported Agents, Features)
