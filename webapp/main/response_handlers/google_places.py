def get_fields(results):
    new_results = []
    for r in results:
        new_results.append({
            "name": r["name"],
            "rating": r["rating"] * 20,
            "total_ratings": r["user_ratings_total"],
            "type": r["types"][0]
        })
    return new_results