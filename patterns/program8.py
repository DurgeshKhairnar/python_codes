

row = 4

for i in range(0,row):
    count = 1
    for j in range(row,i,-1):
        print(count,end="\t")
        count +=1
    print()    
