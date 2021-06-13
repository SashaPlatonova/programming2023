# Показать карту пользователя

Выводит информацию о проживающих

**URL** : `/api/residents/all`

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
        "organization_id": {
            "id": 1,
            "name": "org1",
            "legal_address": "address 1",
            "type": "public company",
            "TIN": "234567453"
        },
        "password": "pbkdf2_sha256$216000$Tfi63QQ9ed0V$bvbdu/xI+pNVlwpjMCxip71ChvcB0voKdy23mi3LQC0=",
        "last_login": "2021-04-20T09:42:30.619771Z",
        "is_superuser": true,
        "username": "alex",
        "first_name": "",
        "last_name": "",
        "email": "",
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-04-02T21:25:14.498126Z",
        "registration_num": 1,
        "full_name": "full_name",
        "passport": "passport",
        "children": 0,
        "educational_institution": "nothing",
        "groups": [],
        "user_permissions": []
    },
    {
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
    {
        "id": 3,
        "organization_id": {
            "id": 1,
            "name": "org1",
            "legal_address": "address 1",
            "type": "public company",
            "TIN": "234567453"
        },
        "password": "nklkkokok",
        "last_login": "2021-04-02T21:28:15Z",
        "is_superuser": false,
        "username": "user2",
        "first_name": "Ivan",
        "last_name": "Ivanov",
        "email": "mail78@mail.com",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-04-02T21:28:08Z",
        "registration_num": 3,
        "full_name": "Ivan Ivanov",
        "passport": "8089 789876",
        "children": 2,
        "educational_institution": "nothing",
        "groups": [],
        "user_permissions": [
            32
        ]
    },
    {
        "id": 4,
        "organization_id": {
            "id": 1,
            "name": "org1",
            "legal_address": "address 1",
            "type": "public company",
            "TIN": "234567453"
        },
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
        "groups": [],
        "user_permissions": []
    },
    {
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
    {
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
    {
        "id": 7,
        "organization_id": {
            "id": 1,
            "name": "org1",
            "legal_address": "address 1",
            "type": "public company",
            "TIN": "234567453"
        },
        "password": "1234gfhjkmG",
        "last_login": "2021-05-31T20:41:11.110770Z",
        "is_superuser": false,
        "username": "johnyy",
        "first_name": "",
        "last_name": "",
        "email": "johnyy@gmail.com",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-05-31T19:56:54.393690Z",
        "registration_num": 6666,
        "full_name": "John Brown",
        "passport": "4015 56 76 56",
        "children": 0,
        "educational_institution": "1",
        "groups": [],
        "user_permissions": []
    },
    {
        "id": 8,
        "organization_id": {
            "id": 1,
            "name": "org1",
            "legal_address": "address 1",
            "type": "public company",
            "TIN": "234567453"
        },
        "password": "1234pass5678",
        "last_login": "2021-06-01T09:03:33.684074Z",
        "is_superuser": false,
        "username": "mike35",
        "first_name": "",
        "last_name": "",
        "email": "miller_@gmail.com",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-06-01T08:58:49.123135Z",
        "registration_num": 7777,
        "full_name": "Mike Miler",
        "passport": "4014 67 87 78",
        "children": 3,
        "educational_institution": "1",
        "groups": [],
        "user_permissions": []
    },
    {
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
    {
        "id": 10,
        "organization_id": {
            "id": 1,
            "name": "org1",
            "legal_address": "address 1",
            "type": "public company",
            "TIN": "234567453"
        },
        "password": "1234Pass",
        "last_login": "2021-06-01T09:24:04.923350Z",
        "is_superuser": true,
        "username": "superUser",
        "first_name": "",
        "last_name": "",
        "email": "super@gmail.com",
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-06-01T09:23:21.477141Z",
        "registration_num": 222,
        "full_name": "Super User",
        "passport": "4014 90 09 90",
        "children": 0,
        "educational_institution": "1",
        "groups": [],
        "user_permissions": []
    }
]
```


