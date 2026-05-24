import pandas as pd
import numpy as np
import re

df = pd.DataFrame({
    "ID": [101, 102, 103, 104, 105, 106],
    
    "Name": [
        "Amit Kumar",
        "Sara_123",
        "John@Doe",
        "Riya Sharma",
        np.nan,
        "Neha99"
    ],

    "Email": [
        "amit@gmail.com",
        "sara@yahoo.com",
        "wrong_email",
        "riya123@gmail.com",
        "neha#gmail.com",
        np.nan
    ],

    "Phone": [
        "9876543210",
        "9123456780",
        "12345",
        "8888888888",
        np.nan,
        "98765abcd0"
    ],

    "City": [
        "Pune",
        "Mumbai123",
        "Delhi",
        "Nagpur@",
        np.nan,
        "Chennai"
    ],

    "Salary": [
        50000,
        60000,
        np.nan,
        75000,
        58000,
        52000
    ]
})

print(df)

print("Show first 3 rows")
print(df.head(3))

print("Find missing values")
print(df.isnull().sum())

print("Fill missing Salary with mean")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)

print("Fill missing text columns with Unknown")
df[["Name","Email","City"]] = (df[["Name","Email","City"]].fillna("Unknown"))
print(df)

# print("Find names containing numbers")
# for i in df["Name"]:
#  print(re.findall(r".\d",i))

# print("Find names containing special characters")
# for i in df["Name"]:
#  print(re.findall(r"[^a-zA-z0-9]",i))

# print("Find valid emails")
# for i in df["Email"]:
#  print(re.findall(r"^[\w\.-]+@[\w\.-]+\.\w+$",i))

print("Find invalid emails")
for i in df["Email"]:
 if not re.search(r"^[\w\.-]+@[\w\.-]+\.\w+$",i):
  print(i)
    