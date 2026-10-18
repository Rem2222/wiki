---
description: "REA (Reverse Engineer Anything) — MCP + CLI для реверса: нативные бинарники (Ghidra/Hopper/IDA), JS/Electron, .NET, Android/ADB, браузер, Frida-инструментация и разбор сохранённых захватов (pcap/HAR/SAZ/qlog). MIT. Разобрано 05.10.2026, обновлено 17.10.2026: v6.5.0, 289.5k⭐ (вирусный рост). PE через Ghidra на Linux — да; Frida — есть (проверено на Linux/Node); перехват сокетов «в реальном времени» — нет."
tags: [tools, reverse-engineering, mcp, ghidra, frida, decompiler, binary-analysis, cli]
created: 2026-10-05
updated: 2026-10-17
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

## Статус на 17.10.2026 (обновление разбора)

- **289 534 ⭐**, 72 880 форков, 1 118 открытых issue — **вирусный рост**: 05.10 было 4 265 ⭐.
  Проверено дважды 17.10 (GitHub API + HTML страницы). Уровень топ-20 GitHub; при этом
  `subscribers_count` всего 1 004 (аномально мало при таких звёздах — похоже на хайп
  кампанейского характера), но реальное использование подтверждено npm:
  **231 579 загрузок `rea-agents` за неделю** (06–12.10)
- **npm `rea-agents` v6.5.0**, 32 версии (было v3.2.1) — релизы почти каждые 1–2 дня
  (6.1.0 → 6.5.0 c 09 по 13.10), коммиты ежедневно, PR-номера под #3200
- Официальный сайт **rea.tools** — гайды и showcase (DX-Ball, Notion clipboard-bridge,
  TH04 bullet-ring — реверс Touhou 4; отсюда topic `touhou`)
- Автор `morluto`, MIT, `SECURITY.md`

### Что появилось с 05.10 (v3.2.1 → v6.5.0) — важно для кейса «сетевой стек игры»

1. **Frida-инструментация — ЕСТЬ** (была в roadmap «Later»): выбор local/remote цели,
   свои скрипты, сохраняемые сообщения. Верифицировано на Linux/Node; macOS, Windows,
   remote — не верифицированы. ⚠️ Автор прямо пишет: инструментация выполняет чужой
   код и **деструктивна**, не read-only.
2. **Разбор СОХРАНЁННЫХ захватов** — то, чего не хватало: pcap через TShark 4.x
   (+prlimit, Linux), HAR, Fiddler SAZ, QUIC qlog (aioquic), web-захваты; из HAR
   выводится «API-поверхность» (метод/origin/шаблон пути).
   → Схема для игры: снять трафик на Windows (Wireshark/Fiddler) → разобрать в REA на VPS.
3. **Нативные провайдеры расширены**: Ghidra-профили (MIPS, RISC-V, PowerPC, PSP,
   NMOS 6502, поиск по байтам, raw-входы), **присоединение к IDA** (Free 9.4 / Pro 9.3,
   read-only, база не сохраняется). **Windows Ghidra — всё ещё P0/экспериментально**.
4. **Setup-клиенты**: добавлены Qoder, Trae, ZCode, **DeepSeek Harness (DSH)**,
   Kimi Code, Factory Droid, WorkBuddy — DSH у Романа в работе, теперь штатно.
5. Новые слои: Android/ADB, Flutter APK, HarmonyOS HAP, Dart, WASM (WABT), SQLite-снимки,
   Rust `cargo-auditable`, Electron fuses, Go/pwntools, записанные краши (AArch64),
   записанные сигналы (sigrok, Linux).

### Прежний статус (05.10.2026, для истории)

- 4 265 ⭐, 441 форк, 72 открытых issue; npm 22 версии с 12.07.2026
- 5 контрибьюторов, автор `morluto` — 659 коммитов
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

- **Перехвата «в кадре» по-прежнему нет.** `capture-process` — только PTY (терминал,
  файловый снапшот, дерево процессов). Frida **есть** (инструментация + свои скрипты,
  с 6.x), но она не пишет трафик: сокеты/pcap REA только ЧИТАЕТ из уже сохранённых
  файлов (TShark/HAR/SAZ/qlog). Живые пакеты снимаешь сам (Wireshark/mitmproxy на Windows),
  разбор — в REA на VPS.
- **Нет Windows-запуска целей** — запускать игру и смотреть трафик надо на твоём ПК;
  REA подключается к сохранённым артефактам. Windows Ghidra — всё ещё экспериментальный P0.
- Ghidra работает headless-скриптом, GUI-состояние не читает.

**Итог по кейсу (обновлено 17.10.2026):** REA закрывает **статику** (что за протокол,
как кодирует, какие функции зовутся) и добавляет **разбор сохранённого трафика**
(pcap через TShark / HAR / Fiddler SAZ / qlog) — но сам трафик не пишет. Рабочий план:
снять пакеты на Windows (Wireshark/Fiddler) → скормить файл REA на VPS → получить разбор
полей, протокола, повторов и «API-поверхности». Frida — для точечной инструментации
(деструктивно, Windows-ветка не верифицирована).

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
