

row = 4

for i in range(0,row):
    for j in range(row,i,-1):
        print(chr(64 + j),end="\t")
    print()