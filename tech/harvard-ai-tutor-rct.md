---
description: "Гарвардский RCT (Scientific Reports): ИИ-тьютор превзошёл активное обучение в классе. Crossover-дизайн на 194 студентах Physical Sciences 2. Разобраны 7 педагогических принципов дизайна тьютора и защита от галлюцинаций."
tags: [ииобучение, research, education, ai-tutor, harvard, llm, rct]
created: 2026-09-28
updated: 2026-09-28
source: https://www.nature.com/articles/s41598-025-97652-6
related:
  - "[[tech/free-llm-api-resources]]"
---

# Гарвард: ИИ-тьютор против профессоров (RCT в Nature)

Учебный материал к проекту-«обучалке».

**Источник:** [AI tutoring outperforms in-class active learning: an RCT introducing
a novel research-based design in an authentic educational setting](https://www.nature.com/articles/s41598-025-97652-6)
— *Scientific Reports* (Nature).

| | |
|---|---|
| Дизайн | рандомизированное контролируемое испытание (RCT), **crossover** |
| Курс | Physical Sciences 2 (PS2), Fall 2023 — крупнейший курс физики Гарварда |
| Выборка | зачислено 233, в анализ вошло **194** (по согласию, участию в обоих условиях и завершённым пре-тестам) |
| Условия | неделя 1 — одни группы с ИИ, другие в классе; неделя 2 — **условия меняются местами** |
| Темы | поверхностное напряжение (нед. 1) и течение жидкостей (нед. 2) |
| Популярность | 213k просмотров, 202 цитирования |

## Метод: почему результат надёжен

Ключ — **crossover**, а не две независимые группы. Каждый студент прошёл **оба**
условия в разные недели, поэтому разница в личной подготовке студентов
вычитается из сравнения по построению.

В статье перечислено, что контролировалось отдельно:

- предшествующий опыт работы с ChatGPT;
- базовые знания по FCI (Force Concept Inventory) — пре-тестовые баллы сопоставимы с другими университетами;
- особенности crossover: тема урока и версия теста (A/B);
- время на задачу (time on task).

## Результаты

### Прирост знаний

Из статьи дословно:

> Students in the AI group exhibited a higher median (M) post-score (**M = 4.5,
> N = 142**) compared to those in the in-class active learning group
> (**M = 3.5, N = 174**).

> The median learning gains for students, relative to the **pre-test baseline
> (M = 2.75, N = 316)**, in the AI-tutored group were **over double** those for
> students in the in-class active learning group.

Разница значима: Mann–Whitney, **z = −5.6, p < 10⁻⁸**.

> ⚠️ **Числа в тексте и на рисунке — разные статистики.** Головные значения
> (4.5 / 3.5 / 2.75) — это **медианы**. А `Fig. 1`, которую цитируют чаще всего,
> показывает **средние**: `Figure 1 shows mean aggregate results (weeks 1 and 2
> combined)`. Поэтому столбец «AI lesson» на рисунке читается примерно как 4.2–4.3,
> а не 4.5 — и это не ошибка чтения графика, а разный сводник. Точные средние
> пост-тестов в тексте статьи **не приведены** вообще (`Mean = X.X` встречается
> только для вовлечённости и мотивации), поэтому по рисунку их можно лишь
> оценить по шкале.

Заметка по размерам групп: `N = 142` (ИИ) + `N = 174` (класс) = `316` — ровно
`N` базовой линии. Студентов в исследовании 194, и каждый проходит **оба**
условия, поэтому эти N — счётчики наблюдений по урокам, а не «студентов в
группе». В crossover это нормально, но в цитировании легко перепутать.

### Робастность (это важно для вывода)

ИИ-эффект не держится на слабых студентах: подгруппы с пре-инструктажным FCI
**ниже 40%** и **выше 40%** показали значимо лучший послетест с ИИ
(**p < 0.001**), и то же — для порога **65%** по шкале научных установок CLASS.

Линейная регрессия с контролем (пре-тест, midterm, опыт ChatGPT, тема урока,
версия теста, время на задачу) даёт **p < 10⁻⁸** и **effect size 0.63** — но в
статье прямо оговорено, что 0.63 это **занижение из-за ceiling-эффекта**, и
квантильная регрессия даёт оценку выше.

Ещё нюанс методики: рандомизация шла **не по отдельным студентам**, а по группам
пиран-инструкции (2–3 человека). Отдельная модель с кластеризацией на уровне
группы дала те же результаты (p < 0.001) — то есть на вывод это не влияет.

### Время

- в классе: 75-минутное занятие минус 15 минут на пре- и послетест → принято за **60 минут** обучения;
- **70%** студентов в группе с ИИ уложились **менее чем за 60 минут**;
- медианное время в группе с ИИ — **49 минут**.

### Восприятие (5-балльная шкала Лайкерта)

| | ИИ-тьютор | Активное в классе | Тест |
|---|---|---|---|
| Вовлечённость | **4.1** (SD 0.98) | 3.6 (SD 0.92) | t(311) = −4.5, p < 0.0001 |
| Мотивация | **3.4** (SD 1.0) | 3.1 (SD 0.86) | t(311) = −3.4, p < 0.001 |

Удовольствие (enjoyment) и установка на рост (growth mindset) — **без статистически
значимой разницы**.

Дополнительно: **83%** студентов сказали, что объяснения тьютора не хуже или лучше,
чем у живых преподавателей.

## Дизайн тьютора: 7 принципов

Вот это самое ценное для «обучалки». Статья перечисляет ключевые педагогические
практики **дословно**:

> Key practices include (i) facilitating active learning, (ii) managing cognitive
> load, (iii) promoting a growth mindset, (iv) scaffolding content, (v) ensuring
> accuracy of information and feedback, (vi) delivering such feedback and
> information in a targeted and timely fashion, and (vii) allowing for self-pacing.

| # | Принцип в оригинале | Суть |
|---|---|---|
| i | facilitating active learning | активное обучение, а не пассивное потребление |
| ii | managing cognitive load | управление когнитивной нагрузкой |
| iii | promoting a growth mindset | установка на рост |
| iv | scaffolding content | скаффолдинг — опоры под новое |
| v | ensuring accuracy of information and feedback | точность информации и обратной связи |
| vi | targeted and timely feedback | адресная и своевременная обратная связь |
| vii | allowing for self-pacing | саморегуляция темпа |

Отдельно отмечено, что (i)–(v) соблюдаются легко, а **(vi)–(vii) в классе
невозможны физически** — преподаватель не может давать персональную обратную
связь каждому своевременно, и не может пускать всех в своём темпе. Именно это
ИИ закрывает.

И что принципиально — **те же семь принципов** лежат и в очном обучении.
Тьютор не «лучше методом», он применяет тот же метод без ограничений масштаба:

> The novel design of the custom AI tutor is informed by the same pedagogical
> best practices as employed in the in-class lessons.

## Ведение по шагам вместо решения за студента

> the AI platform was designed to **guide students sequentially through each part
> of each problem** in the lesson, mirroring the approach taken by the instructor
> during the in-class active learning.

То есть бот не выдаёт готовый ответ — он прогоняет студента по частям задачи
так же, как это сделал бы преподаватель.

## Защита от галлюцинаций

Прямая цитата — приём, который стоит перенести:

> The occurrence of inaccurate "hallucinations" by the current generation of large
> language models (LLMs) poses a significant challenge for their use in education.
> Thus, we avoided relying solely on GPT-4 to generate solutions for these
> activities. Given that LLMs proceed by next-token prediction, accuracy in
> complex math or science problems is enhanced when the system generates, or is
> **provided with, detailed step-by-step solutions**. Therefore, we **enriched our
> prompts with comprehensive, step-by-step answers**, guiding the AI tutor to
> deliver accurate and high-quality explanations to students.

**Приём:** не просить модель решать «на лету», а заранее вшить в промпт полные
пошаговые решения. Модель генерирует текст, и ей физически проще повторить
заданный правильный ход, чем выдумать свой.

## Общая рамка: «голый чат» vs обучалка

Статья прямо описывает проблему обычных чат-ботов:

> AI chatbots are generally designed to be **helpful, not to promote learning**.
> They are not trained to follow pedagogical best practices (e.g., facilitating
> active learning, managing cognitive load and promoting a growth mindset).

И ещё один известный дефект, названный в статье:

> Another well-known flaw of AI tutors is their **uncanny confidence when giving
> an incorrect answer** or when marking a correct reply as incorrect.

Тезис «угодничество заблокировано промптами» **в статье не встречается** — я
искал (`sycophan`, `people-pleas`, `agreeable`) и не нашёл. Есть постановка
проблемы «designed to be helpful, not to promote learning» и описание того, как
этому противостояли на уровне дизайна (7 принципов, ведение по шагам, вшитые
решения). Разграничение важно: это **описание проблемы**, а не заявленный
проптовый запрет.

## Аналогия с Grok Educational — авторская, не из статьи

⚠️ Отдельно: упоминания **Musk / Grok Educational / Сальвадор / PISA / Швеция в
этой статье нет** — я искал (`PISA`, `Sweden`) и совпадений ноль. Это
самостоятельная параллель, и она полезна, но к данному исследованию
относится как внешний контекст, а не как результат.

Суть параллели: в **обоих** успешных кейсах (Гарвард, Grok в Сальвадоре)
использовали **специально спроектированных ботов обучения**, а не «голый чат».
Везде же, где исследователи оценивали влияние на школьников и студентов именно
«голых чатов», наблюдалась деградация образования. Вывод: дело не в модели как
таковой, а в наличии педагогического фреймворка поверх неё.

## Что брать в «обучалку»

1. **Педагогический фреймворк обязателен.** Модель без него ведёт к «helpful, not
   to promote learning» — и это констатируется в статье как общий порок чатов.
2. **Веди по шагам, не выдавай ответ.** `guide students sequentially through each
   part of each problem` — дешёвый в реализации и проверенный эффект.
3. **Вшей пошаговые решения в промпт** вместо того чтобы полагаться на генерацию.
   Это прямой анти-галлюцинационный механизм из статьи.
4. **Принципы vi и vii — то, где ИИ объективно сильнее класса.** Персональная
   своевременная обратная связь и свой темп физически недоступны одному
   преподавателю на поток.
5. **Мери не вовлечённость, а прирост.** Работает baseline → post-test, а не
   «понравилось ли»; enjoyment и growth mindset в этом исследовании значимой
   разницы не дали.
6. **Crossover дешевле и чище** больших групп: каждый респондент служит своим
   же контролем.
7. **Считай время.** 49 против 60 минут при большем приросте — сильнее любого
   маркетингового аргумента.

## Связи

- Источник: https://www.nature.com/articles/s41598-025-97652-6
- [[tech/free-llm-api-resources]] — бесплатные LLM API для экспериментов
