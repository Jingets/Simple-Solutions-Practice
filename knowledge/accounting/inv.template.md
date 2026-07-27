# СЧЁТ НА ОПЛАТУ № {{invoice.number}}

Дата: {{invoice.date}}

Основание: Договор-оферта № {{contract.number}} от {{contract.date}}

Проект: {{project.id}}

---

## Исполнитель

Наименование:

{{contractor.legal_name}}

ИНН:

{{contractor.inn}}

КПП:

{{contractor.kpp}}

ОГРН:

{{contractor.ogrn}}

Юридический адрес:

{{contractor.address}}

Расчётный счёт:

{{contractor.bank_account}}

Банк:

{{contractor.bank_name}}

БИК:

{{contractor.bank_bik}}

Корреспондентский счёт:

{{contractor.bank_corr}}

---

## Заказчик

Наименование:

{{client.organization}}

Контактное лицо:

{{client.name}}

ИНН:

{{client.inn}}

Адрес:

{{client.address}}

Электронная почта:

{{client.email}}

Телефон:

{{client.phone}}

---

## Перечень услуг

| № | Наименование     | Количество |                                   Цена |                                  Сумма |
| - | ---------------- | ---------: | -------------------------------------: | -------------------------------------: |
| 1 | {{service.name}} |          1 | {{pricing.price}} {{pricing.currency}} | {{pricing.price}} {{pricing.currency}} |

---

## Итого

**К оплате:**

**{{pricing.price}} {{pricing.currency}}**

НДС: Без НДС (если применимо)

---

## Назначение платежа

Оплата консультационной услуги **«{{service.name}}»** по договору-оферте № {{contract.number}}.

Проект: {{project.id}}

---

## Порядок оплаты

Оплата настоящего счёта означает акцепт договора-оферты.

После поступления денежных средств платформа SSP автоматически:

* регистрирует оплату;
* создаёт проект;
* открывает рабочее пространство проекта;
* уведомляет Исполнителя о начале выполнения работ.

---

Счёт сформирован автоматически платформой **Simple Solutions Practice (SSP)**.

Идентификатор проекта: **{{project.id}}**
