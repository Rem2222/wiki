---
description: "Бесплатные AI coding agents в 2026 (Habr 1086812): 10 сервисов, их бесплатные квоты, вердикт по нашему стеку (8 из 10 уже закрыты) и что реально стоит покупать — GLM Coding Lite $12.60–18, Google AI Pro $19.99, ChatGPT Go $8."
tags: [ai-agents, coding, free, pricing, opencode, codex, cline, cursor, habr]
updated: 2026-09-26
source: "https://habr.com/ru/articles/1086812/"
related:
  - "[[tech/free-llm-api-resources]]"
  - "[[chinese-ai-pricing-research]]"
  - "[[concepts/llm-tier-strategy]]"
  - "[[tech/codex-cli-inference-optimization]]"
---

# Бесплатные AI coding agents 2026 — сравнение и что покупать

**Источник:** https://habr.com/ru/articles/1086812 — MihaDeev, данные **на 25.09.2026**, 12 мин чтения.

Статья перечисляет 10 coding-агентов и разбирает, что в них реально бесплатно. Ключевая мысль автора: **«бесплатный агент» ≠ «бесплатные модели»** — приложение может стоить $0, а inference платный, и наоборот.

> [!NOTE]
> Сами клиенты из списка почти все бесплатны. Деньги всегда идут на **inference**. Поэтому сравнивать нужно не «какой агент лучше», а «откуда идёт модель и что за неё платят».

## Сводная таблица из статьи

| Сервис | Что бесплатно | Бесплатный лимит | Платное |
|---|---|---|---|
| **OpenCode** | Open-source агент + free-модели Zen | Общей цифры нет — зависит от модели | Go $5 первый мес → **$10/мес**; Zen pay-as-you-go |
| **Freebuff** | Free inference, режимы Full/Limited | Full: **100 Freebucks/день**. Limited: DeepSeek V4 Flash, **6 × 1 ч/день** | Платный уровень моделей |
| **CodeGPT** | Free-тариф, BYOK, локальные модели | **10 взаимодействий/день** (Economy) + $1 welcome credit | Pro **$10/мес** ($9 год.); Teams $30 ($27) |
| **Cline** | Open-source агент, BYOK, local/free models | Зависит от модели/провайдера | ClinePass **$9.99/мес** |
| **TRAE** | Free + trial Pro | Token-based, фиксированной цифры нет | Lite $3 / Pro $10 / Pro+ $30 / Ultra $100 |
| **ZCode** | Trial для новых | **5 дней**, квота зависит от GLM-моделей | GLM Coding Lite/Pro/Max |
| **Codex** | В ChatGPT Free | Ограниченная квота | Go **$8** / Plus $20 / Pro $100 (5x) / Pro $200 (20x) |
| **Kilo Code** | Open-source, free/local/BYOK | Зависит от источника inference | Pass Starter **$19** / Pro $49 / Expert $199; Teams $15/user |
| **Cursor** | Hobby | Ограниченный Agent usage | Pro $20 / Pro+ $60 / Ultra $200 |
| **Antigravity** | Клиент + доступные модели | **Basic weekly rate limits** | Google AI Pro / Ultra (отдельно не продаётся) |

### Ошибка в статье

