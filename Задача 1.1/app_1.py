from fastapi import FastAPI

main = FastAPI()

@main.get("/")
async def root():
    return {"message": "Добро пожаловать в моё приложение FartAPI!"}