import pandas as pd


data = {
    "name":["durgesh","sai","vishal","mukesh","ganesh"],
    "age":[10,20,30,40,50],
    "city":["pune","malegoan","dyane","mumbai","patne"]
}

df = pd.DataFrame(data)

# assing column in DataFrame 
# df['Salary'] = [1000,2000,3000,4000,5000]

# assing column in DataFrame useing insert on sepecific index
# df.insert(1,"Salary",[1000,2000,3000,4000,5000])

# add new row
# df.loc[len(df)] = ["mohit",60,6000]

# df.loc[df['name'] == 'durgesh',"Salary"] = 3000

# check a specific the row
# df.loc[0]

# check multiple column
# print(df[['name','age']])

df.loc[0,'age'] = 27
print(df)