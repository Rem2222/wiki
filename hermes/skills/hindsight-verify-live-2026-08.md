# Проверка Hindsight вживую после переезда (verified 21.08.2026)

Когда переезд на Hindsight выполнен (MUL-875 развёрнуто, MUL-876 бэкфилл, MUL-877 провайдер
переключён), проверка «не на слово», что память реально активна и пишется:

## 1. Провайдер активен

```bash
hermes memory status        # → Provider: hindsight, Plugin installed ✓, Status available ✓
cat ~/.hermes/hindsight/config.json
```

Активный конфиг пользователя (боевой, verified):
```json
{ "mode": "local_external", "api_url": "http://localhost:8888", "bank_id": "hermes",
  "memory_mode": "hybrid", "auto_recall": true, "auto_retain": true,
  "llm_provider": "opencode-go", "llm_model": "mimo-v2.5", "embeddings_model": "bge-m3" }
```
⚠️ **Проверять `hermes memory status`, не yaml.** Секция `memory:` в config.yaml ненадёжна из-за
`config set`-клобберинга (см. MUL-696 в SKILL.md). Рабочие комбо для этого VPS: `mode: local_external`
(а не `local`) + `llm_provider: opencode-go/mimo-v2.5` (а не ollama) — mimo-v2.5 выбран как дешёвый
провайдер, умеющий XML (см. AgentMemory leak-секцию SKILL.md).

## 2. Всё ли пишется — объёмы в Postgres

Hindsight хранится в отдельном контейнере `hindsight-db` (Postgres). Таблицы (23 шт, `\dt`):
`memory_units` (текст факта + embedding vector(1024) + event_date/fact_type), `documents`,
`entities`, `entity_cooccurrences`, `observation_history` (jsonb: previous_text/new_source_memory_ids),
`mental_models`, `knowledge_pages`, `banks`, `chunks`.

```bash
docker exec hindsight-db psql -U hindsight_user -d hindsight_db -tAc \
  "SELECT 'units:'||count(*) FROM memory_units;
   SELECT 'docs:'||count(*) FROM documents;
   SELECT 'entities:'||count(*) FROM entities;
   SELECT 'observations:'||count(*) FROM observation_history;"
```

Проверено на боевой БД bank=hermes: units 29 991, docs 3 851, entities 11 481, observations 1 545.
Живая запись после переключения — каждый час +166..253 memory_units:
```sql
SELECT to_char(date_trunc('hour',created_at),'HH24:00') h, count(*)
FROM memory_units WHERE created_at > timestamp '2026-08-21 05:18:00'
GROUP BY 1 ORDER BY 1;
```

## 3. Авто-recall реально тянет прошлую память

Запрос через клиент Hindsight должен вернуть релевантные факты из ПРОШЛЫХ сессий, а не только
текущей. Готовый зонд — `scripts/hindsight-recall-test.py`. Пример самопроверки:
задать вопрос «Что Роман решил по переезду памяти?» → возвращает отпечаток решения из банка.

## 4. Сырые сессии НЕ переезжают в Hindsight

**Hindsight хранит извлечённую память (факты/убеждения/связи), а НЕ дословную копию разговора** —
`retain()` проходит через LLM-экстракцию. Поэтому канон сырых сессий остаётся `~/.hermes/state.db`
(Hermes пишет туда всегда, независимо от провайдера). state.db не трогать никогда
(см. `references/state-db-hardline-rule.md`).

## Pitfall: hindsight_client не ставится системным pip

```bash
pip install hindsight-client   # → error: externally-managed-environment (PEP 668)
```
Фикс — в venv:
```bash
python3 -m venv /tmp/hsvenv && /tmp/hsvenv/bin/pip install hindsight-client
/tmp/hsvenv/bin/python - <<'PY'
from hindsight_client import Hindsight
c = Hindsight(base_url="http://127.0.0.1:8888", api_key="<из /root/.hermes/hindsight/config.json>")
for r in c.recall(bank_id="hermes", query="Что Роман решил по переезду памяти?").results:
    print(r.text[:160])
PY
```
⚠️ Небольшой шум в конце: `Unclosed client session / aiohttp connector` — безвредно (неверная форма
завершения aiohttp, не ошибка памяти).