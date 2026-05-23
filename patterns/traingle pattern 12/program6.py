

row = 4
char = 65

for i in range(1,row+1):
    for j in range(1,(i+1)):
        if i % 2 == 1:
            print(j,end="\t")
        else:
            print(chr(char),end="\t")
        char +=1     
    print()       