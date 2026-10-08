---
description: JAWL — Just Another Workflow Library. Python-агент (Jinx). УДАЛЁН 2026-10-03.
tags:
  - ops
  - service
  - archived
type: service
status: removed
related:
  - ops/services/dex
  - ops/services/hermes-agent
service:
  name: jawl
  category: agent-platform
  purpose: Автономный Python-агент (Jinx)
  install_date: 2025-06
  removed_date: 2026-10-03
  removed_reason: >-
    Заменён самописным Дексом Романа. Остановлен (user-юнит jawl + jawl-dashboard,
    понадобился SIGKILL — висел в deactivating), удалены unit-файлы jawl.service (user),
    jawl.service (system, legacy-дубль), jawl-dashboard.service и каталог /root/JAWL (1.1G);
    nginx-роут /jawl/ снят ещё 2026-10-02. Хроническая причина неработоспособности:
    LLM отвечает 404 «model unavailable for free» (slug nemotron-3-nano-30b-a3b)
    плюс TelegramConflictError getUpdates/webhook ~66 часов.
  last_verified: 2026-10-08
  type: systemd (user) — удалён
  backup: /root/backups/jawl-final-20261003.tar.gz (226M, 1155 файлов, без venv)
  notes: >-
    Был автономный Python-агент ~1.3G RAM, дашборд :5002 (включался через systemd jawl-dashboard),
    Telegram-бот @Jawl_Jinx_bot, LLM OpenRouter (nvidia/nemotron-3-nano-30b-a3b:free),
    вектор на fastembed MiniLM и граф на kuzu 0.11.3 (Graph DB инициализировался при старте).
    Вместе с venv уехали в архив python-пакет kuzu и бэкапы логов; остаток /root/JAWL-rem
    (git-чекаут от 2026-06-01, 2.4M) не трогали. Данных для переноса не осталось —
    агент не вёл внешних хранилищ.
last_verified: 2026-10-09
---
