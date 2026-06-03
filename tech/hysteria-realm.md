---
description: P2P-режим Hysteria, не требующий публичного IP и проброса портов. Сервер регистрирует realm (имя) в сервисе рандеву (rendezvous), клиент подключается к тому же realm — они пробивают UDP hole punchi...
tags: [tech]
---

# Hysteria 2 Realm — P2P-режим без публичного IP

## Что такое Realm

P2P-режим Hysteria, не требующий публичного IP и проброса портов. Сервер регистрирует realm (имя) в сервисе рандеву (rendezvous), клиент подключается к тому же realm — они пробивают UDP hole punching и соединяются напрямую.

## Как работает

1. Сервер регистрирует realm в rendezvous-сервере, сообщая свои UDP-адреса (через STUN)
2. Клиент с тем же realm-адресом просит rendezvous соединить
3. Rendezvous возвращает адреса — обе стороны шлют UDP-пакеты друг другу, пробивая NAT
4. Отверстие открыто — QUIC-рукопожатие идёт напрямую. Rendezvous выходит из игры

**Rendezvous не передаёт трафик** — только знакомит стороны.

## Realm-адрес

Формат:
```
realm://token@rendezvous-host:port/realm-name
```

- `realm://` — HTTPS (порт 443, рекомендуется)
- `realm+http://` — HTTP (только для разработки)
- `token` — bearer-токен rendezvous
- `realm-name` — имя, общее для клиента и сервера

Параметры URL:
- `?stun=host:port` — кастомный STUN-сервер
- `?lport=1234` — привязать локальный UDP-сокет к порту

## Публичный rendezvous

```
realm://public@realm.hy2.io/твой-realm-name
```

Без гарантий. Бесплатно, as-is.

Можно развернуть свой rendezvous-сервер.

## Конфигурация сервера

```yaml
## server.yaml
realm:
  addr: realm://public@realm.hy2.io/moy-server

acl:
  inline:
    - allow all
    - proxy all

bandwidth:
  up: 100 mbps
  down: 100 mbps
```

## Конфигурация клиента

```yaml
## client.yaml
server: realm://public@realm.hy2.io/moy-server
auth: ПАРОЛЬ_ОТ_СЕРВЕРА

transport:
  type: udp

socks5:
  listen: 127.0.0.1:1080

http:
  listen: 127.0.0.1:8080
```

## Плюсы/минусы

**Плюсы:** не нужен домен, не нужен открытый порт, можно с телефона/дома/кафе
**Минусы:** зависит от работоспособности rendezvous, UDP hole punching не всегда работает (симметричный NAT),速度 может быть ниже чем у прямого сервера
