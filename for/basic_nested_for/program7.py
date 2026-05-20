

num = 4
char = 64 + num
count = 1
for i in range(num):
    for j in range(num):
        print(chr(char)+str(count),end="\t")
        count += 1
    print()    
