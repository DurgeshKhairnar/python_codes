

row = 4
char = 97


for i in range(1,row+1):
    temp = row+1
    for j in range(1,i+1):
        if j % 2  == 1:
            print(temp,end="\t")
        else:
            print(chr(char),end="\t") 
            char += 1
        temp += 1 
    print()    
           
