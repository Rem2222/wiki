---
description: | Разработчик | Dimitri van Heesch |
tags: [concept]
---

# doxygen

**Doxygen** — генератор документации из исходного кода. Извлекает информацию из специально форматированных комментариев и генерирует документацию в различных форматах.

## Основные факты

| | |
|---|---|
| Разработчик | Dimitri van Heesch |
| Первый релиз | 26 октября 1997 |
| Текущая версия | 1.17.0 (апрель 2026) |
| Написан на | C++ |
| Лицензия | GPLv2 |
| Сайт | [doxygen.nl](https://doxygen.nl) |
| Репозиторий | [github.com/doxygen/doxygen](https://github.com/doxygen/doxygen) |

## Поддерживаемые языки

C/C++ (основной), Java, Python, C#, PHP, Fortran, Objective-C, VHDL, IDL и другие.

## Форматы вывода

- **HTML** (самый популярный)
- PDF (через LaTeX)
- RTF, PostScript
- Markdown
- CHM (Windows HTML Help)

## Ключевые возможности

- Парсит комментарии: `/** ... */`, `///`, `//!`
- Автоматические диаграммы: наследование, вызовы, collaboration
- Интеграция с [[tech/graphviz]] для визуализации
- Поддержка Markdown в комментариях

## GitHub интеграция

Doxygen часто используется в [[concepts/github-actions]] для автоматической сборки документации и деплоя на GitHub Pages. Доступны экшены:
- `doxygen-action`
- `Doxygen GitHub Pages Deploy Action`

См. также: [[concepts/github-actions]]

## Альтернативы

| Инструмент | Язык | Примечания |
|---|---|---|
| [[concepts/javadoc]] | Java | Аналог для Java |
| [[concepts/sphinx]] | Python | Особенно для Python |
| Doxygen | C/C++ | Стандарт де-факто |

## Ресурсы

- [Документация](https://doxygen.nl/manual/)
- [GitHub](https://github.com/doxygen/doxygen)