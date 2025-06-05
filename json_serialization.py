from fastapi import FastAPI
from pydantic import BaseModel, field_serializer, Field
from typing import List, Optional
from datetime import datetime
import json
import os

app = FastAPI()


class PostUser(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_active: bool = False
    created_at: datetime
    tags: List[str] = []


class GetUser(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = False
    tags: List[str] = []


class Event(BaseModel):
    name: str
    event_time: datetime
    event_duration_in_minutes: int
    notes: Optional[str] = None

    @field_serializer("event_time")
    def serialize_event_time(self, dt: datetime) -> str:
        return dt.strftime("%Y-%m-%d %H:%M")


sample_user = {
    "name": "ABC",
    "age": 20,
    "is_active": True,
    "courses": ["OS", "SE"],
    "address": {"street": "Indrapur, Nagaram road", "city": "Nizamabad"},
}

print("Original Py Obj: ", sample_user)
print("Type: ", type(sample_user))

# json to a string

json_string = json.dumps(sample_user, indent=4)
print("Json Data: ", json_string)
print("Type: ", type(json_string))

un_packed_data = json.loads(json_string)
print("Unpacked data: ", un_packed_data)

# json to a file

file_name = "json_data.json"

with open(file_name, "w") as json_file:
    json.dump(sample_user, json_file, indent=4)

# Verify the file exists (optional)
print(f"File '{file_name}' size: {os.path.getsize(file_name)} bytes")

with open(file_name, "r") as json_file:
    unpacked_json_file = json.load(json_file)


# os.remove(file_name)  if required to remove file that is created.


@app.get("/users/{user_id1}", response_model=GetUser)
async def get_user(user_id: int):
    user_data = PostUser(
        id=user_id,
        name="John Doe",
        email=f"john.doe{user_id}@example.com",
        password="ABCDEFG",
        is_active=True,
        created_at=datetime.now(),
        tags=["admin", "developer"],
    )
    return user_data  # Auto serialized to JSON


@app.post("/events")
async def create_event(event: Event):
    return event
