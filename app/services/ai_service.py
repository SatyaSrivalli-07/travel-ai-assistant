def generate_itinerary(city, days, interests):
    itinerary = []

    for day in range(1, days + 1):
        itinerary.append({
            "day": day,
            "plan": [
                f"Explore {interests}",
                "Visit popular attractions",
                "Enjoy local food"
            ]
        })

    return itinerary