# GoNotesUserFast
 Notes User FastAPI


poetry add fastapi

poetry add uvicorn[standard]

poetry add sqlalchemy
poetry add psycopg2
poetry add alembic


docker run --name notes_fast -p 5432:5432 -e POSTGRES_PASSWORD=567234 -d postgres

src/database/db.py
src/database/models.py


alembic init migrations

migrations/env.py    отредактировать файл env.py, в папке migrations, согласно описания в лекции

alembic revision --autogenerate -m 'Init'
    Якщо файл з міграцією успішно створився в папці migrations/versions, то:
alembic upgrade head

src/schemas.py

add in main.py

src/routes/contacts.py

src/repository/contacts.py


uvicorn main:app --host localhost --port 9000 --reload

module 12

poetry add libgravatar
poetry add python-jose["cryptography"]
poetry add passlib["bcrypt"]
poetry add python-multipart

uvicorn main:app --host localhost --port 8000 --reload

edit src/database/models.py
edit src/schemas.py
src/repository/users.py
src/services/auth.py

alembic revision --autogenerate -m 'Init'
alembic upgrade head

src/routes/auth.py

in main.py add:
app.include_router(auth.router, prefix='/api')

edit src/repository/contacts.py

edit src/routes/contacts.py

не забувати про:
alembic revision --autogenerate -m 'Init'
alembic upgrade head











