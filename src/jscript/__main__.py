"""Entry point for `python -m jscript`."""

from __future__ import annotations

from .fix_tasks import main


def run() -> None:
    """Fallback entrypoint for `python -m jscript`."""
    main()


if __name__ == "__main__":
    run()