В таблице Codex два раза подряд «Pro — $100» и «Pro — $200». По факту это **Pro с 5x usage = $100** и **Pro с 20x usage = $200** ([morphllm.com/codex-pricing](https://www.morphllm.com/codex-pricing), [chatgpt.com/codex/pricing](https://chatgpt.com/codex/pricing/)).

### Цены, которых в статье нет (проверено отдельно)

Автор честно не ставит цифры, которых нет на публичных страницах. Дознакомил:

| Позиция | Цена | Источник |
|---|---|---|
| **GLM Coding Lite** | **$18/мес**, с промо −30% → **$12.60** | [z.ai/subscribe](https://z.ai/subscribe), [codingplan.org](https://codingplan.org/en/plans/glm), [aipricing.guru](https://www.aipricing.guru/z-ai-subscription-pricing/) |
| GLM Coding Pro | $72–80/мес | там же (разброс между обзорами) |
| GLM Coding Max | $160–168/мес | там же |
| **Google AI Pro** | **$19.99/мес** | [gemini.google](https://gemini.google/us/students/) |
| ChatGPT Go | $8/мес | см. выше |

Лимиты GLM Coding Lite: **~80 prompts / 5 ч**, **~400 / неделю**, модели GLM-5.3 и GLM-5.3-Flash, **контекст 1M** на всех тирах, 50% кредитов в off-peak ([layer3labs](https://www.layer3labs.io/guides/z-ai-pricing), данные доков от 21.07.2026).

## Freebuff — разбор двух режимов (самое необычное в статье)

Сервис покрывает inference рекламой. **Два режима, их нельзя смешивать в одну цифру:**

**Full mode — 100 Freebucks/день**, обновляются ежедневно, не переносятся. Модели (значения **не складываются** — все считаются от одного дневного запаса):
- GLM 5.3 Flash — до 20 ч
- Solar Mini 4 — до 20 ч
- MiMo 2.6 Flash — до 10 ч
- DeepSeek V4.1 Flash — до 6 ч
- Muse Spark 1.2 — до 6 ч

**Limited mode** — глобальный fallback для регионов, где Full недоступен (в статье названа Чехия и другие):
- DeepSeek V4 Flash
- **6 сессий/день, каждая до 1 часа** → до 6 часов

Платный уровень: GPT-6 Luna, MiMo 2.6 Pro, Gemini 3.8 Flash.

## Четыре типа «бесплатности» (типология автора)

1. **Бесплатен агент + есть бесплатные модели** — OpenCode, Freebuff
2. **Бесплатен агент, inference выбираешь сам** — Cline, Kilo Code, CodeGPT (выгодно при наличии своего ключа / Ollama / LM Studio)
3. **Бесплатный тариф с квотой** — Cursor, Codex, Antigravity, TRAE
4. **Бесплатный trial** — ZCode (5 дней)

Вопросы для выбора вместо «какой бесплатный»: (1) есть ли бесплатный inference, (2) сколько именно дают — запросы/credits/токены/часы/weekly/session limits, (3) можно ли свой API, (4) можно ли локальная модель.

---

## Вердикт по нашему стеку: 8 из 10 уже закрыты

Наш inference уже подключён: `opencode-go` (основной, подписка оплачена) + `qwen-tp` (Alibaba token-plan) + `openrouter` + `freellmapi` + self-hosted `FreeQwenApi` (:9656) и `FreeDeepseekAPI` (:9655) + локальный Ollama `qwen2.5:7b`.

| Сервис | Статус | Комментарий |
|---|---|---|
| OpenCode | ✅ **Основной провайдер** | `opencode-go`, Go оплачен — не трогать |
| Codex | ⚠️ Monitors only | CodexBar следит за квотой, CLI не установлен |
| Cline | ➖ Закрыт | Дублирует OpenCode, не установлен |
| TRAE | ➖ Закрыт | IDE ByteDance, не нужен |
| Cursor | ➖ Закрыт | Hobby хватит, Pro $20 не оправдан |
| CodeGPT | ➖ Закрыт | Расширение для VS Code/JetBrains, а мы в терминале |
| Kilo Code | ➖ Закрыт | Pass $19 дороже при равной ценности |
| Antigravity | ⚠️ Частично | Gemini у нас через прокси `127.0.0.1:8083` — ненадёжно |
| **Freebuff** | ❌ **Не закрыт** | Реальный бесплатный inference без BYOK |
| **ZCode** | ❌ **Не закрыт** | Триал 5 дней на GLM-5.3 |

Смысл: статья перечисляет **клиентов**, а все 10 бесплатны как приложения. У нас клиент — Hermes, и платить за второй клиент незачем.

## Рекомендации

### Бесплатно, нулевой риск
1. **Freebuff** — проверить, включается ли Full mode (есть региональная оговорка)
2. **ZCode trial 5 дней** — потрогать GLM-5.3 в агентном окружении до решения о покупке

### Платно — только после триала
**GLM Coding Lite: $18/мес, с промо $12.60** — единственный покупной пункт с реальным приростом:
- GLM-5.3 с **контекстом 1M** (против стандартного у OpenCode Go)
- ~80 prompts/5h + ~400/нед
- Подключается к Hermes как обычный OpenAI-compatible provider
- Работает с Claude Code, Codex, OpenCode, Cline, Kilo
- Дешевле текущего OpenCode Go ($10), но с многократно бо́льшим контекстом

### Платно — опционально
- **Google AI Pro $19.99/мес** — брать ради стабильного Gemini + 2TB. Antigravity в подарок. Если прокси с Gemini стабилен — не нужно
  - ⚠️ Квота Antigravity **привязана к Google AI подписке**, отдельно не продаётся. На форуме Google жалобы: лимит Claude Opus сбрасывается каждые 5 часов, но бывает уезжает на 2 дня ([discuss.ai.google.dev](https://discuss.ai.google.dev/t/antigravity-limit/119036))
- **ChatGPT Go $8/мес** — только если решишь поставить Codex CLI вторым агентом

### Не брать
ClinePass $9.99 · Kilo Pass $19 · Cursor Pro $20 · CodeGPT $10 · TRAE Lite $3 · GLM Pro $72–80 · GLM Max $160+ · ChatGPT Plus $20 / Pro $100–200 · Antigravity отдельно (не продаётся)

Всё это перекрывается существующим: `opencode-go` + `qwen-tp` + `freellmapi` + два self-hosted прокси.

## Оговорка о актуальности

Автор прямо пишет: данные на 25.09.2026, «не обещаю, что эти цифры останутся такими навсегда». Free-модели исчезают, лимиты меняются. Перед оплатой проверять страницу тарифов провайдера.

Отдельно в статье подчёркнуто: **232K контекста ≠ 232K бесплатных токенов в день** — контекст и бесплатная квота это разные величины, сравнивать их некорректно.

## Источники

- 🌐 [Habr 1086812](https://habr.com/ru/articles/1086812/) — основной источник, MihaDeev
- 🌐 [z.ai/subscribe](https://z.ai/subscribe) — GLM Coding Plan
- 🌐 [codingplan.org/en/plans/glm](https://codingplan.org/en/plans/glm) — цены GLM
- 🌐 [chatgpt.com/codex/pricing](https://chatgpt.com/codex/pricing/) — тарифы Codex
- 🌐 [antigravity.google](https://antigravity.google/) — Antigravity
- 📄 [[tech/free-llm-api-resources]] — бесплатные API-эндпоинты (cheahjs + @Ungated): Atria, Vireonix, ShareLLM, OdiRouter, Selora, Routeway
- 📄 [[chinese-ai-pricing-research]] — цены Qwen/GLM/Kimi/MiniMax напрямую
- 📄 [[concepts/llm-tier-strategy]] — зачем платить за большую модель на конкретном этапе
