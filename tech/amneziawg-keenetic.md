---
description: "Как установить AmneziaWG 3.0 на Keenetic (не застрять на обычном WireGuard)"
tags: [tech, vpn, keenetic, awg, networking]
source: https://share.google/3tmM4KVXdatexWGbK
source_date: 2026-08-28
---

# AmneziaWG 3.0 на Keenetic

## Суть проблемы

С AmneziaWG 3.0 на Keenetic есть один неочевидный момент. Просто загрузить новый .conf в штатный WireGuard роутера **недостаточно**. Встроенная реализация Keenetic умеет работать с предыдущими поколениями AmneziaWG, но специфические параметры AWG 3.0 требуют либо отдельного модуля ядра версии 3.x, либо обработки через sing-box.

**Вместо ручной сборки конфигурации в веб-интерфейсе** — ставить **AWG-Manager**.

## Что такое AWG-Manager

AWG-Manager работает поверх Entware, принимает обычные файлы .conf и ссылки vpn://, создаёт туннели, настраивает маршрутизацию и сразу показывает, какой вариант AmneziaWG реально запущен.

## Совместимость

- KeeneticOS 4.x и 5.x
- Архитектуры: mipsel-3.4, mips-3.4, aarch64-3.10
- Процессор → архитектура Entware:
  - EcoNet → mips
  - MT7628, MT7621 → mipsel
  - MT7622, MT7981, MT7988 → aarch64

## Подготовка

1. **Установить компоненты** в Keenetic (Управление → Настройки системы → Изменить набор компонентов):
   - WireGuard VPN
   - OPKG

2. **USB-накопитель** (ext4) — для Entware. На KeeneticOS 5.x можно отформатировать через веб-интерфейс.

3. **Сохранить** startup-config и резервную копию текущей конфигурации.

4. **Проверить архитектуру**: WebCLI → `show version` → arch.

## Установка Entware

Открыть WebCLI: http://192.168.1.1/a

```bash
opkg disk
# нажать Tab — покажет доступные накопители
```

Для MIPS:
```bash
opkg disk <накопитель> https://bin.entware.net/mipssf-k3.4/installer/mips-installer.tar.gz
```

Для MIPSLE:
```bash
opkg disk <накопитель> https://bin.entware.net/mipselsf-k3.4/installer/mipsel-installer.tar.gz
```

Для ARM64:
```bash
opkg disk <накопитель> https://bin.entware.net/aarch64-k3.10/installer/aarch64-installer.tar.gz
```

Если Entware ставится во встроенную память — использовать `storage:` вместо имени накопителя.

**Проверка:**
```bash
show log | grep Opkg::Manager:
# Должно быть: [5/5] "Entware" installed!
```

## Установка AWG-Manager

Подключиться к Entware SSH:
```bash
ssh root@192.168.1.1 -p 222
# пароль: keenetic (сразу сменить через passwd)
```

Установка AWG-Manager:
```bash
opkg update
wget -qO- http://repo.hoaxisr.ru/install.sh | sh
```

Скрипт сам определит архитектуру, подключит репозиторий, установит пакет и запустит службу.

**Веб-панель AWG-Manager:** http://192.168.1.1:2222

## Что именно для AmneziaWG 3.0

Для AWG 3.0 нужно:
- Либо отдельный модуль ядра версии 3.x
- Либо обработка через sing-box (рекомендуется)

AWG-Manager определяет, какой вариант AWG реально запущен, и показывает это в интерфейсе.

## Дисклеймер

Материал предназначен для легальной настройки собственной сети и собственных VPN-серверов. Соблюдайте законодательство своей страны.
