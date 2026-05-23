import pandas as pd
import numpy as np

emp = pd.DataFrame({
    "EmpID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Sara", "John", "Riya", np.nan, "Neha"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Age": [25, np.nan, 28, 32, 29, 24],
    "Salary": [50000, 60000, np.nan, 75000, 58000, 52000],
    "City": ["Pune", "Mumbai", "Delhi", np.nan, "Chennai", "Pune"]
})

projects = pd.DataFrame({
    "EmpID": [101, 102, 103, 107],
    "Project": ["AI", "Banking", "WebApp", "Cloud"],
    "Experience": [2, 5, 3, 4]
})

print("Show first 3 rows")
print(emp)

# print("Show only Name and Salary")
# print(emp[["Name","Salary"]])

# print("Find employees with salary greater than 55000")
# print(emp[emp["Salary"] > 55000])

# print("Find employees from Pune")
# print(emp[emp['City'] == 'Pune'])

# print("Find employees from IT department")
# print(emp[emp['Department'] == 'IT'])

# print("Find employees age greater than 25 and salary greater than 50000")
# print(emp[(emp['Age'] > 25 ) & (emp['Salary'] > 50000)])

# print('Count missing values in each column')
# print(emp.isnull().sum())

# print('Fill missing Age with average age')
# emp['Age'] = emp['Age'].fillna(emp['Age'].mean())
# print(emp)

# print("Fill missing City with Unknown")
# emp['City'] = emp['City'].fillna('Unknown')
# print(emp)

# print("Remove rows where Salary is missing")
# emp = emp.dropna(subset="Salary")
# print(emp)

# print("Replace Pune with Nagpur")
# emp['City'] = emp['City'].replace("Pune","Nagpur")
# print(emp)

# print("Add new column Bonus")
# emp.insert(len(emp),"Bonus",[100,200,50,300,400])
# print(emp)

# print("Add one new employee row")
# emp.loc[len(emp)] = [107,"vishal","IT",23.0,60000,230,"Mumbai"]
# print(emp)

# print("Update Amit salary to 70000")
# emp.loc[emp['Name'] == "Amit","Salary"] = 100
# print(emp)

# print("Remove City column")
# emp.drop("City",axis=1,inplace=True)
# print(emp)

# print("Remove employee with index 2")
# emp = emp.drop(1)
# print(emp)

# print("Sort salary ascending")
# emp = emp.sort_values('Salary')
# print(emp)

# print("Sort salary decending")
# emp = emp.sort_values('Salary',ascending=False)
# print(emp)

# print("Sort by Department and Salary")
# print(emp.sort_values(['Department',"Salary"]))

# print("Find average salary")
# print(emp['Salary'].mean())

# print("Find max salary")
# print(emp['Salary'].max())

# print("Find department-wise average salary")
# print(emp.groupby("Department")['Salary'].mean())


# print("Find department-wise employee count")
# print(emp.groupby("Department")['Name'].count())

# print("Find department-wise max Salary")
# print(emp.groupby("Department")['Salary'].max())

# print("Merge employees and projects using EmpID")
demo = pd.merge(emp,projects,on="EmpID",how="left")
print(demo)

# print("Find employees who do not have projects")
# print(demo[demo['Project'].isnull()])

# print("Find employees whose names start with A")
# print(demo[demo["Name"].str.startswith("A")])

# # multiple column chnage
# demo[["Name","City","Project"]] = (demo[["Name","City","Project"]].fillna("unkown"))
# print(demo)

# # all column

demo["Age"] = pd.to_numeric(
    demo["Age"],
    errors="coerce"
)

demo["Salary"] = pd.to_numeric(
    demo["Salary"],
    errors="coerce"
)

demo["Experience"] = pd.to_numeric(
    demo["Experience"],
    errors="coerce"
)




demo['Age'] = demo['Age'].fillna(demo['Age'].mean())
demo['Salary'] = demo['Salary'].fillna(demo['Salary'].mean())
demo['Experience'] = demo['Experience'].fillna(demo['Experience'].mean())

demo = demo.fillna("unkown")

print(demo)