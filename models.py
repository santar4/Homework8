from datetime import datetime

from pydantic import BaseModel, Field, EmailStr, HttpUrl, field_validator



class Movie(BaseModel):
    id: int
    title: str
    director: str
    release_year: int = Field(..., ge=1888, le=datetime.now().year)
    rating: float = Field(..., ge=0, le=10)

    # @field_validator('release_year')
    # def validate_release_year(self, value):
    #     current_year = datetime.now().year
    #     if value > current_year:
    #         raise ValueError('Рік випуску не може бути в майбутньому')
    #     return value
