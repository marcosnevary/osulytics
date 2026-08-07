def score_to_row(score: dict) -> dict:
    return {
        "id": score["id"],
        "date": score["created_at"],
        "artist": score["beatmapset"]["artist"],
        "title": score["beatmapset"]["title"],
        "version": score["beatmap"]["version"],
        "difficulty_rating": score["beatmap"]["difficulty_rating"],
        "total_length": score["beatmap"]["total_length"],
        "rank": score["rank"],
        "accuracy": score["accuracy"],
        "pp": score["pp"],
    }
