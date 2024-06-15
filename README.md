# Проект виртуальной стажировки онлайн-школы Skillfactory
## Описание проекта
### Мобильное приложение для оправки информации туристами о посещённых ими горных перевалов.

Мобильное приложение для Android и IOS, пользователями которого будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР ( Федерация спортивного туризма России ), как только появится доступ в Интернет, для того чтобы поделиться информацией с другими людьми, увлеющимися туризмом и преодолением горных перевалов.
## Работа проекта
### Внесение личной информации.

Для отправки информации туристу необходимо будет заполнить данные о себе (регистрация не требуется):
1. Фамилия
2. Имя
3. Отчество
4. Электронная почта
5. Номер телефона

### Внесение информации о горном перевале.

Для отправки информации о горном перевале, туристу необходимо будет также заполнить несколько полей:
1. Название горного перевала
2. Альтернативное название горного перевала
3. Произвольный текст ввиде комментария
4. Координаты горного перевала
5. Сложность восхождения (в зависимости от времени года)

### Обработка информации.

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

## Содержание проекта

### Основные пункты.

* Проект выполнен на языке программирования Python
* С использованием фреймворка Django
* В проекте используется СУБД PostgreSQL(пароли сохранены в файле ".env")

### Модели проекта.

Модель пользователя `Users` содержит 5 полей для заполнения данных о пользователе:
* 4 поля `CharField` для заполения данных
* 1 поле `EmailField` для указания электронной почты

Модель `Coords` служит для указания координат горного перевала и имеет 3 поля:
* 2 поля `FloatField` для указания широты и долготы
* 1 поле `IntegerField` для указания высоты

Модель `Level` служит для указания уровня сложности восхождения на тот или иногй горный перевал:
* Имеет 4 поля `CharField` в каждом из которых необходимо выбрать уровень сложности восхождения от 1А до 4A

Основной моделью проекта является модель `Pereval` включающая в себя 9 полей:
* 4 поля `CharField` включающие в себя общее название, название и альтернативное название горного перевала, а таже поле `status` с выбором статуса модерации.
* 1 поле `DateTimeField` для даты добавления горного перевала
* 1 поле `TextField` для добавления произвольного комментария от пользователя
* Поля `level` и `tourist_id` имеющие отношения один ко многим с соответствующими моделями
* Поле `coord_id` имеющее отношение один к одному с соответствующей моделью

Модель `Images` служит для добавления фото горного перевала, имеет 3 поля:
* Поле `pereval_id` имеющее имеющие отношения один ко многим с соответствующей моделью
* Поле `image` имеющее тип `ImageField` для добавления изображений либо ссылки на него
* А также поле `title` для обозначения названия изображения



### Сериализаторы проекта.

Каждая модель проекта имеет соответствующий сериализатор.
Основным сериализатором проекта служит `PerevalSerializer` содержащий в себе сериализаторы остальных моделей.

```
class PerevalSerializer(WritableNestedModelSerializer):
    tourist_id = UsersSerializer()
    coord_id = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)
    
```

### Представления и маршрутизация проекта.

В качестве представлений в проекте используется наследование класса `ModelViewSet`.
В проекте используются единственный url, предоставляющий список всех добавленных перевалов от пользователей
 path('', include(router.urls)),`
Можно просмотреть информацию об отдельном перевале по id.
При этом есть возможность использовать CRUD методы, а также фильтровать добавленную информацию по электронной почте пользователя.

### Ограничения в проекте.

В проекте существует условие при котором пользователь может изменить отправленные данные:
1. Данные не должны относиться к данным о самом пользователе (фамилия, имя, телефон и т.д.)
2. Статус модерации данной информации должен быть статусом 'new', при остальных статусах модерации, изменение данных невозможно. 

### Пример JSON файла с данными.

     {     
        "beauty_title": "title_1",
        "title": "title_1",
        "other_titles": "title_1",
        "connect": "title_1",
        "tourist_id": {
           
            "email": "ivanov@gmail.ru",
            "last_name": "Иванов",
            "first_name": "Иван",
            "patronymic": "Иванович",
            "phone": "2222222223"
        },
        "coord_id": {
            
            "latitude": "54.87690019",
            "longitude": "43.36759009",
            "height": 1244
        },
        "level": {
           
            "winter_lev": "4A",
            "spring_lev": "2A",
            "summer_lev": "1A",
            "autumn_lev": "3A"
        },
        "images": []
    }


### Документация проекта с помощью Swagger.

http://127.0.0.1:8000/redoc/
http://127.0.0.1:8000/swagger/
