
row = 4
temp = row
char = 96 + row
for i in range(0,row):
    num = temp - i
    char = 96 + (row - i)
    for j in range(row,i,-1):
     if j % 2 == 0:          
        print(num,end="\t")
     else:
        print(chr(char),end='\t')
     char -=1     
     num -= 1 
    print()   

