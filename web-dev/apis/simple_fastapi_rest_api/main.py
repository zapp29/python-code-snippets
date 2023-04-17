from enum import Enum
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[int, None] = None):
    return {"item_id": item_id, "q": q}


class SomeValueOptions(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/options/{option_name}")
def get_options(option_name: SomeValueOptions):
    if option_name == SomeValueOptions.alexnet:
        return {"option_name": option_name, "message": "Deep Learning FTW!"}
    if option_name.value == "lenet":
        return {"option_name": option_name, "message": "LeCNN all the images"}
    return {"option_name": option_name, "message": "Have some residuals"}

