# write a program to print sum of odd number from 150 to 101

i = 150
total = 0


while i >= 101 and  i <= 150 :
    if i % 2 != 0:
        total += i
    i -= 1

print(total)        