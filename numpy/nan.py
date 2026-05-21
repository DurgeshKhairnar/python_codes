import numpy as np

# nan value in array
arr = np.array([1,2,3,4,5,np.nan])

print(arr) 

# print(sum(arr)) # nan

# print(np.isnan(arr)) print boolen array if value is nan print Ture , otherwise flase

# arr[np.isnan(arr)] = 0
# print(arr) # assing nan value

# nan value methos ignor nan value and sum,avg
# print(np.nansum(arr))
# print(np.nanmean(arr))

# if infinaite value print True in array otherwise False 
# print(np.isinf(arr))



# a = np.array([1,2,np.nan,4,5,np.inf,-np.inf])
# b = np.nan_to_num(a)
# print(b) #[ 1.00000000e+000  2.00000000e+000  0.00000000e+000  4.00000000e+000 5.00000000e+000  1.79769313e+308 -1.79769313e+308]

# result = np.nan_to_num(a,nan=100,posinf=200,neginf=-300)
# print(result)