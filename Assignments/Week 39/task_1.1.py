from pathlib import Path

import pandas as pd

# Define paths relative to this script so it works from any terminal working directory.
SCRIPT_DIR = Path(__file__).resolve().parent
input_csv = SCRIPT_DIR / "psa_clinical_data.csv"
project_root = SCRIPT_DIR / "project_root"

if not input_csv.exists():
    raise FileNotFoundError(
        f"Input dataset not found at '{input_csv}'. "
        "Make sure 'psa_clinical_data.csv' is in the same folder as this script."
    )

# Load and prepare data
df = pd.read_csv(input_csv)

df["surgery_date"] = pd.to_datetime(df["surgery_date"])
df["psa_date"] = pd.to_datetime(df["psa_date"])

# Zero-pad patient_id to 3 digits for logical sorting
df["patient_id_padded"] = df["patient_id"].astype(str).str.zfill(3)
df["unique_id"] = df["study_id"].astype(str) + "_" + df["patient_id_padded"]

# Group by study to process each study directory
for study_id, study_group in df.groupby("study_id"):
    study_dir = project_root / str(study_id)
    study_dir.mkdir(parents=True, exist_ok=True)

    summary_rows = []

    # Group by patient within the current study
    for (p_id, u_id), patient_group in study_group.groupby(
        ["patient_id", "unique_id"]
    ):
        patient_dir = study_dir / u_id
        patient_dir.mkdir(parents=True, exist_ok=True)

        # 1. Save patient follow-up records sorted chronologically by psa_date
        patient_records = patient_group.sort_values("psa_date").drop(
            columns=["patient_id_padded"]
        )
        patient_file_path = patient_dir / f"{u_id}_followup.csv"
        patient_records.to_csv(patient_file_path, index=False)

        # 2. Compute patient summary fields
        dob = patient_group["date_of_birth"].iloc[0]
        surg_date = patient_group["surgery_date"].iloc[0]
        max_psa_date = patient_group["psa_date"].max()

        follow_up_days = (max_psa_date - surg_date).days
        num_measurements = len(patient_group)
        relative_patient_path = patient_dir.relative_to(project_root)

        summary_rows.append(
            {
                "unique_id": u_id,
                "date_of_birth": dob,
                "surgery_date": surg_date.strftime("%Y-%m-%d"),
                "follow_up_days": follow_up_days,
                "number_of_psa_measurements": num_measurements,
                "patient_folder_path": str(relative_patient_path),
            }
        )

    # 3. Create and save the study summary CSV
    summary_df = pd.DataFrame(summary_rows)
    summary_df.sort_values("unique_id", inplace=True)
    summary_file_path = study_dir / f"{study_id}_summary.csv"
    summary_df.to_csv(summary_file_path, index=False)

