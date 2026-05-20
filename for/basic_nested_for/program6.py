
num = 4
char = 96 + num
for i in range(num):
    for j in range(num):
        print(chr(char - j), end=" ")
    print()    
