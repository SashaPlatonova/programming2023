# Показать информацию об общежитии

Выводит информацию о конкретном общежитии

**URL** : `/api/hostels/all/<int:pk>/`

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`
```json
{
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
}
```
