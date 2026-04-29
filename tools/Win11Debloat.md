---
title: "Win11Debloat"
description: ""
tags: [Windows, PowerShell, debloat, privacy]
related: 
---

# Win11Debloat

**URL:** https://github.com/raphire/win11debloat

## Что это
PowerShell-скрипт для очистки Windows 10/11 от предустановленного мусора.

## Возможности
- Удаление предустановленных bloatware-приложений
- Отключение телеметрии
- Удаление навязчивых элементов интерфейса
- Тонкая настройка Windows experience
- CLI-интерфейс для автоматизации
- Поддержка Windows Audit mode

## Установка (Quick method)
```powershell
& ([scriptblock]::Create((irm "https://debloat.raphi.re/")))
```

Или классика:
1. Скачать последний релиз: https://github.com/Raphire/Win11Debloat/releases/latest
2. Распаковать ZIP
3. Запустить `Run.bat` от администратора

## Важно
> Используйте на свой страх и риск. Скрипт не должен ломать OS, но возможны проблемы.

## Документация
https://github.com/raphire/win11debloat/wiki/
