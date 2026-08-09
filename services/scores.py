from typing import TYPE_CHECKING

from storage.dataframe import (
    append_new_score_rows,
    load_scores_dataframe,
    save_dataframe,
)
from utils.converters import score_to_row

if TYPE_CHECKING:
    from pathlib import Path


def update_scores(scores: list[dict], file_path: Path):
    df_scores = load_scores_dataframe(file_path)

    rows = [score_to_row(score) for score in scores]

    df_scores = append_new_score_rows(
        df_scores,
        rows,
    )

    save_dataframe(df_scores, file_path)
