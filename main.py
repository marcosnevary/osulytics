from api.auth import get_access_token
from api.scores import get_recent_scores
from api.user import get_user
from config import CLIENT_ID, CLIENT_SECRET, LIMIT, SCORES_FILE_PATH, USERS_FILE_PATH
from services.scores import update_scores
from services.users import update_user


def main(username: str, mode: str):
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)

    user = get_user(access_token, username, mode)
    update_user(user, USERS_FILE_PATH)

    scores = get_recent_scores(access_token, user["id"], mode, LIMIT)
    update_scores(scores, SCORES_FILE_PATH)


if __name__ == "__main__":
    main("nixusxD", "osu")
