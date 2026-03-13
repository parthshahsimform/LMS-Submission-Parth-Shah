import pandas as pd
import numpy as np
import logging
import os
from datetime import datetime

# create logs folder
log_folder = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(log_folder, exist_ok=True)

# define log file path
log_path = os.path.join(log_folder, "employee.log")

# configure logging
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

# load employee dataset
data_path = os.path.join(os.path.dirname(__file__), "employees.csv")
df = pd.read_csv(data_path, parse_dates=["Joining_Date"])

logger.info(f"Dataset loaded successfully with {len(df)} records")

print("\nSample Data:")
print(df.head())

# check missing values
missing_values = df.isnull().sum()
logger.info(f"Missing values:\n{missing_values}")

# fill missing age with median
if "Age" in df.columns:
    median_age = df["Age"].median()
    df["Age"].fillna(median_age)
    logger.info(f"Filled missing Age with median {median_age}")

# fill missing salary with mean
if "Salary" in df.columns:
    mean_salary = df["Salary"].mean()
    df["Salary"].fillna(mean_salary)
    logger.info(f"Filled missing Salary with mean {mean_salary}")

# remove duplicate employee records
before = len(df)
df.drop_duplicates(subset=["Employee_ID"], inplace=True)
removed = before - len(df)

logger.info(f"Removed {removed} duplicate records")

# standardize column names
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

# convert column data types
df["age"] = df["age"].round().astype(int)
df["salary"] = df["salary"].astype(float)
df["resigned"] = df["resigned"].astype(bool)
df["joining_date"] = pd.to_datetime(df["joining_date"])

logger.info("Data cleaning completed")

# function to filter and manipulate employee data
def manipulate_data(dataframe):

    logger.info("Starting data manipulation")

    before_count = len(dataframe)

    filtered_df = dataframe[
        ((dataframe["age"] > 25) | (dataframe["salary"] > 40000)) &
        (dataframe["resigned"] == False)
    ].copy()

    after_count = len(filtered_df)

    logger.info(f"Records before filtering {before_count}")
    logger.info(f"Records after filtering {after_count}")

    today = pd.Timestamp(datetime.today())

    filtered_df["years_in_company"] = (
        (today - filtered_df["joining_date"]).dt.days / 365
    ).astype(int)

    logger.info("Years in company column created")

    return filtered_df


# function to analyze department statistics
def analyze_data(dataframe, department="IT"):

    logger.info("Starting data analysis")

    stats = dataframe.groupby("department").agg(
        average_salary=("salary", "mean"),
        median_age=("age", "median")
    )

    print("\nDepartment Insights:")
    print(stats)

    logger.info("Department statistics calculated")

    dataframe.loc[dataframe["department"] == department, "salary"] *= 1.10

    logger.info(f"10 percent salary increment applied to {department}")

    return dataframe, stats


# run data manipulation
df = manipulate_data(df)

# run data analysis
df, stats = analyze_data(df)

# rename columns for final output
df = df.rename(columns={
    "employee_id": "Employee_ID",
    "emp_name": "Name",
    "department": "Department",
    "years_in_company": "YearsInCompany",
    "joining_date": "JoiningDate",
    "age": "Age",
    "salary": "Salary"
})

# keep only required columns
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

# sort employees by joining date
df = df.sort_values(by="JoiningDate", ascending=False)

# export final dataset to json
output_file = os.path.join(os.path.dirname(__file__), "final_employee_data.json")

df.to_json(output_file, orient="records", indent=4)

logger.info(f"Data exported successfully to {output_file}")
logger.info(f"Total records exported {len(df)}")

print("\nFinal dataset exported successfully.")
