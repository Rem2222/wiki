---
description: "Mesh VPN / Zero-Trust-сеть на WireGuard, конкурент Tailscale (Go, сеть SSO/MFA, P2P)."
tags: [vpn,wireguard,mesh,zerotrust,networking]
related: [[ops/services/tailscale]] [[tech/dpi-zapret-netfix]]
---

# netbird

**NetBird** — mesh VPN / Zero-Trust сети на базе **WireGuard** (Go, BSD-3 + AGPLv3). Прямой конкурент [tailscale]([[ops/services/tailscale]]).

## Суть
Безконфигурная P2P-оверлейная сеть + централизованный контроль доступа в одном. Соединяет машины через зашифрованный WireGuard-туннель без открытия портов, сложных firewall-правил и VPN-шлюзов.

## Ключевые фичи
- **SSO + MFA**, access-политики через группы и правила, Zero-Trust (ZTNA)
- P2P через ICE/STUN/Signal (`pion/ice`), fallback на relay при CGNAT
- Web-админка (`netbirdio/dashboard`), SSH с центральными политиками, Browser SSH/RDP
- **Квантово-устойчивость** через Rosenpass
- Self-host ~5 мин (1 CPU / 2GB, порты 80/443/3478, свой домен)
- Public API, Terraform provider, Ansible, setup keys
- Платформы: Linux/macOS/Windows/Android/iOS/Apple TV + MikroTik/OpenWRT/pfSense/OPNsense/Proxmox/Docker/FreeBSD

## Архитектура
- `client/` — agent на каждой машине (управляет WireGuard)
- `management/` — состояние сети, IP пиров, распределение обновлений
- `signal/` — обмен кандидатами после ICE/STUN (end-to-end encrypted)
- `relay/` — fallback-туннель когда P2P невозможен (CGNAT)

## Лицензия (важно для self-host)
Основная часть — **BSD-3**, но `management/`, `signal/`, `relay/` — под **AGPLv3** (сгенерится требование открывать серверный код).

## Community
- `netbird-tui` — terminal UI для пиров/маршрутов
- `caddy-netbird` — Caddy-плагин, проксирует трафик через NetBird
- кастомный installer-скрипт

## Репо
`netbirdio/netbird` · 28.6k★ · Go · создан 04.2021 · активно обновляется · https://netbird.io
