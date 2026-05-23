
row = 4
char = 65 + row

for i in range(1,row+1):
    for j in range(1,(i+1)):
        print(chr(char),end="\t")
        char += 1
    print()    