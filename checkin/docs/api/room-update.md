# Изменить информацию о комнате

Изменение информации о конретной комнате

**URL** : `/api/rooms/update/<int:pk>/`

**Method** : `PATCH`, `PUT`

**Auth required** : Yes

**Permissions required** : IsAdmin

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
    {
        "id": 8,
        "hostel_id": {
            "id": 3,
            "address_id": {
                "id": 3,
                "city_district": "Адмиралтейский",
                "street": "Витебская",
                "zip_code": "190121"
            },
            "name": "Высшая школа экономики",
            "house_num": 14,
            "building": 1,
            "organization_id": 2
        },
        "floor": 3,
        "beds": 6,
        "area": 49.8,
        "busy_beds": 5
    }
```
