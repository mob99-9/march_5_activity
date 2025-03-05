#Prog10: Create a program that ask user to input 2 numbers. 
# Print all the numbers between the two numbers.
num1 = int(float(input('Enter the first number: ')))
num2 = int(float(input('Enter the second number: ')))
for i in range (num1 + 1, num2):
    print(i)
    i += 1