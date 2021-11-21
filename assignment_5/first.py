#Create a program that will ask for grade percentage. 
#Display the equivalent Grade/Mark and Description
#Input grade: 87.6
#Grade/Mark: 1.75
#Description: Very Good

# grade/mark    percentage     description
# 1.0           97-100          Excellent
# 1.25          94-96           Excellent
# 1.5           91-93           Very Good
# 1.75          88-90           Very Good
# 2.0           85-87           Good
# 2.25          82-84           Good
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Droped

def intro():
    print("Hello, User! Got your card and wondering what mark you got and the description? This is the program for you!")

def grade():
    grades = float (input("enter your grades: "))
    
    if grades >= 97.4 and grades <= 100:
        print("Grade Mark: 1.00 Description: Excellent")
    elif grades >= 93.5 and grades <= 97.4:
        print("Grade Mark: 1.25 Description: Excellent")
    elif grades >= 90.5 and grades <= 93.4:
        print("Grade Mark: 1.5 Description: Very Good")
    elif grades >= 87.5 and grades <= 90.4:
        print("Grade Mark: 1.75 Description: Very Good")
    elif grades >= 84.5 and grades <= 87.4:
        print("Grade Mark: 2.0 Description: Good")
    elif grades >= 81.5 and grades <= 84.4:
        print("Grade Mark: 2.25 Description: Good")
    elif grades >= 78.5 and grades <= 81.4:
        print("Grade Mark: 2.5 Description: Satisfactory")
    elif grades >= 75.5 and grades <= 78.4:
        print("Grade Mark: 2.75 Description: Satisfactory")
    elif grades >= 74.5 and grades >= 75.4:
        print("Grade Mark: 3.0 Description: Passing")
    elif grades >= 64.5 and grades <= 74.4:
        print("Grade Mark: 5.0 Description: Failure")
    else:
        print("category:")
        print("i = Incomplete, w = Withdrawn, d = Dropped")
        categorycode = input("Input code: ")
        if categorycode == "i":
            print("Grades: Incomeplete.")
        elif categorycode == "w":
            print("Grades: Widrawn")
        elif categorycode == "d":
            print("Grades: Dropped")

intro() 
grade()
