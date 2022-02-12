from pydantic import BaseModel
from datetime import date


class Genre(BaseModel):
    code: int
    price: int
    city: str

class Book(BaseModel):
    code: int
    price: int
    city: str

