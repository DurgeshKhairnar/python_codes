
char = 64
for i in range(4):
    char += i
    for j in range(i + 1):
        print(chr(char),end = "\t") 
        char += j   
    print()
  