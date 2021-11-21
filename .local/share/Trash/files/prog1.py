#Program 1: Number Sorter
#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

numb_list = []
numbers = input("Enter three numbers separated by space: ")
numb_list = [int(i) for i in numbers.split()]
sort_list = []
print (numb_list)