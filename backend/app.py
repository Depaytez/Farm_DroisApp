# backend/app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "DroisApp Backend is running!"}

# To run app.py, you would install FastAPI and Uvicorn:
## pip install fastapi uvicorn
## Then run: uvicorn app:app --reload