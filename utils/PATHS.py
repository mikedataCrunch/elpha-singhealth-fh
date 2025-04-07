from dotenv import load_dotenv
import os, sys

from dotenv import load_dotenv
load_dotenv("../.env")  # take environment variables
PROJECT_ROOT = os.environ.get("PROJECT_ROOT")

DATA_ROOT = os.path.join(PROJECT_ROOT, "data", "processed")

LABS = os.path.join(DATA_ROOT, "1 Lab General")
DIAGNOSIS = os.path.join(DATA_ROOT, "2 Diagnosis")
DRUG_DISPENSED = os.path.join(DATA_ROOT, "3 Drug Dispensed")
PROBLEM_LIST = os.path.join(DATA_ROOT, "4 Problem List")
