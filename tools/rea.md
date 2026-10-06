---
description: "REA (Reverse Engineer Anything) — MCP + CLI для реверса приложений: нативные бинарники (Hopper/Ghidra), JS/Electron, .NET, браузер. MIT, 4.2k⭐. Проверено 05.10.2026: PE-файл через Ghidra на Linux — поддерживается, динамический сетевой стек — НЕТ."
tags: [tools, reverse-engineering, mcp, ghidra, decompiler, binary-analysis, cli]
created: 2026-10-05
source: https://github.com/morluto/rea
related:
  - tools/aquilum
  - tech/jev-ultrafast
---

# REA — Reverse Engineer Anything

**Репо:** github.com/morluto/rea · **MIT** · TypeScript · npm `rea-agents` v3.2.1

Инструмент реверса под агентов: MCP-сервер + CLI. Модель
`Decompile → Understand → Recreate` — разобрать бинарник, объяснить как
работает фича, перенести похожее в свой проект. 116 инструментов в каталоге.

**Статус:** записано для дела, **не устанавливалось**. Ghidra, JDK 21 и REA на
VPS отсутствуют — шаг «Развёртывание» ниже проработан, но не выполнялся.

**Зачем зафиксировано:** Роман хочет разобрать сетевой стек Windows-игры,
чтобы понять как работает.

## Статус на 05.10.2026

- **4 265 ⭐**, 441 форк, 72 открытых issue (в основном рефакторинг-бэклог)
- MIT, `SECURITY.md` с приватным каналом отчётов — уровень зрелого проекта
- 5 контрибьюторов, автор `morluto` — 659 коммитов
- npm: 22 версии с 12.07.2026, CI есть, последний пуш 05.10.2026
- Node 22.19+ или 24.11+ (на VPS: v22.23.2 ✓)

## Что умеет (по провайдерам)

