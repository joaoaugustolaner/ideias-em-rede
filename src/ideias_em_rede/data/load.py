from pathlib import Path

import pandas as pd


def load_csv(path: str | Path, **kwargs) -> pd.DataFrame:
    return pd.read_csv(Path(path), **kwargs)


def load_jsonl(path: str | Path, **kwargs) -> pd.DataFrame:
    return pd.read_json(Path(path), lines=True, **kwargs)
