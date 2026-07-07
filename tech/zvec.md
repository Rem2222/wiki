---
type: concept
title: Zvec
description: Встраиваемая векторная БД от Alibaba — SQLite-подход для векторного поиска. pip install, одна коллекция, один файл.
tags: [tech, vector-search, vector-db, opensource, alibaba, embedding, rag]
related: "[[tech/rag-projects-summary]] [[concepts/rag]] [[tech/1c-mcp]]"
ingested_via: 'mcp:put_page'
ingested_at: '2026-06-19T20:23:59.597Z'
source_kind: 'mcp:put_page'
---

# zvec

**GitHub:** https://github.com/alibaba/zvec
|**Звёзды:** 13,8K ⭐
|**Лицензия:** Apache 2.0
|**Автор:** Alibaba (боевое применение внутри группы)
|**Релиз:** v0.5.0 (12 июня 2026) — активная разработка, коммиты ежедневно

## Суть

Встраиваемая векторная БД — как SQLite для векторного поиска. Никаких серверов, конфигов, Docker. `pip install zvec` — и готово.

## Ключевые фишки

| Фича | Описание |
|------|----------|
| **Dense + Sparse векторы** | Оба типа, мульти-векторные запросы |
| **FTS (полнотекстовый поиск)** | Нативный, без внешних движков — добавляешь FTS индекс к любому строковому полю |
| **Гибридный поиск** | `MultiQuery` = векторное сходство + FTS + скалярные фильтры в одном запросе |
| **DiskANN** | On-disk индекс — данные на диске, RAM только для горячего кэша |
| **WAL (write-ahead logging)** | Данные не теряются при краше процесса или отключении питания |
| **Concurrent reads** | Много процессов читают одну коллекцию; пишет только один |

## SDK

| Язык | Установка |
|------|-----------|
| Python | `pip install zvec` (3.10–3.14) |
| Node.js | `npm install @zvec/zvec` |
| Go | Официальные биндинги |
| Rust | Официальные биндинги |
| Dart/Flutter | `flutter pub add zvec` |

## Платформы

Linux (x86_64, ARM64), macOS (ARM64), Windows (x86_64), **RISC-V**

## Пример за 1 минуту

```python
import zvec

schema = zvec.CollectionSchema(
    name="example",
    vectors=zvec.VectorSchema("embedding", zvec.DataType.VECTOR_FP32, 4),
)
collection = zvec.create_and_open(path="./zvec_example", schema=schema)
collection.insert([zvec.Doc(id="doc_1", vectors={"embedding": [0.1, 0.2, 0.3, 0.4]})])
results = collection.query(
    zvec.VectorQuery("embedding", vector=[0.4, 0.3, 0.3, 0.1]),
    topk=10
)
```

## Версия 0.5.0 (12 июня 2026)

- **FTS** — полнотекстовый поиск без внешних движков (Snowball stemmer, токен-фильтры)
- **Гибридный поиск** — MultiQuery: векторы + FTS + скалярные фильтры
- **DiskANN** — on-disk индекс, радикальное снижение RAM
- **Zvec Studio** — визуальный тул (просмотр, отладка запросов без кода)
- **Новые SDK** — Go, Rust, Dart/Flutter
- **RISC-V поддержка**

## Применение: 1C Help Server (RAG)

zvec можно использовать как замену Qdrant в HelpSearchServer для 1С. Вместо отдельного Docker-сервиса с векторной БД — встраиваемая zvec прямо в процесс Python-сервера.

**Как было:** HelpSearchServer (Docker) → Qdrant (ещё один Docker) — два сервиса, сетевое взаимодействие, конфиг, Healthcheck.

**Как стало:** HelpSearchServer (Docker или без) → zvec (pip install, файл на диске) — один процесс, zero конфигов, один файл БД.

**Плюсы замены:**
- Не нужно поднимать и мониторить ещё один Docker-контейнер
- Гибридный поиск из коробки (векторы + полнотекстовый) — без external search engine
- Меньше RAM — данные на диске, а не в памяти сервиса
- Проще бэкапить — один .zvec файл

**Минусы:**
- Нет сетевого доступа (только встраиваемая) — нельзя шарить БД между сервисами
- Нет репликации и шардирования (но для 1С Help Server не нужно)
- Сообщество/экосистема меньше чем у Qdrant

### Вердикт для 1С Help Server

zvec — **отличная замена Qdrant** для этого сценария. Объём данных (справочная информация по платформе 1С) не требует кластеризации, а гибридный поиск (векторы + полнотекстовый по названиям функций) — это именно то, что нужно для поиска по справке.

## Для чего ещё

Для небольших проектов, где поднимать Pinecone/Weaviate/Qdrant — оверхед.
zvec даёт векторный поиск «из коробки» без серверной инфраструктуры.