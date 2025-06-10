#login Task
# make a list of usernames
# ask the user for his/her username
# if the username exists on lists of username print login successful
# else invalid login

a=['anisha@22gmail.com','ram@gmail.com','sita@00gmail.com','anjali@gmail.com','piyush40@gmail.com']
b= input('Enter you username:')

if b in a:
    print("Login Successfull")
else:
    print("Invalid Login")
    