

for i in range(0,5):
    count = i + 1
    for j in range(5,i,-1):
        print(count,end="\t")
        count +=1
    print()    