import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
arr1 = np.array([[7,8,9],[10,11,12]])
result = np.concatenate((arr,arr1),axis=0)
print(result)

arr = np.array([[1,2,3],[4,5,6]])
arr1 = np.array([[7,8,9],[10,11,12]])
result = np.stack((arr,arr1),axis=1)
print(result)

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# result = np.hstack((arr1,arr2))
# print(result)


# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# result = np.vstack((arr1,arr2))
# print(result)

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# result = np.dstack((arr1,arr2))
# print(result)
