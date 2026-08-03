import os
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import hf_hub_download

from ideias_em_rede.config import PATHS


DATASET_REPOSITORY_ID = "unicamp-dl/PublicHearingBR"
LDS_FILENAME = "PublicHearingBR_LDS.jsonl"
NLI_FILENAME = "PublicHearingBR_NLI.jsonl"


def download_lds_dataset(destination: str | Path | None = None) -> Path:
    return download_dataset_file(LDS_FILENAME, destination)


def download_nli_dataset(destination: str | Path | None = None) -> Path:
    return download_dataset_file(NLI_FILENAME, destination)


def download_dataset_file(
    filename: str,
    destination: str | Path | None = None,
) -> Path:
    load_dotenv(PATHS.root / ".env")
    destination_dir = Path(destination) if destination else PATHS.raw_data
    destination_dir.mkdir(parents=True, exist_ok=True)
    dataset_path = destination_dir / filename

    if dataset_path.is_file() and dataset_path.stat().st_size > 0:
        return dataset_path

    token = os.getenv("HF_TOKEN") or None
    downloaded_path = hf_hub_download(
        repo_id=DATASET_REPOSITORY_ID,
        filename=filename,
        repo_type="dataset",
        token=token,
        local_dir=destination_dir,
        force_download=dataset_path.exists(),
    )
    return Path(downloaded_path)
