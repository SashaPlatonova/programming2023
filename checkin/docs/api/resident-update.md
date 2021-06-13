# Редактирование данных пользователя

Форма для редактирования оплаты

**URL** : `/api/residents/update/<int:pk>`

**Method** : `PATCH`, `PUT`

**Auth required** : Yes

**Permissions required** : IsAuthenticated

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 4,
    "password": "pbkdf2_sha256$260000$oc48ggKSkcI3IkpJELsc3h$WDvz2ttEgZgiJ4e7YkE3hYKzTMP2IgF2dwSCtxv6gp4=",
    "last_login": "2021-05-03T16:33:00.609554Z",
    "is_superuser": true,
    "username": "sash",
    "first_name": "",
    "last_name": "",
    "email": "",
    "is_staff": true,
    "is_active": true,
    "date_joined": "2021-05-03T16:32:34.711731Z",
    "registration_num": 76,
    "full_name": "full_name",
    "passport": "passport",
    "children": 0,
    "educational_institution": "nothing",
    "organization_id": 1,
    "groups": [],
    "user_permissions": []
}
```
