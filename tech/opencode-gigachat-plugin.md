---
description: Плагин для OpenCode, подключающий модели GigaChat от Сбера (транслятор протоколов, TLS Минцифры, OAuth)
tags: [tech, opencode, gigachat, sber, plugin]
related: [tech/mimo-code]
---

# OpenCode GigaChat Plugin

**Репозиторий:** <https://github.com/Overman775/opencode-gigachat-plugin>
**Автор:** Overman775
**Лицензия:** MIT

---

## Что это

Плагин-коннектор для консольного AI-ассистента **OpenCode** ([anomalyco/opencode](https://github.com/anomalyco/opencode)), который добавляет поддержку **GigaChat от Сбера**. Решает проблемы несовместимости OpenAI-протокола и GigaChat API.

## Основные возможности

- **Транслятор протоколов** — на лету конвертирует OpenAI-формат запросов в GigaChat API, вырезает несовместимые параметры, преобразует `reasoning_effort` / `thinking` в системные инструкции
- **TLS/SSL для РФ** — встроен сертификат Минцифры РФ (Russian National CA). Либо автопоиск системных, либо fallback на встроенный PEM-бандл — без отключения `rejectUnauthorized`
- **OAuth 2.0** — автоматическое получение и обновление JWT-токенов (превентивное обновление за 5 мин до истечения 30-минутного лимита), семафорные блокировки от параллельных запросов
- **Vision (мультимодальность)** — перехватывает base64 `image_url`, загружает на сервера Сбера через `/files`, передаёт `file_id` как attachment
- **Адаптация инструментов** — GigaChat поддерживает только 1 function call за запрос; плагин оптимизирует массив tools под это ограничение
- **Без лишних конфигов** — credentials задаются прямо в `opencode.json` в секции провайдера, без отдельных файлов

## Модели GigaChat

| Модель | Тип | Vision |
|---|---|---|
| `GigaChat` | Classic Text | Нет |
| `GigaChat-2` | Text | Нет |
| `GigaChat-2-Lite` | Alias GigaChat-2 | Нет |
| `GigaChat-Plus` | Text | Нет |
| `GigaChat-Pro` | Multimodal | Да |
| `GigaChat-2-Pro` | Multimodal (новое поколение) | Да |
| `GigaChat-Max` | Multimodal (флагман) | Да |
| `GigaChat-2-Max` | Reasoning + Multimodal | Да |

Все модели — 128K контекст.

## Установка

```bash
# 1. Скачать скомпилированный файл из GitHub Releases
# 2. Положить в папку плагинов OpenCode
mkdir -p "$HOME/.opencode/plugins"
cp gigachat-plugin.js "$HOME/.opencode/plugins/"

# 3. Добавить в opencode.json
```

Конфиг в `~/.config/opencode/opencode.json`:

```json
{
  "plugin": ["./.opencode/plugins/gigachat-plugin.js"],
  "provider": {
    "GigaChat (Sberbank)": {
      "options": {
        "baseURL": "https://api.gigachat.local/v1"
      },
      "models": { ... }
    }
  }
}
```

## Нюансы

- **Base URL** `https://api.gigachat.local/v1` — виртуальный, транслируется в `https://gigachat.devices.sberbank.ru/api/v1/chat/completions`
- **Сертификаты** — либо установка сертификатов Минцифры, либо `"verifySSL": false`
- **Лимит размера** — предупреждает при >400 КБ сообщения (лимит пакета GigaChat ~10 МБ)
- **Статус** — экспериментальный PoC, автор не планирует дальнейшую поддержку

## Ссылки

- [ARCHITECTURE.md](https://github.com/Overman775/opencode-gigachat-plugin/blob/main/docs/ARCHITECTURE.md) — внутреннее устройство
- [Habr-статья](https://github.com/Overman775/opencode-gigachat-plugin/blob/main/docs/HABR-ARTICLE.md) — история создания
- [GigaChat API Spec](https://github.com/Overman775/opencode-gigachat-plugin/blob/main/docs/GIGACHAT_API_SPEC.md)
