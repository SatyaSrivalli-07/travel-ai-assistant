# Travel AI Assistant

## Overview

This project is a backend application that helps users plan their travel. It provides APIs to search hotels, recommend the best hotels based on user preferences, and generate a day-wise travel itinerary using AI-based logic.

The application is built using FastAPI and follows a modular structure for better scalability and maintainability.

---

## Features

* Hotel Search API to find hotels by city
* Hotel Recommendation System based on budget and rating
* AI Trip Planner to generate day-wise itineraries
* Structured API responses using Pydantic models
* Basic database setup using SQLite and SQLAlchemy

---

## Tech Stack

* Python
* FastAPI
* Pydantic
* SQLAlchemy (SQLite)
* OpenAI API / Mock AI logic

---

## Project Structure

travel-ai-assistant/

app/

main.py

routes/

hotels.py

trip.py

services/

ai_service.py

recommendation.py

models/

database.py

user.py

data/

hotels.json

---

## Installation and Setup

1. Clone the repository

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate the virtual environment

```bash
venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run the server

```bash
python -m uvicorn app.main:app --reload
```

---

## API Documentation

Once the server is running, open the following URL in your browser:

http://127.0.0.1:8000/docs

---

## API Endpoints

### 1. Search Hotels

GET /hotels/search

Query Parameters:

* city

---

### 2. Recommend Hotels

GET /hotels/recommend

Query Parameters:

* city
* budget
* min_rating

---

### 3. Generate Trip Plan

POST /trip/plan

Request Body:

```json
{
  "city": "Goa",
  "days": 3,
  "interests": "beaches, nightlife"
}
```

Response Example:

```json
{
  "itinerary": [
    {
      "day": 1,
      "plan": [
        "Explore beaches",
        "Visit popular attractions",
        "Enjoy local food"
      ]
    }
  ]
}
```

---

## AI Integration

The project includes an AI-based itinerary generator. It can be implemented using OpenAI API or a fallback mock logic for offline usage. The AI component generates a structured day-wise travel plan based on user input.

---

## Database

A basic SQLite database is integrated using SQLAlchemy. It can be extended to store users, trip history, and hotel data.

---

## Notes

* The project is designed with modular architecture for easy extension.
* The AI feature can be enhanced with real-time APIs or external data sources.
* The system can be extended with authentication and frontend integration.

---
