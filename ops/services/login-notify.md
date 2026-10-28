---
description: "login-notify.sh — PAM-хук: уведомление в ntfy о каждом SSH-входе (+ локальный лог)."
tags:
  - ops
  - service
  - security
  - notifications
type: service
related:
  - ops/services/sshd
  - ops/services/ntfy
service:
  name: login-notify
  category: security
  purpose: Уведомлять в ntfy о каждом открытии SSH-сессии с классификацией источника (Tailscale / внешний / локальный)
  install_date: 2026-10-17
  last_verified: 2026-10-29
  health_url:
  type: pam hook (bash script)
  processes:
    -
      pattern: login-notify.sh
  config_paths:
    - /usr/local/bin/login-notify.sh
    - /etc/pam.d/sshd
    - /root/.hermes/.env
  logs:
    - /var/log/login-notify.log
  depends_on:
    - ntfy
    - sshd
  notes: >-
    Вызывается из /etc/pam.d/sshd строкой `session optional pam_exec.so /usr/local/bin/login-notify.sh`.
    Работает только на PAM_TYPE=open_session (закрытие сессии игнорируется). При любом сбое логин
    не ломается (флаг optional). Тема/URL берутся из /root/.hermes/.env (NTFY_TOPIC, NTFY_URL);
    если NTFY_URL пуст — фолбэк http://127.0.0.1:2586.
last_verified: 2026-10-29
---

# login-notify

PAM-хук, который шлёт уведомление в ntfy при каждом входе по SSH и дописывает строку в локальный лог.

## Как устроено

- Точка входа: `/etc/pam.d/sshd` → `session optional pam_exec.so /usr/local/bin/login-notify.sh` (добавлен 2026-10-17).
- Обрабатывается только `open_session` — закрытие сессии не шлёт уведомлений.
- Источник (`$PAM_RHOST`) классифицируется:
  - `127.*` / `::1` — локальный вход (сам сервер), priority default;
  - `100.*` — вход через Tailscale, priority default;
  - пусто/неизвестно — priority high, тег `warning`;
  - всё остальное — **ВНЕШНИЙ вход**, priority urgent, тег `rotating_light`.
- Дублируется в `/var/log/login-notify.log` (формат `дата | user=… | from=…`).

## Проверка

```bash
grep pam_exec /etc/pam.d/sshd          # строка на месте
tail -5 /var/log/login-notify.log      # последние входы
```

Живой вход от 2026-10-21 00:35 (root, 100.80.140.66 — Tailscale) подтверждает, что хук отрабатывает.

## Связанные

- [[ops/services/sshd]] — сервер SSH, в котором висит хук.
- [[ops/services/ntfy]] — получатель уведомлений (порт 2586).
