
big = 65
small = 97


for i in range(0,5):
    big = 65
    small = 97
    for j in range(5,i,-1):
       if i % 2 == 0: 
          print(chr(big),end="\t")
          big +=1
       else:
          print(chr(small),end="\t")
          small +=1
    print()         