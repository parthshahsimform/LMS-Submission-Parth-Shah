import pandas as pd
import numpy as np
import logging
import os
from datetime import datetime

# Setup Logging

log_folder = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(log_folder, exist_ok=True)

log_path = os.path.join(log_folder, "employee.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Program started")

# Task 1 : Load Employee Dataset

logger.info("Loading employee dataset")

df = pd.read_csv("employees.csv", parse_dates=["Joining_Date"])

logger.info(f"Dataset loaded successfully. Total records: {len(df)}")

print("\nSample Data:")
print(df.head())

# Task 2 : Data Cleaning

logger.info("Starting data cleaning process")

# Check missing values
missing_values = df.isnull().sum()
logger.info(f"Missing values:\n{missing_values}")

# Fill missing Age with median
if "Age" in df.columns:
    median_age = df["Age"].median()
    df["Age"].fillna(median_age, inplace=True)
    logger.info(f"Missing Age values filled with median: {median_age}")

# Fill missing Salary with mean
if "Salary" in df.columns:
    mean_salary = df["Salary"].mean()
    df["Salary"].fillna(mean_salary, inplace=True)
    logger.info(f"Missing Salary values filled with mean: {mean_salary}")

# Remove duplicate employees
before = len(df)
df.drop_duplicates(subset=["Employee_ID"], inplace=True)

removed = before - len(df)
logger.info(f"Removed {removed} duplicate records")

# Standardize column names
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

# Convert datatypes
df["age"] = df["age"].astype(int)
df["salary"] = df["salary"].astype(float)
df["resigned"] = df["resigned"].astype(bool)
df["joining_date"] = pd.to_datetime(df["joining_date"])

logger.info("Data cleaning completed")

# Task 3 : Data Manipulation

def manipulate_data(dataframe):

    logger.info("Starting data manipulation")

    try:
        original_count = len(dataframe)

        # Filter employees based on conditions
        filtered_df = dataframe[
            ((dataframe["age"] > 25) | (dataframe["salary"] > 40000)) &
            (dataframe["resigned"] == False)
        ].copy()

        filtered_count = len(filtered_df)

        logger.info(f"Records before filtering: {original_count}")
        logger.info(f"Records after filtering: {filtered_count}")

        # Calculate years in company
        today = pd.Timestamp(datetime.today())

        filtered_df["years_in_company"] = (
            (today - filtered_df["joining_date"]).dt.days / 365
        ).astype(int)

        logger.info("Years in company column created")

        return filtered_df

    except Exception as error:
        logger.error(f"Error during data manipulation: {error}")
        raise

# Task 4 : Data Analysis

def analyze_data(dataframe, department="IT"):

    logger.info("Starting data analysis")

    try:

        # Calculate department statistics
        department_stats = dataframe.groupby("department").agg(
            average_salary=("salary", "mean"),
            median_age=("age", "median")
        )

        print("\nDepartment Insights:")
        print(department_stats)

        logger.info("Department statistics calculated")

        # Apply salary increment for selected department
        dataframe.loc[
            dataframe["department"] == department,
            "salary"
        ] *= 1.10

        logger.info(f"10% salary increment applied to {department} department")

        return dataframe, department_stats

    except Exception as error:
        logger.error(f"Error during analysis: {error}")
        raise


# Run manipulation
df = manipulate_data(df)

# Run analysis
df, stats = analyze_data(df)

# Task 5 : Export Final Data

logger.info("Preparing final dataset for export")

df = df.rename(columns={
    "employee_id": "Employee_ID",
    "emp_name": "Name",
    "department": "Department",
    "years_in_company": "YearsInCompany",
    "joining_date": "JoiningDate",
    "age": "Age",
    "salary": "Salary"
})

# Select important columns
df = df[
    [
        "Employee_ID",
        "Name",
        "Age",
        "Department",
        "Salary",
        "YearsInCompany",
        "JoiningDate"
    ]
]

# Sort by joining date
df = df.sort_values(by="JoiningDate", ascending=False)

# Export to JSON
output_file = "final_employee_data.json"

df.to_json(output_file, orient="records", indent=4)

logger.info(f"Data exported successfully to {output_file}")
logger.info(f"Total records exported: {len(df)}")

print("\nFinal dataset exported successfully.")
