num = 30

for i in range(4):
    for j in range(4, i, -1):

        while num >= 0:

            if num % 2 == 1:
                print(num, end="\t")
                num -= 1
                break

            num -= 1

    print()