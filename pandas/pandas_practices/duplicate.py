import pandas as pd
import numpy as np
import re

# ---------------------------
# Missing Values
# ---------------------------

print("Count missing values")
print(df.isnull().sum())

print("Fill missing Name with Unknown")
df["Name"] = df["Name"].fillna("Unknown")

print("Fill missing Department with mode")
df["Department"] = df["Department"].fillna(
    df["Department"].mode()[0]
)

print("Fill missing Salary with mean")
df["Salary"] = df["Salary"].fillna(
    df["Salary"].mean()
)

print("Fill missing Experience with median")
df["Experience"] = df["Experience"].fillna(
    df["Experience"].median()
)

# ---------------------------
# Duplicate Data
# ---------------------------

print("Find duplicate rows")
print(df[df.duplicated()])

print("Remove duplicate rows")
df = df.drop_duplicates()

print("Check duplicates again")
print(df[df.duplicated()])

# ---------------------------
# String Cleaning
# ---------------------------

print("Remove spaces from Name")
df["Name"] = df["Name"].str.strip()

print("Remove spaces from City")
df["City"] = df["City"].str.strip()

print("Convert Name to Title Case")
df["Name"] = df["Name"].str.title()

print("Convert Department to Uppercase")
df["Department"] = df["Department"].str.upper()

# ---------------------------
# Email Validation
# ---------------------------

print("Find invalid emails")
print(
    df[
        ~df["Email"].str.match(
            r"^[\w\.-]+@[\w\.-]+\.\w+$",
            na=False
        )
    ]
)

print("Create Email_Status")
df["Email_Status"] = np.where(
    df["Email"].str.match(
        r"^[\w\.-]+@[\w\.-]+\.\w+$",
        na=False
    ),
    "Valid",
    "Invalid"
)

print(df[["Email", "Email_Status"]])

print("Replace invalid emails")
df["Email"] = np.where(
    df["Email"].str.match(
        r"^[\w\.-]+@[\w\.-]+\.\w+$",
        na=False
    ),
    df["Email"],
    "Invalid"
)

# ---------------------------
# Phone Validation
# ---------------------------

print("Find invalid phones")
print(
    df[
        ~df["Phone"].str.match(
            r"^\d{10}$",
            na=False
        )
    ]
)

print("Create Phone_Status")
df["Phone_Status"] = np.where(
    df["Phone"].str.match(
        r"^\d{10}$",
        na=False
    ),
    "Valid",
    "Invalid"
)

print(df[["Phone", "Phone_Status"]])

print("Replace invalid phones")
df["Phone"] = np.where(
    df["Phone"].str.match(
        r"^\d{10}$",
        na=False
    ),
    df["Phone"],
    "Unknown"
)

# ---------------------------
# Regex Cleaning
# ---------------------------

print("Remove special chars from Name")
df["Name"] = df["Name"].str.replace(
    r"[^a-zA-Z0-9 ]",
    "",
    regex=True
)

print(df["Name"])

print("Remove numbers from City")
df["City"] = df["City"].str.replace(
    r"\d",
    "",
    regex=True
)

print(df["City"])

print("Remove special chars from City")
df["City"] = df["City"].str.replace(
    r"[^a-zA-Z ]",
    "",
    regex=True
)

print(df["City"])

# ---------------------------
# Data Types
# ---------------------------

print("Check data types")
print(df.dtypes)

print("Convert Salary to numeric")
df["Salary"] = pd.to_numeric(
    df["Salary"],
    errors="coerce"
)

print("Convert Experience to numeric")
df["Experience"] = pd.to_numeric(
    df["Experience"],
    errors="coerce"
)

# ---------------------------
# Salary Outliers
# ---------------------------

print("Negative Salary")
print(df[df["Salary"] < 0])

print("Salary > 500000")
print(df[df["Salary"] > 500000])

print("Replace negative salary with NaN")
df.loc[
    df["Salary"] < 0,
    "Salary"
] = np.nan

median_salary = df["Salary"].median()

print("Replace extreme salary with median")
df.loc[
    df["Salary"] > 500000,
    "Salary"
] = median_salary

# ---------------------------
# Experience Cleaning
# ---------------------------

print("Negative Experience")
print(df[df["Experience"] < 0])

median_exp = df["Experience"].median()

print("Replace negative experience")
df.loc[
    df["Experience"] < 0,
    "Experience"
] = median_exp

print("Experience > 15")
print(df[df["Experience"] > 15])

print("Replace experience > 15")
df.loc[
    df["Experience"] > 15,
    "Experience"
] = median_exp

# ---------------------------
# Analysis
# ---------------------------

print("Average Salary Department-wise")
print(
    df.groupby("Department")["Salary"]
      .mean()
)

print("Employee Count City-wise")
print(
    df.groupby("City")["EmpID"]
      .count()
)

print("Highest Paid Employee")
print(
    df.loc[
        df["Salary"].idxmax()
    ]
)

print("Lowest Paid Employee")
print(
    df.loc[
        df["Salary"].idxmin()
    ]
)

print("Average Experience Department-wise")
print(
    df.groupby("Department")["Experience"]
      .mean()
)

print("Top 3 Highest Salaries")
print(
    df.nlargest(
        3,
        "Salary"
    )
)

# ---------------------------
# Final Report
# ---------------------------

print("Create Bonus")
df["Bonus"] = df["Salary"] * 0.10

print("Create Tax")
df["Tax"] = df["Salary"] * 0.05

print("Create NetSalary")
df["NetSalary"] = (
    df["Salary"]
    + df["Bonus"]
    - df["Tax"]
)

print(df)

# ---------------------------
# Save Cleaned Data
# ---------------------------

df.to_csv(
    "cleaned_employee_data.csv",
    index=False
)

print("File Saved Successfully")