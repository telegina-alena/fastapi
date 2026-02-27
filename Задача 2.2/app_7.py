from fastapi import FastAPI
from model import Feedback

main = FastAPI()

message = Feedback(name="Алена", message="я устала просто ужас")
all_feedback = []

@main.post("/feedback")
async def feedback(feedback: Feedback):
    all_feedback.append(feedback)
    return {"message": f"Спасибо большое за ваше мнение, {feedback.name}!"}