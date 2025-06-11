# login
# make a dictionary with user datas
# a = {'ram': 'ram@gmail.com'}
# ask the user for username and password
# check whether the username and password is in a user data or not in the dictionary
# if it is then print login successful
# else print invalid credentials

user_registry = {
    'anisha': 'anisha123',
    'ram': 'ram456',
    'hari': 'hari789',
    'ashish': 'ashish000'
}

username = input("Enter your username:")
password = input("Enter your password:")

if username in user_registry and password == user_registry[username]:
    print('login sucessful')
else:
    print('invalid credentials')
