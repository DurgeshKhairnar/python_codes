# write a program to print odd and even  digit count

num = 1234567
count_even = 0
count_odd = 0

while num > 0 :
    rev = num % 10
    if rev % 2 == 1:
        count_odd += 1
    else :
        count_even += 1    

    num = num // 10  

print(f"even digit count {count_even}")  

print(f"odd digit count {count_odd}")  