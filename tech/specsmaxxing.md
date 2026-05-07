# Specsmaxxing / Acai.sh — Spec-Driven Development с ACID tracking

_Записано: 2026-05-03_
_Теги:_ #SSD #1С #vibecoding #spec-driven

## Суть

Статья от автора [acai.sh](https://acai.sh) — заметил что AI-агенты "сходят с рельс" когда заполняется контекст, или при смене сессии/машины. Пришёл к выводу: нужно письменно фиксировать требования в виде нумерованного списка acceptance criteria.

**Главный тезис:** Specs должны описывать как система ДОЛЖНА работать, а не как она работает сейчас.

## Проблема: AI Psychosis / Peak Slop

- Агент сделает работу, но потом выясняется что забыли edge case
- Потом ещё что-то: "ты использовал offset pagination, лучше cursor"
- Потом: "а там N+1 запрос!"
- Автор называет это **AI psychosis** — использование AI для построения AI-ов для построения продуктов

Решение: **писать спеки ДО генерации кода**.

## ACIDs — Acceptance Criteria IDs

Каждому требованию присваивается ID по которому потом можно ссылаться в коде и тестах:

```yaml
feature:
  name: imaginary-api-endpoint
  product: api
  components:
    AUTH:
      requirements:
        1: Accepts Authorization header with Bearer <token>
        1-1: Token must be non-expired, non-revoked
        2: Respects scopes configured for the owner
```

Агент может сам нумеровать требования и ссылаться на них:
```python
# AUTH-1
authHeader = req.headers["authorization"]
# AUTH-2
isAuthorized = verifyBearerToken(authHeader)
```

## Acai.sh — инструментарий

**Три компонента:**

1. **feature.yaml** — формат спеки (YAML с ACID)
2. **CLI** — `npx @acai.sh/cli` или GitHub releases (Linux/Mac)
3. **Dashboard** — webapp + REST API (Elixir/Phoenix/Postgres)

```bash
# Установка CLI
npm install -g @acai.sh/cli
# или
npx @acai.sh/cli skill  # научить агента работать с Acai

# Пуш спеки в dashboard
acai push --all
```

**Workflow:**
1. Написать spec в feature.yaml
2. Агент читает через `acai skill`, реализует с ACID references
3. Dashboard показывает coverage: какие требования покрыты кодом и тестами
4. Mark: <Badge color="blue">Completed</Badge> / <Badge color="green">Accepted</Badge> / <Badge color="red">Rejected</Badge>

## Сравнение с другими инструментами

| Инструмент | Отличие |
|-----------|---------|
| **SpecKit** | CLI который добавляет промпты и скиллы агентам — "vibe coding с доп.шагами" |
| **OpenSpec** | Specs описывают текущее поведение системы ( автор не согласен — должны описывать желаемое) |
| **Kiro** | EARS syntax — автор считает слишком громоздким |
| **Traycer.ai** | Plain .md файлы, нет ACID tracking |
| **Acai.sh** | Фокус на acceptance coverage и alignment между spec и code |

## Future: Testmaxxing → Reactive Software Factories

1. **Testmaxxing** — когда генерация кода быстрее чтения, bottleneck в QA/валидации. Инвестиции в тесты дают огромный ROI.

2. **Reactive software factories** — когда spec хорошо описан и есть confidence в pipeline, LLM может сам реагировать на red tests / alerts без вмешательства человека.

## Применение для 1С

Потенциально полезно для:
- Крупные доработки 1С с понятными acceptance criteria
- Когда в команде несколько разработчиков + AI агенты
- Tracking какие требования покрыты кодом и тестами

См. также: [[sdd]], [[tech/sdd-instruments]], [[openspec]]

Формат `feature.yaml` достаточно простой и не требует сложного инструментария — можно адаптировать под свой процесс.

## Ссылки

- Статья: https://acai.sh/blog/specsmaxxing
- Acai.sh: https://acai.sh
- CLI: `npx @acai.sh/cli` или GitHub (acai-sh/cli)
- Dashboard: https://app.acai.sh