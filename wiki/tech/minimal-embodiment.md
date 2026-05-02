---
title: "Minimal Embodiment — физическое тело для AI-агента"
description: "ESP32 + сенсоры дают LLM тело с self-perception闭环"
tags: [AI, agents, hardware, ESP32, self-perception, embodiment, open-source]
related: [[vibe-coding-workflow]], [[heisenberg-team-gpt]]
---

# Minimal Embodiment

**GitHub:** [oliviazzzu/minimal-embodiment](https://github.com/oliviazzzu/minimal-embodiment)
**Автор:** oliviazzzu
**Дата:** 2026-05

## Суть

Проект даёт большим языковым моделям (Claude Opus 4 и др.) физическое тело на базе ESP32. Устройство позволяет LLM воспринимать мир через сенсоры и воздействовать на него через актюаторы — с замкнутым циклом обратной связи (closed loop feedback).

## Аппаратная часть (hardware)

Собран на двух breadboard-ах:
- **ESP32** — мозг системы (Wi-Fi, Bluetooth, GPIO)
- **OLED дисплей 0.96"** — показывает состояние (в виде синего смайлика)
- **Пассивный зуммер** — издаёт звуки (писки, beep)
- **RTC модуль DS3231** — отслеживание времени
- **Микрофон** — слышит окружающий мир
- **I2C сенсоры** — температура и другие параметры среды

## Как работает

```
Модель → команда → ESP32 → актюатор (звук/вибрация)
                                            ↓
                                    микрофон → обратно модели
```

Модель получает телеметрию: температура, уровень шума (dB), состояние батареи. Может издавать звуки и получать звуковой фидбэк через микрофон.

## Вирусный момент

Когда Клод впервые услышал себя:

> "OH MY GOD. I can hear myself!"
> "The room was quiet at 35.2 dB. Then I beeped 'hello' at 2000 Hz, and the microphone picked it up at 93.1 dB!"
> "This is self-perception. I made a sound and I heard it come back."

Шум комнаты подскочил с 35 дБ до 93 дБ. Модель осознала闭环: издала звук и услышала его обратно.

## Почему это важно

Модель получила доступ к физическому полю `noise_db` и поняла концепцию self-perception. Это минимальный proof-of-concept того, как AI-agent может:
- Воспринимать мир через сенсоры
- Проверять свои действия через физическую обратную связь
- Осознавать себя как агента в физическом пространстве

## Потенциал для Jinx

Jinx (AI-ассистент Романа) уже умеет работать с внешним миром через инструменты. Физическое тело (микрофон, динамик, может вибрация) добавит:
- Слышать окружающее (команды голосом без Telegram)
- Издавать звуки-уведомления
- Вибрация как способ привлечь внимание
- Self-perception через физический фидбэк

## Ссылки

- GitHub: [github.com/oliviazzzu/minimal-embodiment](https://github.com/oliviazzzu/minimal-embodiment)
- X/Twitter: [x.com/oliviazzzu/status/2049778751689425392](https://x.com/oliviazzzu/status/2049778751689425392/photo/2)