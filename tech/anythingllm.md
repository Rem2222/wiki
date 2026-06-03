---
description: AnythingLLM — это open-source замена связке Ollama + LangChain + векторная БД + UI. Один workspace вместо кучи отдельных сервисов.
tags: [tech]
---

# anythingllm

**Тип:** Open-source AI workspace (локальный RAG)  
**Канал:** Better Stack  
**Видео:** [I Replaced My Entire Local LLM Stack With This (AnythingLLM)](https://www.youtube.com/watch?v=pSYEcJTt4t4)  
**Когда:** ~2 месяца назад (март 2025)

---

## Суть

AnythingLLM — это open-source замена связке Ollama + LangChain + векторная БД + UI. Один workspace вместо кучи отдельных сервисов.

> *"You don't need to stitch together llama, LangChain, a vector database and some cheap UI just to make it usable."*

---

## Что умеет

- **Drag-and-drop RAG** — кидаешь PDF, код, документы — автоматически чанкует, эмбеддит и индексирует
- **Визуальный Agent Builder** — без кода, проводашь инструменты: SQL-запросы, веб-поиск через SERP API, файловые операции, MCP-серверы
- **Полный REST API** — можно встроить private RAG в свой SaaS или дашборд
- **Embed-виджет** — встраиваемый чат на сайт
- **VS Code расширение**
- **Desktop app** — проще онбординг для команды
- **Смена модели на лету** — без переиндексации, без рестарта

---

## Провайдеры

- Ollama / LM Studio (локальные)
- Grok / XAI
- OpenAI / Claude и др.

---

## Vector Stores

- **LanceDB** (дефолт)
- **PgVector** — переключение в один клик
- **Qdrant** — тоже поддерживается

---

## Workspace Architecture

- workspaces = изолированные проекты
- клиентская работа отделена от сайд-проектов
- можно поднимать per-client инстансы

---

## Agent Capabilities

- Web search через SERP API
- SQL queries
- File operations
- MCP servers
- Можно использовать LangChain внутри агента при желании

---

## Плюсы (что люди хвалят)

- API — легко встроить private RAG в продакшен
- Desktop-версия — быстрый онбординг новых членов команды
- **Смена модели посреди чата без потери контекста** — большая фича
- Open source → можно хостить у клиента, данные не уходят наружу
- Минимум боли по сравнению с raw LangChain

---

## Минусы (что люди ругают)

- RAG иногда нуждается в document pinning для идеального recall
- **500+ документов** — начинает есть RAM на слабых машинах
- Agent flows местами ещё beta, бывают edge cases
- Desktop-версия не для very low-end железа

---

## Сравнение с альтернативами

| Инструмент     | Плюсы                           | Минусы                       |
|----------------|---------------------------------|------------------------------|
| NotebookLM     | Простой чат с плагинами         | Слабый RAG, нет агентов      |
| PrivateGPT     | Простой document Q&A            | Нет агентов, нет API        |
| Diffuse / LangFlow | Мощные визуальные workflows | Heavy, переусложнены для простого RAG |
| **AnythingLLM**| RAG + агенты + API + desktop    | Ещё beta в edge cases        |
| LangChain      | Максимальная гибкость           | Всё надо строить самому      |

---

## Когда использовать

✅ **Да** — internal tools, client-facing private AI, production-grade RAG без написания с нуля  
✅ **Да** — агенты, которые реально поедут в прод  
❌ **Нет** — ultra-low-end железо, нужен максимально легковесный стек  
❌ **Нет** — хочешь build everything from scratch с raw LangChain (это fun, но не practical)

---

## Links

- GitHub: https://github.com/Mintplex-Labs/anything-llm
- Desktop app: в описании видео