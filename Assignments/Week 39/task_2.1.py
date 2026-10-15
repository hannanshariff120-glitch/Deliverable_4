import os
import pandas as pd

def process_sequencing_files(seq_dir: str, root_dir: str) -> None:
    manifest_rows = []

    for filename in os.listdir(seq_dir):
        file_path = os.path.join(seq_dir, filename)

        if not os.path.isfile(file_path) or filename.startswith("."):
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
                        study_id = value
                    elif key == "patient_id":
                        patient_id = int(value)

        if study_id is not None and patient_id is not None:
            unique_id = f"{study_id}_{patient_id:03d}"
            rel_seq_path = os.path.join(seq_dir, filename)

            manifest_rows.append({
                "unique_id": unique_id,
                "study_id": study_id,
                "patient_id": patient_id,
                "sequencing_file_path": rel_seq_path
            })

    manifest_df = pd.DataFrame(manifest_rows)
    if not manifest_df.empty:
        manifest_df = manifest_df.sort_values("unique_id")

    manifest_path = os.path.join(root_dir, "sequencing_manifest.csv")
    manifest_df.to_csv(manifest_path, index=False)
    print(f"Task 2 complete! Saved manifest to: {manifest_path}")

if __name__ == "__main__":
    SEQ_DATA_DIR = "raw_sequencing_data"
    PROJECT_ROOT = "prostate_cancer_project"
    os.makedirs(PROJECT_ROOT, exist_ok=True)
    process_sequencing_files(SEQ_DATA_DIR, PROJECT_ROOT)

