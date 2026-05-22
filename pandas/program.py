import pandas as pd


data = {
    "name":["durgesh","sai","vishal","mukesh","ganesh"],
    "age":[10,20,30,40,50],
    "rate":[435,543,200,346,500],
    "city":["pune","malegoan","dyane","mumbai","patne"]
}

df = pd.DataFrame(data)
# print(df)

# print all informain about data frame
# print(df.info())

# print all staticstic calculation about dataframe
# print(df.describe())

# data frame size using shape
# print(df.shape)

# column name show in DataFrame
# print(df.columns)

# condition in DataFrame
# print(df[df['age'] > 22])

# multiple condition (&) and condition
# print(df[(df['age'] > 20) & (df['rate'] > 300) ])

# multiple condition (|) or condition
# print(df[(df['age'] > 20) | (df['rate'] > 300) ])

# apply condtion and show only name
# print(df[df["age"] > 20],df['name'])

df.to_csv("data.csv")