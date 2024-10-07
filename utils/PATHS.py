import os

DATA_ROOT = "/Users/mdorosan/Desktop/2024/datasets" # local_mac
DATA_DIR = os.path.join(DATA_ROOT, "elpha-fh")

# DATA_ROOT = "/mnt/d/PROJECT_ELPHA" # hsrc_michael
# DATA_DIR = os.path.join(DATA_ROOT, "FH/raw")

# LABS = os.path.join(DATA_DIR, "1 Lab General")
# DIAGNOSIS = os.path.join(DATA_DIR, "2 Diagnosis")
# DRUG_DISPENSED = os.path.join(DATA_DIR, "3 Drug Dispensed")
# PROBLEM_LIST = os.path.join(DATA_DIR, "4 Problem List")

LABS = os.path.join(DATA_DIR, "1 Lab General")
DIAGNOSIS = os.path.join(DATA_DIR, "2 Diagnosis (with HtWtBMI)")
PROBLEM_LIST = os.path.join(DATA_DIR, "4 Problem List")
# DIAGNOSIS = os.path.join(DATA_DIR, "2 Diagnosis")
DRUG_DISPENSED = os.path.join(DATA_DIR, "3 Drug_Dispensed_Subject")
