#Program 2: Find the lowest number
#Create a program that ask 3 numbers. 
#Find the lowest number using only if-else statement.
#Display the lowest number

def greetings():
    print("Hello User! This program helps you find the lowest of 3 numbers all you need to do is input the numbers!")

def lowestNumber():
    first = int(input("input the first Number: "))
    second = int(input("input the second Number: "))
    third = int(input("input the third Number: "))
    if first <= second and first <= third:
        print("The lowest number is ", first)
    elif second <= first and second <=  third:
        print("The lowest number is ", second)
    else:
        third <= first and third <= second
        print("The lowest number is ", third)

greetings()
lowestNumber()