from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app=FastAPI(
    title="Trading App"
)


fake_users = [
    {"id": 1, "role": "trader", "name": "John Doe"},
    {"id": 2, "role": "analyst", "name": "Jane Smith"},
    {"id": 3, "role": "investor", "name": "David Johnson"},
    {"id": 4, "role": "investor", "name": "Homer Simpson",
     "degree": [{"id": 1, "created_at": "2022-01-15", "type_degree": "newbie"}]}

]


class DegreeType(Enum):
    newbie="newbie"
    expert="expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]]=[]


@app.get("/users/{user_id}",response_model=List[User])
def hello(user_id: int):
    return [user for user in fake_users if user.get("id")==user_id]


fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 40000, "amount": 0.05},
    {"id": 2, "user_id": 2, "currency": "ETH", "side": "sell", "price": 3000, "amount": 1.5},
    {"id": 3, "user_id": 3, "currency": "LTC", "side": "buy", "price": 200, "amount": 5}
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str=Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post("/trades")
def add_trades(trades:List[Trade]):
    fake_trades.extend(trades)
    return {"status":200,"data":fake_trades}

