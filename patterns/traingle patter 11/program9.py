

row = 4

for i in range(0,row):
    count = i
    for j in range(row,i,-1):
        count+=1
        print(count,end="\t")
    print()    