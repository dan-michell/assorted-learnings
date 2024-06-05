from schemas.test import Item

from enum import Enum
from typing import Union
from typing_extensions import Annotated

from fastapi import FastAPI, Query


class ModelName(str, Enum):  # Inherit str to define enum value as strings for API
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


"""
PATH PARAMETERS
"""


# Needs to be defined before a route of the same name with parameter. Otherwise will be read as a path parameter.
@app.get("/items/myitem")
async def my_item():
    return {"item": "This is my item"}


@app.get("/items/{item_id}")
# Declare type here, FastAPI will enforce the type of the parameter and ensure return value is of the same type.
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/models/{model_name}")
# Setting the type of model_name to be the enum means the docs will only show those as possible parameter values
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")  # File path as a parameter
async def read_file(file_path: str):
    return {"file_path": file_path}


"""
QUERY PARAMETERS
"""

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
# If no parameters in URL, additional function arguments are treated as query parameters: http://127.0.0.1:8000/items/?skip=0&limit=10
async def read_db(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/users/{user_id}/items/{item_id}")
# With query parameters and path parameters (item_id) in the same route, query parameters must be defined after path parameters
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}

    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )

    return item


"""
USING MODELS
"""


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict


# Request body + path params + query params.
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.model_dump()}

    if q:
        result.update({"q": q})

    return result


"""
QUERY PARAMETERS AND STRING VALIDATIONS
"""


@app.get("/items_validation/")
async def read_items_validation(
    q: Annotated[
        Union[str, None],
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            max_length=50,
        ),
    ] = None
):  # Default value of ... explicitly states that value is required.
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_multiple_query_params/")
async def read_items_multiple_query_params(
    q: Annotated[Union[list[str], None], Query()] = [
        "Foo",
        "Bar",
    ]  # Will accept multiple values for same query param: http://localhost:8000/items_multiple_query_params/?q=foo&q=bar
):
    query_items = {"q": q}
    return query_items
