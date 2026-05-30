
row = 4
total = row * (row + 1) // 2
character = 64 + total

for i in range(0,row):
    for j in range(row,i,-1):
        print(chr(character),end="\t")
        character -=1
    print()    