---
description: Каждый L2 интерфейс состоит из 3 файлов:
created: 2026-05-01
tags: [jawl, howto, interface]
related: [[tech/jawl]] [[tech/jawl-architecture]] [[tech/jawl-howto-add-provider]]
parent: "[[tech/jawl]]"

# HOWTO: Добавить L2 интерфейс в JAWL

## Структура интерфейса

Каждый L2 интерфейс состоит из 3 файлов:

```
src/l2_interfaces/<interface>/
├── client.py       ← Подключение к внешнему сервису
├── events.py       ← Обработка входящих событий
├── bootstrap.py    ← Инициализация и регистрация навыков
└── skills/         ← Навыки интерфейса
    ├── __init__.py
    └── my_skill.py
```

## Шаги

### 1. Создать структуру

```bash
mkdir -p src/l2_interfaces/my_interface/skills
touch src/l2_interfaces/my_interface/__init__.py
touch src/l2_interfaces/my_interface/skills/__init__.py
```

### 2. client.py

```python
class MyClient:
    def __init__(self, config):
        self.config = config
    
    async def connect(self):
        """Установить подключение."""
        pass
    
    async def disconnect(self):
        """Закрыть подключение."""
        pass
```

### 3. events.py

```python
from src.utils.event.bus import EventBus
from src.utils.event.registry import Events

class MyEvents:
    def __init__(self, client: MyClient, bus: EventBus):
        self.client = client
        self.bus = bus
    
    async def start(self):
        """Запустить обработку событий."""
        pass
```

### 4. bootstrap.py

```python
from src.l2_interfaces.my_interface.client import MyClient
from src.l2_interfaces.my_interface.events import MyEvents

class MyBootstrap:
    def __init__(self, bus, agent_state):
        self.client = MyClient(config)
        self.events = MyEvents(self.client, bus)
        # Регистрация навыков
        from src.l2_interfaces.my_interface.skills.my_skill import MySkill
        self.my_skill = MySkill(self.client)
    
    async def start(self):
        await self.client.connect()
        await self.events.start()
```

### 5. Зарегистрировать в main.py

```python
from src.l2_interfaces.my_interface.bootstrap import MyBootstrap

## В методе инициализации
self.my_interface = MyBootstrap(self.bus, self.agent_state)
await self.my_interface.start()
```

### 6. Добавить навыки

→ [[tech/jawl-howto-add-skill|HOWTO: Добавить навык]]

## Существующие интерфейсы

→ [[tech/jawl-skills-registry|Skills Registry]] — полный список

## Связанные статьи

- [[tech/jawl-architecture|Architecture]] — расположение в L0-L3
- [[tech/jawl-events|EventBus]] — события для взаимодействия
