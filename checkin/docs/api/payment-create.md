# Создание оплаты

Форма создания оплаты

**URL** : `/api/payments/create/`

**Method** : `POST`

**Auth required** : Yes

**Permissions required** : IsAuthenticated


## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 9,
    "amount": 6000.0,
    "status": "np",
    "date_pay": "2021-06-04",
    "check_in_out_id": 11
}
```
