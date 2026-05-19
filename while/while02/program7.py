# write a program to print odd digit given numbers

num = 1234567

while num > 0 :
    rev = num % 10
    if rev % 2 == 1:
        print(rev, end = " ")
    num = num // 10       
