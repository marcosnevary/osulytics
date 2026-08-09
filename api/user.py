import requests


def get_user(access_token: str, username: str, mode: str) -> dict:
    response = requests.get(
        f"https://osu.ppy.sh/api/v2/users/@{username}/{mode}",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
        },
        params={
            "mode": mode,
        },
        timeout=10,
    )

    return response.json()
