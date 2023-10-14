# eZcode-server
API Instruction



GET /api

Получение словаря со всеми json объектами из базы данных [{ "id": , "likes": , "dislikes": , "about": , "isActive": , "link": }, ...]

<Response [200]> - без ошибок



GET /api/id:int

Получение json объекта из базы данных по id Получаемая форма: { "id": , "likes": , "dislikes": , "about": , "isActive": , "link": }

<Response [200]> - без ошибок



POST /api

Создание объекта в базе данных Форма для запроса: { "link": "", "about": "" }

<Response [201]> - без ошибок



PUT /api

Изменения объекта из базы данных по id id в запросе обязательно Форма для запроса: { "id": , ... }

<Response [200]> - без ошибок



DELETE /api/id:int

Удаление объекта из базы данных id обязательно Форма для запроса: { "id": }

<Response [204]> - без ошибок
