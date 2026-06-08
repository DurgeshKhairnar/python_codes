import pandas as pd
import numpy as np

df = pd.DataFrame({

    "EmpID": [
        101,102,103,104,105,
        106,107,108,109,110,
        111,112,113,114,115
    ],

    "Name": [
        " Amit Kumar ",
        "Sara_123",
        "John@Doe",
        np.nan,
        "Riya Sharma",
        "Neha99",
        "Vikas",
        "Ankit#",
        "Pooja",
        "Rahul123",
        "Priya",
        "Karan$",
        "Rohit@123",
        "Sneha",
        " Amit Kumar "
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
        "rahul123@yahoo.in",
        "priya123@gmail.com",
        "karan$gmail.com",
        "rohit@gmail.com",
        "sneha@gmail.com",
        "amit@gmail.com"
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
        "11111abcde",
        "9876501234",
        "999999999",
        "9876543210"
    ],

    "Department": [
        "IT",
        "hr",
        "Finance",
        np.nan,
        "Marketing",
        "IT",
        "HR",
        "finance",
        "IT",
        "Marketing",
        "HR",
        "IT",
        "Sales",
        "sales",
        "IT"
    ],

    "City": [
        " Pune ",
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
        "Bangalore@",
        "Mumbai22",
        "Delhi@",
        " Pune "
    ],

    "Salary": [
        50000,
        60000,
        np.nan,
        75000,
        58000,
        -1000,
        45000,
        9999999,
        90000,
        61000,
        55000,
        70000,
        65000,
        1200000,
        50000
    ],

    "Experience": [
        2,
        5,
        np.nan,
        7,
        4,
        3,
        -2,
        6,
        20,
        2,
        8,
        5,
        10,
        25,
        2
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
        4.3,
        4.7,
        5.0,
        4.5
    ]
})

print(df)

print("Show first 5 rows.")
print(df.head())

print("Show last 5 rows.")
print(df.tail())

print("Check shape.")
print(df.info())


print("Display column names.")
print(df.columns)

print("Check data types.")
print(df.dtypes)


print("Show dataset info.")
print(df.info())


print("Show statistical summary.")
print(df.describe())


print("Show statistical summary.")
print(df.isnull().sum())


print("Fill missing Salary with mean.")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df["Salary"])

print("Fill missing Experience with median.")
df["Experience"] = df["Experience"].fillna(df["Experience"].mode())
print(df["Experience"])


print("Fill missing Rating with mean.")
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())
print(df["Rating"])

print("Fill missing text fields with Unknown")
column_name = ["Name","Email","Department","City"]
df[column_name] = df[column_name].fillna("Unknown")
print(df)


print("Find duplicate rows.")
print(df[df.duplicated()])

print("Remove duplicate rows.")
df = df.drop_duplicates()
print(df)

print('Check duplicates again.')
print(df[df.duplicated()])

print("Remove extra spaces from Name.")
df["Name"] = df['Name'].str.strip()
print(df["Name"])

print("Remove extra spaces from City.")
df["City"] = df['City'].str.strip()
print(df["City"])

print("Convert Name to Title Case.")
df["Name"] = df['Name'].str.title()
print(df["Name"])

print("Convert Department to Uppercase.")
df["Department"] = df["Department"].str.upper()
print(df["Department"])


print("Employees with Salary > 60000.")
print(df[df["Salary"] > 60000])

print("Employees from Pune.")
print(df[df["City"] == "Pune"])

print("Employees in IT department.")
print(df[df["Department"] == "IT"])

print("Salary between 50000 and 70000.")
print(df[(df["Salary"] > 50000) & (df["Salary"] < 70000) ])

print("Experience > 5.")
print(df[df["Experience"] > 5])

print("Rating > 4.5.")
print(df[df["Rating"] > 4.5])

print("Sort Salary ascending.")
print(df["Salary"].sort_values())

print("Sort Salary descending.")
print(df["Salary"].sort_values(ascending=False))


print("Sort by Department and Salary.")
print(df.groupby("Department")["Salary"].max())

