def get_fields(results):
    new_results = []
    for r in results:
        new_results.append({
            "name": r["name"],
            "rating": calculate_rating(r["rating"]),
            "total_ratings": r["user_ratings_total"],
            "type": r["types"][0],
            "location": get_location_from_compound_code(r["plus_code"]["compound_code"]),
            "place_id": r["place_id"]
        })
    return new_results

def calculate_rating(rating):
    return rating * 20

def get_location_from_compound_code(compound_code):
    words = compound_code.split(" ")
    location = words[1:]
    return location