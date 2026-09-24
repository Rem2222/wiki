---
description: "Qwen3.8-Flash-Next (176B-класс, 111 GB GGUF) на GTX 1080 Ti 11 GB через llama.cpp + DeepSeek Harness: рецепт offload, флаги llama-server, подключение DSH-плагина, 11 tok/s."
tags: [llm, qwen, gguf, llama.cpp, dsh, deepseek-harness, gpu, moe, local-ai]
related: ["[[tech/qwen38-27b-local-gpu]]", "[[tech/local-models-1c-sept2026]]", "[[llm/local-gemma-4-12b-setup]]"]
updated: 2026-09-23
source: "https://habr.com/ru/articles/1085544/"
---

# Qwen3.8-Flash-Next 176B на GTX 1080 Ti — рецепт запуска в DSH

Разбор статьи @SkalolazOther на Habr: как запустить модель **176B-класса** (GGUF ~111 GB) на видеокарте с **11 GB VRAM** и получить ~11 tok/s.

## Почему это вообще возможно

| Параметр | Значение |
|---|---|
| Основная модель | 125B |
| n-gram embedding-таблицы | ~51B |
| Итого «176B-класс» | 125B + 51B |
| **Активируется на токен** | **~6B** |
| MoE | 512 экспертов, 10 маршрутизируемых + shared |
| Слои | 48 (3 из 4 — Gated DeltaNet, каждый 4-й — QSA) |
| Нативный контекст | 262 144 (256K) |
| MTP-компонент | 4B |
| Квантовка в кейсе | Unsloth `UD-Q4_K_XL` ≈ 111 GB |

Ключ: **MoE + hybrid CPU/GPU execution**. Веса не обязаны помещаться в VRAM — карта работает ускорителем, основная масса модели живёт в RAM, а часть таблиц лениво грузится с SSD.

> Qwen называет модель ранним предпросмотром архитектуры, лежащей в основе Qwen4. В llama.cpp внутреннее имя — `qwen4exp`.

## Требования

**Железо (минимум для описанного кейса):**
- GPU ~10–12 GB VRAM
- ≥ 64 GB RAM
- быстрый SSD/NVMe
- 150–250 GB свободного места (GGUF 111 GB + временная копия при склейке шардов)

**Софт:** Linux, Git, CMake, GCC, CUDA toolkit (совместимый с картой), llama.cpp, Node.js **22.19+ или 24+** (нужно DSH).

**Конфигурация автора:** GTX 1080 Ti 11 GB · Core i9-9900K · 64 GB RAM · Ubuntu.

## Пошагово

### 1. Ollama не подходит

- Официальный тег `qwen3.8-flash-next:125b-mlx` — это **MLX** (экосистема Apple Silicon), не для Linux + NVIDIA.
- MLX-поддержка появилась в Ollama 0.33.1, но импорт стороннего GGUF в 0.33.2 падал: `failed to validate GGUF...` — при том что тот же файл грузился через llama.cpp напрямую.

Схема вместо Ollama:

```
Qwen3.8-Flash-Next GGUF → llama.cpp → llama-server → DeepSeek Harness
```

### 2. Скачать GGUF

Четыре шарда `UD-Q4_K_XL` с [huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF/tree/main/UD-Q4_K_XL](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF/tree/main/UD-Q4_K_XL):

```
Qwen3.8-Flash-Next-UD-Q4_K_XL-00001-of-00004.gguf   10.9 MB
Qwen3.8-Flash-Next-UD-Q4_K_XL-00002-of-00004.gguf   49.9 GB
Qwen3.8-Flash-Next-UD-Q4_K_XL-00003-of-00004.gguf   49.4 GB
Qwen3.8-Flash-Next-UD-Q4_K_XL-00004-of-00004.gguf   12.1 GB
```

```bash
mkdir -p ~/GGUF/qwen-flash-next
cd ~/GGUF/qwen-flash-next
```

### 3. Собрать llama.cpp

Поддержка появилась в **PR #27742**, слита **27.08.2026**. Стабильный **llama.cpp 0.4.1** вышел **14.09.2026** — для новой установки к nightly уже не привязываться нужно, но версия должна содержать `qwen4exp`.

Для GTX 1080 Ti (compute capability **61**):

```bash
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build \
  -DGGML_CUDA=ON \
  -DCMAKE_CUDA_ARCHITECTURES=61
cmake --build build --config Release -j $(nproc)

./build/bin/llama-server --version   # проверка
```

