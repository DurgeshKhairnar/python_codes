import pandas as pd
import numpy as np


data = {
    "name":["durgesh","sai",np.inf,"mukesh",np.inf],
    "age":[10,20,30,np.inf,50],
    "city":["pune",None,"dyane","mumbai","patne"]
}

df = pd.DataFrame(data)

# print(df.isnull().sum())

df["age"] = df["age"].replace(np.inf,np.nan)

df['age'] = df["age"].fillna(df['age'].mean())

# df.fillna(method='bfill') check in char gpt how to use 

df["city"] = df["city"].fillna("pune")

df["name"] = df["name"].replace(np.inf,np.nan)

df["name"] = df["name"].fillna("rahul")

print(df)



