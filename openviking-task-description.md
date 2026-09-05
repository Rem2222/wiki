# OpenViking: загрузка данных из Hermes state.db

## Контекст

OpenViking установлен на VPS (Docker, `127.0.0.1:8900`). Контейнер работает, данные НЕ загружены. 
Нужно выгрузить все сессии/сообщения из `state.db` и загрузить в OpenViking для формирования долгосрочной памяти агента.

## Источник данных

**state.db** (`/root/.hermes/state.db`) — SQLite с FTS5:
- Таблица `sessions` — все сессии (telegram, cron, cli)
- Таблица `messages` — все сообщения (user + assistant)
- Фильтрация: только `role='user'` (чтобы не загружать ответы агента как контекст)

## Целевая структура в OpenViking

```
viking://user/default/memories/
├── .abstract          — "Personal memory bank from Hermes agent conversations"
├── .overview          — "Facts, preferences, and conversation history (~37k facts)"
├── sessions/
│   ├── 2026-08-07_telegram.md    — сессия за день
│   ├── 2026-08-08_cron.md        — cron-выводы за день
│   └── ...
└── facts/
    └── (автоматически из semantic processing)
```

## План выполнения

### Шаг 1: Экспорт из state.db

Создать скрипт `/root/openviking-export.py`:

```python
import sqlite3, json, os
from datetime import datetime, timedelta
from collections import defaultdict

DB_PATH = os.path.expanduser("~/.hermes/state.db")
OUTPUT_DIR = "/root/openviking-export"

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

# Получаем все сессии
sessions = conn.execute("""
    SELECT id, source, title, started_at, ended_at 
    FROM sessions 
    WHERE ended_at IS NOT NULL
    ORDER BY started_at
""").fetchall()

# Группируем по дням и платформе
daily = defaultdict(list)
for s in sessions:
    date = datetime.fromtimestamp(s['started_at']).strftime('%Y-%m-%d')
    source = s['source'] or 'unknown'
    daily[(date, source)].append(s)

# Для каждой сессии получаем сообщения
for (date, source), sess_list in daily.items():
    messages = []
    for s in sess_list:
        msgs = conn.execute("""
            SELECT role, content, created_at 
            FROM messages 
            WHERE session_id = ? AND role = 'user'
            ORDER BY created_at
        """, (s['id'],)).fetchall()
        for m in msgs:
            messages.append({
                'time': datetime.fromtimestamp(m['created_at']).strftime('%H:%M'),
                'text': m['content'][:2000]  # обрезаем длинные сообщения
            })
    
    if messages:
        # Формируем markdown
        lines = [f"# {date} ({source})\n"]
        for msg in messages:
            lines.append(f"## {msg['time']}\n")
            lines.append(msg['text'])
            lines.append("")
        
        # Записываем файл
        filename = f"{date}_{source}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'w') as f:
            f.write('\n'.join(lines))

print(f"Exported {len(daily)} daily files to {OUTPUT_DIR}")
```

### Шаг 2: Загрузка в OpenViking

Создать скрипт `/root/openviking-import.py`:

```python
import os, json, requests, time

OV_URL = "http://127.0.0.1:8900"
EXPORT_DIR = "/root/openviking-export"
BATCH_SIZE = 50

def batch_write(files):
    operations = []
    for f in files:
        with open(os.path.join(EXPORT_DIR, f)) as fh:
            content = fh.read()
        uri = f"viking://user/default/memories/sessions/{f}"
        operations.append({"uri": uri, "content": content, "mode": "create"})
    
    resp = requests.post(f"{OV_URL}/api/v1/content/batch-write", json={
        "root_uri": "viking://user/default/memories/sessions",
        "operations": operations,
        "wait": False
    })
    return resp.json()

# Создаём директории
requests.post(f"{OV_URL}/api/v1/fs/mkdir", json={"uri": "viking://user/default/memories/sessions"})

# Загружаем файлы батчами
files = sorted(os.listdir(EXPORT_DIR))
for i in range(0, len(files), BATCH_SIZE):
    batch = files[i:i+BATCH_SIZE]
    result = batch_write(batch)
    print(f"Batch {i//BATCH_SIZE + 1}: {len(batch)} files, status={result.get('status')}")
    time.sleep(1)  # пауза для Ollama

print(f"Total: {len(files)} files loaded")
```

### Шаг 3: Верификация

1. Проверить статус очереди: `curl -s http://127.0.0.1:8900/api/v1/observer/queue`
2. Recall-тест: `curl -s http://127.0.0.1:8900/api/v1/search/recall -d '{"query":"Где я живу?","limit":3}'`
3. Проверить количество файлов: `curl -s "http://127.0.0.1:8900/api/v1/fs/ls?uri=viking://user/default/memories/sessions"`

### Шаг 4: Мониторинг обработки

Semantic processing (L0/L1/L2) идёт в фоне через VLM (mimo-v2.5). Скорость: ~5-60 сек/файл.

Проверка:
```bash
# Очередь
curl -s http://127.0.0.1:8900/api/v1/observer/queue | python3 -m json.tool

# Обработанные файлы
curl -s "http://127.0.0.1:8900/api/v1/fs/ls?uri=viking://user/default/memories/sessions" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for item in d.get('result',[]):
    print(f\"{item['uri'].split('/')[-1]:40s} {item.get('size',0):>6d} bytes\")
"
```

## Не забыть

- Скрипты `/root/openviking-export.py` и `/root/openviking-import.py` уже созданы (обновить под новый формат)
- После загрузки — подождать обработки (очередь Embedding + Semantic)
- Внешний доступ (nginx) пока НЕ нужен
- Интеграция с Hermes — позже (только один memory provider за раз)
