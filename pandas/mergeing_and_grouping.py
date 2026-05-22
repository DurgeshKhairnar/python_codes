import pandas as pd


data1 = {
    "EmpId":[1,2,3,4],
    "Name":["durgesh","sai","vishal","rohit"],
}

df1 = pd.DataFrame(data1)

data2 = {
    "Department":["IT","HR","IT","HR"],
    "EmpId":[1,2,3,4],
}

df2 = pd.DataFrame(data2)

#merging_data = pd.merge(df1,df2,on="EmpId") means rows where empid matches

# inner_merge = pd.merge(df1,df2,on="EmpId",how="inner") # only matching data

# left_merge = pd.merge(df1,df2,on="EmpId",how="left") # keep all left table row

# right_merge = pd.merge(df1,df2,on="EmpId",how="right") # keep all right table row

outer_merge = pd.merge(df1,df2,on="EmpId",how="outer") # keep everything

print(outer_merge)
