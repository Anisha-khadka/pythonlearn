# Task calculator

# while asking for number, check whether user has sent a number or not
# If user has sent number then do the calculation
# else ask the user for number again and again whether its a number


while True:
    first_input = input("Enter first number:")
    if first_input.isdigit():
        first_input = int(first_input)
    else:
        print("Please enter valid number")
        continue

    second_input = input("Enter second number:")
    if second_input.isdigit():
        second_input = int(second_input)
    else:
        print("Please enter valid number")
        continue

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
    else:
        print("Please enter the correct operator")
        continue
