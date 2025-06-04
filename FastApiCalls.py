from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    mobile: int
    is_major: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"message": "Hello User."}


@app.get("/users/{user_id}")
def read_user(user_id: int, queryParams: Union[str, None] = None):
    return {"user_id": user_id, "queryParams": queryParams}


@app.post("/users")
async def create_user(user: User):
    return {
        "user_name": user.name,
        "user_mobile": user.mobile,
        "user_is_major": user.is_major,
    }


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    return {"user_id": user_id, "user": user}


@app.delete("users/{user_id}")
async def delete_user(user_id: int):
    return {"message": f"User with id {user_id} has been deleted"}
