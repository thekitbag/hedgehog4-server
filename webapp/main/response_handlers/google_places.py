def get_fields(results):
    new_results = []
    for r in results:
        new_results.append({
            "name": r["name"],
            "rating": calculate_rating(r["rating"]),
            "total_ratings": r["user_ratings_total"],
            "type": get_place_type(r["types"]),
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

def get_place_type(place_types):
    mapping = {
        "bar": "Pub or Bar",
        "meal_takeaway": "Takeaway"
    }

    if place_types[0] in mapping:
        return mapping[place_types[0]]
    else:
        return place_types[0]