from enum import Enum
from typing import Union, Any
from typing_extensions import Annotated

from fastapi_learning.schemas.test import (
    Item,
    User,
    Offer,
    Image,
    UserIn,
    UserOut,
    BaseUser,
    UserInFromBase,
)

from fastapi import (
    FastAPI,
    Query,
    Path,
    Body,
    Cookie,
    Header,
    status,
    HTTPException,
    Depends,
)
from fastapi.security import OAuth2PasswordBearer


class ModelName(str, Enum):  # Inherit str to define enum value as strings for API
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token"
)  # Use this endpoint to get the auth token


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


@app.get("/items-validation/")
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


@app.get("/items-multiple-query-params/")
async def read_items_multiple_query_params(
    q: Annotated[Union[list[str], None], Query()] = [
        "Foo",
        "Bar",
    ]  # Will accept multiple values for same query param: http://localhost:8000/items_multiple_query_params/?q=foo&q=bar
):
    query_items = {"q": q}
    return query_items


"""
PATH PARAMETERS AND NUMERIC VALIDATIONS
"""


@app.get("/items-path-validation/{item_id}")
async def read_items_path_validation(
    item_id: Annotated[
        int, Path(title="The ID of the item to get", ge=1)
    ],  # Use Path to add metadata to path parameters, similar to using Query for query parameters. ge=1 means greater than or equal to 1.
    q: Annotated[Union[str, None], Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


"""
MULTIPLE BODY PARAMETERS
"""


@app.put("/items-multiple-body-params/{item_id}")
async def update_item_multiple_body_params(
    item_id: int,
    item: Annotated[
        Item, Body(embed=True)
    ],  # Expects response of {item: {...}} instead of {"name": ""...},
    user: User,
    importance: Annotated[int, Body()],  # Will add 'importance' key to request body
    q: Union[str, None] = None,
):
    results = {
        "item_id": item_id,
        "item": item,
        "user": user,
        "importance": importance,
    }

    if q:
        results.update({"q": q})

    return results


"""
NESTED MODELS
"""


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images


"""
READING COOKIES AND HEADERS
"""


@app.get("/items-with-cookie/")
async def read_items_with_cookie(
    ads_id: Annotated[Union[str, None], Cookie()] = None
):  # Will read ads_id value from cookies
    return {"ads_id": ads_id}


@app.get("/items-with-header/")
async def read_items_with_header(
    user_agent: Annotated[Union[str, None], Header()] = None
):
    return {"User-Agent": user_agent}


"""
RETURN TYPE
"""


@app.get("/items-with-return-type")
async def items_with_return_type() -> list[Item]:
    return [Item(name="item1", price=1.4), Item(name="item2", price=1.6)]


@app.get(
    "/items-with-response-model", response_model=list[Item]
)  # response_model used as return type could be a dict representing a pydantic model.
async def read_items_with_response_model() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]


@app.post("/user/", response_model=UserOut)
async def create_user(
    user: UserIn,
) -> (
    Any
):  # returning user of type UserIn, however as response model is declared as UserOut, only the attributes of UserOut will be returned. i.e. password will be omitted
    return user


# alternatively use a base user class and create a child class with additional parameters:
@app.post("/user-base-model/")
async def create_user_base_model(user: UserInFromBase) -> BaseUser:
    return user


"""
STATUS CODES
"""


@app.post("/items-status-code/", status_code=status.HTTP_201_CREATED)
async def create_item_with_status_code(name: str):
    return {"name": name}


"""
ERROR HANDLING
"""
items = {"foo": "The Foo Wrestlers"}


@app.get("/items-error-handling/{item_id}")
async def items_error_handling(item_id: str) -> dict[str, str]:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"item": items[item_id]}


"""
DEPENDENCY INJECTION
"""


async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items-common/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


# Share common query parameters
@app.get("/users-common/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


# Same as using function
class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items-class-dependencies/")
async def read_items_class_dependency(
    commons: Annotated[CommonQueryParams, Depends()]  # Shorthand for below
    # commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response


"""
SECURITY
"""


def fake_decode_token(token: str) -> User:
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    user = fake_decode_token(token=token)
    return user


@app.get("/items-secure/", response_model=dict[str, str])
async def items_secure(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


@app.get("/users/me", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
