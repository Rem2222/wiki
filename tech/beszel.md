---
description: Лёгкая система мониторинга серверов. Docker compose (Hub + Agent), решение проблем с сетью.
tags: [beszel, monitoring, docker, metrics, hub, agent]
related: [[tech/cockpit]], docker
---

# Beszel

**URL:** https://beszel.dev  
**License:** MIT  
**Репозиторий:** https://github.com/henrygd/beszel

## Что это

Beszel — лёгкая система мониторинга серверов с веб-интерфейсом. Hub (центральный сервер с UI) + Agent (на отслеживаемых системах). Метрики CPU, RAM, диск, сеть, процессы. Минималистичный интерфейс.

## Установка (Docker compose)

```yaml
services:
  beszel:
    image: henrygd/beszel:latest
    container_name: beszel
    restart: unless-stopped
    ports:
      - 127.0.0.1:9480:9480
    volumes:
      - ./beszel_data:/beszel_data

  beszel-agent:
    image: henrygd/beszel-agent:latest
    container_name: beszel-agent
    restart: unless-stopped
    environment:
      PORT: 45876
      KEY: <agent-key>
    ports:
      - 127.0.0.1:45876:45876
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - /:/mnt/host:ro
```

Hub доступен на `http://localhost:9480` (за reverse proxy — `https://rem2222.top/beszel/`).

## Как добавить систему в Hub

1. Запустить Hub, зайти в веб-интерфейс
2. Add System → имя хоста + ключ агента
3. Запустить Agent с этим ключом

## nginx reverse proxy

```nginx
location /beszel/ {
    auth_request /authelia/api/verify;
    proxy_pass http://127.0.0.1:9480/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_buffering off;
}
```

## Проблемы и решения

### Agent offline

**Симптом:** Hub видит Agent, но статус Offline.

**Root cause:** Docker network isolation — Hub и Agent в разных сетях.

**Решение:** Подключить Agent к сети Hub:
```bash
docker network connect beszel_default beszel-agent
```

### Agent не видит Docker-контейнеры

**Решение:** Пробросить `/var/run/docker.sock`.

## Ссылки

- Hub UI: `https://rem2222.top/beszel/`
- Agent порт: 45876 (localhost)
