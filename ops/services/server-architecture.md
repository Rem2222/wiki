---
description: "Полная карта серверной инфраструктуры VPS: сервисы, порты, связи, категории."
tags:
  - ops
  - architecture
  - index
type: map
related:
  - ops/services/hermes-agent
  - ops/services/gbrain
  - ops/services/agentmemory
  - ops/services/multica
  - ops/services/nginx
  - ops/services/authelia
  - ops/services/beszel
  - ops/services/cockpit
  - ops/services/duc
  - ops/services/tailscale
  - ops/services/ufw-fail2ban
  - ops/services/docker
  - ops/services/postgresql
  - ops/services/jawl
  - ops/services/gemini-web2api
  - ops/services/freellmapi
  - ops/services/freedeepseekapi
  - ops/services/ntfy
  - ops/services/codegraph
  - ops/services/hermes-dashboard
  - ops/services/mercury
  - ops/services/monitor-ui
  - ops/services/cgc
  - ops/services/multica-inbox-bridge
  - ops/services/multi-exporter
  - ops/services/unattended-upgrades
  - hosting/rdp-monster
  - ops/services/sshd
  - ops/services/agentmemory-exporter
  - ops/services/skills-dashboard
---

# Server Architecture

Полная карта серверной инфраструктуры VPS.

## Core (ядро)

- [[ops/services/hermes-agent]] — основной AI-агент
- [[ops/services/gbrain]] — графовая база знаний
- [[ops/services/agentmemory]] — долговременная память агента
- [[ops/services/multica]] — платформа managed-агентов
- [[ops/services/nginx]] — reverse proxy + SSL
- [[ops/services/authelia]] — SSO
- [[ops/services/multica-inbox-bridge]] — Multica → Telegram мост

## LLM Proxies

- [[ops/services/freellmapi]] — универсальный LLM-роутер
- [[ops/services/freedeepseekapi]] — DeepSeek Web Chat прокси
- [[ops/services/gemini-web2api]] — Gemini Web прокси

## Network

- [[ops/services/tailscale]] — mesh VPN
- [[ops/services/tor]] — Tor
- [[ops/services/sshd]] — SSH-сервер
- [[ops/services/ufw-fail2ban]] — файрвол + защита от брутфорса

## Storage

- [[ops/services/postgresql]] — PostgreSQL x2 (Multica + GBrain)
- [[ops/services/docker]] — Docker контейнеры

## Monitoring

- [[ops/services/beszel]] — мониторинг серверов
- [[ops/services/cockpit]] — веб-администрирование
- [[ops/services/duc]] — визуализация дисков
- [[ops/services/ntfy]] — push-уведомления
- [[ops/services/monitor-ui]] — панель управления ntfy
- [[ops/services/multi-exporter]] — Prometheus exporter (ntfy, GBrain, Hermes, FreeLLMAPI)
- [[ops/services/agentmemory-exporter]] — Prometheus метрики AgentMemory
- [[ops/services/hermes-dashboard]] — веб-дашборд Hermes
- [[ops/services/skills-dashboard]] — Skills Approval Dashboard
- [[ops/services/mercury]] — Mercury Agent Dashboard

## Agent Platform

- [[ops/services/jawl]] — Just Another Workflow Library
- [[ops/services/codegraph]] — MCP-сервер графа кода
- [[ops/services/cgc]] — CodeGraphContext MCP-сервер

## System

- [[ops/services/unattended-upgrades]] — автообновления безопасности
