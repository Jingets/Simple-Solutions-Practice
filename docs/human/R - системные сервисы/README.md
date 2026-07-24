# Раздел R — Репозиторий и интерфейсы модулей

## Назначение раздела

Раздел **R** определяет единые правила организации репозитория платформы **Simple Solutions Practice (SSP)** и контракты взаимодействия между Platform Kernel и бизнес-модулями.

Документы этого раздела являются мостом между архитектурой (разделы A, B, C) и реализацией (раздел E). Они определяют:
- структуру репозитория (каталоги, файлы, их назначение);
- интерфейсы модулей (Manifest, Capability, Events, Context, Artifact);
- правила модульной разработки;
- ограничения и запреты.

Все разработчики и среды вайб-кодинга обязаны следовать структуре и контрактам, описанным в данном разделе.

---

## Перечень документов раздела

### 1. R-001 Структура репозитория

**Статус:** MVP | **Приоритет:** P0

**Назначение:**  
Определяет единую структуру репозитория платформы Simple Solutions Practice. Все исходные коды, конфигурации, документация и ресурсы должны размещаться в соответствии с настоящим документом.

**Структура репозитория:**

ssp/
├── backend/ # Серверная часть
│ ├── app/ # Основное приложение
│ ├── kernel/ # Platform Kernel (инфраструктура)
│ │ ├── module_registry.py
│ │ ├── workflow_engine.py
│ │ ├── event_engine.py
│ │ ├── artifact_manager.py
│ │ ├── context_manager.py
│ │ └── policy_engine.py
│ ├── modules/ # Бизнес-модули
│ │ ├── lead_intake/
│ │ ├── checkup/
│ │ ├── offer_contract/
│ │ ├── project_execution/
│ │ ├── acceptance_certificate/
│ │ └── organizational_memory/
│ ├── workflows/ # Описание бизнес-процессов
│ ├── shared/ # Общие компоненты
│ ├── models/ # Модели данных
│ ├── services/ # Сервисный слой
│ ├── repositories/ # Доступ к данным
│ ├── events/ # Обработка событий
│ ├── artifacts/ # Управление артефактами
│ ├── policies/ # Бизнес-правила
│ ├── security/ # Аутентификация и авторизация
│ ├── api/ # API-эндпоинты
│ ├── config/ # Конфигурация
│ └── main.py
├── frontend/ # Клиентская часть
│ ├── src/
│ │ ├── components/
│ │ ├── pages/
│ │ ├── layouts/
│ │ ├── hooks/
│ │ ├── services/
│ │ ├── types/
│ │ ├── styles/
│ │ └── assets/
│ └── ...
├── database/ # Управление БД
│ ├── migrations/
│ ├── seed/
│ ├── schema/
│ └── backup/
├── infrastructure/ # Инфраструктура
│ ├── nginx/
│ ├── docker/
│ ├── postgres/
│ ├── storage/ # Конфигурация хранения Artifact
│ └── deployment/
├── artifacts/ # Хранилище файлов проектов
├── docs/ # Документация
│ ├── architecture/
│ ├── modules/
│ ├── repository/
│ ├── policies/
│ └── roadmap/
├── scripts/ # Скрипты автоматизации
├── tests/ # Тесты
│ ├── unit/
│ ├── integration/
│ └── system/
├── .env
├── docker-compose.yml
├── README.md
└── LICENSE

**Ключевые архитектурные ограничения:**
- Kernel не содержит бизнес-логики
- Модули независимы и не имеют прямых зависимостей друг от друга
- Frontend взаимодействует только через Backend API
- Все изменения БД — через Alembic
- Artifact доступен только через Artifact Manager

---

### 2. R-002 Спецификация интерфейсов модулей

**Статус:** MVP | **Приоритет:** P0

**Назначение:**  
Определяет единый контракт взаимодействия между Platform Kernel и бизнес-модулями. Каждый модуль обязан реализовывать настоящий интерфейс.

