# Редактировать договор

Метод для редактирования данных договора

**URL** : `/api/checkin/update/<int:pk>/`

**Method** : `PATCH`

**Auth required** : Yes

**Permissions required** : isAdmin

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`
```json
{
        "id": 11,
        "doc_num": 6348,
        "date_of_issue": "2021-06-04",
        "comment": "",
        "check_out_reason": "",
        "date_of_checkout": "2025-06-05",
        "doc_name": "Checkin Document",
        "date_of_start": "2021-06-05"
    }
```
