---
created: 2026-05-16
updated: 2026-05-16
tags:
  - ai-agents
  - multiagent
  - jawl
  - moisha
  - jinx
type: guide
---

# JAWL — Мультиагентный режим

**Issue:** [MUL-74: МультиАгентность в Jawl](mention://issue/48f5d7e3-76ae-461b-850e-cef1a7fbd638)

Мультиагентный режим позволяет запускать **N независимых AI-агентов** в одном процессе. Каждый агент имеет изолированную базу данных, свои настройки LLM, личную папку с конфигами SOUL.md/STYLE.md, собственный Telegram-интерфейс и независимый Heartbeat-цикл.

## Где лежит код

Репозиторий: **github.com/th0r3nt/JAWL**

Ветка: `main`

Директория на сервере: `/tmp/jawl_repo/` — полный git worktree со всеми мультиагентными изменениями (незакоммичены).

```
/tmp/jawl_repo/
├── config/
│   ├── agents.example.yaml     # пример конфига для 2 агентов
│   └── agents.yaml             # рабочая конфигурация
├── src/
│   ├── main.py                 # точка входа (ветвление multi/single)
│   ├── builder.py              # SystemBuilder (single) + фабрика is_multi_agent_configured()
│   ├── l3_agent/
│   │   ├── runtime.py          # AgentRuntime — per-agent обёртка L0-L3
│   │   ├── runtime_builder.py  # AgentRuntimeBuilder — сборщик для 1 агента
│   │   ├── manager.py          # AgentManager — оркестратор всех агентов
│   │   ├── settings.py         # Pydantic модель AgentConfig + загрузчик agents.yaml
│   │   ├── prompt/builder.py   # per-agent SOUL.md/STYLE.md override
│   │   ├── skills/registry.py  # per-agent (SCOPE_AGENT) vs shared (SCOPE_SHARED) скиллы
│   │   └── context/builder.py  # ContextBuilder с agent_id для фильтрации скиллов
│   ├── cli/
│   │   ├── menu.py             # добавлен пункт «Агенты» в main_menu
│   │   ├── screens/
│   │   │   └── agents_dashboard.py  # questionary-цикл дашборда
│   │   └── widgets/
│   │       └── agent_widgets.py     # Rich-виджеты (таб-бар, панель, сводка)
│   ├── l2_interfaces/
│   │   ├── initializer.py      # L2 с is_skip_web_hooks флагом
│   │   ├── telegram/telethon/bootstrap.py  # per-agent session_name
│   │   └── telegram/aiogram/bootstrap.py   # per-agent session_name
│   └── utils/
│       ├── _tools.py           # get_agents_status_file_path()
│       ├── event/bridge.py     # EventBridge с типизацией Any
│       └── web/hooks/
│           ├── agents.py       # GET /api/agents — REST статус
│           └── router.py       # setup_agents_router()
```

## Как это работает

### Архитектура

```
main.py
  │
  ├── agents.yaml найден? ──да──→ AgentManager.full_lifecycle()
  │                                     │
  │                              build_all():               ← L0 синхронно
  │                              build_all_async():          ← L1-L3 асинхронно
  │                              start_all()                 ← запуск компонентов
  │                              run_all()                   ← asyncio.gather всех Heartbeat
  │                              stop_all()                  ← плавная остановка
  │
  └── agents.yaml не найден ──→ System.run() (legacy single-agent, полная обратная совместимость)
```

### AgentRuntime

Каждый агент — экземпляр `AgentRuntime`:
- Изолированный data dir: `local_data_dir/agents/<agent_id>/`
- Своя SQLite, Vector DB, Graph DB
- Свой LLM Client (разделяет API ключи, но может иметь свою модель)
- Свой Heartbeat (asyncio-задача)
- Свои метрики для дашборда (тики, токены, аптайм)

### AgentManager

Оркестратор:
- Читает `agents.yaml`
- Создаёт N `AgentRuntime`
- Собирает каждый через `AgentRuntimeBuilder`
- Запускает все Heartbeat-циклы конкурентно (`asyncio.gather + FIRST_COMPLETED`)
- Публикует `agents_status.json` для CLI дашборда

### Изоляция

| Аспект | Механизм |
|--------|----------|
| **Данные** | `local_data_dir/agents/<id>/sql/db/agent.db`, `.../vector/db/`, `.../graph/` |
| **Telegram** | Per-agent session_name, env-префиксы (`MOISHA_TELETHON_API_ID`) |
| **Personality** | Per-agent `SOUL.md`/`STYLE.md` из `agents/<id>/` (fallback на глобальные) |
| **Скиллы** | `SCOPE_AGENT` (Telegram-скиллы) + `SCOPE_SHARED` (Host OS, Web) |
| **Heartbeat** | Каждый агент — своя asyncio-задача |
| **WebHooks** | Singleton — один сервер на всех |

## Конфигурация (`agents.yaml`)

Файл: `config/agents.yaml` (создаётся автоматически из `agents.example.yaml` при первом запуске).

```yaml
agents:
  jinx:
    identity:
      agent_name: Jinx
    llm:
      main_model: gpt-4
      temperature: 0.9
      max_react_steps: 10
    system:
      heartbeat_interval: 600
      timezone: 3
    telegram:
      telethon:
        enabled: false
        session_name: "jinx_telethon"
        recent_chats_limit: 10
      aiogram:
        enabled: false
        recent_chats_limit: 10

  moisha:
    identity:
      agent_name: Moisha
    llm:
      main_model: gpt-4
      temperature: 1.0
      max_react_steps: 15
    system:
      heartbeat_interval: 300
      timezone: 3
    telegram:
      telethon:
        enabled: false
        session_name: "moisha_telethon"
      aiogram:
        enabled: false
        recent_chats_limit: 20
```

**Env-переменные для Telegram:** используются с префиксом `{AGENT_ID_UPPER}_`:
- `MOISHA_TELETHON_API_ID` / `MOISHA_TELETHON_API_HASH`
- `JINX_TELETHON_API_ID` / `JINX_TELETHON_API_HASH`
- Если переменная с префиксом не найдена — fallback на глобальную `TELETHON_API_ID`

**Если `agents.yaml` отсутствует** — JAWL запускается в legacy single-agent режиме как обычно. Полная обратная совместимость.

## Как запускать

### Обычный запуск (мультиагент если есть agents.yaml)

```bash
cd /tmp/jawl_repo
python -m src.main
```

Система сама определит режим:
- `agents.yaml` есть → мультиагент (AgentManager)
- `agents.yaml` нет → single-agent (SystemBuilder)

### Подготовка нового агента

1. Добавить секцию в `agents.yaml`:

```yaml
agents:
  новый_агент:
    identity:
      agent_name: Новый Агент
    llm:
      main_model: gpt-4
      temperature: 0.8
      max_react_steps: 12
    system:
      heartbeat_interval: 300
    telegram:
      telethon:
        enabled: true
        session_name: "noviy_telethon"
```

2. Добавить Telegram ключи в `.env`:

```
НОВЫЙ_АГЕНТ_TELETHON_API_ID=12345
НОВЫЙ_АГЕНТ_TELETHON_API_HASH=abc123...
```

3. (Опционально) Создать персональную личность:

```bash
mkdir -p src/utils/local/data/agents/новый_агент/
# положить SOUL.md и/или STYLE.md в эту папку
```

## Как смотреть за работой

### 1. CLI Dashboard

Вкладка **«Агенты»** в основном меню JAWL.

```
┌─────────────────────────────────────────────────────────┐
│              🤖 ДАШБОРД АГЕНТОВ                          │
├─────────────────────────────────────────────────────────┤
│ [○ Все]  [● Moisha]  [○ Jinx]                          │
│                                                         │
│ ┌─ Moisha ────────────────────────────────────────────┐ │
│ │  ● ONLINE  │  PID: 12345                            │ │
│ │  Модель: gpt-4                                      │ │
│ │  Heartbeat: 300s  │  Последний тик: 12s назад      │ │
│ │  Аптайм: 2ч 15м  │  Тиков: 1,234                    │ │
│ │  Последняя активность: 2 мин назад                   │ │
│ │  "Привет, чем помочь?"                               │ │
│ │  Интерфейсы: ● TG Telethon  ○ TG Aiogram  ● Web... │ │
│ └────────────────────────────────────────────────────┘ │
│                                                         │
│ [↩ К выбору]  [▶ Запустить]  [■ Остановить]  [↩ Меню] │
└─────────────────────────────────────────────────────────┘
```

**Статусы:**
- ● ONLINE (зелёный) — агент работает
- ○ OFFLINE (красный) — агент остановлен
- ● STALE (жёлтый) — статус не обновлялся >30с

**Навигация:** ↑↓ Enter (questionary keyboard-only)

### 2. REST API

```bash
curl http://localhost:8080/api/agents
```

Возвращает JSON:

```json
{
  "moisha": {
    "id": "moisha",
    "name": "Moisha",
    "status": "online",
    "pid": 12345,
    "model": "gpt-4",
    "heartbeat_interval": 300,
    "started_at": "2026-05-16T14:30:00+0300",
    "last_tick_at": "2026-05-16T17:15:23+0300",
    "total_ticks": 42,
    "interfaces": {"telegram_telethon": true, "github": false, ...}
  }
}
```

### 3. Логи

```
/tmp/jawl_repo/logs/
├── jawl.log              — общие логи
├── jawl.error.log        — только ошибки
└── agents/<agent_id>/   — per-agent логи (если настроено)
```

В логах есть префикс `[AgentManager]`, `[AgentRuntime:moisha]`, `[EntryPoint]`, etc.

## Основные файлы (карта)

| Файл | Назначение |
|------|-----------|
| `src/main.py` | Точка входа. Ветвление multi/single-agent через `is_multi_agent_configured()` |
| `src/builder.py` | SystemBuilder (single) + `is_multi_agent_configured()` |
| `src/l3_agent/runtime.py` | Per-agent контейнер L0-L3 (аналог System для 1 агента) |
| `src/l3_agent/runtime_builder.py` | Сборщик 1 рантайма (выделен из SystemBuilder) |
| `src/l3_agent/manager.py` | Оркестратор: создание, сборка, запуск, остановка всех агентов |
| `src/utils/settings.py` | Pydantic-модели: `AgentConfig`, `AgentsConfig` + `load_agents_config()` |
| `src/l3_agent/skills/registry.py` | Per-agent (SCOPE_AGENT) vs shared (SCOPE_SHARED) скиллы |
| `src/l3_agent/prompt/builder.py` | SOUL.md/STYLE.md per-agent override |
| `src/cli/screens/agents_dashboard.py` | Questionary-цикл дашборда агентов |
| `src/cli/widgets/agent_widgets.py` | Rich-виджеты (таб-бар, детальная панель, сводка) |
| `src/utils/web/hooks/agents.py` | GET /api/agents — REST endpoint |
| `src/utils/web/hooks/router.py` | Регистрация роутера |
| `config/agents.yaml` | Конфигурация агентов |
| `config/agents.example.yaml` | Пример конфига |

## Типичные проблемы

1. **`agents_status.json` пустой** — дашборд показывает «Нет данных». Проверить, запущен ли AgentManager (а не single-agent System).
2. **Порт 8080 занят** — WebHooks стартует один раз для первого агента. Если стартует второй раз — проверить, что в `interfaces.yaml` `web.hooks.enabled` не включён для второго.
3. **Telegram сессии конфликтуют** — если session_name одинаковый для двух агентов, Telethon упадёт. В конфиге имена должны быть уникальными (автоматически префиксируются agent_id при дефолтном значении).
4. **Один агент не стартует** — ошибка не валит всех. AgentManager логирует `[AgentRuntime:moisha] Ошибка запуска` и продолжает с остальными.

## Запуск на VPS

Код в `/tmp/jawl_repo/` — это git worktree. Для продакшена:

```bash
# скопировать в постоянное место или сделать deploy-скрипт
cp -r /tmp/jawl_repo /opt/jawl-multiagent/
cd /opt/jawl-multiagent
cp .env.example .env  # настроить ключи
nano config/agents.yaml  # настроить агентов
python -m src.main
```
