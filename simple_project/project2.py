# create simple to-do list

print('Add Task to press 1 :')
print('Remove Task to press 2 :')
print('Show all Task to press 3 :')




task_List = []

isAddTask = 'yes'
isOperation = 'yes'

while isOperation == 'yes' :
   enter_taskNumber = input('Enter number :')
   if enter_taskNumber == '1':
    while isAddTask != 'no' :
        task = input("Enter the task :").lower()
        task_List.append(task)
        isAddTask = input("Enter another task plz Yes/No :").lower()
   elif enter_taskNumber == '2':
        print(task_List)
        task_name = input("Enter the task in the list :").lower()
        if task_name in task_List :
             task_List.remove(task_name)
        else :
             print('Task not present in the list')
   elif enter_taskNumber == '3':
       print(task_List)         
   else :
    print('Invalid number')
    break  
                       




if task_List :
    for i in range(len(task_List)):
        print(task_List[i])
else :
    print("Task List is Empty")


print('Thank You')    

