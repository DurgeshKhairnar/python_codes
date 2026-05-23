

row = 4

for i in range(0,row):
    count = 65 + i
    for j in range(row,i,-1):
        if count % 2 == 1 :
            print(count,end="\t")
        else:
            print(chr(count),end="\t")
        count += 1 
    print()           