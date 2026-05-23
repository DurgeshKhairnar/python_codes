

row = 3

for i in range(1,row+1):
    for j in range(row,0,-1):
        if j >= i:
            print(i,end="\t")
    print()        