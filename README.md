1. Для запуску API з кореня проекту необхідно виконати наступну команду: 
`docker-compose up`
2. Тести запускаються автоматичкно у момнет створення контейнеру. Для ручного запуску тестів необхідно виконати наступну команду після запуску проекту: 
`docker-compose exec api python -m pytest tests/`
3. Структура API

* **Show urls with keywords**
---
Повертає список url разом з ключовими словами
* **URL**

  /api/url/:url
  
 * **Method:**

  `GET`
  
 *  **URL Params**
 
    **Optional:**
 
    `url=[alphanumeric]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ```{ 
    "status": "success", 
    "data": [ 
    { "keywords": 
        [ "DEV Challenge",
         "Challenge", 
         "DEV" ],
          "url": "https://devchallenge.it/" 
          } ]
     }```

* **Add urls with keywords**
---
Добавляє новий url разом з ключовими словами
* **URL**

  /api/url/:url
  
 * **Method:**

  `POST`
  
 *  **URL Params**
 
    **Require:**
 
    `url=[alphanumeric]`

* **Success Response:**

  * **Code:** 201 CREATED <br />
    **Content:** ```{ 
    "status": "success",
     "data": { 
        "keywords": [ 
                "Technology BBC News", 
                "Technology BBC", 
                "Technology", 
                "BBC News", 
                "News",
                "BBC" ], 
         "url": "https://www.bbc.com/news/technology" 
         } 
     }```
    
  * **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ "message": "Url already exists" }`
    
* **Update urls with keywords**
---
Оновлює ключові слова для заданого url
* **URL**

  /api/url/:url
  
 * **Method:**

  `PUT`
  
 *  **URL Params**
 
    **Require:**
 
    `url=[alphanumeric]`

* **Success Response:**

  * **Code:** 204 CREATED <br />
    **Content:** ```{ 
    {'message': 'Url already updated'}```
    
  * **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{'message': 'Url does not exist'}`
    
* **Delete urls with keywords**
---
Видаляє ключові слова для заданого url
* **URL**

  /api/url/:url
  
 * **Method:**

  `DELETE`
  
 *  **URL Params**
 
    **Require:**
 
    `url=[alphanumeric]`

* **Success Response:**

  * **Code:** 204 CREATED <br />
    
  * **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{'message': 'No input data provided'}`

 4. Опис алгоритму створення ключових слів. 

 У яскості основного методу ключових слів було використанно алгоримт генерування n-грам для попередньо підговоленого тексту. Процедура
 підготовки тексту полягає у видаленні спеціальних символів, цифр та стоп слів (слів союзів типу "a", "the") які не можуть бути ключовими словами. Після підготовки текст розбивається масив токенів з яких будується послідовність n-грам від 1 до n, де n-розмір масиву токенів. Ця послідовність є шуканим масивом ключових слів.

 5. Шляхи подальшого поліпшення 

 1. Можна добавити обробку спеціальних для генерації ключових слів. Наприклад пошук дати в заданому форматі, або версіїї бібліотек у title 
 2. Скористатися методами обробки природних мов для пошуку іменованих сутностей (імен, назв що складаються біль ніж з одного токену) та фільтрації вихідного масиву ключових слів 