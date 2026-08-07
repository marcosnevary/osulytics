import requests


def get_access_token(client_id: str, client_secret: str) -> str:
    response = requests.post(
        "https://osu.ppy.sh/oauth/token",
        json={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
            "scope": "public",
        },
        timeout=10,
    )
    return response.json()["access_token"]
