

for i in range(4):
    num = 4 - i
    for j in range(4,i,-1):
        if i % 2 == 0:
         print(chr(64 + num),end="\t")
         num -=1
        else: 
         print(chr(96 + num),end="\t")
         num -=1
    print()    
