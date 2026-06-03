---
description: Навык (skill) — метод Python с `@skill()` декоратором, возвращающий `SkillResult`. Привязан к L2 интерфейсу.
created: 2026-05-01
tags: [jawl, howto, skill]
parent: "[[tech/jawl]]"

# HOWTO: Добавить навык в JAWL

## Обзор

Навык (skill) — метод Python с `@skill()` декоратором, возвращающий `SkillResult`. Привязан к L2 интерфейсу.

## Шаги

### 1. Выбрать интерфейс

| Интерфейс | Папка |
|-----------|-------|
| Aiogram Bot | `src/l2_interfaces/telegram/aiogram/skills/` |
| Telethon Userbot | `src/l2_interfaces/telegram/telethon/skills/` |
| Host OS | `src/l2_interfaces/host/os/skills/` |
| Calendar | `src/l2_interfaces/calendar/skills/` |
| Meta | `src/l2_interfaces/meta/skills/` |
| Multimodality | `src/l2_interfaces/multimodality/skills/` |

### 2. Создать файл

```python
## src/l2_interfaces/host/os/skills/my_skill.py

from src.l3_agent.skills.registry import SkillResult, skill
from src.l2_interfaces.host.os.client import HostOSClient

class HostOSMySkill:
    def __init__(self, client: HostOSClient):
        self.client = client

    @skill()
    async def my_action(self, param1: str, param2: int = 10) -> SkillResult:
        """
        Краткое описание — попадёт в промпт LLM.
        
        Args:
            param1: Описание параметра 1
            param2: Описание параметра 2 (default: 10)
        """
        try:
            result = f"Выполнено: {param1}, {param2}"
            return SkillResult.ok(result)
        except Exception as e:
            return SkillResult.fail(f"Ошибка: {e}")
```

### 3. Зарегистрировать в bootstrap.py

```python
from src.l2_interfaces.host.os.skills.my_skill import HostOSMySkill

class HostOSBootstrap:
    def __init__(self, ...):
        self.my_skill = HostOSMySkill(client)
```

### 4. Перезапустить JAWL

```bash
bash /home/rem/JAWL/scripts/start-safe.sh
```

## Правила

- Обязателен декоратор `@skill()` — без него LLM не увидит навык
- Типы параметров в сигнатуре помогают LLM вызывать правильно
- Docstring первого абзаца = описание для LLM
- Всегда async def
- Всегда возвращай `SkillResult`, не raw string
- Для Host OS: проверяй `self.client.access_level`

## Связанные статьи

- [[tech/jawl-skills-registry|Skills Registry]] — все существующие навыки
- [[tech/jawl-howto-add-interface|HOWTO: Добавить интерфейс]]
