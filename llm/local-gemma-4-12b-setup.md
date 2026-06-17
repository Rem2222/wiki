---
type: concept
title: Local Gemma 4 12b Setup
description: >-
  Gemma 4 12B coder Q4_K_M — локальный запуск на домашнем ПК XE2690 через
  llama-server (Windows, CPU). Используется для Cursor, OpenClaw и веб-чата.
ingested_via: 'mcp:put_page'
ingested_at: '2026-06-16T15:40:59.505Z'
source_kind: 'mcp:put_page'
tags:
  - gemma
  - llama.cpp
  - llm
  - local
  - setup
  - windows
---

# Gemma 4 12B coder — локальный запуск

**Модель:** `gemma4-coding-Q4_K_M.gguf` (7.3 ГБ, 12B params, Q4_K_M)
**Источник:** yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF
**Инференс:** llama-server (CPU, Xeon E5-2690 v3, 12 ядер)

## Пути

- **Модель:** `D:\AI\models\gemma4-coding-Q4_K_M.gguf`
- **llama.cpp:** `C:\ai\llama-b9670-bin-win-cpu-x64\`
- **Сервис Windows:** GemmaServer (NSSM)

## Параметры запуска

```
llama-server.exe -m D:\AI\models\gemma4-coding-Q4_K_M.gguf --host 127.0.0.1 --port 8080 --threads 12 -ngl 0 -c 32768
```

- `-ngl 0` — без GPU (GT 1030 не помогает)
- `-c 32768` — 32K контекст
- `--threads 12` — половина ядер Xeon E5-2690 v3

## Доступ

- **Веб-чат:** http://127.0.0.1:8080
- **API:** http://127.0.0.1:8080/v1/chat/completions
- **Модель в API:** `gemma4-coding-Q4_K_M.gguf`

## Подключение

**Cursor:** Settings → Models → OpenAI Base URL: `http://127.0.0.1:8080/v1`, API Key: `any`, Model: `gemma4-coding-Q4_K_M.gguf`

**OpenClaw:**
```yaml
providers:
  gemma:
    base_url: http://127.0.0.1:8080/v1
    api_key: any
    default_model: gemma4-coding-Q4_K_M.gguf
```

## Скорость

~4-7 ток/с на CPU Xeon E5-2690 v3 (DDR4 @ 2133 MHz, 4 канала). Для чата и автокомплита достаточно, для продакшена — нет.
