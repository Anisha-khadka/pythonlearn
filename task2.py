# Task calculator

# while asking for number, check whether user has sent a number or not
# If user has sent number then do the calculation
# else ask the user for number again and again whether its a number
# new requirement

#do exception handling and handle the int conversion error in such a way that if the error occurs ask the user for the number again but if the error doesnot occur then continue the calculator


while True:
    
    try :
        first_input = int(input("Enter first number:"))
    except ValueError:
        continue
    # if first_input.isdigit():
    #     first_input = int(first_input)
    # else:
    #     print("Please enter valid number")
    #     continue
    try:
        second_input = int(input("Enter second number:"))
    except ValueError:
        continue
    # if second_input.isdigit():
    #     second_input = int(second_input)
    # else:
    #     print("Please enter valid number")
    #     continue
    try:
        operator_input = input("Enter the operation to perform(+,-,*,/,%):")
        if operator_input == '+':
            print(first_input+second_input)
        elif operator_input == '-':
            print(first_input-second_input)
        elif operator_input == '*':
            print(first_input*second_input)
        elif operator_input == '/':
            print(first_input/second_input)
        elif operator_input == '%':
            print(first_input % second_input)
    except:
        continue
    # else:
    #     print("Please enter the correct operator")
    #     continue
