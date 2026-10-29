import csv
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def process_sequencing_data(
    seq_folder_path: str,
    output_manifest_path: str = "sequencing_manifest.csv",
):
    """Iterates through sequencing files in `seq_folder_path`, parses header lines

    starting with '##', extracts study_id and patient_id, and writes a
    summary CSV manifest.
    """
    seq_folder = Path(seq_folder_path).resolve()
    output_path = (SCRIPT_DIR / output_manifest_path).resolve()

    # Check if folder exists to avoid FileNotFoundError
    if not seq_folder.exists():
        raise FileNotFoundError(
            f"Directory '{seq_folder_path}' was not found. "
            "Please create the folder or provide the correct path to your sequencing files."
        )

    manifest_rows = []

    # Iterate through files in the sequencing directory
    for file_path in seq_folder.iterdir():
        if not file_path.is_file():
            continue

        study_id = None
        patient_id = None

        # Read line-by-line efficiently to handle large gigabyte-scale files
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                # Stop reading immediately once header lines (##) end
                if not line.startswith("##"):
                    break

                # Clean line content
                clean_line = line.strip().lstrip("#")

                # Parse key-value pairs (e.g., study_id = A12 or study_id=A12)
                if "=" in clean_line:
                    key, val = clean_line.split("=", 1)
                    key = key.strip().lower()
                    val = val.strip().strip("$")  # Handle formatted inputs

                    if key == "study_id":
                        study_id = val
                    elif key == "patient_id":
                        patient_id = val

        # Append to manifest if both IDs were identified
        if study_id and patient_id:
            # Consistent unique_id generation matching Task 1 logic
            try:
                p_id_int = int(patient_id)
                unique_id = f"{study_id}_{p_id_int:03d}"
            except ValueError:
                unique_id = f"{study_id}_{patient_id}"

            # Calculate a stable relative path; if the input directory is not under
            # the project root, fall back to the directory-local filename.
            if file_path.is_relative_to(seq_folder):
                relative_path = file_path.relative_to(seq_folder).as_posix()
            else:
                relative_path = file_path.as_posix()

            manifest_rows.append(
                {
                    "unique_id": unique_id,
                    "study_id": study_id,
                    "patient_id": patient_id,
                    "sequencing_file_path": relative_path,
                }
            )

    # Write output CSV file
    fieldnames = [
        "unique_id",
        "study_id",
        "patient_id",
        "sequencing_file_path",
    ]
    with open(output_path, "w", newline="", encoding="utf-8") as out_file:
        writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(manifest_rows)


if __name__ == "__main__":
    # Ensure folder exists prior to running
    raw_dir = SCRIPT_DIR / "raw_sequencing_data"
    raw_dir.mkdir(parents=True, exist_ok=True)

    process_sequencing_data(
        seq_folder_path=str(raw_dir),
        output_manifest_path="sequencing_manifest.csv",
    )