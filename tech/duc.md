---
description: Disk usage визуализатор (sunburst-диаграммы). Фикс CGI redirect при клике на лепесток. Настройка duc-server.py.
tags: [duc, disk-usage, storage, cgi, server]
related: [[tech/cockpit]], ncdu
---

# Duc

**URL:** https://duc.zevv.nl  
**License:** GPLv2  
**Репозиторий:** https://github.com/zevv/duc

## Что это

Duc — утилита для визуализации использования дискового пространства. Генерирует sunburst-диаграммы (кольцевые графики), где каждый сегмент — директория, а размер сегмента пропорционален занимаемому месту. Работает как CGI-скрипт, доступный через браузер.

## Установка

```bash
apt install duc
```

## Настройка

Duc индексирует файловую систему в бинарный кэш, потом показывает диаграмму через CGI:

```bash
## Индексация (первичная)
duc index / -p   # -p = прогресс

## Индексация по расписанию
## Добавить в cron: 0 6 * * * duc index / -q
```

### duc-server.py

Для работы через HTTP используется Python-сервер, запускающий `duc cgi` как CGI-скрипт. Примерная структура:

```python
#!/usr/bin/env python3
import subprocess
import os
import sys
from http.server import HTTPServer, CGIHTTPRequestHandler

os.chdir('/')

class DucHandler(CGIHTTPRequestHandler):
    cgi_directories = ['/cgi-bin']

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8081), DucHandler)
    server.serve_forever()
```

Структура файлов:
```
/var/www/duc/
  ├── index.html        # страница с sunburst-диаграммой
  └── cgi-bin/
      └── duc           # симлинк на /usr/bin/duc
```

## Решение проблем

### 302 redirect при клике на лепесток sunburst

**Симптом:** При клике на лепесток (петалу) sunburst-диаграммы появляется сырой текст с CGI-заголовками:

```
Status: 302 Found
Location: ?path=/var/lib/...
URI: ?path=/var/lib/...
Connection: close
Content-type: text/html
```

Вместо перехода внутрь директории.

**Root cause:** JavaScript sunburst-диаграммы определяет координаты клика и шлёт запрос с координатами (`?x=...&y=...&path=...`). Команда `duc cgi` обрабатывает координаты, находит директорию, формирует **302 редирект** на путь этой папки. Старая версия `duc-server.py` не умела обрабатывать CGI-редиректы — она оборачивала сырой CGI-вывод (вместе с заголовками `Status:`, `Location:`, `URI:`) как тело 200-го ответа. Браузер показывал сырой текст вместо перехода.

**Фикс:** `duc-server.py` должен парсить CGI-вывод:

```python
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler

class DucHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Запускаем duc cgi
        proc = subprocess.run(
            ['duc', 'cgi'],
            capture_output=True,
            env={'QUERY_STRING': self.path.lstrip('/?')}
        )

        output = proc.stdout.decode()

        # Парсим CGI-заголовки
        headers = {}
        body_start = 0
        for i, line in enumerate(output.split('\n')):
            if line == '':
                body_start = i + 1
                break
            if ':' in line:
                key, val = line.split(':', 1)
                headers[key.strip()] = val.strip()

        # Определяем статус
        status = int(headers.get('Status', '200').split()[0])
        location = headers.get('Location', '')

        if status == 302:
            # Чистый редирект
            self.send_response(302)
            self.send_header('Location', location)
            self.end_headers()
        else:
            # Обычный ответ
            body = '\n'.join(output.split('\n')[body_start:])
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(body.encode())
```

**Ключевые моменты фикса:**
1. Читаем заголовок `Status:` → определяем HTTP-статус (302)
2. Читаем `Location:` → пробрасываем как HTTP-редирект
3. Отделяем CGI-заголовки от тела ответа (пустая строка — разделитель)
4. Возвращаем корректный 302-редирект браузеру

**Результат:** Клик по любому лепестку диаграммы ведёт внутрь папки, как и задумано.