Рекомендуют CUDA 12.x.

### 4. Склеить шарды (опционально)

Современный llama.cpp умеет работать с раздельными GGUF, но единый файл удобнее для части плагинов:

```bash
./build/bin/llama-gguf-split --merge \
  ~/GGUF/qwen-flash-next/Qwen3.8-Flash-Next-UD-Q4_K_XL-00001-of-00004.gguf \
  ~/GGUF/qwen-flash-next/Qwen3.8-Flash-Next-merged.gguf
```

Указывается первый shard + имя выходного файла, остальные части находятся автоматически. После успешного merge исходники можно удалить (~111 GB обратно).

### 5. Первый запуск llama-server

```bash
llama-server \
  -m ~/GGUF/qwen-flash-next/Qwen3.8-Flash-Next-merged.gguf \
  -c 16384 \
  -b 2048 \
  -ub 1024 \
  -np 1 \
  --cache-type-k q8_0 \
  --cache-type-v q8_0 \
  --host 127.0.0.1 \
  --port 55555
```

| Флаг | Смысл |
|---|---|
| `-c 16384` | начальный контекст 16K |
| `-b 2048` / `-ub 1024` | batch / ubatch |
| `-np 1` | один параллельный слот |
| `--cache-type-k/v q8_0` | компромисс качество/память на KV-кэше |

> ⚠️ **Главное правило: не ставить `-ngl 999` / `-ngl all`.** Современный llama.cpp умеет автоматический подбор слоёв (`-ngl auto`, дефолт) плюс отдельный `--n-cpu-moe N` для размещения MoE-экспертов первых N слоёв на CPU. Именно ручная комбинация `-ngl` + `--n-cpu-moe` у автора давала нехватку VRAM. Значения с другой видеокарты 1-в-1 не переносить.

### 6. Проверка без DSH

```bash
curl -s http://127.0.0.1:55555/v1/models | jq

curl -s http://127.0.0.1:55555/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"slot-a","messages":[{"role":"user","content":"2+2"}],"max_tokens":50}' | jq
```

Имя модели не всегда `slot-a` — смотреть по `/v1/models`.

### 7. Подключение к DeepSeek Harness

DSH — локальная агентная среда DeepSeek, распространяется как developer preview, плагинная архитектура (models, tools, sandbox, storage, workflows = плагины).

```bash
npm install -g @deepseek-ai/dsh     # или npx @deepseek-ai/dsh web
dsh web                             # UI: http://127.0.0.1:3080
dsh web --port 8080                 # смена порта
```

Плагин для запуска/остановки llama-server из интерфейса DSH:

```bash
dsh plugin --profile web add dsh-local-llm-controller
# если dsh не в PATH:
npx @deepseek-ai/dsh plugin --profile web add dsh-local-llm-controller
```

После установки — **перезапустить Web UI**. Плагин появится в `Settings → Plugins → Local LLM Controller`.

**Настройка:**

| Поле | Значение |
|---|---|
| llama.cpp directory | `/home/user/.local/bin` (каталог с исполняемым) |
| Port | например `5555` |
| Slot A / Slot B | **абсолютный** путь к каталогу модели, напр. `/home/user/GGUF/qwen-flash-next/` |
| Launch args | см. ниже |

```
-c 16384
-b 2048
-ub 1024
-np 1
--cache-type-k q8_0
--cache-type-v q8_0
```

`-m`, `--host`, `--port` плагин добавляет сам — вручную их не задавать. Абсолютный путь вместо `~/GGUF/...` избавляет от проблем с обработкой путей в GUI-плагине.

> 🪤 **Грабли Linux:** плагин ожидает исполняемый файл **`llama-server.exe`** (так прямо в настройках), тогда как на Linux файл называется `llama-server`. Чинится симлинком:
> ```bash
> ln -s ~/.local/bin/llama-server ~/.local/bin/llama-server.exe
> ```
> Это workaround для плагина, а не особенность llama.cpp.

## Производительность (конфигурация автора)

| Параметр | Результат |
|---|---|
| Decode | **≈ 11 tok/s** |
| Prefill | **≈ 19 tok/s** |
| VRAM | ≈ 9.5 GB |
| Контекст | 16K (64K тоже тянет) |
| Загрузка модели | 1–3 мин |

Зависит от CPU, пропускной способности RAM, VRAM, квантовки, числа CPU-offloaded экспертов, контекста и флагов. На RTX 4090 и конфигурациях 24 GB VRAM + `--n-cpu-moe` цифры значительно выше.

