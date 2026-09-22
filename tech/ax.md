---
description: "AX — открытый агентный оркестратор Google: декларативно объявляешь задачу агента в YAML, AX песочничит, собирает workspace (git/MCP/скиллы) и запускает миллиарды задач на кластере. «Kubernetes для ИИ-агентов»."
tags: [agents,orchestrator,google,kubernetes,sandbox]
related: [[tech/agentation]] [[tech/Mercury-Agent-Skills]] [[concepts/mcp]]
---

# AX

# AX — оркестратор ИИ-агентов от Google

**Сайт:** https://agentexecutor.io/
**GitHub:** [google/ax](https://github.com/google/ax)

## Что это

Открытый агентный оркестратор Google. Декларативно объявляешь задачу агента в YAML (apiVersion: ax.io/v1alpha1), AX её песочничит, собирает workspace, изолирует сеть и запускает в большом количестве на одном кластере. Позиционируется как «Kubernetes для ИИ-агентов».

## Примитивы

- **Task** — изолированное исполнение: песочница с CPU/RAM-лимитами, дёшево создавать/суспендить/удалять
- **Workspace** — подготовка окружения: git-репы, MCP-серверы, скиллы — AX всё разворачивает в песочнице до старта задачи
- **Gateway** — сетевые политики: allowlist хостов/портов, инъекция кредов во входящие запросы
- **Model** — единый конфиг моделей/параметров/секретов; ротация ключа или пин новой версии модели — одним apply

## Ключевые фичи (заявленные)

- **Миллиарды задач на кластер** — каждый таск лёгкий actor поверх Agent Substrate (compute runtime для массовой плотности и быстрых stateful-жизненных циклов)
- **Sub-second resume** — простаивающие агенты (ждут ответ модели, вызовов инструментов, человека) чекпоинтятся, суспендятся и возвращаются <1 сек без cold start
- **Dense multiplexing** — десятки задач делят ресурсы воркера, idle-ожидание превращается в spare compute
- **CLI**: `ax apply -f task.yaml`, `ax watch`, `ax get tasks`, `ax ssh task -- cmd`, `ax suspend/resume/delete task`

## Пример

```yaml
apiVersion: ax.io/v1alpha1
kind: Task
metadata:
  name: test
spec:
  workspaces:
    - name: golang
      goal: "Ensure that Go tool chain is available and is built from source"
```

## Стадия

Ранняя (API v1alpha1), «пощупать можно». Проект развивается.

## Связанное

- [[tech/agentation]]
- [[tech/Mercury-Agent-Skills]]
- [[concepts/mcp]]
