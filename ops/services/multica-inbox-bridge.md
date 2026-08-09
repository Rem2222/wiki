---
description: Multica Inbox → Telegram Bridge — доставка уведомлений из Multica в Telegram.
tags:
  - ops
  - service
  - core
type: service
related:
  - ops/services/multica
service:
  name: multica-inbox-bridge
  category: core
  purpose: Мост Multica → Telegram
  install_date: 2026-07-03
  last_verified: 2026-08-10
  health_url: 
  type: systemd
  systemd_units:
    - multica-inbox-bridge
  depends_on:
    - multica
  notes: Доставляет уведомления из Multica в Telegram.
---
