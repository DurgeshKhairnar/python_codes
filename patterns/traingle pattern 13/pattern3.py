
row = 5
num = row * (row + 1)

for i in range(0,5):
    for j in range(5,i,-1):
        print(num,end="\t")
        num-=1
    print()    