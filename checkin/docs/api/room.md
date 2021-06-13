# Показать все комнаты

Выводит информацию обо всех комнатах 

**URL** : `/api/rooms/all`

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
        "hostel_id": {
            "id": 1,
            "address_id": {
                "id": 1,
                "city_district": "Петроградский",
                "street": "Вяземский пер.",
                "zip_code": "197022"
            },
            "name": "ИТМО",
            "house_num": 5,
            "building": 7,
            "organization_id": 1
        },
        "floor": 3,
        "beds": 8,
        "area": 60.5,
        "busy_beds": 4
    },
    {
        "id": 2,
        "hostel_id": {
            "id": 1,
            "address_id": {
                "id": 1,
                "city_district": "Петроградский",
                "street": "Вяземский пер.",
                "zip_code": "197022"
            },
            "name": "ИТМО",
            "house_num": 5,
            "building": 7,
            "organization_id": 1
        },
        "floor": 2,
        "beds": 6,
        "area": 48.9,
        "busy_beds": 2
    },
    {
        "id": 3,
        "hostel_id": {
            "id": 1,
            "address_id": {
                "id": 1,
                "city_district": "Петроградский",
                "street": "Вяземский пер.",
                "zip_code": "197022"
            },
            "name": "ИТМО",
            "house_num": 5,
            "building": 7,
            "organization_id": 1
        },
        "floor": 1,
        "beds": 2,
        "area": 20.7,
        "busy_beds": 1
    },
    {
        "id": 4,
        "hostel_id": {
            "id": 1,
            "address_id": {
                "id": 1,
                "city_district": "Петроградский",
                "street": "Вяземский пер.",
                "zip_code": "197022"
            },
            "name": "ИТМО",
            "house_num": 5,
            "building": 7,
            "organization_id": 1
        },
        "floor": 1,
        "beds": 4,
        "area": 60.8,
        "busy_beds": 4
    },
    {
        "id": 5,
        "hostel_id": {
            "id": 2,
            "address_id": {
                "id": 2,
                "city_district": "Калининский",
                "street": "Хлопина",
                "zip_code": "194021"
            },
            "name": "Университет Петра Великого",
            "house_num": 9,
            "building": 2,
            "organization_id": 2
        },
        "floor": 3,
        "beds": 2,
        "area": 25.0,
        "busy_beds": 2
    },
    {
        "id": 6,
        "hostel_id": {
            "id": 2,
            "address_id": {
                "id": 2,
                "city_district": "Калининский",
                "street": "Хлопина",
                "zip_code": "194021"
            },
            "name": "Университет Петра Великого",
            "house_num": 9,
            "building": 2,
            "organization_id": 2
        },
        "floor": 2,
        "beds": 4,
        "area": 47.9,
        "busy_beds": 3
    },
    {
        "id": 7,
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
        "floor": 1,
        "beds": 2,
        "area": 30.1,
        "busy_beds": 2
    },
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
]
```

