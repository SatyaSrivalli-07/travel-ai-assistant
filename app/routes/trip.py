from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.services.ai_service import generate_itinerary

router = APIRouter()


class TripRequest(BaseModel):
    city: str
    days: int
    interests: str


class DayPlan(BaseModel):
    day: int
    plan: List[str]

class TripResponse(BaseModel):
    itinerary: List[DayPlan]


@router.post("/plan", response_model=TripResponse)
def plan_trip(request: TripRequest):
    itinerary = generate_itinerary(
        request.city,
        request.days,
        request.interests
    )

    return {"itinerary": itinerary}