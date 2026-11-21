[The user sent an image~ Here's what I can see:
This sequence diagram shows a client–server event-polling protocol, likely for an agent runtime. The client first calls `events/list`, and the server returns event types with `name`, `inputSchema`, `payloadSchema`, and `delivery`. The client then calls `events/poll {name, arguments, cursor: null}`, receiving `{events: [], cursor, nextPollMs}`; after waiting `nextPollMs`, it polls again with the returned `cursor`. The second poll returns `{events: [occurrence], cursor, nextPollMs}`, after which the occurrence is handed to the agent runtime.]

Представлен MCP Events.

Теперь ИИ-агенты могут подписываться на внешние события и реагировать на них, не дожидаясь запроса пользователя.

Например, агент может отслеживать репозиторий на GitHub и при появлении нового пул-реквеста автоматически запускать проверку кода и тесты.

MCP Events поддерживает три способа доставки событий.

- Poll — периодический опрос сервера.
- Push — отправка событий сервером клиенту.
- Webhook — уведомление о событии через вебхук.

На схеме показана работа Poll. Сначала клиент обнаруживает доступные события, затем обращается к серверу, ожидает некоторое время и повторяет запрос.

Когда происходит событие, информация о нём передаётся в среду выполнения ИИ-агента.

https://github.com/modelcontextprotocol/ext-events
