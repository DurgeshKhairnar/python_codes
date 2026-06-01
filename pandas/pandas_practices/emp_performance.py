import pandas as pd
import numpy as np
import re

df = pd.DataFrame({
    "EmpID": [101,102,103,104,105,106,107,108,109,110,111,112],

    "Name": [
        "Amit Kumar",
        "Sara_123",
        "John@Doe",
        "Riya Sharma",
        np.nan,
        "Neha99",
        "Vikas",
        "Ankit#",
        "Pooja",
        "Rahul123",
        "Priya",
        "Karan$"
    ],

    "Department": [
        "IT",
        "HR",
        "Finance",
        "IT",
        "Marketing",
        np.nan,
        "HR",
        "IT",
        "Finance",
        "Marketing",
        "HR",
        "IT"
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
        61000,
        55000,
        70000
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
        2,
        8,
        5
    ],

    "Rating": [
        4.5,
        3.8,
        4.2,
        np.nan,
        3.9,
        4.8,
        3.5,
        4.1,
        4.9,
        np.nan,
        4.6,
        4.3
    ],

    "Email": [
        "amit@gmail.com",
        "sara@yahoo.com",
        "wrong_email",
        "riya@gmail",
        "priya@gmail.com",
        np.nan,
        "vikas@outlook.com",
        "ankit#gmail.com",
        "pooja@gmail.com",
        "rahul123@yahoo.in",
        "priya123@gmail.com",
        "karan$gmail.com"
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
        "9876540000",
        "9988776655",
        "11111abcde"
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
        "Hyd#",
        "Pune",
        "Bangalore@"
    ]
})

print(df)

print("Find total missing values.")
print(df.isnull().sum())

print("Fill missing Salary with mean.")
df['Salary'] = df["Salary"].fillna(df["Salary"].mean())
print(df["Salary"])

print("Fill missing Experience with median.")
df['Experience'] = df["Experience"].fillna(df["Experience"].median())
print(df["Experience"])

print("Fill missing Rating with average rating.")
df['Rating'] = df["Rating"].fillna(df["Rating"].mean())
print(df["Rating"])

print("Fill missing text values with Unknown")
text_missing = ["Email","Name","City","Department"]
df[text_missing] = df[text_missing].fillna("Unkonown")
print(df)

print("Remove rows where Name is missing.")
df = df.dropna(subset=['Name'])

print("Employees with Salary > 60000.")
print(df[df['Salary'] > 60000])

print("Employees from Pune.")
print(df[df['City'] == "Pune"])

print("Employees from IT department.")
print(df[df['Department'] == "IT"])

print("Salary between 50000 and 70000.")
print(df[(df['Salary'] > 50000) & (df['Salary'] < 70000)])

print("Rating greater than 4.5.")
print(df[df['Rating'] > 4.5])

print("Experience greater than 5.")
print(df[df['Experience'] > 5])

print("Sort Salary ascending.")
df = df.sort_values("Salary")
print(df)


print("Sort Salary descending.")
df = df.sort_values("Salary",ascending=False)
print(df)


print("Sort by Department and Salary.")
df = df.sort_values(["Department","Salary"])
print(df)


print("Average salary department-wise.")
print(df.groupby("Department")['Salary'].mean().round())

print("Maximum salary city-wise.")
print(df.groupby("City")['Salary'].max())

print("Employee count department-wise.")
print(df.groupby("Department")['EmpID'].count())


print("Average rating department-wise.")
print(df.groupby("Department")['Rating'].mean().round())

print("Total salary department-wise.")
print(df.groupby("Department")['Salary'].sum())


print("Names containing numbers.")
for i in df['Name']:
    if re.search(r"\d",i):
        print(i)

print("Names containing special characters.")
for i in df['Name']:
    if re.search(r"^[a-zA-Z0-9]",i):
        print(i)        

print("Valid emails.")
for i in df['Email']:
    if re.search(r"^[\w\.-]+@[\w\.-]+\.\w+$",i):
        print(i)  

print("Valid emails.")
for i in df['Email']:
    if re.search(r"^[\w\.-]+@[\w\.-]+\.\w+$",i):
        print(i)  

print("NOT Valid emails.")
for i in df['Email']:
    if not re.search(r"^[\w\.-]+@[\w\.-]+\.\w+$",i):
        print(i)                  


print("Invalid phone numbers.")
print(df[df['Phone'].str.match(r"\d{10}",na=False)])

print("Cities containing numbers.")
for i in df['City']:
    if not re.search(r"\d{10}",i):
        print(i) 


print("Cities containing special characters.")
for i in df['City']:
    if not re.search(r"^[a-zA-Z0-9]",i):
        print(i)


print("Emails ending with gmail.com.")
print(df[df["Email"].str.endswith("gmail.com")])

print("Convert names to uppercase.")
df['Name'] = df['Name'].str.upper()
print(df)


print("Convert departments to lowercase.")
df['Department'] = df['Department'].str.lower()
print(df)

print("Remove special characters from names.")
df['Name'] = df['Name'].str.replace(r"[^a-zA-Z0-9]","",regex=True)
print(df)


print("Remove numbers from cities.")
df['City'] = df['City'].str.replace(r"\d","",regex=True)
print(df)





