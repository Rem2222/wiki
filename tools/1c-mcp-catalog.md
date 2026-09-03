---
description: "Каталог MCP-серверов для 1С:Предприятие — 35+ серверов для AI-разработки, интеграции и DevOps"
tags: [tools, 1c, ai, mcp, devops, catalog]
source: https://github.com/Untru/1c-mcp
version: v2026.08.25
release_date: 2026-08-25
---

# 1c-mcp — Каталог MCP-серверов для 1С

## Что это

Комплексный справочник MCP-серверов (Model Context Protocol) для экосистемы **1С:Предприятие**. Позволяет AI-ассистентам (Claude, Cursor, VS Code Copilot, OpenCode и др.) взаимодействовать с 1С: читать метаданные, запускать тесты, анализировать код, управлять базами.

## Ключевые особенности

- **35+ MCP-серверов** Open Source + 5 коммерческих продуктов
- **4 архитектурных паттерна** подключения к 1С
- Матрица совместимости по транспорту и версиям 1С (8.2.13+ — 8.3.27.x)
- Описания сценариев использования с готовыми стеками серверов

## MCP-серверы по категориям

**IDE-интеграции:** EDT-MCP, CodePilot1C, 1C: Platform Tools MCP

**Фреймворки:** 1c_mcp, 1c-mcp-toolkit, http1c

**Метаданные и анализ кода:**
- mcp-1c, 1C_MCP_metadata, 1c-mcp-metacode (Neo4j)
- rlm-tools-bsl, mcp-1c-v1 (Qdrant RAG), 1c-templates-mcp

**Справка:** mcp-bsl-platform-context, onec-help-mcp, 1c-syntax-helper-mcp

**Тестирование:** bsl-mcp, mcp-bsl-lsp-bridge, bsl-analyzer (Rust, 180 диагностик), mcp-onec-test-runner (METR/YaXUnit)

**1С:Напарник:** 1c-buddy, spring-mcp-1c-copilot, 1c-ai-mcp (12 инструментов, Direct-режим)

**Учётные системы:**
- 1c-rest-mcp (OData), **ИИкона/1c-ai-connector** (RAG + MCP + агентская петля)
- ARQA MCP Server (коммерч.), 1c-accounting-mcp

**Графовый анализ:** bsl-graph (NebulaGraph)

**DevOps:** 1c-log-checker (ЖР/ТЖ + ClickHouse/Grafana), 1c-ai-sandbox, v8-runner (Rust), compose4mcp, v8-session-manager

## 4 архитектурных паттерна

1. **Прямое подключение к базе** — расширение + HTTP-сервис (mcp-1c, 1c_mcp, 1c-mcp-toolkit). Живые данные и метаданные.

2. **Работа с выгрузкой** — парсинг XML/EDT без работающей базы (1c-mcp-metacode, bsl-graph). Для CI/CD и code review.

3. **RAG/семантический поиск** — индексация в Qdrant/Neo4j (mcp-1c-v1, 1c-mcp-metacode, onec-help-mcp).

4. **Мост к инструментам** — MCP-обёртка над LSP, REST API (mcp-bsl-lsp-bridge, 1c-rest-mcp, 1c-buddy).

## 1C:Element (облачная платформа)

В v2026.08.25 добавлен раздел 1C:Element (1cmycloud.com):

- **elemctl** — CLI + MCP + Python-библиотека для Console API v2. ~20 инструментов: управление приложениями, сборка .xasm/.xlib, деплой, ветки. Experimental.
- **xbsl** — Линтер (161 правило), LSP-сервер, индекс проекта, документация, MCP-сервер. Experimental.

## AI Rules / Skills

| Проект | Описание |
|--------|----------|
| **ai_rules_1c** | Кросс-платформенный тулкит для 11+ AI-инструментов. 13 субагентов, 8+ SKILL-пакетов, ~25 файлов правил |
| **claude-code-skills-1c** | 117 skills + 40 правил для Claude Code. 536 regression-тестов |
| **cursor-1c-skills** | 116 skills + 40 правил для Cursor |
| **Unica** | Плагин для Codex/Claude Code. Skills для форм, метаданных, EPF/ERF, ролей, СКД |

## Коммерческие продукты

| Продукт | Описание | Цена |
|---------|----------|------|
| OneMCP | SaaS с семантическим поиском | Бета (free) |
| ARQA MCP Server | Бизнес-операции с 1С | Paid |
| OneRPA Suite | Docker-контейнеры | Paid |
| VibeCoding1C | Конструктор MCP без программирования | от 9 000 руб. |

## Что нового в v2026.08.25

- Раздел **1C:Element** (elemctl, xbsl)
- 116-117 skills для Claude Code и Cursor
- 1c-ai-mcp — 12 инструментов для 1С:Напарник
- ИИкона — агентская петля + RAG + MCP
- ai_rules_1c — кросс-платформенный тулкит (расширен из cursor_rules_1c)
