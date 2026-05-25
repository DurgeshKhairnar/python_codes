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



# df["Phone"] = pd.to_numeric(
#     df["Phone"],
#     errors="coerce"
# )

# convert the NaN to 0

# df['Phone'] = df['Phone'].replace(np.nan,1234567890)
# print(df)

# print("Find valid 10-digit phone numbers") 
# for i in df["Phone"]:
#  if not re.findall(r"\d{10}",i):
#   print(i)

print(df)

print("Find cities containing numbers")
for i in df['City']:
 if re.findall('\d',i):
  print(i)

print("Find cities containing special characters")  
for i in df["City"]:
    if re.findall(r"[^a-zA-Z0-9]",i):
      print(i)

# print("Replace special characters from Name column")
# df['Name']  = df["Name"].replace(r"[^a-zA-Z0-9]"," ")
# print(df["Name"]) 

# print("Extract only numbers from Phone column")
# for i in df["Phone"]:
#   if i in r"\d":
#     print(i)

print("Convert Salary to integer")
df["Salary"] = pd.to_numeric(
    df["Salary"],
    errors="coerce"
)
print(df["Salary"].dtype)


print("Find names starting with A" )
print(df[df['Name'].str.startswith("A")])

print("Find emails ending with gmail.com")
print(df[df['Email'].str.endswith("gmail.com")])

print("Find rows where Salary > 55000")
print(df[df['Salary'] > 55000])

print("Create new column:")
df['Bonus'] = df['Salary'] * 0.1
print(df)

print("Sort by Salary descending")
df["Salary"].sort_values(ascending=False)
print(df)

print("Group by City and find average Salary")
print(df.groupby("City")['Salary'].mean())

# print("Remove duplicate rows")
# df.drop_duplicates()

# print("""Rename column "Salary" to "Income""")
# df.rename([df["Salary"] = "Income"])

print("Check data types")
print(df.dtypes)