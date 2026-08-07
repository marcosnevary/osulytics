from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from pathlib import Path


def load_dataframe(file_path: Path) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        df = pd.DataFrame(
            columns=[
                "id",
                "date",
                "artist",
                "title",
                "version",
                "difficulty_rating",
                "total_length",
                "rank",
                "accuracy",
                "pp",
            ],
        )
    return df


def append_new_rows(df: pd.DataFrame, rows: list) -> pd.DataFrame:
    existing_ids = set(df["id"]) if not df.empty else set()

    new_rows = []
    for row in rows:
        if row["id"] not in existing_ids:
            new_rows.append(row)
            existing_ids.add(row["id"])

    if new_rows:
        df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)

    return df


def save_dataframe(df: pd.DataFrame, file_path: Path):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(file_path, index=False)
