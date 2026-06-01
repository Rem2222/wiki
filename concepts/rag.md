---
description: Retrieval-Augmented Generation — дополнение LLM внешними данными
tags: [rag, llm, retrieval, ai]
related: [[concepts/llm-wiki]] [[concepts/mcp]]
---

# Retrieval-Augmented Generation (RAG)

Подход к улучшению ответов LLM, при котором модель перед генерацией запрашивает релевантные фрагменты из внешней базы знаний (документы, wiki, БД) и использует их как контекст.

## В контексте вики Rem

Личная вики (`~/Documents/wiki/`) реализует паттерн LLM-wiki — гибрид RAG и ручного управления знаниями. Модель может искать по страницам вики через search_files и добавлять новую информацию.
