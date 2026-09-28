---
description: "Cognee — open-source платформа памяти для AI-агентов: ECL-пайплайн, knowledge graph + векторный и реляционный поиск; кандидат на единый memory-провайдер."
tags: [memory,cognee,agent-memory,knowledge-graph,rag,mcp]
related: [[patterns/vibe-coding-memory-architecture]] [[patterns/1c-multi-agent-development]] [[ops/services/hindsight]]
---

# Cognee

## Что это

**Cognee** ([topoteretes/cognee](https://github.com/topoteretes/cognee)) — open-source платформа долгосрочной памяти для AI-агентов: даёт агентам персистентную память между сессиями через комбинацию графа, векторного и реляционного поиска. Развёртывается self-hosted (Docker, on-prem) или как облачный сервис (Cognee Cloud) с MCP-интеграцией для подключения агентов.

Ключевая идея — пайплайн **ECL (Extract → Cognify → Load)**: данные сначала извлекаются и нормализуются, затем «когнифицируются» (обогащаются сущностями и связями), затем загружаются в knowledge graph и векторное хранилище — вместо наивного RAG «чанки → эмбеддинги».

## Почему страница появилась в вике

- [[patterns/vibe-coding-memory-architecture]] — паттерн «Cognee (graph) + OpenViking (RAG) как MCP-серверы» для любых агентов.
- [[patterns/1c-multi-agent-development]] — shared memory координатора и агентов разработки 1С (Cognee + OpenViking).
- Кандидат на единый memory-провайдер для VPS / домашнего ПК / телефона — оценка Романа (2026-08/09) на фоне проблем стабильности Hindsight и тяжести GBrain.

## Фишка

Не «ещё один векторный поиск»: граф связей между фактами (кто, что, когда, почему) переживает смену моделей и репозиториев — память не теряется вместе с подпиской на конкретную LLM.

## Ссылки

- GitHub: https://github.com/topoteretes/cognee
- Сайт: https://www.cognee.ai/
