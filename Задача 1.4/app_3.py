from fastapi import FastAPI
from model import User

main = FastAPI()

user = User(name="Телегина Алена", id=1)

@main.get("/users")
async def get_user():
    return user