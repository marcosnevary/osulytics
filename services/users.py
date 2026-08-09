from typing import TYPE_CHECKING

from storage.dataframe import (
    load_users_dataframe,
    save_dataframe,
    upsert_user_row,
)
from utils.converters import user_to_row

if TYPE_CHECKING:
    from pathlib import Path


def update_user(user: dict, file_path: Path) -> None:
    df_users = load_users_dataframe(file_path)

    row = user_to_row(user)

    df_users = upsert_user_row(
        df_users,
        row,
    )

    save_dataframe(df_users, file_path)
