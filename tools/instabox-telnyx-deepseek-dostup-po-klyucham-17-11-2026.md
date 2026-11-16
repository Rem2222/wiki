---
description: "Проверка живыми запросами ключей, присланных Романом 15–16.11.2026: InstaBox (бесплатное рабочее пространство 4 vCPU/8 ГБ, машин нет), Telnyx (ключ активен, баланс 0, inference 403 на account level), DeepSeek (баланс 19.88 CNY). Коarena/ZCode/Qiniu/Epic/OpenRouter/Duck/Numes ключей в почте нет. Отдельно: номер Telnyx не подходит для верификации Codex — OpenAI запрещает VoIP."
tags: [instabox,telnyx,deepseek,api,keys,codex,verification]
related:
  - tools/coarena-besplatnyy-api-k-18-modelyam-5-v-den
  - tech/z-ai
  - ops/services/hermes-agent
created: 2026-11-17
updated: 2026-11-17
source: "https://api.instabox.sh/v1/machines; https://api.telnyx.com/v2/balance; https://api.deepseek.com/user/balance; https://help.openai.com/en/articles/8983040-what-does-phone-verification-look-like"
---

# Проверка доступов по ключам из почты (17.11.2026, 01:40 МСК)

## Где ключи и как проверяли

Три письма в Gmail Inbox Романа:

- 16.11, 15:18 МСК — «tel» (Telnyx, API v2 key),
- 16.11, 15:19 МСК — «insta» (InstaBox, `ibk_…`),
- 15.11, 12:51 МСК — письмо без темы (DeepSeek, `sk-…`).

Значения ключей **в вику и в чат не кладём**; проверка шла локально из scratch-файла с режимом 600.Все выводы ниже — от живых HTTP-ответов API, а не из описаний тарифов.

## Что реально доступно

### InstaBox — работает

- `GET https://api.instabox.sh/v1/machines` с `X-API-Key` → HTTP 200, `status: success`.
- Рабочее пространство `Free`, создано 16.11.2026 12:19 UTC, лимит **4 vCPU / 8 ГБ RAM**.
- Машин на данный момент **0** — можно создать одну в рамках free-лимита.
- `allowed_specs` — только `compute.basic`; в ответе приходит объект лицензии с истечением в 2027 году.
- Практика: поднимать пока не стали — создание ВМ не было запрошено отдельно.

### Telnyx — ключ живой, но inference закрыт

- `GET /v2/balance` → HTTP 200, `balance: 0.00 USD`, `available_credit: 0.00` — обещанные $25 в API-балансе **не видны**.
- `GET /v2/ai/models` → HTTP 200, модель `zai-org/GLM-5.3-Flash` в списке.
- `POST /v2/ai/openai/chat/completions` с правильной моделью → **HTTP 403, код 10038 «Feature not permitted at this account level. Refer to telnyx.com/upgrade»**. То есть бесплатный inference в Telnyx **не работает до апгрейда/активации аккаунта**.
- `GET /v2/phone_numbers` → пусто (номеров нет), `GET /v2/available_phone_numbers` → HTTP 200, каталог номеров доступен для чтения.
- Вывод: аккаунт Pretrial, ключ валидный, но платные фичи (inference и, вероятно, покупка номера) ограничены уровнем аккаунта. Статус обещанного $25 кредита и одного US-номера надо смотреть в портале Telnyx, API его не подтверждает.

### DeepSeek — работает, баланс есть

- `GET https://api.deepseek.com/v1/models` → HTTP 200, в том числе `deepseek-flash` (DeepSeek-V4.1-Flash, контекст 1 048 576, вывод 393 216).
- `GET /user/balance` → HTTP 200, `is_available: true`, **19.88 CNY** на счёте (granted 0, topped_up 19.88), USD 0.
- Это платный ключ; в провайдеры по умолчанию его **не ставим** без отдельного согласования.

### Остальные позиции утреннего списка

- **Coarena** — ключа в почте нет. `/api/v1/models` отдаёт 18 моделей без авторизации, но `/api/v1/chat/completions` требует ключ, создаваемый только после входа через Google на `coarena.ai/account/api/keys`. Раньше оставляли резервом из-за того, что арена видит промпты.
- **ZCode** (`zcode.z.ai/cn`) — в почте нет ни токена, ни логина. Проверенный `z.ai` endpoint отвечает «token expired or incorrect», но это наш старый токен, не ZCode.
- **Qiniu / Conatus** (`qiniu.com/ai`) — ключа нет; `api.qnaigc.com/v1/models` с DeepSeek-ключом дал 401 (ожидаемо).
- **Epic / Knightica** — ключи не нужны, нужно забрать игру в launcher в срок акции.
- **OpenRouter, Duck, Numes** — ключей в почте нет; ранее по OpenRouter уже проверяли лимиты (50 запросов/день, 1000 после $10).

## Номер телефона для верификации Codex

Я действительно писал, что Telnyx даёт «один US-номер» — это из тарифного описания. **Для Codex он не подойдёт.**

Официальная справка OpenAI (`help.openai.com/en/articles/8983040-what-does-phone-verification-look-like`, обновлена ~20 дней назад) говорит:

- телефон могут спросить при входе в **Codex в desktop-приложении ChatGPT**, а также при **первом создании API-ключа** на platform.openai.com;
- код приходит только **SMS**, либо WhatsApp в списке стран (AE, EG, ID, IL, IN, MY, NG, PK, SA, TR, UA, VN);
- **не поддерживаются** стационарные, **VoIP**, Google Voice и премиум-номера.

Telnyx — VoIP/телеком-оператор, его номер попадает под прямой запрет.Попытки обойти это не стоит: аккаунт могут заблокировать. Рабочий вариант — обычный мобильный номер, который уже есть у Романа, или легальная мобильная eSIM с входящими SMS (не VoIP) в поддерживаемой стране. email/TOTP замену телефону не дают.

## Что мы можем сделать дальше

1. По запросу — создать одну ВМ InstaBox на 4 vCPU / 8 ГБ и использовать её как песочницу или отдельного агента (сейчас не создано).
2. Подключить DeepSeek как резервного провайдера через секрет из почты; по умолчанию не трогаем (`model.default` остаётся `opencode-go/deepseek-v4.1-flash`).
3. Попросить Романа зайти в портал Telnyx и уточнить статус Pretrial/$25 и апгрейд, если нужен inference; затем уже проверять по API.
4. Для Coarena — создать ключ через Google-вход Романа; для ZCode/Qiniu — зарегистрироваться; для Epic — просто забрать игру в лаунчере.
5. Для Codex — использовать реальный мобильный номер; Telnyx-номер даже если получится, для верификации не годится.
