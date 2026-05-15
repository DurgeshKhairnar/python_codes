# build expensce tracker

expense_list = []
total_expense = 0

print('Add all Expences :')

addEx = "yes"

while addEx == 'yes':
    expense_price = int(input('Enter Expense price :'))
    expense_list.append(expense_price)
    addEx = input('Add another expense plz enter yes or no :')

for i in range(len(expense_list)) :
    total_expense  += expense_list[i]


print(f"Highest Expense in The List :{max(expense_list)}") 
print("total expense :",total_expense)   

    