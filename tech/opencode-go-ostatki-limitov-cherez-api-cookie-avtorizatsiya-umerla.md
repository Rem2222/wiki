---
description: "Консольный API OpenCode Go теперь принимает API-ключ в Authorization: Bearer — /console/api/go/status отдаёт полные метры (лимиты, расход, даты сброса, период подписки), /zen/go/v1/usage — готовые проценты. Cookies и x-org-id больше не работают. Здесь структура ответа, что не работает, и починка CodexBar-Win коммитом 03ae34b."
tags: [opencode,api,limits,codexbar,quota,bearer]
related:
  - tech/codexbar-win-cookie-decryption
  - tech/cookie-decryptor
updated: 2026-11-02
source: "живая проверка эндпоинтов 02.11.2026 + коммит 03ae34b"
---

# OpenCode Go — остатки лимитов через API (cookie-авторизация умерла)

## Что случилось

OpenCode Go переделали выдачу остатков: консольная страница и её cookie-авторизация перестали работать. CodexBar-Win показывал пустоту и ошибку «session expired; update cookie in settings», потому что ходил на `/console/api/go/status` с cookies `auth` + `__Host-console_session` и заголовком `x-org-id`.

Проверка 02.11.2026 показала: **эндпоинт и структура ответа не изменились — изменился способ авторизации.** Теперь консольный API принимает обычный API-ключ Go в заголовке `Authorization: Bearer`. Ни cookies, ни `x-org-id` больше не нужны.

## Два рабочих эндпоинта

**1. Полные данные (лимиты, расход, даты сброса, период подписки)**

```
GET https://opencode.ai/console/api/go/status
Authorization: Bearer oc_sk_...
```

Ответ (проверено живьём):

```json
{
  "subscriberUserId": "acc_...",
  "product": "go",
  "renewalCurrency": "usd",
  "access": {
    "startsAt": "2026-10-15T13:08:28.000Z",
    "endsAt": "2026-11-15T13:08:28.000Z",
    "meters": {
      "fiveHour": {"startsAt": "...", "resetsAt": "2026-11-02T21:25:45.000Z",
                   "limitMicroCents": "1200000000", "usedMicroCents": "41631021"},
      "week":     {"resetsAt": "2026-11-09T00:00:00.000Z",
                   "limitMicroCents": "3000000000", "usedMicroCents": "177698161"},
      "month":    {"resetsAt": "2026-11-15T13:08:28.000Z",
                   "limitMicroCents": "6000000000", "usedMicroCents": "3793608910"}
    }
  },
  "upgradePrice": {"amountMicroCents": "...", "currency": "usd"}
}
```

Процент считается как `usedMicroCents / limitMicroCents * 100`. Суммы в микро-центах: `limitMicroCents` 6 000 000 000 — это $60 месячного лимита.

**2. Готовые проценты (запасной путь)**

```
GET https://opencode.ai/zen/go/v1/usage
Authorization: Bearer oc_sk_...
```

```json
{"usage": {
  "rolling": {"status": "ok", "percent": 3, "resetsAt": "2026-11-02T21:25:45.000Z"},
  "weekly":  {"status": "ok", "percent": 5, "resetsAt": "2026-11-09T00:00:00.000Z"},
  "monthly": {"status": "ok", "percent": 63, "resetsAt": "2026-11-15T13:08:28.000Z"}
}}
```

Окна соответствуют друг другу: `fiveHour` = `rolling`, `week` = `weekly`, `month` = `monthly`, проценты совпадают (с поправкой на округление).

## Что НЕ работает

- `GET /console/api/go/status` **без** ключа → `401 {"_tag":"Unauthorized"}`. Это и видел CodexBar, когда слал мёртвые cookies
- `GET /console/api/go/status` со старыми cookies (`auth`, `__Host-console_session`) и `x-org-id` → тот же 401
- `/zen/go/usage`, `/zen/v1/usage`, `/api/usage`, `/dashboard/billing/`, `/zen/go/v1/usage/limits`, `/zen/go/v1/subscription`, `/billing`, `/account`, `/profile` → 404
- Работает и `GET /zen/go/v1/models` (каталог моделей, 200)

## Починка CodexBar-Win

Коммит **03ae34b** в ветке `refactor/unify-ui-panels` репозитория `Rem2222/openclaw-workspace`, каталог `projects/CodexBar-Win-Enhance` (+182 / −2 строки):

- в `codexbar_lib/fetchers/opencode.py` добавлен путь по API-ключу: ключ берётся из настроек (`opencode_api_key`), затем из окружения (`OPENCODE_GO_API_KEY`, `OPENCODE_API_KEY`). Запрос идёт с `Authorization: Bearer`, без cookies и без `x-org-id`
- если консольный ответ пришёл без `meters`, фетчер пробует `/zen/go/v1/usage` и разбирает готовые проценты
- cookie-путь сохранён как запасной: при отказе ключа фетчер пробует cookies и только потом отдаёт ошибку
- в окне настроек появилось поле **API key** (`oc_sk_...`) над полем cookie; кнопка Test сначала проверяет ключ
- проверено живьём на VPS: `source=api-key`, `plan=Go till 2026-11-15`, 5 часов — 4% (сброс через 2 ч 35 м), неделя — 6% (6 д 5 ч), месяц — 63% (12 д 18 ч). Совпадает с `/zen/go/v1/usage`
- отдельно проверены отказы: битый ключ → «API key rejected (401/403)», пустые ключ и cookie → прежняя ошибка про cookie, фейковая cookie → «session expired» без падения

**Что нужно сделать на Windows-ПК:** подтянуть ветку `refactor/unify-ui-panels`, открыть настройки, вписать API-ключ Go в поле над cookie, нажать Test (должно быть «✓ API key works»), сохранить. Поле cookie после этого можно оставить пустым.

## Вывод на будущее

У этого провайдера правильный путь — API-ключ, а не парсинг консоли и не cookies. Cookie-подход умер дважды: сначала сессии жили меньше дня и требовали постоянной перевставки, теперь их вообще не принимают. Всё, что строится на cookies, здесь обречено.

Связанное: `tech/codexbar-win-cookie-decryption` (механика расшифровки Chromium-cookies — для OpenCode больше не нужна, но осталась для других провайдеров), `tech/cookie-decryptor`.
