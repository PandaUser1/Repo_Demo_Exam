import datetime
from fastapi import FastAPI
from pydantic import BaseModel

class Order(BaseModel):
    number: int
    startDate: datetime.date
    device: str
    problemType: str
    description: str
    client: str
    status: str

repo = []

app = FastAPI()

@app.get("/")
def get_order():
    return "SHello"
