---
created: 2026-11-17
updated: 2026-11-17
source: "https://llama.app/"
description: "Локальный трей-сервер инференса от llama.cpp и Hugging Face для Windows 11 с OpenAI и Anthropic API на порту 9931, автоподбором настроек под RAM/VRAM и общим кэшем моделей. Записано, не устанавливалось."
tags: [llama,llama-cpp,windows,local-llm,tools]
related:
  - hardware/xe2690-workstation
  - ops/services/ollama
  - tech/codex-cli-inference-optimization
---

# Llama for Windows

## Что это

**Llama for Windows** (`ggml-org/Llama-Windows`, MIT) — нативное WinUI 3-приложение для системного трея Windows 11: обёртка над llama.cpp с локальным сервером инференса. Модель запускается в один клик, без терминала и ручной настройки окружения; работает офлайн, без облачных API-ключей. Есть веб-интерфейс чата, оверлей `Alt+Space`, OpenAI-совместимый `/v1/...` и Anthropic-совместимый `/v1/messages` на `localhost:9931`, стриминг, tool calling и vision.

Проверено 2026-11-17 живыми запросами: страница загрузки и GitHub-ассет отвечают HTTP 200. Репозиторий: 457 звёзд, 61 fork, 20 открытых issues, лицензия MIT, `pushed_at` 2026-11-17. Бандл v0.14.1 скачан 26 036 раз, отдельный x64 — 5 070, ARM64 — 431.

## Ссылки и установка

- 🌐 Сайт: https://llama.app/
- 🌐 Загрузка для Windows: https://llama.app/download/windows
- 🌐 Прямой бандл v0.14.1 (30.10.2026, 133,2 МБ): https://github.com/ggml-org/Llama-Windows/releases/download/v0.14.1/LlamaApp-v0.14.1.msixbundle
- 🌐 Репозиторий: https://github.com/ggml-org/Llama-Windows
- 🌐 Официальный пост: https://huggingface.co/blog/huggingface/llama-windows — в правке от 10.11.2026 указано, что приложение уже в Microsoft Store (ищи `Llama`).
- PowerShell: `irm https://llama.app/install.ps1 | iex`. Это выполнение удалённого скрипта — перед запуском прочитать содержимое. Не запускалось.
- Требования: Windows 11, x64 или ARM64, права администратора не нужны.

## Утверждение из поста → реальность

| Утверждение в посте | Проверка |
|---|---|
| «Утилита весом 1 МБ» | 1 МБ — размер скачиваемого `.dmg` **Mac**-версии; установленное приложение Mac — 4 МБ. Windows `.msixbundle` = **133,2 МБ** (x64 67,5 МБ, ARM64 65,7 МБ). ⚠️ В чате 17.11 сначала была названа цифра ~86 МБ из релиз-ноутов про self-contained сборку — для скачиваемого файла она неверна. |
| «Релиз в Microsoft Store в ближайшее время» | Уже доступно с **10.11.2026**, согласно правке в официальном блоге. |
| «Анонс на кейноуте Microsoft .NET Conf» | Подтверждается перепечатками поста Jeff Boudier; официальный пост датирован 13.10.2026, правка о Store — 10.11.2026. |
| «Бухгалтер-аудитор токенов» | Точнее — аудитор **железа и конфигурации**: подбирает квантование, лимит контекста, batch size и speculative decoding под RAM/VRAM. Счётчик `usage` и `timings` llama.cpp (tok/s, `cache_n`) — отдельная функция. |
| «Порт 9931, API OpenAI и Anthropic» | Подтверждено документацией: `/v1/...` и `/v1/messages`, стриминг, инструменты, vision. |
| «Веса в едином HF-кэше, выгрузка через 5 минут» | Подтверждено сайтом/документацией: `%USERPROFILE%\.cache\huggingface\hub`, простой >5 мин выгружает модель. |

## Чем интересно Роману

Домашняя станция [[hardware/xe2690-workstation]] — Windows, 64 ГБ RAM, GT 1030 на 2 ГБ; на VPS крутится [[ops/services/ollama]] (`:11434`, bge-m3 + qwen2.5:7b). Llama for Windows — не замена серверу, а недостающий сегодня локальный endpoint именно на Windows-машине.

- Сейчас: чтобы подключить IDE или кодинг-агента к локальной модели, надо поднимать llama-server/Ollama и править конфиги → станет: трей сам поднимает `:9931`, endpoint совместим с OpenAI/Anthropic, ключ не нужен. Смежный разбор — [[tech/codex-cli-inference-optimization]].
- Сейчас: квант и контекст под 2 ГБ VRAM подбираются руками → станет: приложение сканирует RAM/VRAM и выбирает режим само, а через 5 минут простоя выгружает модель.
- Сейчас: веса разных инструментов оседают в разных папках → станет: общий кэш Hugging Face, который видят и другие тулы.

Ограничение: GT 1030 (2 ГБ) не потянет 7B/12B целиком — реалистичны только маленькие модели с CPU/частичным GPU. Свободного места на станции после расчистки NVMe хватит на одну небольшую модель, но не на большую библиотеку.

**Чего НЕ делает:** не работает сервисом на VPS (только Windows 11), не ускоряет слабый GPU, не даёт облачный аккаунт или ключ, не обходит антибот-защиту сайтов, не заменяет Ollama на сервере. Капчи не решались, сторонние прокси не использовались.

## Статус

**Записано, НЕ устанавливалось.** Ничего не скачивал и не ставил; проверял только страницы, GitHub API и живые HTTP-ответы 17.11.2026. Установка — только по отдельной команде Романа.

## Источники

- 🌐 https://huggingface.co/blog/huggingface/llama-windows
- 🌐 https://llama.app/ и https://llama.app/docs/api
- 🌐 https://api.github.com/repos/ggml-org/Llama-Windows/releases/latest
- 📄 [[hardware/xe2690-workstation]], [[ops/services/ollama]], [[tech/codex-cli-inference-optimization]]
