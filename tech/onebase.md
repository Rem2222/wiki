---
description: Заметка о OneBase
tags: [tech]
related: [[tech/1c-mcp]] [[tech/cursor-rules-1c]] [[tech/metadata-1c]]
---

# onebase

**Open-source бизнес-платформа с 1С-подобным DSL** — лёгкая ERP/low-code платформа для пет-проектов, MVP и автоматизаций без лицензий.

- **Автор:** Иван Титов (ivanarama / ivantitov)
- **Лицензия:** MIT © 2026
- **Язык:** Go (1.23+)
- **Репозиторий:** https://github.com/ivanarama/onebase
- **Сайт:** https://onebase.ivantitov.tech/
- **Live demo (ПуТ):** https://demo.ivantitov.tech/
- **YouTube:** https://youtu.be/Fqy2nYqV914 — "I built an open-source '1C' alternative in 25 days using AI"
- **Статья:** https://infostart.ru/1c/articles/2694204/
- **Dev-документация:** https://github.com/ivanarama/onebase/blob/main/DEVELOPER.md

### Стек
- **Go** — один бинарник ~20MB
- **PostgreSQL 14+** / **SQLite** — на выбор
- **YAML** — метаданные конфигурации (git-friendly)
- **DSL (.os)** — 1С-подобный язык бизнес-логики

### Возможности
- 📄 Документы, справочники, регистры, проведение
- 🗣 Язык запросов в стиле 1С (ВЫБРАТЬ, РегистрНакопления.Остатки(), и т.д.)
- ⚙️ YAML-конфигурации метаданных
- 🗄 SQLite / PostgreSQL — перенос между движками `.obz`-файлом
- 🛠 Визуальный конфигуратор в браузере (дерево объектов, формы, регистры, права)
- 🐛 Отладчик и консоль запросов
- 🔄 REST API из коробки
- 🌐 Веб-клиент (авто-генерация форм)
- 📊 Диаграммы через ECharts
- 🔥 Hot reload для разработки
- 🖨 Печатные формы (ТабличныйДокумент)
- 📦 Типовые конфигурации: ПуТ, ПуТ-полная

### Системные требования
- Windows / Linux / macOS (включая arm64)
- Raspberry Pi 3+ / Orange Pi 3+ (4 ГБ ОЗУ)
- ~20MB дистрибутив, десятки MB RAM на холостом ходу
- На Orange Pi 4 ГБ — 5-10 параллельных баз + сайт

### Конфигурации
- **ПуТ** (Программа Управления Торговлей) — базовая: 4 справочника, 2 документа, 4 регистра, 4 отчёта
- **ПуТ полная** — 10 справочников, 11 документов, 6 регистров, 13 отчётов
- **В разработке:** ПУП, ПУЗ

### Команды CLI
| Команда | Описание |
|---------|----------|
| `onebase start` | Открыть лаунчер |
| `onebase ibases list` | Список баз |
| `onebase ibases add` | Добавить базу |
| `onebase dev --project ./app --db ...` | Dev-сервер с hot reload |
| `onebase run --project ./app --db ...` | Production-сервер |
| `onebase migrate` | Применить схему БД |
| `onebase init` | Создать заготовку проекта |

### Пример DSL
```os
Процедура ОбработкаПроведения()
  Движения.ПартииТоваров.Очистить();

  Запрос = Новый Запрос;
  Запрос.Текст = "ВЫБРАТЬ ДатаПоставки, КоличествоОстаток, СуммаОстаток
                  ИЗ РегистрНакопления.ПартииТоваров.Остатки()
                  ГДЕ Номенклатура = &Ном И КоличествоОстаток > 0
                  УПОРЯДОЧИТЬ ПО ДатаПоставки";
  Запрос.УстановитьПараметр("Ном", Строка.Номенклатура);
  // ...
КонецПроцедуры
```

### Статистика
- 328 коммитов, 128 тегов, 5 веток
- 8 звёзд, 2 форка (на момент 22.05.2026)
- Создан за ~25 дней с помощью ИИ (GLM 5.1, Sonnet, Opus)
- Развёрнут на Orange Pi 4 ГБ / Armbian / Cloudflare Tunnel

### Ссылки
- [GitHub](https://github.com/ivanarama/onebase)
- [Сайт](https://onebase.ivantitov.tech/)
- [Demo](https://demo.ivantitov.tech/)
- [YouTube](https://youtu.be/Fqy2nYqV914)
- [Статья на Infostart](https://infostart.ru/1c/articles/2694204/)
- [ПуТ (конфигурация)](https://github.com/ivanarama/PuT)