#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
x = 0
while x < 101:
    if x % 2 == 0:
        x += 1
    else:
        print(x)
        x += 1