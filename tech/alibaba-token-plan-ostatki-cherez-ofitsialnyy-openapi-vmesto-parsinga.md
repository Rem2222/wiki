---
description: "У Token Plan из Alibaba Model Studio есть документированный OpenAPI: GetSubscriptionStats и ListSubscriptionSharedPackages отдают остатки кредитов и срок подписки по AccessKey, без браузера и cookie. Разбор эндпоинтов, регионов, схемы подписи ACS3-HMAC-SHA256 и того, что уже внедрено в CodexBar-Win."
tags: [alibaba,modelstudio,token-plan,openapi,codexbar,windows,playwright]
related: tech/codexbar-win-varianty-perevoda-s-python-na-nativnyy-stek-2026 tech/opencode-go-ostatki-limitov-cherez-api-cookie-avtorizatsiya-umerla
---

# Alibaba Token Plan: остатки через официальный OpenAPI вместо парсинга

## Зачем

Панель Alibaba в CodexBar-Win показывала остатки Token Plan, но брала их со страницы `modelstudio.console.alibabacloud.com` через Playwright и cookie. Это два минуса сразу: Playwright падает на Python 3.13, а cookie `login_aliyunid_ticket` живёт меньше суток, то есть раз в день панель ломается. Проверено 02.11.2026: у Token Plan есть официальный OpenAPI, который отдаёт те же данные без браузера.

## Что нашлось

Token Plan API — часть Model Studio OpenAPI, документация лежит в базе `bailian-docs-llm-wiki` (`wiki/api/token-plan-api.md` и `raw/model-api-reference/token-plan-api/`).

**Остатки кредитов:**

```
GET https://modelstudio.{region}.aliyuncs.com/tokenplan/subscription/stats
x-acs-action: GetSubscriptionStats
x-acs-version: 2026-02-10
```

Отдаёт `Data.SubscriptionStartTime`, `Data.SubscriptionEndTime` (миллисекунды) и `Data.Items` с кредитами по типам мест — `SeatRemainingCredits` и общим объёмом. Из этого считается процент использования: `used = total - remaining`, `pct = used / total`.

**Детализация пакетов:**

```
GET https://modelstudio.{region}.aliyuncs.com/tokenplan/subscription/shared-packages
x-acs-action: ListSubscriptionSharedPackages
x-acs-version: 2026-02-10
Параметры: PageNo, PageSize, StatusList (флэт: StatusList.1=NORMAL)
```

**Регионы.** Оба конца работают и в китайском `cn-beijing`, и в международном `ap-southeast-1` — проверено ошибкой `MissingDate` (значит action распознан) и затем `InvalidAccessKeyId.NotFound` с правильно подписанным запросом.

**Авторизация.** `ACS3-HMAC-SHA256` с AccessKey. Ключ модели (Bearer, тот что `ALIBABA_TOKENPLAN_KEY`) здесь не работает: сервер отвечает `MissingAccessKeyId`, то есть заголовок `Authorization: Bearer` просто игнорируется. Нужен AccessKey ID и Secret от RAM-пользователя.

## Как подписать запрос

Канонический запрос собирается так:

```
GET\n
<путь>\n
<отсортированные query-параметры, percent-encoded>\n
<заголовки host, x-acs-action, x-acs-version, x-acs-date, x-acs-content-sha256, x-acs-signature-nonce — по алфавиту, каждый "имя:значение"\n>\n
<те же имена через ";">\n
<hex sha256 от пустого тела>
```

Дальше `StringToSign = "ACS3-HMAC-SHA256\n" + hex(sha256(канонический запрос))`, подпись — `hex(hmac_sha256(secret, StringToSign))`, и заголовок:

```
Authorization: ACS3-HMAC-SHA256 Credential=<AK ID>,SignedHeaders=<список>,Signature=<подпись>
```

Тело для GET пустое, поэтому `x-acs-content-sha256` — хеш пустой строки (`e3b0c442...b855`). Реализация в `codexbar_lib/fetchers/alibaba_openapi.py`.

## Что сделано в приложении

- Новый модуль `codexbar_lib/fetchers/alibaba_openapi.py`: подпись, вызовы, перевод кредитов в проценты, читаемые ошибки API (`Code` и `Message` из ответа)
- `alibaba.py`: путь через OpenAPI пробуется первым, ключи берутся из переменных окружения или из настроек (`alibaba_ak_id`, `alibaba_ak_secret`); CLI, cookie и Playwright остались запасными путями
- В настройках появились поля AccessKey ID и Secret рядом с cookie, сохраняются через тот же `_preserve()`, что и остальные секреты
- Коммит **3baa278** в ветке `refactor/unify-ui-panels`

## Что проверено живьём

- Подпись принимается: с фиктивным AccessKey сервер отвечает `InvalidAccessKeyId.NotFound`, а не ошибкой подписи — значит формат `ACS3-HMAC-SHA256` собран верно
- Без ключей OpenAPI молча уступает, приложение работает по прежней цепочке
- С неверными ключами — тоже чистый откат, в интерфейсе появляется «Specified access key is not found»
- `py_compile` чистый

Не проверено: полный путь с настоящим AccessKey. На сервере его нет, а Bearer-ключ модели для этих двух вызовов не годится принципиально.

## Что нужно, чтобы закрыть

Создать AccessKey (RAM-пользователь) с правами на Model Studio Token Plan — минимум `GetSubscriptionStats` и `ListSubscriptionSharedPackages` — и вписать его в настройки приложения. После этого Playwright для Alibaba отключается совсем, а вместе с ним уходят падения на Python 3.13 и ежедневное обновление cookie.

⚠️ AccessKey — это не ключ модели: он шире по правам, поэтому его стоит завести отдельно от основного аккаунта и дать только нужные действия.

## Источники

- 📁 `~/.hermes/skills/bailian-docs-llm-wiki/wiki/api/token-plan-api.md`
- 📁 `~/.hermes/skills/bailian-docs-llm-wiki/raw/model-api-reference/token-plan-api/token-plan-api-subscription/get-subscription-stats.md`
- 📁 `~/.hermes/skills/bailian-docs-llm-wiki/raw/model-api-reference/token-plan-api/token-plan-api-subscription/list-subscription-shared-packages.md`
- 🌐 OpenAPI Explorer: https://api.aliyun.com/api/ModelStudio/2026-02-10/GetSubscriptionStats
- 🔧 Живые пробы curl: `modelstudio.cn-beijing.aliyuncs.com` и `modelstudio.ap-southeast-1.aliyuncs.com`, 02.11.2026
