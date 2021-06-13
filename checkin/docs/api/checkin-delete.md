# Удалить договор

Метод для удаления договора

**URL** : `/api/checkin/delete/<int:pk>/`

**Method** : `DELETE`

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
        "comment": "accepted",
        "check_out_reason": "",
        "date_of_checkout": "2025-06-05",
        "doc_name": "Checkin Document",
        "date_of_start": "2021-06-05"
    }
```