## Контекст: почему не 256K сразу

Нативные 262 144 токена не означают, что надо ставить `-c 262144`. Память и скорость всё равно зависят от KV/cache-структур и backend, а в llama.cpp на границе полного окна уже находили проблемы — на некоторых конфигурациях это **не OOM, а ошибки CUDA/kernel или деградация поведения**.

Порядок: `16K` → `32K` → `64K` → `128K` → полное окно. У автора 64K работали нормально, дальше он не шёл (чем больше контекст, тем дольше работа LLM).

## Reasoning — две разные вещи

Частая ошибка: **`--no-reasoning-preserve` НЕ отключает reasoning.** Он управляет *сохранением reasoning-трассы в полной истории*. Само размышление и сохранение его результата — отдельные вопросы.

- Управление в llama.cpp: `--reasoning`, `--reasoning-effort`, `--reasoning-budget`
- Старый механизм `chat_template_kwargs: {"enable_thinking": false}` в новых сборках **deprecated** — при написании своего клиента не зашивать единственный вариант, а ориентироваться на конкретную версию и её `/v1` API
- В DSH уровень размышления для Qwen3.8-Flash-Next выбирается прямо в меню выбора модели

## Что работает / что неидеально

**Работает:** запуск модели, OpenAI-compatible API, сохранение контекста между запросами, работа с DSH, агентные сценарии, tool calls, reasoning, запуск без Ollama, работа на 11 GB VRAM.

**Неидеально:**
- ~11 tok/s decode — ответ на сотни токенов занимает десятки секунд, при первом обращении (большой system prompt) — минуты
- CPU/RAM становятся частью вычислительной системы: скорость = GPU bandwidth + CPU + RAM bandwidth + VRAM + SSD (SSD особенно важен для lazy loading больших n-gram/PLE-таблиц)

**Куда расти:**
1. GPU с 24 GB VRAM — больше экспертов помещается
2. Тонкая настройка `--n-cpu-moe` (`40` у одной конфигурации, `30` у другой — зависит от VRAM/RAM)
3. Более компактная квантовка: `UD-Q3_K_XL`, `UD-IQ3_XXS`, `UD-IQ2_K_XL`, `UD-IQ1_M`, `UD-IQ1_S` (минимум ~72–75 GB) — с потерей качества; `UD-Q4_K_XL` автор рекомендует как баланс «ум/скорость»

## Нужен ли DSH

Если задача — просто поговорить с моделью, **DSH не обязателен**: хватает `llama.cpp → llama-server → OpenAI-compatible API`.

DSH (и OpenCode, и аналоги) интересны на следующем уровне — когда нужна агентная среда, инструменты, работа с файлами, shell, workflows и многошаговое выполнение. Сам DeepSeek позиционирует Harness как *extensible agent runtime*.

## Применимость к нашему железу

⚠️ **Домашний ПК (XE2690: GT 1030 2 GB, CPU-only, 64 GB RAM) — схема НЕ воспроизводится как есть:**
- 111 GB весов не помещаются в 64 GB RAM
- 2 GB VRAM роли ускорителя не играют (у автора 11 GB вытягивают заметную часть графа)
- на чистом CPU — порядки ниже 11 tok/s, вероятен своп на диск

**Реалистичный кандидат:** сборка **X99-TF + E5-2696 v4** с добавлением GPU класса 1080 Ti / 1060 6G / 1660 Super и 64–128 GB DDR4 — тогда рецепт отрабатывает почти дословно. Для старта можно взять меньшую квантовку (72–75 GB).

## Источники

- 🌐 [Habr: Как запустить 176B-класс Qwen3.8-Flash-Next в DeepSeek Harness на GTX 1080 Ti](https://habr.com/ru/articles/1085544/) — автор @SkalolazOther, основной источник
- 🌐 [Unsloth Qwen3.8-Flash-Next GGUF](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF/tree/main/UD-Q4_K_XL) — файлы квантизаций
- 🌐 [llama.cpp](https://github.com/ggml-org/llama.cpp) — поддержка `qwen4exp` (PR #27742)
- 📄 [[tech/qwen38-27b-local-gpu]] — почему 27B не подошла автору (следование инструкциям в агентных сценариях) и бенчмарки квантизации
- 📄 [[llm/local-gemma-4-12b-setup]] — как у нас запускается локальная модель через llama-server (Windows, CPU)
