---
description: Готовый шаблон админ-панели для SaaS-проектов. Тёмная и светлая темы, 3 цветовых варианта:
tags: [tech]
related: [[tech/jawl-dashboard]] [[tech/landing]]
---

# nexus-dashboard

**Ссылки:** [GitHub](https://github.com/Pinky057/nexus-dashboard) | [Демо](https://nexus-dashboard-phi-five.vercel.app/)

**Стек:** Next.js 14 + Tailwind CSS + Framer Motion + Recharts + TypeScript
**Лицензия:** MIT, 2 ★ (свежий, апрель 2026)

---

## Что это

Готовый шаблон админ-панели для SaaS-проектов. Тёмная и светлая темы, 3 цветовых варианта:

- 🌑 **Elite Dark** — индиго/фиолетовый акцент (основной)
- 🌃 **Classic Dark** — бирюзовый/циановый акцент
- ☀️ **Studio Light** — белый фон, фиолетовый акцент

## Страницы

- **Dashboard** — AI Command Center: KPI карточки (MRR, подписки, API токены, Uptime) + график Revenue Stream + AI Insight на каждой метрике
- **Analytics** — Avg Session Duration, Bounce Rate, Customer LTV, Predictive AI Engine, Donut Chart
- **Kanban** — канбан-доска
- **Products / Users / Transactions** — страницы управления
- **UI Kit** — кнопки, формы, Badges, таблицы, графики
- **Auth** — Login, Register, Forgot Password
- **404** — кастомная страница

## Особенности

- AI Assistant — плавающий чат-бот в углу с Human-in-the-Loop (читает данные, но не DELETE без подтверждения)
- Ctrl+K — глобальный поиск (как в Linear/Notion)
- 5 типов графиков (Recharts): Area, Bar, Line, Pie/Donut, Radar
- Анимации Framer Motion
- Тёмная тема по умолчанию (Zinc + Indigo)

---

## Анализ: можно ли применить к проектам

**Проблема:** Nexus Dashboard — Next.js 14 (React/TypeScript). У Романа оба дашборда на Flask (Python) с vanilla HTML/CSS/JS. Это **разные стеки**, просто так не вставить.

### 🔵 Jinx (JAWL Dashboard)

**Текущее:** Flask в `/home/rem/JAWL/dashboard.py`. Вся HTML-разметка внутри Python-строки `TEMPLATE`. API-эндпоинты: `/api/status`, `/api/logs`, `/api/drives`, `/api/tasks`, `/api/thoughts`, `/api/crypto`, `/api/knowledge`, `/api/providers` и др.

**Варианты апгрейда:**

1. **Лёгкий** — выдрать CSS/стили/компоненты из Nexus Dashboard и адаптировать в TEMPLATE строку. Тот же Flask, но выглядит как Nexus. Самый быстрый путь.
2. **Средний** — поднять Nexus Dashboard отдельно (Next.js, порт 3000), научить его ходить в Flask API за данными. Два приложения, больше сложности.
3. **Полный переезд** — переписать дашборд целиком на Next.js/React. Всё единообразно, но надо писать на JS.

**Контекст:** Уже есть задача REM-168 «Переделать дизайн дашборда — сделать современным». В процессе перекраска в Catppuccin Mocha (REM-181—189).

### 🧠 MemPalace Dashboard

**Текущее:** Flask SPA в `/root/mempalace-dashboard/app.py` + vanilla HTML/CSS/JS. Уже готовая SPA с навигацией по Wing→Room→Drawer, графом знаний, поиском.

**Варианты:** Аналогично — только CSS/дизайн-референс, либо переезд на React.

---

## Вывод

Nexus Dashboard — отличный **дизайн-референс**. Его стиль (тёмная тема, стеклянные карточки, неоновые акценты, AI Insights) можно адаптировать в текущие Flask-дашборды без смены стека. Полноценный переезд на Next.js имеет смысл только если есть желание/необходимость писать фронт на React.

Ссылка на задачу в Мультике: **MUL-303** — «Апгрейд UI для Джинкс»