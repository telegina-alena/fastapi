from fastapi import FastAPI
from models import User

main = FastAPI()
first_user = User(name="Телегина Алена", age=19)

@main.post("/user")
async def get_user(user: User):
    if user.age < 18:
        is_adult = False
    else:
        is_adult = True
    return {"name": user.name, "age": user.age, "is_adult": is_adult}