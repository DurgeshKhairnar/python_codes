

# for i in range(5,0,-1) :
#     for j in range(i):
#         print("*",end = " ")
#     print()    


for i in range(0,5) :
    for j in range(5,0,-1):
        if j > i  :
            print("*",end = " ")
        else :
            print(" ",end = " ")    
    print()    

