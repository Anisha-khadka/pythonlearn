# login
# make a dictionary with user datas
# a = {'ram': 'ram@gmail.com'}
# ask the user for username and password
# check whether the username and password is in a user data or not in the dictionary
# if it is then print login successful
# else print invalid credentials
# If the user data exists then give him/her choices of : view balance(balance print), add balance(ask the amount to add and print the new amount), redeem balance(askthe amount
# if the user data doesnot exists print invalid credentials

user_registry = {
    'anisha': 'anisha123',
    'ram': 'ram456',
    'hari': 'hari789',
    'ashish': 'ashish000'
}
balance = {
    'anisha':2300,
    'ram':2000,
    'hari':3000,
    'ashish':2000
}

def ViewBalance():
    user_amount=balance.get(username)
    print(f'your total balance is:{user_amount}')
    
def AddBalance():
    user_amount_to_add=int(input("Enter the amount you want to add:"))
    user_balance_amount=balance.get(username)
    new_balance_amount=user_balance_amount+user_amount_to_add
    print(f'Your new balance is {new_balance_amount}')
    
def RedeemBalance():
    user_redeem_amount =int(input('Enter the amount you want to reedem:'))
    user_actual_amount =balance.get(username)
    if user_redeem_amount>user_actual_amount:
        print(f'You donot have sufficient balance! Your balance is {user_actual_amount}')
        return
    redeemed_amount=user_actual_amount-user_redeem_amount
    print(f'You redeem {user_redeem_amount}')
    print(f'your remaining balance is {redeemed_amount}')

username = input("Enter your username:")
password = input("Enter your password:")

if username in user_registry and password == user_registry.get(username):
    print(f'Welcome {username}')
    user_choice =input("Enter the operation you want to perform[1. View balance  2. Add balance 3.Reedem balance ]:")
    if user_choice == '1':
        ViewBalance()
    elif user_choice =='2':
        AddBalance()
    elif user_choice =='3':
        RedeemBalance()
    else:
        print('Invalid choice! Please try again')
        
else:
    print('invalid credentials')
    


