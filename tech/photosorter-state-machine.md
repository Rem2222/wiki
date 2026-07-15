---
description: Полный автомат состояний Photo Sorter — приложения для сортировки фотографий по году снятия, матрица пересечений, dry run и организация файлов.
tags:
  - tech
  - photo
  - automation
  - state-machine
  - mermaid
related:
  - tools/photo-sorter
---

# Photo Sorter — автомат состояний

```mermaid
stateDiagram-v2
    [*] --> IDLE

    state IDLE {
        [*] --> adding_folders
        adding_folders --> ready_to_scan : добавлены 1+ папки
        ready_to_scan --> adding_folders : удалили все папки
    }

    IDLE --> SCANNING : нажали "Start Analysis"

    state SCANNING {
        [*] --> reading_file_list
        reading_file_list --> building_index : просканированы все папки
        building_index --> computing_overlap : построен индекс (name+size)
        computing_overlap --> SCANNED : overlap matrix готова
    }

    SCANNED --> SELECTING : показана матрица пересечений

    state SELECTING {
        [*] --> showing_overlap
        showing_overlap --> choosing_folders : пользователь видит % дублей
        choosing_folders --> ready_to_preview : выбраны папки для обработки
        ready_to_preview --> choosing_folders : изменили выбор
    }

    SELECTING --> ANALYZING_DATES : нажали "Preview by Year"

    state ANALYZING_DATES {
        [*] --> reading_exif
        reading_exif --> exif_found : EXIF дата есть
        reading_exif --> fallback_mtime : EXIF нет
        exif_found --> aggregating_years
        fallback_mtime --> aggregating_years
        aggregating_years --> DATE_ANALYZED : сводка по годам готова
    }

    state DATE_ANALYZED {
        [*] --> showing_distribution
        showing_distribution --> ready_to_copy : указана папка назначения
    }

    DATE_ANALYZED --> ORGANIZING_DRY : "Dry Run"
    DATE_ANALYZED --> CONFIRMING : "Organize!"

    state CONFIRMING {
        [*] --> asking_confirmation
        asking_confirmation --> ORGANIZING : подтвердили
        asking_confirmation --> DATE_ANALYZED : отменили
    }

    state ORGANIZING_DRY {
        [*] --> simulating_copy
        simulating_copy --> DRY_DONE : симуляция завершена
        DRY_DONE --> DATE_ANALYZED : можно запустить реальное копирование
    }

    state ORGANIZING {
        [*] --> copying_files
        copying_files --> deduplicating : файл уже есть → переименовать/пропустить
        deduplicating --> copying_files
        copying_files --> DONE : все файлы скопированы
    }

    DONE --> IDLE : начать заново
    DONE --> ANALYZING_DATES : изменить папку назначения

    state ERROR {
        [*] --> showing_error
        showing_error --> IDLE : исправить папки
        showing_error --> DATE_ANALYZED : вернуться к настройкам
    }

    SCANNING --> ERROR : папка не найдена
    ANALYZING_DATES --> ERROR : exiftool недоступен
    ORGANIZING --> ERROR : диск переполнен
```

## Легенда переходов

| Из | В | Условие |
|----|----|---------|
| `IDLE` | `SCANNING` | Есть папки, нажата кнопка |
| `SCANNING` | `SCANNED` | Индекс построен, overlap посчитан |
| `SCANNED` | `SELECTING` | Матрица показана пользователю |
| `SELECTING` | `ANALYZING_DATES` | Выбраны папки → «Preview by Year» |
| `ANALYZING_DATES` | `DATE_ANALYZED` | EXIF/mtime прочитаны, года агрегированы |
| `DATE_ANALYZED` | `ORGANIZING_DRY` | «Dry Run» |
| `DATE_ANALYZED` | `CONFIRMING` | «Organize!» |
| `CONFIRMING` | `ORGANIZING` | Подтвердил |
| `ORGANIZING_DRY` | `DATE_ANALYZED` | Сухой прогон показал результат |
| `ORGANIZING` | `DONE` | Все файлы скопированы |
| `DONE` | `IDLE` | «Начать заново» |
| `DONE` | `ANALYZING_DATES` | Сменить папку назначения |
| Любой `-->` | `ERROR` | Ошибка (нет папки, нет прав, нет места) |

## Что можно доработать потом

```mermaid
stateDiagram-v2
    [*] --> DONE_CLASSIFY : фото рассортированы по годам
    DONE_CLASSIFY --> CLASSIFYING : запустить CLIP

    state CLASSIFYING {
        [*] --> embedding_all_images
        embedding_all_images --> zero_shot_classify
        zero_shot_classify --> moving_to_categories
        moving_to_categories --> CLASSIFIED
    }

    CLASSIFIED --> REVIEW : confidence < threshold
    CLASSIFIED --> [*] : всё OK
    REVIEW --> [*] : вручную разобрал
```
