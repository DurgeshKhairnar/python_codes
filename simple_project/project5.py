# Expense manager 

expenses = []
expense = {}

isAdd = 'yes'
total = 0

while isAdd == 'yes':
    expense['expense_name'] = input("Enter expense name :").title()
    expense['price'] = int(input("Enter expense price :"))
    total += expense['price']
    expenses.append(expense)
    isAdd = input("if you add another product plz type yes/no :").lower()

for items in expenses:
    print(items)


print("Total Expense :",total)    

