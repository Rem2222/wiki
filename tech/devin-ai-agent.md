---
description: Devin — AI Software Engineer от Cognition Labs (бывший Windsurf). IDE + облачные агенты. Включает GLM-5.2 в подписке Pro.
tags: [devin, cognition, glm, ai-coding-assistant, windsurf]
related: [tech/z-ai, tech/buyglm-com, tech/hermes-mcp]
---

# Devin (Cognition Labs)

**Devin** — AI coding ассистент от Cognition Labs (ранее назывался Windsurf). Предоставляет IDE (Desktop) + облачных агентов (Devin Cloud) + CLI.

## Планы и цены

| План | Цена | Модели | API | Конкурентные сессии |
|------|------|--------|-----|---------------------|
| **Free** | $0 | Только базовые/SWE 1.6 (Slow), ❌ premium frontier | ❌ | 0 |
| **Pro** | $20/мес | OpenAI, Claude, Gemini, **GLM-5.2**, SWE 1.6 (full) ✅ | ✅ Devin API | До 10 |
| **Max** | $200/мес | Всё из Pro + значительно выше квоты | ✅ | До 10 |
| **Teams** | $80/мес + $40/место | Всё из Pro + совместная работа | ✅ | Unlimited |
| **Enterprise** | Custom | Всё из Teams + VPC/SAML/SSO | ✅ | Unlimited |

## Модели в разных планах

- **Free:** без доступа к premium frontier моделям (Claude, GPT-4, Gemini, GLM-5.2). SWE 1.6 доступна в медленном режиме.
- **Pro+:** полный доступ ко всем моделям, включая **GLM-5.2** (от Zhipu).

## Devin API

- REST API для оркестрации агентов, **НЕ** OpenAI-совместимый
- Эндпоинт: `https://api.devin.ai/v3/organizations/{id}/sessions`
- API ключи: начинаются с `cog_`
- Доступен только на планах Pro+
- **Нельзя использовать как провайдер для Multica** — нет `/v1/chat/completions`

## Devin CLI

Есть CLI-инструмент, подробнее: https://docs.devin.ai

## Ссылки

- [Сайт](https://devin.ai)
- [Документация](https://docs.devin.ai)
- [Pricing](https://devin.ai/pricing)
- [API Docs](https://docs.devin.ai/cloud/devin-api/devin-api-overview)
- [Страница организации Романа](https://app.devin.ai/org/roman-skogorev-e9865a665a5e/settings/devin-api)

## Заметки

- GLM 5.2 доступен **внутри IDE** Devin Desktop и через Devin Cloud, но **не как внешний API**
- Для Multica нужно OpenAI-совместимое API (Xiaomi MiMo, OpenCode Go, z.ai)
- Devin CLI не даёт прямого доступа к моделям для сторонних инструментов
