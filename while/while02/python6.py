# write a program to count digit give number

num = 1234890
count = 0

while num > 0 :
    rev = num % 10
    count += 1
    num = num // 10

print(f"count the number of digit {count}")