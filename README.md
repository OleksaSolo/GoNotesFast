# GoNotesFast
 Notes FastAPI

poetry add fastapi

poetry add uvicorn[standard]

poetry add sqlalchemy
poetry add psycopg2
poetry add alembic

├── src
|  ├─database
│  |   ├── db.py
│  |   └── models.py
│  ├── repository
│  |   ├── notes.py
│  |   └── tags.py
│  ├── routes
│  |   ├── notes.py
│  |   └── tags.py
│  └── schemas.py
├── pyproject.toml
└── main.py

Точка входу в наш застосунок - main.py, а всередині папки src ми помістимо файли для роботи з нашим застосунком.

Кожен файл буде мати свою зону відповідальності:

repository/notes.py, repository/tags.py - додатковий шар абстракції, який містить методи для роботи з базою даних.
Кожен файл відповідає за роботу із конкретною таблицею.
database/db.py - буде відповідати за підключення до бази даних PostgreSQL
database/models.py - буде містити наші моделі бази даних
routes/notes.py, routes/tags.py - тут будуть знаходитись маршрути нашого REST API застосунку,
для роботи з нашими сутностями – нотатками (notes) та тегами (tags).
Звідси ми будемо викликати методи репозиторію, а не звертатись до бази даних напряму
schemas/notes.py - схеми для валідації наших вхідних та вихідних даних

docker run --name notes_fast -p 5432:5432 -e POSTGRES_PASSWORD=567234 -d postgres

src/database/db.py
src/database/models.py


alembic init migrations

migrations/env.py    отредактировать файл env.py, в папке migrations, согласно описания в лекции

alembic revision --autogenerate -m 'Init'
    Якщо файл з міграцією успішно створився в папці migrations/versions, то:
alembic upgrade head

src/schemas.py

Щоб реалізувати повний цикл CRUD операцій, нам необхідно реалізувати набір маршрутів нашого REST API застосунку:
Отримати список усіх тегів: маршрут - /api/tags, HTTP метод GET
Створити тег: маршрут - /api/tags, HTTP метод POST
Отримати тег за id: маршрут - /api/tags/<int:id>, HTTP метод GET
Оновити тег: маршрут - /api/tags/<int:id>, HTTP метод PUT
Видалити тег: маршрут - /api/tags/<int:id>, HTTP метод DELETE

add in main.py

src/routes/tags.py

src/repository/tags.py

Робота з нотатками будується аналогічно до роботи з тегами:
Отримати список нотаток: маршрут - /api/notes, HTTP метод GET
Створити нотатку: маршрут - /api/notes, HTTP метод POST
Отримати нотатку за id: маршрут - /api/notes/<int:id>, HTTP метод GET
Оновити статус нотатки: маршрут - /api/notes/<int:id>, HTTP метод patch
Видалити нотатку: маршрут - /api/notes/<int:id>, HTTP метод DELETE

src/routes/notes.py

src/repository/notes.py



