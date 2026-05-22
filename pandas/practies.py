import pandas as pd
import numpy as np

data = {
    "Name": ["Amit", "Sara", "John", "Riya", "Karan"],
    "Age": [22, 21, np.nan, 23, 20],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Marks": [85, 90, 78, np.nan, 88],
    "City": ["Pune", "Mumbai", "Delhi", "Pune", None]
}

df = pd.DataFrame(data)

# print(df)
print(df[df["Marks"] > 85])
print(df)