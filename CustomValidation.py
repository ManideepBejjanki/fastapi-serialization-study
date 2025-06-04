from pydantic import BaseModel, model_validator, ValidationError
from datetime import date
from fastapi import FastAPI, HTTPException

app = FastAPI()


class Event(BaseModel):
    name: str
    start_date: date
    end_date: date

    @model_validator(mode="after")
    def check_dates(cls, values):
        start, end = values.get("start_date"), values.get("end_dates")
        if start and end and start >= end:
            raise ValueError("start_date must be befor the end_date")
        return values


@app.post("/event")
async def post_event(event: Event):
    try:
        return {"event:", event}
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors())
