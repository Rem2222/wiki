---
description: Обзор RAG-проектов из репозитория Sumanth077/Hands-On-AI-Engineering — 11 проектов, архитектуры, технологии, фишки.
tags: [tech, rag, ml]
related: [[tech/mcp-projects-summary]] [[tech/hermes-memory-setup-vps]]
---

# RAG-проекты: Hands-On AI Engineering

Репозиторий: [Sumanth077/Hands-On-AI-Engineering](https://github.com/Sumanth077/Hands-On-AI-Engineering) — раздел `rag_apps/`. 11 проектов, 1.5k ★.

## Общая картина

| Параметр | Значение |
|----------|----------|
| Самый популярный LLM | Mistral (Small 4, Large) — 5 проектов |
| Самая популярная векторная БД | ChromaDB — 6/11 |
| Самый популярный фреймворк | LangChain (4), Agno (3) |
| Самый популярный UI | Streamlit — 9/11 |

## Проекты

### 1. Agentic RAG with O3-Mini & DuckDuckGo
- **LLM:** GPT-4o-mini | **Embeddings:** OpenAI | **Vector DB:** Milvus (Docker)
- **Фреймворк:** Agno
- **Фишка:** Двойной источник знаний — Milvus + DuckDuckGo fallback
- **Pipeline:** PDF → чанкинг → Milvus → query → Agno Agent → если контекста мало → DuckDuckGo

### 2. Agentic RAG with Qwen & FireCrawl
- **LLM:** Qwen3:8b (Ollama, локально) | **Embeddings:** BGE-small-en-v1.5 | **Vector DB:** Milvus
- **Фреймворк:** Agno
- **Фишка:** Полностью локальный стек (не нужны API-ключи для LLM), FireCrawl для веб-скрапинга

### 3. Vision RAG (Multimodal Search & VQA)
- **Vision LLM:** GPT-4o-mini | **Embeddings:** Cohere embed-english-v3.0
- **Векторная БД:** нет (sklearn косинусная близость)
- **Фишка:** Visual-first RAG — поиск по визуальным сегментам PDF, не по тексту. Модель «смотрит» на картинку

### 4. Clinical RAG with ADE
- **LLM:** Mistral Large | **Embeddings:** Mistral Embed | **Vector DB:** ChromaDB
- **Фреймворк:** LangChain | **Парсинг:** LandingAI ADE (Agentic Document Extraction)
- **Фишка:** Медицинские PDF → LandingAI ADE визуально парсит → Markdown + grounding metadata. Таблицы не разбиваются

### 5. YouTube Transcript RAG
- **LLM:** Mistral Small 4 | **Vector DB:** ChromaDB
- **Транскрипция:** Whisper (openai-whisper)
- **Фишка:** Чат с любым YouTube-видео. Ответы с таймкодами

### 6. GraphRAG Knowledge System
- **LLM:** Mistral Small 4 | **Vector DB:** ChromaDB
- **Граф:** NetworkX | **UI:** Streamlit
- **Фишка:** Самый сложный проект (7 модулей). Извлекает сущности и связи из документов, строит knowledge graph, community detection. Два типа запросов: entity-level и thematic

### 7. Hybrid RAG System
- **LLM:** Mistral Small 4 | **Vector DB:** ChromaDB
- **Граф:** NetworkX
- **Фишка:** Параллельная индексация в knowledge graph и векторное хранилище. Fused context из обоих путей

### 8. HyDE RAG (Hypothetical Document Embeddings)
- **LLM:** Gemini 3 Flash | **Embeddings:** Gemini Embedding 2 | **Vector DB:** ChromaDB
- **Фреймворк:** LangChain
- **Фишка:** LLM генерирует гипотетический ответ на запрос, эмбедит его, и использует как запрос для поиска. Даёт более релевантные чанки

### 9. Rock Music RAG
- **LLM:** Gemma 4 | **Retrieval:** BM25 (без векторов)
- **Фишка:** Специализированная база знаний по рок-музыке из Wikipedia. BM25, не embedding-based

### 10. RAG Agent with Database Routing
- **LLM:** Mistral Small 4 | **Vector DB:** Qdrant (3 базы: products, support, financial)
- **Фреймворк:** Agno + LangGraph
- **Фишка:** Агент-маршрутизатор направляет запрос в одну из трёх Qdrant-баз. Если ничего не найдено — fallback на LangGraph ReAct web search

### 11. Reasoning RAG
- **LLM:** Gemini 3 Flash
- **Фишка:** Двух-агентный RAG с live reasoning trace. Один агент ищет, другой проверяет

## Выводы

- **ChromaDB** — доминирующая векторная БД (6 проектов из 11). Простая локальная персистентность
- **Mistral** — самый используемый LLM (Small 4 и Large). Хороший balance качества/цены
- **LangChain** и **Agno** — два конкурирующих фреймворка. Agno проще, LangChain гибче
- Тренд: **агентные RAG** (не просто поиск+генерация, а multi-step: grading, routing, web search fallback)
- Интересные ниши: Visual RAG, Clinical RAG, HyDE, Reasoning RAG
