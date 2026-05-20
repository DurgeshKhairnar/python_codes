

num = 3

for i in range(num):
    for j in range(num):
        print(str(j+1) + chr(65+j),end=" ")
    print()