
from pathlib import Path


class Config:
    """Config."""

    dir_app = Path(__file__).parent.parent
    dir_dat = dir_app / "data"
    dir_out = dir_app / "out"