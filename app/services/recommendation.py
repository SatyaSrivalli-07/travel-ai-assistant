def recommend_hotels(hotels, budget, min_rating):
    filtered = [
        h for h in hotels
        if h["price_per_night"] <= budget and h["rating"] >= min_rating
    ]

    sorted_hotels = sorted(filtered, key=lambda x: x["rating"], reverse=True)

    return sorted_hotels[:3]