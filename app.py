import datetime
from typing import Annotated, Optional
from fastapi import FastAPI, Form
from fastapi import Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Order(BaseModel):
    number: int
    startDate: datetime.date
    device: str
    problemType: str
    description: str
    client: str
    status: str
    master: Optional[str] = "Не назначен"

class UpdateOrderDTO(BaseModel):
    number: int
    status: Optional[str] = ""
    description: Optional[str] = ""
    master: Optional[str] = ""

repo = [
    Order(
        number=1,
        startDate=datetime.date(2000, 12, 1),
        device="123",
        problemType="123",
        description="123",
        client="123",
        status="в ожидании"
    ),
    Order(
        number=2,
        startDate=datetime.date(2000, 12, 1),
        device="123",
        problemType="123",
        description="123",
        client="123",
        status="в ожидании"
    ),
      Order(
        number=3,
        startDate=datetime.date(2000, 12, 1),
        device="123",
        problemType="123",
        description="123",
        client="123",
        status="в ожидании"
    )
]

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins = ["*"],
  allow_methods = ["*"],
  allow_headers = ["*"]
)

message = ""

@app.get("/orders/")
def get_order(param: Optional[int] = Query(None)):
    if param is not None:
        filtered_orders = [order for order in repo if order.number == param]
        return filtered_orders if filtered_orders else {"detail": "Order not found"}
    return {"repo" :repo, "message": message}

@app.post("/orders")
def create_order(dto: Annotated[Order, Form()]):
    repo.append(dto)

@app.post("/update")
def update_order(dto: Annotated[UpdateOrderDTO, Form()]):
    for o in repo:
        if o.number == dto.number:
            if dto.status != o.status and dto.status != "":
                o.status = dto.status
                message += f"Статус заявки №{o.namber} изменен"\n
            if dto.description != "":
                o.description = dto.description
            if dto.master != "":
                o.master = dto.master
            return o
    return "Не найдено"
