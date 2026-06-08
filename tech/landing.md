---
description: Лендинг rem2222.top — стартовая страница с карточками сервисов на VPS.
tags: [landing, rem2222, frontend, html, css, vps, services]
related: [[tech/revealjs]] [[tech/jawl-dashboard]] [[tech/authelia]]
---

# Лендинг rem2222.top

**URL:** https://rem2222.top  
**Статус:** Опубликован (22 мая 2026)

## Что это

Стартовая страница домена rem2222.top с карточками self-hosted сервисов на VPS 81.17.100.103. Сгруппированы по секциям. Доступ через Authelia SSO.

## Структура

```
Боты
├── Hermes    — AI-агент (:9119)
├── OpenCode  — AI-кодинг (:4096)
└── JAWL      — Just Another Workflow Library

Мониторинг
├── Cockpit   — администрирование сервера
├── Beszel    — метрики
└── Duc       — визуализация дисков

Синк
└── CouchDB   — БД для Obsidian LiveSync

SSO
└── Authelia  — централизованная аутентификация
```

## Формат карточек

Каждая карточка: SVG-иконка + название + описание + badge + ссылка.

**Пример:**
```html
<a href="/hermes/" class="card">
  <div class="card-icon">
    <svg viewBox="0 0 48 48" width="48" height="48">
      <circle cx="24" cy="24" r="20" fill="#6c5ce7" opacity="0.2"/>
      <path d="M16 28 L24 14 L32 28 Z" fill="#6c5ce7"/>
    </svg>
  </div>
  <div class="card-body">
    <h3>Hermes</h3>
    <p>AI-агент с CLI и TUI</p>
    <span class="badge badge-ai">AI</span>
  </div>
</a>
```

### CSS

```css
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1rem;
}
.card {
  display: flex; align-items: center; gap: 1rem;
  padding: 1.25rem; background: #1a1a2e;
  border: 1px solid #2a2a4a; border-radius: 12px;
  text-decoration: none; color: #e0e0e0;
}
.card:hover { border-color: #6c5ce7; }
.badge { display: inline-block; padding: 0.15rem 0.5rem;
  border-radius: 4px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; }
.badge-ai { background: #6c5ce7; color: #fff; }
.badge-monitor { background: #00b894; color: #fff; }
.badge-sync { background: #0984e3; color: #fff; }
.badge-sso { background: #fdcb6e; color: #2d3436; }
```

### SVG иконки

| Сервис | Цвет |
|--------|------|
| Hermes | #6c5ce7 |
| OpenCode | #00b894 |
| JAWL | #fdcb6e |
| Cockpit | #0984e3 |
| Beszel | #00cec9 |
| Duc | #e17055 |
| CouchDB | #e84393 |
| Authelia | #f39c12 |

## Доступ

- **URL:** https://rem2222.top
- **Защита:** Authelia SSO
- **Тема:** тёмная
