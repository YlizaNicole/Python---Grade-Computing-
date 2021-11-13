#Create a program that will ask for grade percentage. 
#Display the equivalent Grade/Mark and Description
#Input grade: 87.6
#Grade/Mark: 1.75
#Description: Very Good

#step 1: create a program that ask for you grade percentage
grade_percentage = int (input("what is your grade percentage?: "))
if grade_percentage >= 101 and grade_percentage <= 64:
    print("Value invalid")    #true
else:
    if grade_percentage >= 97 and grade_percentage <= 100:
        print ("Mark: 1.0  Description: Excellent")
        