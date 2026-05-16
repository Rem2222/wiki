# OpenCode v1.14.48 — VPS Setup

## Версия
**v1.14.48** (anomalyco/opencode, GitHub) — НЕ opencode.ai (там старая v0.0.55)

## Установка на VPS 81.17.100.103
```bash
# Скачать с GitHub (актуальная версия)
wget https://github.com/anomalyco/opencode/releases/latest/download/opencode-linux-x64.tar.gz
tar -xzf opencode-linux-x64.tar.gz
sudo cp opencode /usr/bin/opencode

# Старая версия (v0.0.55 из opencode.ai/releases) НЕ поддерживает `web` команду
```

## Веб-интерфейс
```bash
OPENCODE_SERVER_PASSWORD=smoon2026 \
OPENAI_API_KEY=$(grep 'opencode-go' ~/.openclaw/openclaw.json | grep api_key | sed 's/.*"api_key": "\([^"]*\)".*/\1/') \
/usr/bin/opencode web --port 4096 --hostname 0.0.0.0 &
```

- **URL**: http://81.17.100.103:4096
- **Логин**: opencode
- **Пароль**: smoon2026

## API
- **Endpoint**: https://opencode.ai/zen/go/v1/chat/completions (OpenAI compatible)
- **API ключ**: `~/.openclaw/openclaw.json` → `models.providers.opencode-go.api_key`
- **Config файл**: `~/.config/opencode/config.json` — **НЕ используется** (apiKey/openAIKey отвергаются приложением)

## Порт
- 4096 открыт в iptables: `sudo iptables -I INPUT -p tcp --dport 4096 -j ACCEPT`

## Модели (OpenCodeGo provider)
- GLM 5.1 (MoE, 200K context)
- Kimi K2.5 (MoE, 256K context)