# ЖЁСТКИЙ запрет (hardline): state.db НИКОГДА не удалять

**Канон сырых сессий Hermes.** `~/.hermes/state.db` — точная дословная запись всех разговоров
(~190MB, 895+ сессий, 33 956 сообщений). С 20.08.2026 действует жёсткий запрет (решение Романа):
state.db **никогда** не удалять, не перезаписывать, не чистить, не сжимать, не мигрировать, и не
удалять его `.broken`-бэкапы (напр. `state.db.broken.20260820_020604`, 680MB — «пусть полежит»).

## Почему это важно при смене memory-провайдера

Смена provider (agentmemory → Hindsight) **НЕ влияет на state.db**: Hermes всегда ведёт свой
session-стор в state.db независимо от того, какой провайдер памяти активен.

Ключевое отличие: **Hindsight и другие memory-провайдеры хранят ИЗВЛЕЧЁННУЮ память** (факты,
убеждения, сущности, модели), а **НЕ дословную копию разговора**. Hindsight README прямо: «focused
on making agents that learn, not just remember»; `retain()` через LLM извлекает факты/связи, но
полный текст не дублирует. Значит state.db — ЕДИНСТВЕННЫЙ источник точной записи; его удаление =
необратимая потеря истории.

## Разрешено / запрещено

- ✅ **Разрешено:** только читать state.db (для бэкфилла в Hindsight) + штатный бэкап `pg-backup.sh`
  (state.db+agentmemory → `state-memory-*.tar.gz.enc`, aes-256-cbc).
- ❌ **Запрещено:** удалять, чистить, перезаписывать, compress/migrate содержимое; удалять
  `.broken`-бэкапы.
- ⛔ При любом сомнении — СТОП и спросить Романа.

## Как это внесено в Multica

Блок `%%HARDLINE START/END%%` добавлен в описания задач проекта «переезд памяти»: **MUL-874**,
**MUL-876** (бэкфилл), **MUL-881** (cutover) — чтобы агенты и Stall Checker видели запрет.

### Техника: append hardline-блока в описание задач через psql (base64)

```bash
B64=$(base64 -w0 < hardline-state-db.md)
docker exec multica-postgres-1 psql -U multica -d multica -tAc \
  "UPDATE issue SET description = description || convert_from(decode('$B64','base64'),'UTF8'),
   updated_at=now() WHERE number=<N>;"
```

### Создание задачи с длинным описанием (CLI)

`multica issue create --title "..." --description-file ./desc.md --project <pid> --status backlog`
— файл строго в **текущей рабочей директории** (не в /tmp — иначе отклоняется).

## Проверка

```bash
ls -la /root/.hermes/state.db                                    # на месте (190MB)
docker exec multica-postgres-1 psql -U multica -d multica -tAc \
  "SELECT 'MUL-'||number FROM issue WHERE project_id='335d19cc...' AND description LIKE '%%HARDLINE START%%';"
```
