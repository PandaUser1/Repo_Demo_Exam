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

repo = [
    Order(
        number=1,
        startDate=datetime.date (2000, 12, 1),
        device="123",
        problemType="123",
        description="123",
        client="123",
        status="в ожидании"
    )
]

app = FastAPI()

@app.get("/orders/")
def get_order():
    return repo
