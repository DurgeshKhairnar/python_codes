import numpy as np

# arr = np.zeros(3)
# print(arr)

# arr = np.ones((3,3),int)
# print(arr)

# arr = np.full((2,3),7)
# print(arr)

# sequens in number in array
# same as python range()

# arr = np.arange(1,11)
# print(arr)

# create identity matrix 

# arr = np.eye(3)
# print(arr)

        #   array properties and operation 
        # shap attribute

# arr = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr.shape) 

# arr = np.array([[1,2,3],[4,5,6]])
# print(np.size(arr)) # element in the array

# number of dimention

# arr = np.array(34)
# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# arr3 = np.array([
#     [[1,2,3,4],[5,6,7,8]],
#     [[1,2,3,4],[5,6,7,8]]
#     ])

# print(np.ndim(arr)) # 0
# print(np.ndim(arr1))# 1
# print(np.ndim(arr2))# 2
# print(np.ndim(arr3))# 3

# dtype = datatype of array element

# arr = np.array([1,2,3,4.5])
# print(arr.dtype)

# astype  = change the datatype

# arr = np.array([1.1,2.1,3.1,4.1])
# change_type = arr.astype(int)
# print(change_type) [1,2,3,4]


#   ============= Mathemetical operation ===================

# arr = np.array([1,2,3,4,5])
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.median(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.std(arr))
# print(np.var(arr))

# discount = 10
# arr = np.array([100,200,300])
# discounted_arr = arr -  (arr * discount / 100) 
# print(discounted_arr)


#  Indexing And Slicing

# arr = np.array([10,20,30])
# print(arr[0])
# print(arr[::-1])

# Fancy Indexing
# arr = np.array([10,20,30])
# print(arr[[2,1,0]])

# ================== Filtering and boolean masking ============

# arr = np.array([1,2,3,4,5])
# print(arr[arr > 2])

# ===================== Reshaping and manipulating array ========
# dimention change without modefing
# reshaping does not copy = show view

# == Flattering array

# ravel() = view

# arr = np.array([[1,2,3],[4,5,6]])
# print(arr.ravel())  # copy
# print(arr.flatten()) # show

# [ arr_name , index , value , axis = 0 (row) and 1(column)]

# insert()
# arr = np.array([10,20,30,40])
# arr2 = np.insert(arr,0,100)
# print(arr2)

# arr = np.array([[1,2],[3,4]])
# arr2 = np.insert(arr,1,[5,6],axis=None)
# print(arr2)

# append()

# arr = np.array([[1,2],[3,4]])
# arr2 = np.append(arr,[5,6])
# print(arr2)

# concatenate
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# con_arr = np.concatenate((arr1,arr2))
# print(con_arr)

# arr = np.array([[1,2,3],[4,5,6]])
# arr2 = np.delete(arr,0,axis = 0)
# print(arr2)

# Stacking
"""
vertically
horizontall

vstatck() rowwise
hstatck() column wise

"""

# arr1 = np.array([1,2,3,4])
# arr2 = np.array([5,6,7,8])
# arr3 = np.vstack((arr1,arr2))
# arr4 = np.hstack((arr1,arr2))
# print(arr3)
# print(arr4)

#  spliting

"""
np.split() = equal


np.hsplit()
np.vsplit()
"""

# arr = np.array([10,20,30,40,50])
# print(np.hsplit(arr,20)) /////////////////////////////////////// = check this

#  ============ Brodcasting ==========

# price = np.array([100,200,300])
# discount = 10

# final_price = price - (price * discount/100)
# print(final_price)

# arr = np.array([10,20,30])
# result = arr * 2
# print(result)

# arr = np.array([[10,20,30],[40,50,60]])
# arr2 = np.array([1,2,3])

# arr3 = arr + arr2
# print(arr3)

#  Incompatible shaper

# arr = np.array([10,20])
# arr2 = np.array([[10,20,30],[40,50,60]])

# arr3 = arr + arr2
# print(arr3)

# Vectorization

# arr1 = np.array([10,20,30])
# arr2 = np.array([40,50,60])

# result = arr1 + arr2
# print(result)


# ===============  Handling Missing & Special Value ==============

# arr = np.array([10,20,np.nan,30,40,np.nan])
# print(np.isnan(arr))   # [False,False,True,False,Flase,True]

#  add to number in np.nan value

# arr = np.array([10,20,np.nan,30,40,np.nan])
# print(np.nan_to_num(arr,nan=100)) # [ 10.  20. 100.  30.  40. 100.]


#  infinite value 

# arr = np.array([1,2,np.inf,4,-np.inf,5])
# # print(np.isinf(arr)) # [False False  True False  True False]

# cleaned_arr = np.nan_to_num(arr,posinf=100,neginf=-100)
# print(cleaned_arr)


# arr = np.array([1,2,3,4],dtype='S')
# print(arr)
# print(arr.dtype)


# arr = np.array([1,2,3,4],dtype='i')
# print(arr)
# print(arr.dtype)


# shape
# arr = np.array([1,2,3,4])
# print(arr.shape) (4,)


# arr = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
# print(arr.shape)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr = arr.reshape(4,3)
print(new_arr)