from pathlib import Path
import tyro
import pandas as pd

DEFAULT_PATH = Path("~/.cache/huggingface/lerobot")
def run(repo_id: str):
    path = DEFAULT_PATH.expanduser() / repo_id / "meta" / "tasks.parquet"
    df = pd.read_parquet(path)
    print(df)

def main():
    tyro.cli(run)

if __name__ == "__main__":
    main()
