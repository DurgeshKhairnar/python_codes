

row = 4
big = 65 + row
small = 97 + row

for i in range(1,row+1):
    for j in range(1,(i+1)):
        if i % 2 == 1:
            print(chr(small - j),end="\t")
        else :
            print(chr(big - j),end="\t")  
    print()     