**Общий принцип:**  
Platform Kernel ничего не знает о внутреннем устройстве модуля. Kernel взаимодействует только через опубликованный интерфейс.

**Обязательные компоненты модуля:**

| Компонент | Описание |
|-----------|----------|
| **Manifest** | Идентификатор, имя, версия, описание, автор, статус, требуемая версия платформы, зарегистрированные Capability, опубликованные и подписанные события |
| **Capability Registry** | Список доступных Capability с указанием Identifier, Name, Description, Input Context, Output Context |
| **Event Registry** | Опубликованные события (Published Events) и обрабатываемые события (Subscribed Events) |
| **Configuration** | Собственная конфигурация модуля (не влияет на другие модули) |
| **API Entry Point** | Единая точка входа для вызова Capability, передачи Context и получения Result |

**Контракты:**

| Контракт | Описание |
|----------|----------|
| **Artifact Contract** | Artifact ID, Artifact Type, Project ID, Module ID, Version, Created At, Created By |
| **Context Contract** | Модуль получает Context от Kernel. Изменение глобального Context запрещено |
| **Error Contract** | Стандартизированный результат: Status, Result, Errors, Warnings, Generated Artifacts, Published Events |
| **Version Contract** | Каждый модуль имеет собственную версию. Kernel проверяет совместимость |
| **Dependency Contract** | Зависимости только от Platform Kernel и Shared Library. Прямые зависимости между модулями запрещены |

**Жизненный цикл модуля:**

| Текущее состояние | Событие | Новое состояние |
|-------------------|---------|-----------------|
| Registration | ModuleRegistered | Initialization |
| Initialization | ModuleInitialized | Active |
| Active | ModuleSuspended | Suspended |
| Suspended | ModuleResumed | Active |
| Active | ModuleDisabled | Disabled |
| Disabled | ModuleRemoved | Removed |

**Архитектурные ограничения:**
- Модуль не может изменять Kernel или другие модули
- Модуль не может обращаться к внутренним компонентам другого модуля
- Модуль не может изменять Organizational Memory напрямую

---

## Связи с другими разделами

| Раздел | Связь |
|--------|-------|
| **A — Архитектурные принципы** | R-001 и R-002 реализуют принципы модульности и независимости |
| **B — Бизнес-модель** | Модули R-001 (lead_intake, checkup и др.) реализуют бизнес-процессы B |
| **C — Техническая архитектура** | R-001 и R-002 соответствуют C-001 (Persistence), C-002 (Service Interface), C-004 (Identity) |
| **M — MVP** | Модули из R-001 соответствуют M-102…M-108 |
| **E — Инжиниринг** | R-001 и R-002 являются основой для реализации в E |

---

## Пример реализации модуля (Checkup)

modules/checkup/
├── manifest.py # Module ID: "checkup", Version: "1.0"
├── capabilities.py # diagnostic_interview, project_estimation
├── events.py # Published: CheckupCompleted, ProjectEstimated
├── config.py # Настройки модуля
├── api.py # API Entry Point
├── models/ # Внутренние модели
├── services/ # Бизнес-логика
├── repositories/ # Доступ к данным
├── artifacts/ # Check-up Report, Estimation Report
├── templates/ # Шаблоны документов
├── tests/ # Тесты модуля
└── README.md # Описание модуля


**Пример вызова Capability:**

```json
// Запрос от Kernel
{
  "capability": "diagnostic_interview",
  "context": {
    "project_id": "PRJ-001",
    "consultant_id": "CON-001"
  }
}

// Ответ от модуля
{
  "status": "success",
  "result": {
    "checkup_report_id": "ART-123"
  },
  "errors": [],
  "warnings": [],
  "generated_artifacts": ["ART-123"],
  "published_events": ["CheckupCompleted"]
}

---

Дата последнего обновления: 2026-07-24