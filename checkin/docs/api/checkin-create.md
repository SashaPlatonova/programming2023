# Создание нового документа

## Форма создания договора на заселения или выселения

**URL** : `/api/checkin/create/`

**Method** : `POST`

**Auth required** : Yes

**Permissions required** : IsAuthenticated

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

**Content** : `{[]}`
```json
    {
        "id": 1,
        "resident_id": {
            "id": 2,
            "organization_id": {
                "id": 1,
                "name": "org1",
                "legal_address": "address 1",
                "type": "public company",
                "TIN": "234567453"
            },
            "password": "1234passPa**",
            "last_login": "2021-04-02T21:26:18Z",
            "is_superuser": false,
            "username": "user1",
            "first_name": "Oleg",
            "last_name": "Olegov",
            "email": "mail@mail.com",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2021-04-02T21:27:16Z",
            "registration_num": 2,
            "full_name": "OlegOlegov",
            "passport": "4015355335",
            "children": 0,
            "educational_institution": "ITMO",
            "groups": [],
            "user_permissions": [
                32
            ]
        },
        "room_id": {
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
        "doc_num": 123,
        "date_of_issue": "2021-04-20",
        "comment": "",
        "check_out_reason": "",
        "date_of_checkout": "2022-04-20",
        "doc_name": "checkin_doc",
        "date_of_start": "2021-04-21"
    }
```
