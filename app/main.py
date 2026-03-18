from fastapi import FastAPI
from app.routes import hotels
from app.routes import trip

app = FastAPI()

app.include_router(hotels.router, prefix="/hotels")
app.include_router(trip.router, prefix="/trip")

@app.get("/")
def root():
    return {"message": "API Running"}