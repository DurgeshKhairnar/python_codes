 # exception handling implement in ATM mangement project 

balance = 5000

while True :
    print("""
            === ATM MANGEMENT SYSTEM ===
          1) check bank balance
          2) add deposite
          3) withdraw 
          4) exit
""")
    
    check = int(input("Enter the option for ATM operation : "))

    try :
        if check == 1 :
            print(f" account balance :{balance}")

        elif check == 2 :
            amount = int(input('Enter deposite amount :'))
            if amount < 0 :
                raise ValueError("Account valid amount")

            balance += amount
            print(f" your total balance {balance}")

        elif check == 3 :
            amount = int(input('Enter deposite amount :'))
            if amount > balance :
                raise ValueError("Account balense is not suffishant")
            
            balance -= amount
            print(f"your avilable balance {balance}")

        elif check == 4 :
            print("Exit")
            break
        else :
            print("Invalid options")

    except ValueError :
        print('invalid amount')
    except Exception as e :
        print(f"Error :{e}")
    else :
        print("No any error")
    finally :
        print("Thank you for visiting ATM")               
                              
