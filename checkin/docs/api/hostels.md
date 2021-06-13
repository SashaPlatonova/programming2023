# Показать все общежития

Выводит информацию обо всех общежития

**URL** : `/api/hostels/all`

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "name": "ИТМО",
        "house_num": 5,
        "building": 7,
        "address_id": 1,
        "organization_id": 1
    },
    {
        "id": 2,
        "name": "Университет Петра Великого",
        "house_num": 9,
        "building": 2,
        "address_id": 2,
        "organization_id": 2
    },
    {
        "id": 3,
        "name": "Высшая школа экономики",
        "house_num": 14,
        "building": 1,
        "address_id": 3,
        "organization_id": 2
    }
]
```

