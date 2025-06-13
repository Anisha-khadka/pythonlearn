tasks = []

while True:
    a = 0
    for i in tasks:
        print(str(a) + '->' + i)
        a+=1
    user_choice=input("Enter the operation you want to perform: 1. Add task 2. Remove task 3.End program:")
    if user_choice=='1':
        add_task=input("Enter the task you want to add:")
        tasks.append(add_task)
    elif user_choice=='2':
        remove_task=int(input("Enter the number of the task you want to remove:"))
        tasks.pop(remove_task)
    elif user_choice =='3':
        break
    else:
        print('invalid chocie')
        
        
