from typing import Union

from pydantic import BaseModel, Field, HttpUrl, EmailStr


class Image(BaseModel):
    url: HttpUrl  # Exotic Pydantic type - see https://docs.pydantic.dev/latest/concepts/types/
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        None, description="The description of the item", max_length=300
    )
    price: float = Field(
        gt=0,
        description="The price must be greater than zero",
        examples=["Groovy Item"],
    )
    tax: Union[float, None] = None
    tags: set[str] = set()
    image: Union[Image, None] = None  # Nested model

    model_config = {  # Will overwrite default body values in docs
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[str, None] = None


class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: list[Item]


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserInFromBase(BaseUser):
    password: str
