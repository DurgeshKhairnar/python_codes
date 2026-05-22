import pandas as pd

data = {
    "name":["durgesh","sai","vishal","Rahul"],
    "department":["IT","HR","HR","IT"],
    "age":[23,20,24,25]
}

df = pd.DataFrame(data)
print(df)

print(df.groupby('name')['department'].max())