print("Average salary department-wise.")
print(df.groupby("Department")["Salary"].mean())


print("Maximum salary city-wise.")
print(df.groupby("City")["Salary"].max())


print("Employee count department-wise.")
print(df.groupby("Department")["EmpID"].count())

print("Total salary department-wise.")
print(df.groupby("Department")["Salary"].sum())

print("Average rating department-wise.")
print(df.groupby("Department")["Rating"].mean())


print("Find names containing numbers.")
print(df[df['Name'].str.contains(r"\d",regex=True)])



print("Find names containing special characters.")
print(df[df['Name'].str.contains(r"[^a-zA-Z0-9 ]",regex=True)])

print("Find valid emails.")
print(df[df['Email'].str.match(r"^[\w\.-]+@[\w\.-]+\.\w+$",na=True)])

print("Find not valid emails.")
print(df[~df['Email'].str.match(r"^[\w\.-]+@[\w\.-]+\.\w+$",na=True)])


print("Find valid phone numbers..")
print(df[df['Phone'].str.match(r"\d{10}$",na=True)])



print("Find invalid phone numbers.")
print(df[~df['Phone'].str.match(r"\d{10}$",na=True)])

print("Find cities containing numbers.")
print(df[df['City'].str.match(r"^[0-9]",na=True)])


print("Find cities containing special characters.")
print(df[df['City'].str.match(r"[^a-zA-Z0-9 ]",na=True)])

print("Remove special characters from Name.")
df['Name'] = df['Name'].str.replace(r"[^a-zA-Z0-9 ]","",regex=True)
print(df['Name'])


print("Remove numbers from City.")
df['City'] = df['City'].str.replace(r"\d","",regex=True)
print(df['City'])


print("Remove special characters from City.")
df['City'] = df['City'].str.replace(r"[^a-zA-Z0-9 ]","",regex=True)
print(df['City'])


print("Replace invalid emails with Invalid")
df["Email"] = np.where(df["Email"].str.match(r"^[\w\.-]+@[\w\.-]+\.\w+$"),df['Email'],"Invalid")
print(df["Email"])

print("Replace invalid phone numbers with Unknown")
df["Phone"] = np.where(df["Phone"].str.match(r"\d{10}$"),df['Phone'],"Unknown")
print(df["Phone"])

print("Find negative salaries.")
print(df[df['Salary'] < 0])

print("Find salaries greater than 500000.")
print(df[df['Salary'] > 500000])

print("Replace negative salaries with median salary.")
meadian_salary = df['Salary'].median()
df["Salary"] = np.where(df["Salary"] > 0,df["Salary"],meadian_salary)
print(df["Salary"])

print("Replace extreme salaries with median salary.")
df.loc[
    df["Salary"] > 500000,
    "Salary"
] = meadian_salary

print("Highest-paid employee.")
print(df.loc[df["Salary"].idxmax()])


print("Lowest-paid employee.")
print(df.loc[df["Salary"].idxmin()])

print("Top 3 highest salaries.")
print(df.nlargest(3,"Salary"))

print("Average experience department-wise.")
print(df.groupby("Department")["Experience"].mean())

print("Most common city.")
print(df["City"].mode)


print("Most common city.")
print(df["City"].nunique())

print("Create Bonus = Salary × 10%.")
df["Bonus"] = df["Salary"] * 0.10
print(df)

print("Create Tax = Salary × 5%.")
df["Tax"] = df["Salary"] * 0.05
print(df)

print("Create NetSalary = Salary + Bonus − Tax.")
df["NetSalary"] = (df["Salary"] + df["Bonus"] - df['Tax'])
print(df["NetSalary"])

print("Create Email_Status (Valid/Invalid).")
df["Email_status"] = np.where(df["Email"].str.match(r"^[\w\.-]+@[\w\.-]+\.\w+$"),"Valid","Invalid")
print(df)


print("Create Phone_Status (Valid/Invalid).")
df["Phone_status"] = np.where(df["Phone"].str.match(r"^\d{10}$"),"Valid","Invalid")
print(df)
print(df['Phone'])


pt_table = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc="mean"
)

print(pt_table)