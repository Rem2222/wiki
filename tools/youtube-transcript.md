---
description: "Получение расшифровки/субтитров YouTube-видео с VPS, чей IP заблокирован YouTube. Рабочий endpoint youtube-transcript.ai для LLM + список мёртвых путей (transcript-api, yt-dlp, Tor, Invidious) — проверено 26.09.2026."
tags: [tools, youtube, transcript, subtitles, vps, agent-reach]
updated: 2026-09-26
source: "https://youtube-transcript.ai/llms.txt"
related:
  - "[[tools/yt-dlp]]"
  - "[[tools/agent-reach]]"
  - "[[tech/youtube-relay-setup]]"
---

# YouTube-транскрипт с заблокированного VPS

Задача: получить текст расшифровки ролика. Проблема: **IP VPS (80.241.218.110, датацентр) заблокирован YouTube** — но штатные инструменты об этом не сообщают честно, они просто падают с разными ошибками.

## ✅ Работающий путь (проверено 26.09.2026)

Открытый endpoint `youtube-transcript.ai`, **без ключей и без rate limit** — они сами просят LLM-агентов им пользоваться:

```bash
curl -sL "https://youtube-transcript.ai/transcript/{VIDEO_ID}.txt"
```

| Поле | Значение |
|---|---|
| `{VIDEO_ID}` | 11 символов из URL после `v=` или в `youtu.be/` |
| Формат | `text/markdown` |
| В ответе | таймкоды `[m:ss]`, заголовок, язык, длительность, число слов |
| Язык по умолчанию | en manual → en auto → основной язык ролика |
| Выбор языка | `?lang=ja` (и т.п.) |
| Интерактивная версия | `https://youtube-transcript.ai/transcript?v={ID}` |

Документация: `https://youtube-transcript.ai/llms.txt`

Реальный ответ: 42 КБ markdown на ролик 15:13 / 7708 слов.

### Артефакт ASR — фразы повторены ТРОЕкратно

Автогенерённые субтитры YouTube отдают каждую фразу 3 раза подряд (`hello everyone and welcome to this hello everyone and welcome to this hello everyone and welcome to this ...`). Это не баг endpoint'а, это сам YouTube ASR.

Очистка на Python — скользящий поиск тройного (и двойного) повтора:

```python
def collapse_run(tokens, copies, max_k=45):
    out, i, n = [], 0, len(tokens)
    while i < n:
        hit = False
        for k in range(1, min(max_k, (n - i) // copies) + 1):
            a = tokens[i:i + k]
            if all(tokens[i + j*k : i + (j+1)*k] == a for j in range(1, copies)):
                out.extend(a); i += copies * k; hit = True; break
        if not hit:
            out.append(tokens[i]); i += 1
    return out

def dedupe_all(toks):
    for c in (4, 3, 2):          # от большего к меньшему
        toks = collapse_run(toks, c)
    return toks
```

Порядок важен: сначала 4, потом 3, потом 2 — иначе двойной повтор «съест» середину тройного.

**Потом две отдельные ловушки:**

1. **Таймкод — первый токен строки.** `[0:36] I'm one of ...` — если сравнивать перекрытие не отделив таймкод, сравнение всегда провалится (первый элемент строки — `[0:36]`, а не слово). Сначала `re.fullmatch(r'\[\d+:\d{2}\]', toks[0])`, выкинуть, потом дедуп, потом вернуть.
2. **Перекрытие между таймкодами.** ASR повторяет хвост предыдущего сегмента началом следующего. Лечится сравнением `toks[:L] == prev_tail[-L:]` для `L` до ~14.

Итог на том ролике: **42 085 → 14 287 символов**.

Полный скрипт: `/tmp/dedupe.py` (в сессии; пересоздаётся из этого раздела).

## ❌ Что НЕ работает (проверено, не тратьте время)

| Путь | Результат |
|---|---|
| `youtube-transcript-api` (v1.2.4) | `RequestBlocked` — «IP belonging to a cloud provider» |
| `yt-dlp --list-subs` / `--write-sub` | `Sign in to confirm you're not a bot` |
| `yt-dlp --proxy socks5://127.0.0.1:9050` (Tor) | таймаут 20с × 3 — YouTube блокирует exit-ноды Tor |
| `youtube-transcript-api` + `GenericProxyConfig(socks5...)` | `InvalidSchema` — не установлен `pysocks` (и не поможет: см. Tor выше) |
| `video.google.com/timedtext?type=track` | HTTP 200, пустое тело (0 байт) |
| Invidious: `inv.nadeko.net`, `yewtu.be`, `invidious.nerdvpn.de`, `iv.melmac.space`, `iv.ggtyler.dev`, `vid.puffyan.us`, `invidious.lunivers.trade`, `yt.artemislena.eu`, `invidious.f5.si` | 502/503/500/блок «Verifying your browser» — **ни один инстанс не жив** |
| `pipedapi.kavin.rocks` | 502 |
| `youtubetotranscript.com` | 403 |
| `youtubetranscript.com/?server_vid2={ID}` (их серверный прокси) | 200, но в XML: *«YouTube is currently blocking us from fetching subtitles»* — у них самого сломано |
| `kome.ai/api/transcript` | 429 (Vercel Security Checkpoint) |
| `tactiq-apps-prod.tactiq.io/transcript` | 401 «Missing App Check token» |
| `youtranscripts.com`, `tubetranscript.com`, `downloadyoutubesubtitles.com` | 429 / 404 / 404 |
| `www.youtube.com/watch` (curl) | 200 на страницу, но `ytInitialPlayerResponse.playabilityStatus = LOGIN_REQUIRED` → `reason: "Sign in to confirm you're not a bot"`, блока `captions` в ответе нет |

**Ключевой диагноз:** страница YouTube отдаёт 200, а вот **player API и transcript endpoint — блокируются**. Поэтому «curl вернул 200» ничего не доказывает — надо смотреть `playabilityStatus`.

```bash
# быстрая проверка, почему падает
curl -s -A "Mozilla/5.0" "https://www.youtube.com/watch?v=ID" | \
  grep -o 'playabilityStatus[^}]*' | head -c 300
```

## Что работает для метаданных

`oembed` отдаётся без проблем (заголовок, автор, превью), и `yt-dlp --flat-playlist` **тоже работает** — им можно вытянуть список роликов плейлиста:

```bash
yt-dlp --flat-playlist --print "%(id)s|%(title)s" \
  "https://www.youtube.com/playlist?list=PL..." 
```

Получается 30 ID с названиями за ~2 с. Дальше каждый ID идёт в endpoint транскрипта.

## Практический пайплайн

```bash
ID="QWNxQIq0hMo"
curl -sL "https://youtube-transcript.ai/transcript/${ID}.txt" -o /tmp/raw.txt
python3 /tmp/dedupe.py        # очистка ASR-повторов
```

Если роликов много — `--flat-playlist` → цикл по ID → дедуп → склейка в один файл.

## См. также

- 📄 [[tools/yt-dlp]] — скачивание видео/аудио (субтитры на VPS не получить, см. таблицу выше)
- 📄 [[tools/agent-reach]] — `yt-dlp --write-sub` и `agent-reach transcribe` (Whisper-фоллбэк через Groq key)
- 📄 [[tech/youtube-relay-setup]] — если нужен сам YouTube, а не только текст: релей + zapret
- 🌐 https://youtube-transcript.ai/llms.txt — документация endpoint'а
