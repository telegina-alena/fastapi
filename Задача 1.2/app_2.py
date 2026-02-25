from fastapi import FastAPI
from fastapi.responses import FileResponse

main = FastAPI()

@main.get("/")
async def root():
    index = "index.html"
    return FileResponse(index)