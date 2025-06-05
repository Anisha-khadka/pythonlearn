# Task calculator

# Ask the use for two numbers and store those numbers on two variables
# Ask the user for which operation(+,-,*,/) does he/she wants to do with those numbers
# Do the operation with those numbers according to the provided operation by user and print the output


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = input("Which operation to perform (+,-,*,/,%):")
if c == '+':
    d = a+b
elif c == '-':
    d = a-b
elif c == '*':
    d = a*b
elif c == '/':
    d = a/b
else:
    d = a % b
    
print(d)
