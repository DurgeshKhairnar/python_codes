


row = 4
num = row

for i in range(0,row):
    temp = num - i
    char = 64 + row - i
    for j in range(row,i,-1):
     if i % 2 == 0 :
      print(temp,end="\t")
      temp -=1 
     else:
      print(chr(char),end="\t") 
      char -=1  
    print()    