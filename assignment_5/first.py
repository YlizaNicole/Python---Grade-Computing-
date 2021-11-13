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
    print("Hello User!")

def grade():
    grades = int (input("enter: "))
    if grades >= 101 or grades <= 64:
        print("invalid")
    elif grades >= 97 and grades <= 100:
        print("Grade Mark: 1.00 Description: Excellent")
    elif grades >= 94 and grades <= 96:
        print("Grade Mark: 1.25 Description: Excellent")
    elif grades >= 91 and grades <= 93:
        print("Grade Mark: 1.5 Description: Very Good")
    elif grades >= 88 and grades <= 90:
        print("Grade Mark: 1.75 Description: Very Good")
    elif grades >= 85 and grades <= 87:
        print("Grade Mark: 2.0 Description: Good")
    elif grades >= 82 and grades <= 84:
        print("Grade Mark: 2.25 Description: Good")
    elif grades >= 79 and grades <= 81:
        print("Grade Mark: 2.5 Description: Satisfactory")
    elif grades >= 76 and grades <= 78:
        print("Grade Mark: 2.75 Description: Satisfactory")
    elif grades == 75:
        print("Grade Mark: 3.0 Description: Passing")
    elif grades >= 65 and grades <= 74:
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