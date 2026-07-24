---
description: Supermemory — self-hosted memory & context for AI agents (28k ⭐). Graph engine, локальные embeddings, извлечение фактов, Memory API. Полностью локально.
tags: [tech]
related: "[[tech/agentmemory-vs-current]] [[tech/hermes-memory-setup-vps]] [[tech/tencentdb-agent-memory]] [[tech/agent-memory-research-2026]]"
---

# supermemory-agent-memory

**Репозиторий:** https://github.com/supermemoryai/supermemory
**Звёзды:** ~28k ⭐
**Запуск:** `npx supermemory local` или `supermemory-server`
**Лицензия:** MIT

## Суть

Self-hosted Memory API для AI-агентов. Поднимает полный стек: graph engine, локальные embeddings, извлечение фактов, user profiles. Всё работает локально, модель выбирается (OpenAI, Anthropic, Gemini, Groq или Ollama).

## Архитектура

| Компонент | Описание |
|-----------|----------|
| **Graph engine** | Хранение и связывание фактов |
| **Embeddings** | Локальные (свои) |
| **Extraction** | Извлечение фактов из диалогов |
| **User profiles** | Профили пользователей |
| **Memory API** | REST API для чтения/записи |

## Интеграции

- Claude Code
- Cursor
- Codex
- Hermes Agent
- LangChain
- Vercel AI SDK

Суть: агент может помнить проект, предпочтения, прошлые решения и доставать нужный контекст между сессиями.

## Сравнение с AgentMemory (нашим)

| Параметр | Supermemory | AgentMemory |
|----------|-------------|-------------|
| Запуск | `npx supermemory local` | Docker Compose (III engine) |
| Graph engine | ✅ | ✅ (knowledge graph) |
| Локальные embeddings | ✅ | ✅ (consolidate pipeline) |
| Извлечение фактов | ✅ | ✅ (extract_facts + reflect) |
| Memory API | REST | REST (Hermes API :8642) |
| MCP сервер | ? | ✅ (@agentmemory/mcp) |
| Storage | Шифрованное локальное | PostgreSQL + slots |
| Модели | OpenAI / Anthropic / Gemini / Groq / Ollama | Любые через Hermes provider chain |
| Интеграция с Hermes | Через Memory API | Нативная (memory provider) |
| Звёзды | ~28k ⭐ | ~1.2k ⭐ |

## Статус

🔎 На рассмотрении. Не запущен — может конфликтовать по портам с AgentMemory. Требует изолированного тестирования.

## Ссылки

- [GitHub](https://github.com/supermemoryai/supermemory)
- [Документация](https://github.com/supermemoryai/supermemory)
