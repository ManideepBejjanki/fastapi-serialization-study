from typing import Union, Annotated
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr, ValidationError

app = FastAPI()


class User(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Name must  be with in 3 and 50 characters.",
    )
    # age: conint(gt=0, le=120) = Field(
    #     ..., description="Age is restricted between 0 and 120"
    # )
    # it is depricate dfrom pydantic v2
    age: Annotated[
        int, Field(gt=0, le=120, description="Age is restricted between 0 and 120")
    ]
    email: EmailStr = Field(..., description="Should be a valid email.")
    is_major: Union[bool, None] = None


@app.post("/users")
async def create_user(user: User):
    try:
        return {"message": f"User {user.name} is created successfully"}
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors())
