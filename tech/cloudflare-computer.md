---
description: "Cloudflare Computer — виртуальный «компьютер» для агентов: ФС в Durable Object, плаггируемые бэкенды (container/shell/JS). (TypeScript, MIT, preview)."
tags: [cloudflare,agent,computer,durable-object,serverless]
related: [[tech/netbird]]
---

# cloudflare-computer

# GitHub Cloudflare Computer

**Cloudflare Computer** — виртуальный «компьютер» для агентов: виртуальная ФС внутри Durable Object (TypeScript, MIT, ★8.5k).

## Суть
Durable Object держит authoritative-состояние в SQLite и отдаёт один исполняемый вход через `workspace.runtime`. Три бэкенда:
- **Container** — проецирует SQLite в sandbox-container как FUSE-маунт; демон `computerd` маунтит состояние как ФС и синкается по capnweb RPC. Полный Linux userland, реальные бинари, реальная сеть.
- **Isolate shell** — запускает `just-bash` в Dynamic Worker, достигает Workspace по Workers RPC.
- **Isolate JavaScript** — ECMAScript-модуль в свежем Dynamic Worker, structured ввод/вывод, `node:fs/promises`, доверенные `ws:git` / `ws:artifacts`.

`workspace.runtime.exec(source, {backend})` — единая точка выполнения.

> ⚠️ **PREVIEW ONLY** — для фидбека, API нестабильны, НЕ для production.

## Зачем
Дать агенту (сети Cloudflare) полноценное исполняемое окружение — фактически выделенный «компьютер» с ФС, шеллом и возможностью писать/читать/экзекьютить, независимо от железа.

## Репо
`cloudflare/computer` · TypeScript · MIT · ★8.5k / 470 fork · создан 05.06.2026
