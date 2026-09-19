---
description: AI Guardrails — барьеры безопасности для ИИ-агентов. Классификация рисков tool calls до выполнения. Jev AutoMode, LangChain, кастомные.
tags: [ai, safety, guardrails, agent, tool-calling, risk, automation]
related:
  - tech/jev-jevrouter
  - tech/free-llm-api-resources
---

# AI Guardrails — барьеры безопасности для агентов

## Что это

**Guardrails** («барьеры», «ограждения») — это прослойка, которая **классифицирует и блокирует рискованные действия ИИ-агента до их выполнения**.

Когда агент (Codex, Claude Code, Hermes, DSH) решает вызвать инструмент — bash-команду, удаление файла, отправку письма, MCP-вызов — guardrail проверяет действие **до** того, как оно произойдёт.

## Зачем нужно

Без guardrails агент может:
- Удалить критические файлы (`rm -rf /`)
- Отправить письмо с ошибкой
- Вызвать опасный API-эндпоинт
- Выполнить bash-команду с непредсказуемым результатом
- Подчиниться prompt injection атаке

Текущие coding harnesses (Claude, Codex, Cursor) имеют встроенные проверки Dangerous acciones, но они **закрытые** и работают только внутри своего экосистемы.

## Как работает

### Уровни риска

| Уровень | Примеры | Действие |
|---------|---------|----------|
| **Low** | Чтение файла, поиск в коде | Автоматически |
| **Medium** | Запись файла, git commit | Логируется, может потребовать подтверждения |
| **High** | Bash-команды, MCP-вызовы, деплой | Требует подтверждения пользователя |
| **Critical** | `rm`, `sudo`, отправка писем, публичные API | Блокируется,requires explicit approval |

### Принцип работы

1. Агент решает вызвать инструмент
2. Guardrail перехватывает вызов
3. Классифицирует по уровню риска (на основе описания инструмента + контекста)
4. Если risk ≥ порога → блокирует или запрашивает подтверждение
5. Если risk < порога → пропускает

## Реализации

### Jev AutoMode (TypeSafe)

Самая быстрая реализация — 70мс на классификацию:

```python
from langchain_typesafe.experimental.middleware import AutoModeMiddleware

guardrail = AutoModeMiddleware(tools=["bash", "rm", "deploy"])
agent = create_agent("openai:gpt-5.6-luna", middleware=[guardrail])
```

Jev классифицирует каждый tool call по risk-уровню до его выполнения. Бесплатно в рамках вывода.

### LangChain

```python
from langchain.agents import AgentExecutor
from langchain.callbacks import BaseCallbackHandler

class GuardrailCallback(BaseCallbackHandler):
    def on_tool_start(self, tool_name, input_str):
        risk = classify_risk(tool_name, input_str)
        if risk == "critical":
            raise BlockedAction(f"Blocked: {tool_name}")
```

### Кастомные

Любой LLM или классификатор может выступать guardrail:
- **LLM-based**: GPT-4/Claude анализирует tool call → decision
- **Rule-based**: регулярки/黑名单 для опасных команд
- **Hybrid**: правила + LLM для edge cases

## Типы guardrails

| Тип | Описание | Пример |
|-----|----------|--------|
| **Pre-execution** | До вызова инструмента | Jev AutoMode |
| **Post-execution** | После вызова, перед возвратом | Проверка вывода на sensitive data |
| **Input guardrails** | Валидация входных данных агента | Защита от prompt injection |
| **Output guardrails** | Проверка генерации агента | Фильтрация PII, проверка фактов |

## Интеграция с Hermes/DSH

Для текущего стека:
- **DSH**: guardrail перед bash-командами и MCP-вызовами
- **Hermes**: проверка tool calls в agent loop
- **JevRouter**: встроенный `AutoModeMiddleware` — один npm пакет

## Ссылки

- https://docs.typesafe.ai — Jev AutoMode
- https://github.com/BillionsBobby/JevRouter —cookbook #7 (policy & confirmation)
- https://python.langchain.com/docs/concepts/guardrails — LangChain guardrails
- https://docs.smithlangchain.com/concepts/guardrails — LangSmith guardrails
