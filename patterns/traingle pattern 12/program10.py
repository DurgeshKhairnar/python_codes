row = 4
num = 1

for i in range(1,row+1):
    for j in range(1,i+1):
        if i % 2 == 1:
            print(num,end="\t")
        else:
            print(chr(96+num),end="\t")
        num +=1
    print()    
