from pathlib import Path
import tyro
import pandas as pd

DEFAULT_PATH = Path("~/.cache/huggingface/lerobot")
def main(repo_id: str):
    path = DEFAULT_PATH.expanduser() / repo_id / "meta" / "tasks.parquet"
    df = pd.read_parquet(path)
    print(df)

if __name__ == "__main__":
    tyro.cli(main)
