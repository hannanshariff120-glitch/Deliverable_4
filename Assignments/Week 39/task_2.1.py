import os
from pathlib import Path

import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parent
SEQ_DATA_DIR = SCRIPT_DIR / "raw_sequencing_data"
PROJECT_ROOT = SCRIPT_DIR / "project_root"


def process_sequencing_files(seq_dir: str | os.PathLike, root_dir: str | os.PathLike) -> None:
    manifest_rows = []
    seq_dir = Path(seq_dir).resolve()
    root_dir = Path(root_dir).resolve()

    if not seq_dir.exists():
        raise FileNotFoundError(
            f"Sequencing directory '{seq_dir}' does not exist. "
            "Create it or pass a valid path to the function."
        )

    for filename in os.listdir(seq_dir):
        file_path = seq_dir / filename

        if not file_path.is_file() or filename.startswith("."):
            continue

        study_id = None
        patient_id = None

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.startswith("##"):
                    break

                clean_line = line.strip().lstrip("#")
                if "=" in clean_line:
                    key, value = clean_line.split("=", 1)
                    if key == "study_id":
                        study_id = value.strip()
                    elif key == "patient_id":
                        patient_id = int(value.strip())

        if study_id is not None and patient_id is not None:
            unique_id = f"{study_id}_{patient_id:03d}"
            if file_path.is_relative_to(root_dir):
                rel_seq_path = file_path.relative_to(root_dir)
            else:
                rel_seq_path = file_path.relative_to(seq_dir)

            manifest_rows.append(
                {
                    "unique_id": unique_id,
                    "study_id": study_id,
                    "patient_id": patient_id,
                    "sequencing_file_path": str(rel_seq_path),
                }
            )

    manifest_df = pd.DataFrame(manifest_rows)
    if not manifest_df.empty:
        manifest_df = manifest_df.sort_values("unique_id")

    root_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = root_dir / "sequencing_manifest.csv"
    manifest_df.to_csv(manifest_path, index=False)
    print(f"Task 2 complete! Saved manifest to: {manifest_path}")


if __name__ == "__main__":
    PROJECT_ROOT.mkdir(parents=True, exist_ok=True)
    process_sequencing_files(SEQ_DATA_DIR, PROJECT_ROOT)

