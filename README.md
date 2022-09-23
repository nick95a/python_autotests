# python_autotests

Автотесты на python для работы с API Petstore.\
Ссылка на Swagger: https://petstore.swagger.io/#/

Base URL: petstore.swagger.io/v2

Основной файл main.py лежит в главной папке.
Тесты лежат в папке Tests и проверяют, что пришел корректный статус-код и корректное имя питомца. 

В файле main.py происходит следующее: 

1. Отправляется запрос на создание питомца
URL: petstore.swagger.io/v2/pet
Method: POST

2. Смена имени питомца или его тегов (**Update an existing pet**)
URL: petstore.swagger.io/v2/pet
Method: PUT   

3. Нахождение питомца по айди
URL: petstore.swagger.io/v2/pet/{petId}
Method: GET      
    
В папке Tests в файле test_petstore.py
    
Проверяем, что запрос на нахождение питомца приходит с кодом 200.
Проверяем, что в ответ на запрос о нахождении питомца приходит корректное имя.
