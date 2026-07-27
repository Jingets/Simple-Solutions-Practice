**X-003-008 Техническая спецификация — Artifact**

**Статус:** MVP

**Приоритет:** P0

**Цель**

Настоящий документ определяет техническую спецификацию сущности **Artifact**.

Artifact является универсальной сущностью хранения результатов интеллектуальной работы платформы.

Документ используется для автоматической генерации:

- SQLAlchemy Model;

- PostgreSQL Table;

- Repository;

- DTO;

- API Schema.

**Назначение**

Artifact представляет любой документ, файл или структурированный результат, созданный в процессе выполнения проекта.

Artifact является неизменяемым.

При изменении содержимого создаётся новая версия.

**Таблица**

artifacts

**Первичный ключ**

id : UUID

Генерируется автоматически.

Не изменяется.

**Поля сущности**

<table style="width:61%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 27%" />
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
<td>Идентификатор Artifact</td>
</tr>
<tr>
<td>project_id</td>
<td>UUID</td>
<td>Нет</td>
<td>Связанный Project</td>
</tr>
<tr>
<td>artifact_type</td>
<td>Enum</td>
<td>Нет</td>
<td>Тип артефакта</td>
</tr>
<tr>
<td>version</td>
<td>Integer</td>
<td>Нет</td>
<td>Версия</td>
</tr>
<tr>
<td>title</td>
<td>String(255)</td>
<td>Нет</td>
<td>Название</td>
</tr>
<tr>
<td>storage_uri</td>
<td>String(1024)</td>
<td>Нет</td>
<td>Путь к объекту хранения</td>
</tr>
<tr>
<td>mime_type</td>
<td>String(100)</td>
<td>Нет</td>
<td>MIME-тип</td>
</tr>
<tr>
<td>checksum</td>
<td>String(128)</td>
<td>Нет</td>
<td>Контрольная сумма</td>
</tr>
<tr>
<td>size_bytes</td>
<td>BigInt</td>
<td>Нет</td>
<td>Размер файла</td>
</tr>
<tr>
<td>status</td>
<td>Enum</td>
<td>Нет</td>
<td>Состояние</td>
</tr>
<tr>
<td>created_at</td>
<td>Timestamp</td>
<td>Нет</td>
<td>Дата создания</td>
</tr>
<tr>
<td>created_by</td>
<td>UUID</td>
<td>Нет</td>
<td>Автор создания</td>
</tr>
</tbody>
</table>

**Типы Artifact**

Допустимые значения:

CHECKUP\_REPORT

ESTIMATION\_REPORT

OFFER\_CONTRACT

PAYMENT\_CONFIRMATION

WORK\_DOCUMENT

FINAL\_REPORT

ACCEPTANCE\_CERTIFICATE

MEMORY\_PACKAGE

SYSTEM\_DOCUMENT

OTHER

Добавление нового типа допускается только через изменение настоящей спецификации.

**Статусы**

Допустимые значения:

ACTIVE

SUPERSEDED

ARCHIVED

**Версионирование**

Artifact является неизменяемым.

При любом изменении содержимого:

- существующая запись сохраняется;

- создаётся новая запись;

- номер версии увеличивается;

- предыдущая версия получает статус SUPERSEDED.

**Связи**

Artifact обязательно принадлежит одному Project.

Project может содержать неограниченное количество Artifact.

Artifact может использоваться несколькими бизнес-модулями.

**Индексы**

Обязательные индексы:

PRIMARY KEY(id)

INDEX(project\_id)

INDEX(artifact\_type)

INDEX(created\_at)

UNIQUE(project\_id, artifact\_type, version)

**Repository Contract**

Repository обязан поддерживать операции:

create()

get()

list\_by\_project()

list\_by\_type()

get\_latest\_version()

Изменение существующего Artifact запрещено.

Удаление запрещено.

**API Contract**

Минимальные операции:

POST /artifacts

GET /artifacts/{id}

GET /projects/{project\_id}/artifacts

GET /artifacts/{id}/versions

PATCH и DELETE отсутствуют.

**Validation Rules**

Обязательно наличие:

- Project;

- Artifact Type;

- Version;

- Storage URI;

- Checksum.

Версия должна быть больше нуля.

Контрольная сумма обязательна для проверки целостности.

**Архитектурные ограничения**

Содержимое Artifact не хранится непосредственно в базе данных.

В базе сохраняются только метаданные и ссылка (storage\_uri) на объект в файловом или объектном хранилище.

Доступ к содержимому осуществляется исключительно через Artifact Manager.

**Автоматическая генерация**

На основании настоящей спецификации автоматически создаются:

- SQLAlchemy Model;

- PostgreSQL Schema;

- Alembic Migration;

- Pydantic DTO;

- Repository Interface;

- CRUD API (без операций изменения и удаления).

**Definition of Done**

Сущность считается реализованной, если:

- создана таблица;

- реализована ORM-модель;

- поддерживается версионирование;

- реализован Repository;

- опубликован API;

- проходят автоматические тесты;

- соблюдены ограничения настоящей спецификации.

**Главный принцип**

Artifact является неизменяемым контейнером результата работы платформы.

Любое изменение создаёт новую версию, сохраняя полную историю проекта и обеспечивая воспроизводимость накопленного организационного опыта.
