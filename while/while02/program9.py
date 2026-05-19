# write a program print the given number addition

# num = 123456789
# add = 0

# while num > 0 :
#     rev = num % 10
#     add += rev
#     num = num // 10

# print(f"sum of digit :{add}")    

num = [10,20,30]
num2 = [40,50,60]

for i in zip(num,num2) :
    print(list(i))