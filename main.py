from fastapi import FastAPI

app=FastAPI(
    title="Trading App"
)
fake_users = [
    {"id": 1, "role": "trader", "name": "John Doe"},
    {"id": 2, "role": "analyst", "name": "Jane Smith"},
    {"id": 3, "role": "investor", "name": "David Johnson"}
]
@app.get("/users/{user_id}")
def hello(user_id: int):
    return [user for user in fake_users if user.get("id")==user_id]

fake_trade = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 40000, "amount": 0.05},
    {"id": 2, "user_id": 2, "currency": "ETH", "side": "sell", "price": 3000, "amount": 1.5},
    {"id": 3, "user_id": 3, "currency": "LTC", "side": "buy", "price": 200, "amount": 5}
]

@app.get("/trades")
def get_trades(limit: int=1,offset: int=0):
    return fake_trade[offset:][:limit]

fake_users2 = [
    {"id": 1, "role": "trader", "name": "John Doe"},
    {"id": 2, "role": "analyst", "name": "Jane Smith"},
    {"id": 3, "role": "investor", "name": "David Johnson"}
]

@app.post("/users/{user_id}")
def chage_user_name(user_id:int,new_name:str):
    current_user=list(filter(lambda user:user.get("id")==user_id,fake_users2))[0]
    current_user["name"]=new_name
    return {"status":200,"data":current_user}

