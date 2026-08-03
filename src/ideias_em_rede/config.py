from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class ProjectPaths:
    root: Path = PROJECT_ROOT
    raw_data: Path = PROJECT_ROOT / "data" / "raw"
    figures: Path = PROJECT_ROOT / "reports" / "figures"


PATHS = ProjectPaths()
