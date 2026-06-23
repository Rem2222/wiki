---
description: Набор практических UI-рекомендаций от Jakub Krehel — микровзаимодействия, анимации, производительность, визуальные детали
tags:
  - ui-ux
  - design
  - animation
  - performance
  - tool
related:
  - tools/find-skills
---

# make-interfaces-feel-better

> **Автор:** Jakub Krehel  
> **Установок:** 30 000+  
> **Установка:** `npx skills add jakubkrehel/make-interfaces-feel-better`  
> **Экосистема:** `@skills-cli/core` (npm), отдельная от Hermes skills

## Что это

Пакет с практическими рекомендациями по улучшению пользовательских интерфейсов. Включает советы по:

- **Микровзаимодействиям** — hover-эффекты, переходы, обратная связь на действия
- **Анимациям** — timing, easing, staggered animations, layout animations
- **Производительности** — борьба с layout shifts, оптимизация repaints, will-change
- **Визуальным деталям** — отступы, тени, цвета, скругления, типографика
- **Accessibility** — focus-стили, reduced-motion, contrast ratios
- **Восприятию** — perceived performance, skeleton screens, optimistic UI

## Установка

Требуется глобальный `skills` CLI:

```bash
npm install -g @skills-cli/core
npx skills add jakubkrehel/make-interfaces-feel-better
```

После установки — просмотр через `skills` CLI в терминале.

## Зачем

Jakub Krehel известен докладами про «UI craft» — как мелкие детали (10-20px отступа, 200ms анимации, правильный easing) превращают интерфейс из «просто работает» в «приятно пользоваться». Пакет структурирует эти знания в пошаговые рекомендации с примерами кода.

## Связи

- [[tools/find-skills]] — мета-скилл для поиска agent-скиллов
