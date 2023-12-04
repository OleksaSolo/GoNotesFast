from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    first_name: str = Field(default="", examples=["Michail", "Jon"], min_length=1, max_length=25, title="first_name")
    last_name: str = Field(default="", examples=["Tower", "Smit"], min_length=1, max_length=25, title="last_name")
    email: EmailStr
    phone: str | None = Field(
        None, examples=["+440 44 123-4567", "+170 (44) 1234567", "+490441234567"], max_length=25, title="phone"
    )
    birthday: date | None = None
    comments: str | None = Field(default=None, title="comments")
    favorite: bool = False

class ContactFavoriteModel(BaseModel):
    favorite: bool = False



    # pattern=r"^+[0-9\s\(\)-]+$

class ContactResponse(BaseModel):
    id: int
    first_name: str | None
    last_name: str | None
    email: EmailStr | None
    phone: str | None
    birthday: date | None
    comments: str | None
    favorite: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

    # email: str = Field(default="email@examole.com", pattern=r'^\w+@\w+\.\w+$')


