import os

import pandas as pd


#Step 1: creating the unique_id
study_id = "A12"
patient_id = 1

# Step 2: Adding :03d to zero-pad patient_id to 3 digits
unique_id = f"{study_id}_{patient_id:03d}"
print(unique_id)  # The output should be A12_001
# Loading the CSV file into a DataFrame
df = pd.read_csv('psa_clinical_data.csv')    
#Printing the first 5 rows of the DataFrame
print(df.head())

df["surgery_date"] = pd.to_datetime(df["surgery_date"], format='%Y-%m-%d', errors='coerce')
df["psa_date"] = pd.to_datetime(df["psa_date"], format='%Y-%m-%d', errors='coerce')

# Step 3:Generating zero-padded unique_id for each row in the DataFrame
df["unique_id"] = df.apply(
    lambda row: f"{study_id}_{row['patient_id']:03d}", axis=1)

# Inspect updated dataframe with unique_id
print(df[["study_id", "patient_id", "unique_id", "surgery_date", "psa_date"]].head())

# Step 4: Calculating the difference in days between surgery_date and psa_date
df["days_difference"] = (df["psa_date"] - df["surgery_date"]).dt.days           

# Step 5: Define project root folder
ROOT_DIR = "/path/to/project/root"  # Replace with your actual project root path
os.makedirs(ROOT_DIR, exist_ok=True)




