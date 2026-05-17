# write a program print the number divisible by 4 and 7 in the range 50 - 100

i = 50

while  i >= 50 and i <= 100 :
    if i % 4 == 0 and i % 7 == 0 :
        print(i , end = " ")
    i += 1    