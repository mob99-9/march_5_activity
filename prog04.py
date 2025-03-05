#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
try:
    quo = num1//num2
    print(f'The quotient of the two numbers is {quo:.0f}')
except ZeroDivisionError:
    print('Can\'t print to 0')