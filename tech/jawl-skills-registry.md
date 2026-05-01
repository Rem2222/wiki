---
created: 2026-05-01
tags: [jawl, skills, registry, reference]
parent: "[[tech/jawl]]"
---

# JAWL Skills Registry

Полный список навыков (skills) по интерфейсам.

## Telegram Bot (Aiogram)

| Навык | Описание |
|-------|----------|
| simple_send | Отправка сообщений с throttle + hardblock |
| messages | Управление сообщениями |
| chats | Управление чатами |
| moderation | Модерация |

## Telegram Userbot (Telethon)

| Навык | Описание |
|-------|----------|
| admin | Администрирование групп |
| messages | Управление сообщениями |
| chats | Управление чатами |
| account | Управление аккаунтом |
| polls | Создание опросов |
| reactions | Реакции на сообщения |

## Host OS

| Навык | Описание |
|-------|----------|
| execution | Выполнение команд (access level L0-L3) |
| files | Файловые операции |
| monitoring | Системный мониторинг |
| network | Сетевые операции |
| system | Управление системой |

## Calendar

| Навык | Описание |
|-------|----------|
| management | Создание/чтение событий |

## Meta

| Навык | Описание |
|-------|----------|
| configuration | Чтение/изменение настроек |
| system | Системная информация |

## Multimodality

| Навык | Описание |
|-------|----------|
| vision | Анализ изображений |

## Регистрация навыков

```python
from src.l3_agent.skills.registry import SkillResult, skill

class MySkill:
    @skill()
    async def my_action(self, param: str) -> SkillResult:
        """Описание для LLM."""
        return SkillResult.ok("Результат")
```

## Access Levels (Host OS)

| Level | Разрешено |
|-------|----------|
| L0 | Чтение файлов |
| L1 | Запуск безопасных команд |
| L2 | Запуск произвольных команд |
| L3 | Полный доступ (root) |

## Как добавить навык

→ [[tech/jawl-howto-add-skill|HOWTO: Добавить навык]]
