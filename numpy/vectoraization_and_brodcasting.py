import numpy as np

# vectorization 

# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])

# result = a + b
# print(a + b)

# incompatible boardcasting

# a = np.array([1,2,3,4])
# b = np.array([5,6,7])

# result = a + b
# print(a + b)

# Bordcasting - strech array

a = np.array([[1,2],[3,4]])
b = np.array([5,6])

result = a + b
print(result)