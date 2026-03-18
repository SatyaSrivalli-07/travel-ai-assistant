from fastapi import APIRouter
import json
from app.services.recommendation import recommend_hotels

router = APIRouter()

def load_hotels():
    with open("app/data/hotels.json") as f:
        return json.load(f)

@router.get("/search")
def search_hotels(city: str):
    hotels = load_hotels()
    results = [h for h in hotels if h["city"].lower() == city.lower()]
    return {"hotels": results}
    