# print the char sequense given below where the start = 1 and end = 6 and (if number is odd print the char)

i = 1

while i <= 6:
    if i % 2 == 1 :
        print(chr(64 + i), end=" ")
    else :
        print(i, end=" ")
    i += 1        