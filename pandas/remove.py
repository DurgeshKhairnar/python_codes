

import pandas as pd


data = {
    "name":["durgesh","sai","vishal","mukesh","ganesh"],
    "age":[10,20,30,40,50],
    "city":["pune","malegoan","dyane","mumbai","patne"]
}

df = pd.DataFrame(data)

# drop column
# print(df.drop("name",axis=1))

# remove row by index 
# df.drop(1,inplace=True)

# remove multiple column
# df.drop(['age',"city"],axis=1,inplace=True)



print(df[df['age'] > 25])