**X-003-003 Техническая спецификация — Project**

**Статус:** MVP

**Приоритет:** P0

**Цель**

Настоящий документ определяет техническую спецификацию доменной сущности **Project**.

Документ является единственным источником требований для генерации:

- SQLAlchemy Model;

- PostgreSQL Table;

- Repository;

- DTO;

- API Schema.

**Назначение**

Project представляет собой консалтинговый проект, выполняемый платформой Simple Solutions Practice.

Project является центральной сущностью системы.

Все бизнес-объекты платформы связаны с конкретным Project.

**Таблица**

projects

**Первичный ключ**

id : UUID

Генерируется автоматически.

Не изменяется.

**Поля сущности**

<table style="width:64%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 4%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Поле</strong></th>
<th style="text-align: center;"><strong>Тип</strong></th>
<th style="text-align: center;"><strong>Null</strong></th>
<th style="text-align: center;"><strong>Описание</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>id</td>
<td>UUID</td>
<td>Нет</td>
<td>Идентификатор проекта</td>
</tr>
<tr>
<td>lead_id</td>
<td>UUID</td>
<td>Нет</td>
<td>Ссылка на Lead</td>
</tr>
<tr>
<td>status</td>
<td>Enum</td>
<td>Нет</td>
<td>Текущее состояние проекта</td>
</tr>
<tr>
<td>opened_at</td>
<td>Timestamp</td>
<td>Нет</td>
<td>Дата открытия</td>
</tr>
<tr>
<td>closed_at</td>
<td>Timestamp</td>
<td>Да</td>
<td>Дата закрытия</td>
</tr>
<tr>
<td>created_at</td>
<td>Timestamp</td>
<td>Нет</td>
<td>Дата создания записи</td>
</tr>
<tr>
<td>updated_at</td>
<td>Timestamp</td>
<td>Нет</td>
<td>Дата последнего изменения</td>
</tr>
<tr>
<td>created_by</td>
<td>UUID</td>
<td>Нет</td>
<td>Автор создания</td>
</tr>
<tr>
<td>updated_by</td>
<td>UUID</td>
<td>Нет</td>
<td>Автор последнего изменения</td>
</tr>
</tbody>
</table>

**Статусы**

Допустимые значения:

DRAFT

IN_PROGRESS

ON_HOLD

WAITING_CLIENT

REVIEW

COMPLETED

CLOSED

Другие значения запрещены.

**Связи**

**Один Project содержит**

- Checkups

- Estimation Reports

- Offer Contracts

- Artifacts

- Business Events

- Acceptance Certificates

**Один Project имеет**

- один Lead

- один Project Workspace

- одну запись Organizational Memory

**Ограничения**

Lead обязателен.

Project не может существовать без Lead.

Дата открытия обязательна.

Дата закрытия появляется только после завершения проекта.

Статус не может изменяться произвольно.

Изменение статуса выполняется исключительно через Workflow Engine.

**Индексы**

Обязательные:

PRIMARY KEY(id)

INDEX(status)

INDEX(lead\_id)

INDEX(opened\_at)

**Repository Contract**

Repository обязан поддерживать:

create()

get()

update()

list()

archive()

Физическое удаление запрещено.

**API Contract**

Минимальные операции:

POST /projects

GET /projects/{id}

GET /projects

PATCH /projects/{id}

DELETE отсутствует.

**Artifact Contract**

Каждый Project обязан иметь возможность связываться с произвольным количеством Artifact.

Artifact не хранится внутри Project.

Хранится только ссылка.

**Event Contract**

Каждое изменение состояния Project должно сопровождаться регистрацией Business Event.

**Validation Rules**

Запрещается:

- создание без Lead;

- изменение UUID;

- ручное изменение статуса;

- физическое удаление.

**Автоматическая генерация**

На основании настоящей спецификации должна автоматически создаваться:

- SQLAlchemy Model;

- PostgreSQL Schema;

- Alembic Migration;

- Pydantic DTO;

- Repository Interface;

- CRUD API.

**Definition of Done**

Сущность считается реализованной, если:

- создана таблица;

- создана ORM-модель;

- реализован Repository;

- опубликован API;

- проходят все тесты;

- соблюдены ограничения настоящей спецификации.

**Главный принцип**

Project является центральной бизнес-сущностью платформы и единой точкой объединения всех артефактов, событий, рабочих материалов и результатов консалтингового проекта.
