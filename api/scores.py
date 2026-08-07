import requests


def get_recent_scores(access_token: str, user_id: str, mode: str, limit: int) -> list:
    response = requests.get(
        f"https://osu.ppy.sh/api/v2/users/{user_id}/scores/recent",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
        },
        params={
            "mode": mode,
            "limit": limit,
            "include_fails": 1,
        },
        timeout=10,
    )
    return response.json()
