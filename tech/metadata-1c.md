---
description: Инструмент для генерации отчёта по конфигурации 1С:Предприятие из XML-выгрузки для DevOps/CI/CD
tags: [1c, devops, metadata, report, ci-cd]
source: https://github.com/norkins/metadata
author: norkins
license: MIT
created: 2026-05-27
updated: 2026-05-27
related: [[tech/1c-mcp]] [[tech/cursor-rules-1c]] [[tech/mcp-1c-setup]]
---

# Metadata 1C

Python-инструмент для генерации текстового отчёта (`Report.txt`) по XML-выгрузке конфигурации **1С:Предприятие**. Читает основную конфигурацию (`src/cf`) и опционально расширение (`src/cfe`).

**Назначение:** DevOps — последующая индексация, анализ и сравнение метаданных 1С в CI/CD-пайплайнах.

## Возможности

- CLI (`python generate_config_report.py --config <path>` или `generate-config-report`)
- Полная настройка через JSON (zero hardcode policy)
- Поддержка основной конфигурации и расширения
- Формат отчёта, близкий к штатному отчёту Конфигуратора 1С
- XML-derived overrides (автопостроение правил)
- Диагностика, статистика, логирование
- 42 unit-теста

## Архитектура

```
generate_config_report.py          # точка входа
generate_config_report/
  cli.py, config.py, diagnostics.py, generator.py
  metadata_model.py, object_registry.py
  property_extractors.py, report_writer.py
  settings.py, xml_reader.py, build_xml_overrides.py
  settings/defaults.json, settings/generated/
tests/
```

## Текущее состояние

- 42/42 тестов OK
- Расхождение с эталонным отчётом: ~151 строка из ~197,000
- Проект в активной разработке
