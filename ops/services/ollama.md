---
description: Ollama — локальный LLM-сервер (bge-m3 эмбеддинги для GBrain, qwen2.5:7b).
tags:
  - ops
  - service
  - ai-platform
type: service
related:
  - ops/services/gbrain
  - ops/services/freellmapi
service:
  name: ollama
  category: ai-platform
  purpose: Локальный запуск LLM-моделей и эмбеддингов (ollama serve + llama-server)
  install_date: 2026-08-05
  last_verified: 2026-08-12
  health_url: http://localhost:11434/
  type: systemd
  ports:
    - port: 11434
      protocol: tcp
      bind: 127.0.0.1
      description: ollama serve (REST API)
    - port: 42511
      protocol: tcp
      bind: 127.0.0.1
      description: llama-server (активная модель, bge-m3 embedding)
  systemd_units:
    - ollama
  docker_containers: []
  processes:
    - pattern: "ollama serve"
      description: Основной сервер
    - pattern: "llama-server"
      description: Инференс активной модели
  config_paths:
    - /usr/share/ollama/.ollama/models
  logs:
    - journalctl -u ollama
  depends_on: []
  data_size_hint: "5.5G (модели: bge-m3 1.2G, qwen2.5:7b 4.7G)"
  notes: >
    Установлен 5 августа 2026. С 09.08.2026 GBrain использует ollama:bge-m3 (1024 dims)
    вместо OpenRouter text-embedding-3-small — синк больше не зависит от кредитов OpenRouter.
    qwen2.5:7b — локальная LLM для экспериментов. Проверка эмбеддингов:
    curl -s http://127.0.0.1:11434/api/embed -d '{"model":"bge-m3","input":"тест"}' → 1024 dims.
---