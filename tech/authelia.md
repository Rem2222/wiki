---
description: Self-hosted SSO (Single Sign-On) сервер. Docker compose, конфигурация, интеграция с nginx auth_request, решение проблем.
tags: [authelia, sso, auth, nginx, docker, security]
related: [[tech/cockpit]], nginx, docker
---

# Authelia

**URL:** https://www.authelia.com  
**License:** Apache 2.0  
**Репозиторий:** https://github.com/authelia/authelia

## Что это

Authelia — self-hosted SSO-сервер с поддержкой двухфакторной аутентификации. Позволяет централизованно защитить несколько веб-сервисов за одним логином. Работает через nginx auth_request — nginx проверяет куку/токен через Authelia перед каждым запросом.

## Установка (Docker compose)

Authelia запускается в Docker вместе с Redis. Используется файловая база пользователей (users_database.yml).

### docker-compose.yml

```yaml
services:
  authelia:
    image: authelia/authelia:latest
    container_name: authelia
    restart: unless-stopped
    ports:
      - 127.0.0.1:9091:9091
    volumes:
      - ./config:/config
    environment:
      TZ: Europe/Moscow
    depends_on:
      - redis

  redis:
    image: redis:alpine
    container_name: authelia-redis
    restart: unless-stopped
```

### configuration.yml (ключевые настройки)

```yaml
theme: dark
log_level: debug
server:
  host: 0.0.0.0
  port: 9091
  path: /authelia
totp:
  issuer: rem2222.top
access_control:
  default_policy: deny
  rules:
    - domain: rem2222.top
      resources:
        - '^/authelia($|/.*$)'
      policy: bypass
    - domain: rem2222.top
      resources:
        - '^/cockpit(/.*)?$'
        - '^/hermes(/.*)?$'
        - '^/opencode(/.*)?$'
        - '^/beszel(/.*)?$'
      policy: one_factor
authentication_backend:
  file:
    path: /config/users_database.yml
session:
  name: authelia_session
  secret: <random-secret>
  expiration: 1h
  inactivity: 5m
  domain: rem2222.top
```

### users_database.yml

```yaml
users:
  rem2222:
    password: <bcrypt-hash>
    displayname: Roman
    email: rem2222@gmail.com
    groups:
      - admin
```

Пароль (bcrypt) генерируется через authelia.

## Настройка nginx

### Сниппет для auth_request

**/etc/nginx/snippets/authelia-location.conf:**

```nginx
set $upstream_authelia http://127.0.0.1:9091;
auth_request /authelia/api/verify;
auth_request_set $user $upstream_http_remote_user;
auth_request_set $groups $upstream_http_remote_groups;
auth_request_set $name $upstream_http_remote_name;
auth_request_set $email $upstream_http_remote_email;
proxy_set_header Remote-User $user;
proxy_set_header Remote-Groups $groups;
proxy_set_header Remote-Name $name;
proxy_set_header Remote-Email $email;
```

### Прокси к Authelia

```nginx
location /authelia/ {
    proxy_pass http://127.0.0.1:9091;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_buffering off;
    rewrite ^/authelia/(.*) /$1 break;
}

location /authelia/api/verify {
    internal;
    proxy_pass http://127.0.0.1:9091/api/verify;
    proxy_pass_request_body off;
    proxy_set_header Content-Length "";
    proxy_set_header X-Original-URL $scheme://$http_host$request_uri;
    proxy_set_header X-Original-Method $request_method;
}
```

## Проблемы и решения

### 404 на JS/CSS при /authelia/ sub-path

**Симптом:** HTML страница логина без стилей — JS/CSS не грузятся (404).

**Root cause:** Authelia ожидает статику по `/authelia/...`, но nginx не пробрасывает путь.

**Фикс:** 
1. `server.path: /authelia` в configuration.yml
2. `rewrite ^/authelia/(.*) /$1 break;` в nginx

### 403 на /api/state

**Симптом:** 403 Forbidden при попытке войти.

**Root cause:** `/authelia/api/state` доступен только с localhost.

**Фикс:** Явный rewrite для api в nginx.

### Session/redirect loop после логина

**Симптом:** После ввода пароля обратно на форму логина.

**Фикс:** Проверить `session.domain: rem2222.top` и `X-Forwarded-Proto`.

## Переход с auth_basic на Authelia

1. Удалить `auth_basic` / `auth_basic_user_file` из nginx
2. Подключить `include snippets/authelia-location.conf;`
3. Добавить location /authelia/ в nginx
4. Настроить access_control в configuration.yml
5. Запустить Authelia + Redis

## Логин

- **Пользователь:** rem2222
- **Пароль:** OpenClaw2024!
