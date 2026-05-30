



for i in range(0,5):
    num = 1
    char = 97
    for j in range(5,i,-1):
        if j % 2 == 1 :
         print(num,end="\t"),
         num +=1
        else:
           print(chr(char),end="\t")
           char +=1 
    print()
