import pandas as pd
import numpy as np
import re


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

# print("Rename Salary → Income")
# df = df.rename(
#     columns = {"Salary":"Income"}
# )
# print(df)

# print("Remove Experience column")
# df = df.drop("Experience",axis=1)
# print(df)

print("Reset index")
df = df.reset_index(drop=True)
print(df)

print("Remove duplicate rows")
df.drop_duplicates(inplace=True)
print(df)

# Filtering

print("Find Salary > 60000")
print(df[df["Salary"] > 60000])

print("Find employees from Pune")
print(df[df["City"] == 'Pune'])

print("Find employees from IT department")
print(df[df["Department"] == 'IT'])

print("Find Salary between 50000 and 70000")
print(df[(df["Salary"] > 50000) & (df["Salary"] < 70000)])

print("Find employees with Experience > 3")
print(df[df['Experience'] > 3])

print("Find rows where: Salary > 50000 AND Department = IT")
print(df[(df["Salary"] > 50000) & (df["Department"] == 'IT')])

print("Find rows where: City = Pune OR City = Delhi")
print(df[(df["City"] == "Pune") | (df["City"] == 'City')])

print("Sort by Salary ascending")
df = df.sort_values("Salary")
print(df)

print('Sort by Salary descending')
df = df.sort_values("Salary",ascending=False)
print(df)

print("Sort by Department and Salary")
df = df.sort_values(["Salary","Department"])
print(df)

# Grouping
print("Find average salary department-wise")
print(df.groupby("Department")['Salary'].mean())

print("Find maximum salary city-wise")
print(df.groupby("City")['Salary'].max())

print("Find employee count department-wise")
print(df.groupby("Department")['Name'].count())

print("Find total salary department-wise")
print(df.groupby("Department")['Salary'].sum())

#Regex Practice

print("Find names containing numbers")
for i in df["Name"]:
    if re.findall(r"\d",i):
        print(i)

print("Find names containing special characters")
for i in df["Name"]:
    if re.search(r"[^a-zA-z0-9]",i):
        print(i)       

# print("Find valid emails") 
# for i in df["Email"]:
#     if re.search(r"^[]",i):
#         print(i)  

print("Find valid 10-digit phone numbers")
for i in df["Phone"]:
     if re.findall(r"\d{10}",i):
         print(i)       

print("Find invalid phone numbers")
for i in df["Phone"]:
     if not re.findall(r"\d{10}",i):
         print(i)           
      
         
print("Find cities containing numbers")
for i in df["City"]:
    if re.findall(r"\d",i):
        print(i)         

print("Find cities containing special characters")
for i in df["City"]:
    if re.findall(r"[^a-zA-Z0-9]",i):
        print(i)

print("Find names starting with A")
print(df[df["Name"].str.startswith("A")])  

print("Find emails ending with gmail.com")
print(df[df["Email"].str.endswith("gmail.com")])

# print("Remove special characters from Name")
# for i in df["Name"]:
#     if re.   give me the answer

# print("Create Email_Status column")
# df["Email_Status"] = df['Email_Status'].

print("Convert Name column to uppercase")
df['Name'] =  df['Name'].str.upper()
print(df)

print("Convert Department to lowercase")
df["Department"] = df["Department"].str.lower()
print(df)

print("Replace Pune with Mumbai")
df["City"] = df["City"].replace("Pune","Mumbai")
print(df["City"])

# print("Count total characters in Name")
# count = 0            
# for i in df['Name']:
#     for j in i:
#      if re.match(r"^[a-zA-z]",j):
#         print(j)
#         count +=1

# print(count)       

# File handling

print("Save dataframe to CSV")
df.to_csv("emp.csv")

print("Read CSV again")
readFile =  pd.read_csv("emp.csv")
print(readFile)

# Advanced Practice
print("Convert Salary to integer")
df["Salary"] = df['Salary'].astype(int)
print(df["Salary"].dtype)

print("Replace invalid phone numbers with Unknown")
for i in df['Phone']:
    if not re.search(r"\d{10}",i):
        df["Phone"] = df["Phone"].replace(i,"Unknown")


print(df["Phone"])  


print("Replace invalid emails with Invalid")
for i in df['Email']:
    if not re.search(r"^[\w\.-]+@[\w\.-]+\.\w+$",i):
        df["Email"] = df["Email"].replace(i,"Invalid")

print(df)  

print("Create Tax column")
df["Tax"] = df["Salary"] * 0.5
print(df)


print("Find lowest salary employee")
print(df['Salary'].min())

print("Find average experience department-wise")
print(df.groupby("Department")["Salary"].mean())


print("Most comman city")
print(df['City'].mode())

print("find mising value")
print(df.isnull().sum())

print("fill missing text column")
txt_cols = ["Name","Email","Department","City"]
df[txt_cols] = df[txt_cols].fillna("Missing")
print(df[txt_cols])

print("lowest Salary Employee")
print(df[df["Salary"] == df["Salary"].min()])

print("Count Total Character")
df["Name_length"] = df["Name"].str.len()
print(df[["Name","Name_length"]])

print("Remove special Character from name")
df['Name'] = df["Name"].str.replace(
    r"[^a-zA-Z0-9]",
    "",
    regex=True
)
print(df['Name'])


print("Top 3 hight Salary Employee")
print(df.nlargest(3,"Salary"))

print("Count Unique Cities")
print(df["City"].nunique())

print("Email Status")
df["Email_Status"] = np.where(
    df["Email"].str.match(
        r"^[\w\.-]+@[\w\.-]+\.\w+$",
        na=False
    ),
    "valid",
    "Invalid"
)

print(df[["Email","Email_Status"]])

print("Remove invalid email row")
df = df[
    df["Email"].str.match(
        r"^[\w\.-]+@[\w\.-]+\.\w+$",
        na=False
    )
]

print(df)