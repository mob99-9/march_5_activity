#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
if num1 != num2:
    print(f'Not Equal ')
elif num2 == num1:
    print(f'Equal')
else:
    print(f'Invalid Inputs')
