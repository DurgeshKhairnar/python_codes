
num = int(input('Enter any number :'))


if num % 2 == 0 or num % 5 == 0 and num % 10 == 0 :
    print(f'{num} is divisible by 2,5,12')
else:
    print(f'{num} is Not divisible by 2,5,12')
    
        