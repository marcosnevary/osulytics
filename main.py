from api.auth import get_access_token
from api.scores import get_recent_scores
from config import CLIENT_ID, CLIENT_SECRET, FILE_PATH, LIMIT
from storage.dataframe import append_new_rows, load_dataframe, save_dataframe
from utils.converters import score_to_row


def main(user_id: str, mode: str):
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    scores = get_recent_scores(access_token, user_id, mode, LIMIT)

    df = load_dataframe(FILE_PATH)
    rows = [score_to_row(score) for score in scores]
    df = append_new_rows(df, rows)
    save_dataframe(df, FILE_PATH)


if __name__ == "__main__":
    main(10655638, "osu")
