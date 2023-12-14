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


uvicorn main:app --host localhost --port 8000 --reload





