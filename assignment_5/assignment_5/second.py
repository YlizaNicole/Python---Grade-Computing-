#Program 2: Find the lowest number
#Create a program that ask 3 numbers. 
#Find the lowest number using only if-else statement.
#Display the lowest number

def greetings():
    print("Hello User!")

def lowestNumber():
    first = int(input("first Number: "))
    second = int(input("second Number: "))
    third = int(input("third Number: "))
    if first <= second and first <= third:
        print("The lowest number is ", first)
    elif second <= first and second <=  third:
        print("The lowest number is ", second)
    else:
        third <= first and third <= second
        print("The lowest number is ", third)

greetings()
lowestNumber()