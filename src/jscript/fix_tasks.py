from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil
from typing import Literal

import pandas as pd
import tyro


@dataclass(frozen=True, slots=True)
class Args:
    path: Path
    mode: Literal["drop", "index"] = "drop"
    suffix: str = ".backup"


def load_df(path: Path) -> pd.DataFrame:
    if path.suffix == ".csv":
        return pd.read_csv(path)
    if path.suffix in {".parquet", ".pq"}:
        return pd.read_parquet(path)
    raise ValueError(f"Unsupported file type: {path.suffix}")


def save_df(df: pd.DataFrame, path: Path) -> None:
    if path.suffix == ".csv":
        df.to_csv(path, index=False)
    elif path.suffix in {".parquet", ".pq"}:
        df.to_parquet(path, index=False)
    else:
        raise ValueError(f"Unsupported file type: {path.suffix}")


def run(args: Args) -> None:
    path = args.path

    if not path.exists():
        raise FileNotFoundError(path)

    backup_path = path.with_suffix(path.suffix + args.suffix)
    shutil.copy2(path, backup_path)

    df = load_df(path)
    col = "__index_level_0__"

    if col in df.columns:
        if args.mode == "drop":
            df = df.drop(columns=[col])
        elif args.mode == "index":
            df = df.set_index(col)
            df.index.name = None
        else:
            raise ValueError(f"Unknown mode: {args.mode}")

    save_df(df, path)

    print(f"CLEANED: {path}")
    print(f"BACKUP: {backup_path}")


def main() -> None:
    run(tyro.cli(Args))
