---
description: Go AI coding agent — терминальный инструмент для Claude Code
tags: [go, claude-code, agent, terminal]
related: [[tech/go-skills-claude-code]]
---

# gopilot

**GitHub:** https://github.com/gonzaloserrano/gopilot

Open-source AI coding agent на Go, интегрирующийся с Claude Code. Терминальный инструмент для автоматизации задач разработки.

## Фишка

Go-агент для Go-разработчика — один бинарник, никаких зависимостей, глубокая интеграция с Claude Code harness.

## Возможности

- **Automated workflows:** разбивает сложные задачи на последовательность вызовов инструментов
- **Context-aware:** собирает контекст проекта (дерево исходников, git log, граф зависимостей)
- **Terminal & file ops:** запуск команд, применение diff'ов, git-операции
- **Pluggable backends:** Claude и другие LLM провайдеры

## Установка

Скачать бинарник из релизов или собрать из исходников.

## Нужно ли

❌ **Скорее нет**, если ты уже используешь Claude Code или Hermes Agent — они покрывают те же сценарии. Может быть интересен как Go-native альтернатива.