| Слой | Инструментов | Провайдер | Требует |
|---|---:|---|---|
| Нативные бинарники (Mach-O/ELF/**PE**) | 39 | Hopper или Ghidra | Hopper (платный, demo) **или** Ghidra 12.1.4 + JDK 21 |
| Управляемый PE/CLI (.NET) | 7 | свой, без загрузки | ничего |
| JavaScript / Electron | 5+2 | свой, без запуска | ничего |
| Браузер (структура, сеть, скриншоты) | 9 | CDP `127.0.0.1:9222` | Chrome-браузер |
| macOS-утилиты (Mach-O, plists, Swift) | 7 | локальные | macOS |
| Граф артефактов (APK/IPA/ASAR/ZIP) | 5 | свой | ничего |

Ключевые инструменты нативного слоя: `inspect-native-instruction`,
`resolve-native-call-targets`, `inspect-native-data-type` (Ghidra, ровно 22
read-only операции), `trace-native-values` (def-use граф по p-code),
`trace-native-ui-action`, дегенерация пакетной дегенерации.

## ✅ Твой кейс: сетевой стек Windows-игры

**Статический разбор — ВОЗМОЖЕН на VPS:**

1. Windows-игра — это PE (exe/dll). README: «Open Mach-O, ELF, **PE** …
   through Hopper or Ghidra». Ghidra на **Linux x64** поддерживается.
2. `windows-ghidra-p0.md` — это про запуск Ghidra **на Windows-хосте**
   (`unsupported_host`, не реализовано). К PE-файлам, разобранным **на Linux**,
   это не относится.
3. Путь: скопировать нужные exe/dll на VPS → Ghidra 12.1.4 + JDK 21 →
   REA подключается к Ghidra через `GHIDRA_INSTALL_DIR` → 22 read-only
   операции.

**Что можно вытащить:** сигнатуры вызовов (Winsock `ws2_32.dll`,
`connect`/`send`/`recv`), формат пакетов, протокол, шифрование, порядок
полей, тайминги ретраев — статически, через call-графы и `trace-native-values`.

**Чего НЕ будет — это главное ограничение:**

- **Динамического сетевого стека нет.** `capture-process` — это только PTY
  (терминал, файловый снапшот, дерево процессов). Сокетов, пакетов, таймингов
  в кадре — не пишет.
- **Нет перехвата сокетов/трафика.** В Roadmap «Later»:
  «Observe native apps at runtime: explore LLDB, **Frida**, system logs,
  native API tracing» — это ещё не сделано.
- **Нет Windows-запуска** — запускать игру и смотреть трафик надо на твоём
  ПК (Wireshark / mitmproxy), REA в этом не помогает.
- Ghidra работает headless-скриптом, GUI-состояние не читает.

**Итог по кейсу:** REA закрывает **статику** (что за протокол, как кодирует,
какие функции зовутся), но не закрывает **динамику** (что реально летает по
проводу). Реальный план — комбинация: REA на VPS для чтения кода + Wireshark
на твоём Windows для живых пакетов.

## Развёртывание на VPS

```bash
# Node 22.19+ уже есть (v22.23.2), Ghidra и Java — нет
curl -fsSL https://raw.githubusercontent.com/morluto/rea/main/install.sh | bash
# или: npm install --global rea-agents

# Ghidra 12.1.4 + JDK 21 — ставить руками, REA их не качает
export GHIDRA_INSTALL_DIR=/opt/ghidra_12.1.4_PUBLIC
export JAVA_HOME=/opt/jdk-21
rea doctor --json          # диагностика, ничего не меняет
rea providers --json
```

Подключение к Hermes (в `rea setup` Hermes нет, ручной MCP):
```json
{ "mcpServers": { "rea": { "command": "npx", "args": ["-y", "rea-agents@3.2.1", "mcp"] } } }
```

`setup` поддерживает Claude Code, Claude Desktop, Codex, Cursor, Gemini CLI,
Windsurf (Devin только детектирует). Сначала показывает план и бэкапит конфиг.

## Безопасность

- Мост: capability-токен + Unix-сокет, токены через приватные дескрипторы,
  не через argv/env
- Ghidra: изолированный временный проект, `HeadlessScript`, автоудаление
  при закрытии сессии, REA не трогает пользовательские проекты Ghidra
- Дисклеймер автора: «это не песочница; уже запущенный враждебный процесс
  под твоим юзером не защищён. Открытие недоверенного бинарника = парсинг
  Ghidra под твоими правами»
- Анализ локальный, бинарник наружу не уходит (модель данных самого агента
  — отдельная политика)
- `curl | bash` в установщике: аккуратный (`set -euo pipefail`, проверка
  версий, `--dry-run`), но для установки можно и `npm i -g rea-agents`

## Против альтернатив

- `ghidra-mcp` (~4 000 ⭐) и `GhidraMCP` — мост **только** к Ghidra.
  REA шире: один слой поверх Hopper/Ghidra + JS/Electron/.NET/браузер +
  workflow'ы + evidence. За счёт этого — настройка под каждую платформу.

## Спорные моменты

- **Топики `dsh` / `dsh-plugin` объявлены, в коде не найдены.** Проверено по
  1 444 файлам репо: `dsh` нет ни в README, ни в ChangeLog, ни в skills.
  Возможно плагин отдельным репо либо topic устарел. **DSH — в работе у
  Романа**, пригодится проверка.
- `skills/` содержит один скилл: `reverse-engineer-anything`.

## Источники

- 🌐 github.com/morluto/rea — репозиторий
- 🌐 README.md (raw) — Current status, Requirements, Roadmap
- 🌐 docs/windows-ghidra-p0.md — граница Windows-поддержки
- 🌐 docs/native-investigation.md — нативные операции Ghidra
- 🌐 docs/process-capture.md — что умеет capture-process (и чего не умеет)
- 🌐 SECURITY.md — модель безопасности
