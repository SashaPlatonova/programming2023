# Редактирование оплаты

Форма для редактирования оплаты

**URL** : `/api/payments/create/<int:pk>`

**Method** : `PATCH`, `PUT`

**Auth required** : Yes

**Permissions required** : IsAuthenticated

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 2,
    "amount": 2000.0,
    "status": "p",
    "date_pay": "2021-05-03",
    "check_in_out_id": 1
}
```
