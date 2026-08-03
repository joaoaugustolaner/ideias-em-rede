from collections.abc import Iterable

import pandas as pd


def require_columns(data: pd.DataFrame, columns: Iterable[str]) -> None:
    missing = set(columns) - set(data.columns)
    if missing:
        missing_columns = ", ".join(sorted(missing))
        raise ValueError(f"Colunas obrigatórias ausentes: {missing_columns}")
