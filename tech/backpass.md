---
description: "backpass — «gradient descent для памяти агента»: читает транскрипты сессий (7 харнессов, incl. hermes state.db) и предлагает evidence-обоснованные правки памяти. (JS, MIT)."
tags: [memory,agent-memory,skills,agents,gradient,evidence]
related: [[tech/openviking]] [[tech/semantica]] [[tech/hermes-memory-setup-vps]]
---

# backpass


**backpass** — «Gradient descent for your agent memory»: не пиши AGENTS.md руками — обучай её. (JavaScript, MIT, ★188, macOS/Linux, свежий 08.2026).

## Суть
Твоя `AGENTS.md`/`CLAUDE.md` — «веса», каждая agent-сессия — «forward pass», а транскрипт сессии на диске — «сигнал ошибки», который обычно никто не читает. Цикл замыкается только когда человек вручную вспомнит провал и отредактирует файл. backpass замыкает его как машинное обучение.

```
AGENTS.md (веса) → сессия (forward pass) → транскрипт (loss)
→ backpass: collect samples, distill, calculate loss, aggregate gradients
→ gradient descent (diffs + skill extraction)
→ человек принимает/отклоняет (human gate) → обратно в веса
```

## Принципы
- **Local-first** — читает транскрипт-сторы 7 харнессов с диска (claude, codex, pi, opencode, grok, cursor CLI, **hermes via ~/.hermes/state.db**; hermes — only CLI/ACP, без gateway/cron/WhatsApp). Без API, секреты редастятся.
- **Evidence-gated** — каждая предлагаемая правка несёт **дословные цитаты** из реальных сессий; новая инструкция требует ≥2 независимых сессий; один запуск = ≤5 правок (мелкие шаги, не перезапись).
- **Human in the loop** — анализ никогда не пишет; `backpass apply` — единственная пишущая команда, показывает каждую правку + evidence на ACCEPT/REJECT. **Нет DEFER — отказы запоминаются.**

## Конвейер
1. **Collect** — считай, какие сессии к каким репо: 3 тира (дет./cwd / git-remote / best-effort). Инкрементально, кэш в `.backpass/scan-cache.json`.
2. **Distill** — детерминированная сжимация: user/assistant verbatim, tool-call = одна строка, дистилляция **96-99%**.
3. **Loss** — одна дёшевая модель на дистилляцию (через `acpx`, своих ключей нет): какие инструкции помогли/нарушены, какие ошибки не покрыты. **Claim без цитаты — отбрасывается.** Кэш по content+hash файла.
4. **Aggregate** — детерминированно: счёт/релевантность инструкций, дубликаты-gaps кластеризуются, порог `minGapEvidence` (≥2). Gaps считаются через запуски (`.backpass/gap-ledger.json`).
5. **Gradient descent** — одна high-reasoning сессия правит **staging-копию** файла (репо read-only): ADD/REMOVE/REWRITE/EXTRACT→SKILL. Механические гейты: ≤`maxEditsPerRun`, каждый change = ровно 1 аннотированная правка, новая инструкция требует evidence, каждая правка с цитатой, пост-file влезает в бюджет. Нарушение → re-prompt (≤2), потом **fail loudly** (не молча режет).
6. **Бюджет** — «размер модели»: дефолт **5,000 токенов (~20KB)** на always-loaded файл (байт/4, ±15%). Над бюджетом — zero-sum (добавление требует удаления).
7. **Skills как overflow** — описание скилла = when-условие: дешёво в всегда-загруженном, тело бесплатно до триггера. Широкая/безопасная → память; узкая/кондиционная → скилл; не-детектируемый триггер → кандидат на удаление. (640-токенная процедура для 4% сессий → 35-токенная строка: −611 always-loaded, +35 desc). Сбой триггера скилла → правка описания, не дубль контента.
8. **Apply** — UI через `lavish-axi` (статический шаблон, детерминированный), `--no-ui`/`--no-open`/`--dry-run`.

## memoryFiles logic
Упорядоченный список (дефолт `["AGENTS.md","CLAUDE.md"]`), первый существующий = канон. Указатель `CLAUDE.md → @AGENTS.md` — ок; два полных файла — расхождение (предупреждает, предлагает сводить в один + пойнтер).

## Требования
Node ≥22.5 + `acpx` (OpenClaw) на PATH. Установка: `npm install -g backpass` / `npx backpass`. Нет своих API-ключей — все LLM-вызовы через acpx к уже залогиненному харнессу.

## Репо
`kunchenguid/backpass` · JavaScript · MIT · ★188 · npm `backpass` · x @kunchenguid
