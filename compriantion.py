
#compresion is a short and powefull way to create :
# list,set and dic


# nums = [x*x for x in range(5) if x % 2 == 0]
# print(nums)

# nums = { x:x*x for x in range(10) }
# print(nums)

# nums = [
#     [i*j for j in range(3)]
#     for i in range(3)
# ]
# print(nums)

# nums = [1,2,3,4,5,6,7]
# myList = [ "Even" if x % 2 == 0 else "odd" 
#             for x in nums
#           ]
# print(myList)


# nums = {
#     x:x*x
#     for x in range(5)
#     if x % 2 == 0
# }

# print(nums)


# word = 'durgesh'
# myList = [x.upper() for x in word]
# print(myList)

# list1 = ["durgesh","vishal","saurabh"]
# list2 = [90,70,99]

# for name,value in  zip(list1,list2) :
#  print(type(name))

a = 5
b = 3
print( a is b)