

row = 4

for i in range(1,row+1):
    for j in range(i):
        if i % 2 == 1 :
          print(chr(97+j),end="\t")
        else:
           print("$",end="\t")  
    print()       
