---
description: yt-dlp — командная утилита для скачивания видео/аудио с YouTube и 1000+ сайтов.
tags: [tools, cli, video]
related:
  - tech/agent-reach
created: 2026-08-03
---

# yt-dlp

**GitHub:** github.com/yt-dlp/yt-dlp

Командная утилита для скачивания видео и аудио с YouTube, Vimeo, Twitch и 1000+ других сайтов. Форк youtube-dl.

Установлена в venv Agent Reach: `/opt/agent-reach-venv/bin/yt-dlp`, симлинк `/usr/local/bin/yt-dlp` (2026-08-02).

## Использование

```bash
yt-dlp "https://www.youtube.com/watch?v=..."          # видео
yt-dlp -x --audio-format mp3 "URL"                    # только аудио
yt-dlp --playlist-items 1-5 "URL"                     # часть плейлиста
```

## Команды

- `-f <format>` — выбор формата (bestvideo+bestaudio)
- `-x` — извлечь аудио
- `--embed-thumbnail`, `--embed-metadata` — метаданные в файл
