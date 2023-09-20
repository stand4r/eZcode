# eZcode
API Instruction

GET /api

Получение словаря со всеми json объектами из базы данных
[{
    "id": <int>,
    "likes": <int>,
    "dislikes": <int>,
    "about": <Text>,
    "isActive": <Boolean>,
    "link": <String>
}, ...]

<Response [200]> - без ошибок



GET /api/<id:int>

Получение json объекта из базы данных по id
Получаемая форма:
{
    "id": <int>,
    "likes": <int>,
    "dislikes": <int>,
    "about": <Text>,
    "isActive": <Boolean>,
    "link": <String>
}

<Response [200]> - без ошибок




POST /api

Создание объекта в базе данных
Форма для запроса:
{
    "link": "<String>",
    "about": "<Text>"
} 

<Response [201]> - без ошибок



PUT /api

Изменения объекта из базы данных по id
id в запросе обязательно
Форма для запроса:
{
    "id": <int>,
    ...
}

<Response [200]> - без ошибок




DELETE /api/<id:int>

Удаление объекта из базы данных
id обязательно
Форма для запроса:
{
    "id": <int>
}

<Response [204]> - без ошибок
