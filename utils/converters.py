import json


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


def user_to_row(user: dict) -> dict:
    return {
        "avatar_url": user["avatar_url"],
        "user_id": user["id"],
        "username": user["username"],
        "country_code": user["country"]["code"],
        "country_name": user["country"]["name"],
        "highest_rank": user["rank_highest"]["rank"],
        "highest_rank_date": user["rank_highest"]["updated_at"],
        "global_rank": user["statistics"]["global_rank"],
        "country_rank": user["statistics"]["country_rank"],
        "pp": user["statistics"]["pp"],
        "accuracy": user["statistics"]["accuracy"],
        "play_count": user["statistics"]["play_count"],
        "play_time": user["statistics"]["play_time"],
        "rank_history": json.dumps(user["rank_history"]["data"]),
    }
