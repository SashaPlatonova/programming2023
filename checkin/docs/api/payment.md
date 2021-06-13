# Показать все квитанции на оплату

Выводит информацию об оплате

**URL** : `/api/payments/all`

**Method** : `GET`

**Auth required** : Yes

**Permissions required** : IsAuthenticated

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "check_in_out_id": {
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
        },
        "amount": 1500.0,
        "status": "pp",
        "date_pay": "2021-04-20"
    },
    {
        "id": 2,
        "check_in_out_id": {
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
        },
        "amount": 2000.0,
        "status": "p",
        "date_pay": "2021-05-03"
    },
    {
        "id": 3,
        "check_in_out_id": {
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
        },
        "amount": 9500.0,
        "status": "p",
        "date_pay": "2021-04-20"
    },
    {
        "id": 4,
        "check_in_out_id": {
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
        },
        "amount": 3000.0,
        "status": "p",
        "date_pay": "2021-05-01"
    },
    {
        "id": 5,
        "check_in_out_id": {
            "id": 2,
            "resident_id": {
                "id": 5,
                "organization_id": {
                    "id": 1,
                    "name": "org1",
                    "legal_address": "address 1",
                    "type": "public company",
                    "TIN": "234567453"
                },
                "password": "pbkdf2_sha256$260000$37l2whRdIo6dZi4j8WJnGX$qC/RFpNmpn07OlmpZfRk/Ko/lx3ZhNLMt2oV18XVR7U=",
                "last_login": "2021-05-10T09:39:49.872697Z",
                "is_superuser": false,
                "username": "testUser",
                "first_name": "",
                "last_name": "",
                "email": "",
                "is_staff": false,
                "is_active": true,
                "date_joined": "2021-05-10T09:38:45.430601Z",
                "registration_num": 409,
                "full_name": "full_name",
                "passport": "passport",
                "children": 0,
                "educational_institution": "nothing",
                "groups": [],
                "user_permissions": []
            },
            "room_id": {
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
            "doc_num": 4546,
            "date_of_issue": "2021-05-30",
            "comment": "",
            "check_out_reason": "",
            "date_of_checkout": "2025-05-30",
            "doc_name": "checkin_doc",
            "date_of_start": "2021-05-31"
        },
        "amount": 3600.0,
        "status": "p",
        "date_pay": "2021-05-31"
    },
    {
        "id": 6,
        "check_in_out_id": {
            "id": 4,
            "resident_id": {
                "id": 6,
                "organization_id": {
                    "id": 1,
                    "name": "org1",
                    "legal_address": "address 1",
                    "type": "public company",
                    "TIN": "234567453"
                },
                "password": "pbkdf2_sha256$260000$6tSWjZHnmcOTXqziP9emOV$3Fc3RdGs8+ZHmNjyYDFzenoO8L+PvZPsHZ5vJYfmjiM=",
                "last_login": "2021-05-11T08:56:08.340839Z",
                "is_superuser": false,
                "username": "user12",
                "first_name": "",
                "last_name": "",
                "email": "",
                "is_staff": false,
                "is_active": true,
                "date_joined": "2021-05-11T08:49:30.771843Z",
                "registration_num": 234,
                "full_name": "full_name",
                "passport": "passport",
                "children": 1,
                "educational_institution": "nothing",
                "groups": [],
                "user_permissions": []
            },
            "room_id": {
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
            "doc_num": 8998,
            "date_of_issue": "2021-05-31",
            "comment": "",
            "check_out_reason": "",
            "date_of_checkout": "2025-05-30",
            "doc_name": "Checkin document",
            "date_of_start": "2021-05-31"
        },
        "amount": 3500.0,
        "status": "p",
        "date_pay": "2021-05-31"
    },
    {
        "id": 7,
        "check_in_out_id": {
            "id": 4,
            "resident_id": {
                "id": 6,
                "organization_id": {
                    "id": 1,
                    "name": "org1",
                    "legal_address": "address 1",
                    "type": "public company",
                    "TIN": "234567453"
                },
                "password": "pbkdf2_sha256$260000$6tSWjZHnmcOTXqziP9emOV$3Fc3RdGs8+ZHmNjyYDFzenoO8L+PvZPsHZ5vJYfmjiM=",
                "last_login": "2021-05-11T08:56:08.340839Z",
                "is_superuser": false,
                "username": "user12",
                "first_name": "",
                "last_name": "",
                "email": "",
                "is_staff": false,
                "is_active": true,
                "date_joined": "2021-05-11T08:49:30.771843Z",
                "registration_num": 234,
                "full_name": "full_name",
                "passport": "passport",
                "children": 1,
                "educational_institution": "nothing",
                "groups": [],
                "user_permissions": []
            },
            "room_id": {
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
            "doc_num": 8998,
            "date_of_issue": "2021-05-31",
            "comment": "",
            "check_out_reason": "",
            "date_of_checkout": "2025-05-30",
            "doc_name": "Checkin document",
            "date_of_start": "2021-05-31"
        },
        "amount": 3500.0,
        "status": "np",
        "date_pay": "2021-05-31"
    },
    {
        "id": 8,
        "check_in_out_id": {
            "id": 5,
            "resident_id": {
                "id": 9,
                "organization_id": {
                    "id": 1,
                    "name": "org1",
                    "legal_address": "address 1",
                    "type": "public company",
                    "TIN": "234567453"
                },
                "password": "pbkdf2_sha256$260000$0rUec8FfpTuV0O2HeWWHMs$75F0O3FvoQhiOJn82WPNNWsSBi7zvwPHPv0FAyMtZng=",
                "last_login": "2021-06-04T11:27:36.857692Z",
                "is_superuser": false,
                "username": "geryJoi",
                "first_name": "",
                "last_name": "",
                "email": "grey@mail.com",
                "is_staff": false,
                "is_active": true,
                "date_joined": "2021-06-01T09:18:34.860271Z",
                "registration_num": 67667,
                "full_name": "Genry Grey",
                "passport": "passport",
                "children": 0,
                "educational_institution": "nothing",
                "groups": [],
                "user_permissions": []
            },
            "room_id": {
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
            "doc_num": 7889,
            "date_of_issue": "2021-06-01",
            "comment": "",
            "check_out_reason": "",
            "date_of_checkout": "2025-06-01",
            "doc_name": "Checkin Document",
            "date_of_start": "2021-06-02"
        },
        "amount": 3500.0,
        "status": "np",
        "date_pay": "2021-06-02"
    }
]
```

