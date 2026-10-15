from pathlib import Path

import pandas as pd


def generate_sequencing_manifest(raw_seq_dir, project_root):
    manifest_rows = []
    raw_seq_path = Path(raw_seq_dir)
    project_root_path = Path(project_root)

    # Iterating through all files in the sequencing directory
    for file_path in raw_seq_path.rglob("*"):
        if not file_path.is_file():
            continue

        study_id = None
        patient_id = None

        # Reading the file line-by-line to parse header
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                # Stop reading immediately when the header ends
                if not line.startswith("##"):
                    break

                # Extract study_id and patient_id
                if "study_id" in line:
                    study_id = line.split("=")[-1].strip()
                elif "patient_id" in line:
                    patient_id = line.split("=")[-1].strip()

        # Generate manifest entry if both IDs were extracted
        if study_id and patient_id:
            patient_id_padded = str(patient_id).zfill(3)
            unique_id = f"{study_id}_{patient_id_padded}"
            rel_seq_path = file_path.relative_to(project_root_path)

            manifest_rows.append(
                {
                    "unique_id": unique_id,
                    "study_id": study_id,
                    "patient_id": patient_id,
                    "sequencing_file_path": str(rel_seq_path),
                }
            )

    # Saving sequencing_manifest.csv in the main project folder
    manifest_df = pd.DataFrame(manifest_rows)
    manifest_df.sort_values("unique_id", inplace=True)
    manifest_output_path = project_root_path / "sequencing_manifest.csv"
    manifest_df.to_csv(manifest_output_path, index=False)


# Example usage:
generate_sequencing_manifest("project_root/raw_sequencing_data", "project_root")