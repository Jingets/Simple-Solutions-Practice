# M-001. Дорожная карта Pilot MVP

## 1. Назначение

Документ определяет состав, границы и последовательность реализации Pilot MVP платформы Simple Solutions Practice.

MVP должен реализовать один полный консультационный цикл и служить основанием для демонстрации платформы, первых пилотных внедрений и привлечения финансирования.

---

# 2. Цель Pilot MVP

Pilot MVP считается достигнутым, если пользователь может пройти полный цикл:

```text
Lead
→ Project
→ Workspace
→ Check-up
→ Estimation Report
→ Offer Contract
→ Invoice
→ Payment
→ Project Execution
→ Acceptance Certificate
→ Project Closed
```

Без ручного изменения данных в базе.

Все переходы выполняются средствами платформы.

---

# 3. Границы Pilot MVP

## Входит

### Platform Kernel

- Module Registry
- Capability Registry
- Event Dispatcher (in-process)
- Workflow Dispatcher
- Artifact Manager
- Business Event Store

### Пользователи

- ADMIN
- MANAGER
- SYSTEM

### Доменные сущности

- Lead
- Customer
- Project
- Workspace
- Check-up
- Estimation Report
- Offer Contract
- Invoice
- Acceptance Certificate
- Artifact
- Business Event

### API

REST API

OpenAPI

JWT Authentication

### Frontend

Минимальный рабочий интерфейс:

- авторизация;
- список проектов;
- карточка проекта;
- рабочее пространство;
- просмотр документов;
- выполнение действий жизненного цикла.

### Документы

Генерация:

- Check-up Report
- Estimation Report
- Offer Contract
- Invoice
- Acceptance Certificate

из шаблонов `knowledge/`.

### Тестирование

- unit;
- integration;
- E2E.

---

# 4. Не входит

Не реализуются:

- Organizational Memory;
- AI Worker;
- LiteLLM;
- Ollama;
- NATS JetStream;
- API Gateway;
- микросервисы;
- Discovery Meeting;
- Proposal;
- Agreement;
- клиентский портал;
- Notification Center;
- Trust Levels;
- Delegated Identity;
- Marketplace;
- Billing Platform;
- многоарендность.

---

# 5. Архитектурные ограничения

Pilot MVP реализуется как модульный монолит.

Используется единая PostgreSQL.

Единый backend.

Единый frontend.

Все модули работают внутри одного процесса.

Event Dispatcher является локальным.

---

# 6. Последовательность реализации

## Этап 1

Инфраструктура

Результат:

- Docker Compose;
- PostgreSQL;
- backend;
- frontend;
- nginx;
- миграции;
- JWT;
- health endpoint.

---

## Этап 2

Platform Kernel

Результат:

- Module Registry;
- Capability Registry;
- Event Dispatcher;
- Workflow Dispatcher;
- Artifact Manager;
- регистрация модулей.

---

## Этап 3

Identity

Результат:

- пользователи;
- роли;
- JWT;
- авторизация.

---

## Этап 4

Customer и Lead

Результат:

- создание Lead;
- регистрация Customer;
- поиск;
- просмотр.

---

## Этап 5

Project

Результат:

- создание проекта;
- жизненный цикл;
- Business Events;
- проверка переходов.

---

## Этап 6

Workspace

Результат:

- рабочее пространство проекта;
- загрузка файлов;
- список артефактов.

---

## Этап 7

Check-up

Результат:

- проведение диагностики;
- генерация Check-up Report.

---

## Этап 8

Estimation

Результат:

- подготовка оценки;
- генерация Estimation Report.

---

## Этап 9

Offer

Результат:

- подготовка Offer Contract;
- генерация Invoice;
- событие OfferPublished.

---

## Этап 10

Payment

Результат:

- регистрация оплаты;
- событие PaymentRegistered;
- возможность перехода OfferAccepted.

---

## Этап 11

Execution

Результат:

- выполнение проекта;
- изменение состояний;
- загрузка артефактов.

---

## Этап 12

Acceptance

Результат:

- генерация Acceptance Certificate;
- завершение проекта;
- ProjectClosed.

---

## Этап 13

Frontend

Результат:

Минимальный рабочий интерфейс для прохождения полного сценария.

---

## Этап 14

E2E

Результат:

Полный сценарий выполняется автоматически.

---

# 7. Definition of Ready

Разработка этапа начинается только если:

- определён M-документ;
- определены сущности;
- определены события;
- определены переходы;
- существуют YAML;
- существуют шаблоны;
- существует API-контракт;
- существуют критерии приёмки.

---

# 8. Definition of Done этапа

Этап считается завершённым если:

- реализованы все сущности;
- миграции проходят;
- API работает;
- OpenAPI актуален;
- события сохраняются;
- тесты проходят;
- Docker Compose запускается.

---

# 9. Критерии готовности Pilot MVP

Pilot MVP считается готовым если:

- выполняется полный сценарий раздела 2;
- отсутствуют ручные изменения БД;
- документы генерируются автоматически;
- жизненный цикл Project соответствует X-004;
- Business Events сохраняются;
- REST API соответствует OpenAPI;
- тесты проходят;
- система запускается одной командой:

```bash
docker compose up -d
```

---

# 10. Артефакты Pilot MVP

В результате реализации должны существовать:

- Backend;
- Frontend;
- Docker Compose;
- PostgreSQL;
- OpenAPI;
- Alembic migrations;
- Unit tests;
- Integration tests;
- E2E tests;
- Check-up Report;
- Estimation Report;
- Offer Contract;
- Invoice;
- Acceptance Certificate.

---

# 11. Ограничения MVP

Во время разработки запрещено:

- расширять состав сущностей;
- изменять жизненный цикл Project;
- вводить новые события;
- менять API-контракт;
- менять технологический стек;
- реализовывать Post-MVP функциональность без отдельного архитектурного решения.

---

# 12. Связанные документы

- AI-008. Pilot MVP Canonical Specification
- X-008. Последовательность реализации
- X-004. Внутренние взаимосвязи платформы
- E-017. Module SDK
- E-006. Архитектура API
- S-006. Стандарты разработки с использованием ИИ

---

**Версия:** 2.0

**Статус:** Approved for Pilot MVP