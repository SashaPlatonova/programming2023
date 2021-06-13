# Показать конкретную оплату

Выводит информацию о конкретной оплате

**URL** : `/api/payments/all/<int:pk>/`

**Method** : `GET`

**Auth required** : Yes

**Permissions required** : IsAuthenticated

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 3,
    "amount": 9500.0,
    "status": "p",
    "date_pay": "2021-04-20",
    "check_in_out_id": 1
}
```
