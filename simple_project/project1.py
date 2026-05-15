# simple Bank atm system 

a = int(input("Enter amount to add your account :"))
print(a),

b = int(input("Enter debit amount :"))

if  b < a :
        a -= b
        print(f'Debit Rs {b} in your Account')
        print(f'Avl Balance Rs {a}')
else :
        print('inshficants balence in your account')   

print("Thank You")             