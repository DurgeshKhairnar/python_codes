import pandas as pd
import numpy as np


# ord = pd.DataFrame({
#     "OrderID": [1001, 1002, 1003, 1004, 1005, 1006],
#     "Customer": ["Amit", "Sara", np.nan, "Riya", "Karan", "Neha"],
#     "Product": ["Laptop", "Mobile", "Tablet", np.nan, "Laptop", "Mobile"],
#     "Price": [55000, 20000, np.nan, 15000, 60000, 22000],
#     "Quantity": [1, 2, 1, np.nan, 1, 3],
#     "City": ["Pune", "Mumbai", "Delhi", "Pune", np.nan, "Mumbai"]
# })

# pay = pd.DataFrame({
#     "OrderID": [1001, 1002, 1003, 1007],
#     "PaymentMode": ["UPI", "Card", "Cash", "UPI"],
#     "Status": ["Success", "Success", "Pending", "Success"]
# })

# # print("find the order without paymnet")
# # print(pay[pay["Salary"].isnull()])

# # print("delete row")
# # ord = ord.drop(0)
# # print(ord)

# # print("reset index")
# # ord = ord.reset_index(drop=True)
# # print(ord)


# print("rename column name")
# # ord = ord.rename(
# #     columns = {
# #         "Price":"ProductPrice"
# #     }
# # )

# # print(ord)

# # print("convert quinty to integer")
# # ord["Quantity"] = ord["Quantity"].astype(int)
# # print(ord["Quantity"].dtype)

# print("Sort value price ")
# ord = ord.sort_values("Price")
# print(ord)

df = pd.DataFrame({

    "EmpID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110
    ],

    "Name": [
        "Amit Kumar",
        "Sara_123",
        "John@Doe",
        np.nan,
        "Riya Sharma",
        "Neha99",
        "Vikas",
        "Ankit#",
        "Pooja",
        "Rahul123"
    ],

    "Email": [
        "amit@gmail.com",
        "sara@yahoo.com",
        "wrong_email",
        "riya@gmail",
        np.nan,
        "neha123@gmail.com",
        "vikas@outlook.com",
        "ankit#gmail.com",
        "pooja@gmail.com",
        "rahul123@yahoo.in"
    ],

    "Phone": [
        "9876543210",
        "9123456780",
        "12345",
        np.nan,
        "8888888888",
        "98765abcd0",
        "9999999999",
        "777777777",
        "88888@8888",
        "9876540000"
    ],

    "Department": [
        "IT",
        "HR",
        "Finance",
        "IT",
        np.nan,
        "Marketing",
        "HR",
        "IT",
        "Finance",
        "Marketing"
    ],

    "City": [
        "Pune",
        "Mumbai123",
        "Delhi",
        "Nagpur@",
        np.nan,
        "Chennai",
        "Pune",
        "Mumbai",
        "Delhi1",
        "Hyd#"
    ],

    "Salary": [
        50000,
        60000,
        np.nan,
        75000,
        58000,
        52000,
        45000,
        np.nan,
        90000,
        61000
    ],

    "Experience": [
        2,
        5,
        np.nan,
        7,
        4,
        3,
        1,
        6,
        np.nan,
        2
    ]

})

print(df)

print("Show first 5 rows")
print(df.head(5))

print("Show last 3 rows")
print(df.tail(3))

print("Check shape")
print(df.shape)

print("Show column names")
print(df.columns)

print("Check data types")
print(df.dtypes)

print("Show dataset info")
print(df.info())

print("Show statistical summary")
print(df.describe())

print("Find missing values")
print(df.isnull().count())

print("Fill missing Salary with mean")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df["Salary"])

print("Fill missing Experience with median")
df["Experience"] = df["Experience"].fillna(df["Experience"].median())
print(df["Experience"])

# print("Fill missing text columns with Unknown")
df = df.replace(np.nan,"Unknown")
print(df)


# print("Remove rows with missing Name")
# df = df.drop()

# print("Add new column:")
df["Bonus"] = df["Salary"] * 0.20
print(df)

print("Rename Salary → Income")
df = df.rename(
    columns = {"Salary":"Income"}
)
print(df)

print("Remove Experience column")
df = df.drop("Experience",axis=1)
print(df)

print("Reset index")
df = df.reset_index(drop=True)
print(df)

print("Remove duplicate rows")
df = df.drop_duplicates(inplace=True)
print(df)