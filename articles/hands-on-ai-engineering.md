---
description: Обзор репозитория Hands-On AI Engineering (github.com/Sumanth077) — коллекция 30+ практических AI-проектов: RAG, AI-агенты, MCP, OCR, мультимодальные системы. 1.5k ★, активное сообщество.
tags: [articles, ai-engineering, rag, mcp, agents, reference]
related: [[concepts/rag]] [[concepts/mcp]] [[tech/rag-projects-summary]] [[tech/mcp-projects-summary]]
---

# Hands-On AI Engineering — коллекция AI-проектов

**Репозиторий:** [Sumanth077/Hands-On-AI-Engineering](https://github.com/Sumanth077/Hands-On-AI-Engineering)  
**Звёзд:** 1.5k ★ | **Форков:** 455 | **Коммитов:** 188 | **Лицензия:** MIT

Репозиторий от сообщества [AI Engineering](https://aiengineering.beehiiv.com/) — коллекция production-ready проектов, каждый с полным кодом, README, `requirements.txt` и `.env.example`.

---

## Категории проектов

### 🤖 AI Agents (~20 проектов)
Самая крупная секция. Мультиагентные системы на разных фреймворках (LangChain, Agno, Haystack, Google ADK, smolagents, OpenClaw).

**Примечательные:**
- **Multi-Agent Financial Analyst** — команда агентов для финансового анализа
- **GitHub Intelligence Agent** — через MCP + Haystack, Gemini 3 Flash
- **Eagle Eye** — PR review через Telegram + OpenClaw + GitHub MCP
- **Hotel Finder Agent** — Trivago MCP + qwen через Orq.ai
- **Agentic SQL Search** — natural language → SQL через Gemma 4
- **Stock Portfolio Analyst** — Agno + DeepSeek-V4-Flash + YFinance
- **Multi-Agent Research Assistant** — AG2, три специалиста
- **Self-Reflective Agentic RAG** — LangGraph с grading/rewriting
- **Marketing Strategy Agent** — Market Analyst + Strategy Officer + Creative Director
- **Agent Discovery Agent** — поиск агентов по 5 протоколам (MCP, NANDA, A2A и др.)

### 📚 RAG Applications (11 проектов)
Полный спектр RAG-архитектур: от простого Q&A до GraphRAG и Reasoning RAG.

**Стек:** ChromaDB (6/11), Mistral (5/11), LangChain (4), Agno (3), Streamlit (9/11)

**Ключевые проекты:**
- **HyDE RAG** — гипотетические документы вместо прямого эмбеддинга запроса
- **GraphRAG Knowledge System** — knowledge graph + community detection (NetworkX)
- **Hybrid RAG System** — параллельная индексация в граф и векторное хранилище
- **Clinical RAG with ADE** — LandingAI ADE для визуального парсинга медицинских PDF
- **Vision RAG** — поиск по визуальным сегментам, не по тексту
- **RAG Agent with Database Routing** — маршрутизация по трём Qdrant-базам + web fallback
- **Reasoning RAG** — двух-агентный RAG с live reasoning trace

### 🎬 Multimodal (6 проектов)
- **GLM-OCR Pro** — структурированное извлечение через Ollama
- **Video Understanding Agent** — YouTube → chapters + takeaways
- **Multimodal RAG** — текст + URL + PDF + image + audio + video в ChromaDB
- **Image Question Answering** — PDF → страницы → визуальные вопросы через Gemma 4

### 📸 OCR (3 проекта)
- **Image-to-Structured-Data** — Mistral Large 3 + Instructor → JSON
- **LaTeX Formula OCR** — локальная VLM → LaTeX
- **Medical Prescription Digitizer** — RxNorm валидация лекарств

### 🎧 Audio (1 проект)
- **Music Explorer** — чат с аудио/YouTube через Gemini 3 Flash

---

## MCP-интеграции

Обнаружено **4 проекта** с MCP:

| Проект | MCP-сервер | Транспорт | LLM |
|--------|-----------|-----------|-----|
| GitHub Intelligence Agent | GitHub MCP (api.githubcopilot.com/mcp) | Streamable HTTP | Gemini 3 Flash |
| Hotel Finder Agent | Trivago MCP (mcp.trivago.com/mcp) | Streamable HTTP | qwen3.6-flash |
| Eagle Eye | GitHub MCP (локально) | stdio (npx) | MiniMax M2.7 |
| Agent Discovery Agent | Registry Broker API | REST | Gemini 3 Flash |

Три подхода к MCP: удалённый HTTP, локальный stdio, REST-прокси.

---

## Выводы и relevance

1. **RAG-архитектуры** — репозиторий покрывает практически все современные подходы: Agentic RAG, GraphRAG, HyDE, Hybrid RAG, Multi-DB Routing, Visual RAG. Хорошая база для изучения и выбора под свою задачу
2. **MCP** — примеры интеграции трёмя разными способами (через mcp-haystack, нативный mcp SDK, OpenClaw). Прямая применимость к Hermes Agent
3. **Сообщество** — проекты регулярно обновляются (последний PR 2 дня назад), принимают контрибьюции
4. **Провайдеры** — не привязаны к одному вендору: OpenAI, Anthropic, Google, Mistral, DeepSeek, Qwen, MiniMax, Gemma — все есть

**Что стоит попробовать:** HyDE RAG (интересная техника), GraphRAG (для связанных данных), GitHub MCP через Hermes (прямая интеграция).
