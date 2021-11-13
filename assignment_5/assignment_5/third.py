#Program 3: Life stages
#Create a program that ask for an age of a person
#Display the life stage of the person.
#Rules:
#0 - 12 : Kid
#13 - 17 : Teen
#18 : Debut
#19 above : Adult

def greetings():
    print("Hello, User!. So you want to know what are you in stages of life right now? This is the program for you!")

def lifestages():
    age = int(input("Enter your Age: "))
    if age >= 0 and age <= 12:
        print("You're still a kid, Have fun")
    elif age >= 13 and age <= 17:
        print("You're a Teen, Dont get pregnant!")
    elif age == 18:
        print("You're a Debutant. Am i invited?")   
    elif age >= 19:
        print("You're an Adult. Travel the world")

greetings()
lifestages()