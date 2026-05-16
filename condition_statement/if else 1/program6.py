# check the number divisible by 7 and 3

number = int(input("Enter any number :"))

if  number % 7 == 0 :
    print(f"{number} is divisible by 7")
elif  number % 3 == 0 :
     print(f"{number} is divisible by 3")   
elif number % 7 == 0 and number % 3 == 0 :
    print(f"{number} is divisible by 3 or 7")
else:
    print(f"{number} is not divisible by 3 or 7")






        