from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

users = []

@app.get("/")
async def root():
    return {"message": "Welcome to the User Management API"}

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post("/users", response_model=User)
async def add_user(user: User):
    users.append(user)
    return user

