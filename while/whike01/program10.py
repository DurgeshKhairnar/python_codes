# write a program to print the number in range 100 - 24 which are divisible by 4 and 5

i = 100

while i >= 24 and i <= 100 :
    if i % 4 == 0 and i % 5 == 0 :
        print(i, end = " ")
    i -= 1
