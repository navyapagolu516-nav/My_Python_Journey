#Coding Exercise
# 1. Print Statement:
#   Write a Python program that prints your name.
name = "Navya"
print(name)

##################################################
# 2. Comments:
# Create a Python script with both single-line and multi-line comments explaining the purpose of the script.

#Below code is used to display the values of variables num and name
num = 10
name = "Navya"
print(num)
print(name)

"""
Above code accepts two variables num and name
num is a variable it contains a value 10
name is a variable it contains a value "Navya"
print statement is used to display the values of variables num and name on the screen
"""

##############################################################
# 3. Data Structures & Data Types:
# Define a list containing three different data types.
# Define a set containing employee idʼs.

my_list = [3, 4.5, "Navya", [1,2], (1,2,3), {5,6}]
print(my_list, type(my_list))

my_set = {3, 4.5, "Navya", (1,2,3)}   #set is a collection of immutable datatypes and is unique.
print(my_set, type(my_set))

################################################################
# 4. String Operations:
# Concatenate two strings and print the result..

name1 = "Welcome to "
name2 = "PythonLife"
print(name1 + name2)

###################################################################
# 5. Python Keywords:
# Create a variable with a name that is a Python keyword. What happens?
# observation..

# if = [1,2,4,5,6]
# print(if)           #Syntax error - because keywords cannot be used as variable name

########################################################################
# 6. Python Variables:
# Declare two variables, one storing an integer and the other a string. Print their values.

num = 10
name = "Navya"
print(num)
print(name)

########################################################################
# 7. Type Conversions:
# Convert a float to an integer and print the result.
# Convert an integer to a string and display the output.

num1 = int(10.5)
num2 = str(10)

print(num1, "|", type(num1))
print(num2, "|", type(num2))
########################################################################
# 8. Simple Input & Output:
# Take the user's age as input and print a message using that input.

age = int(input("Enter your age: "))
print("Your age is:", age)
print("The data type of the age is:", type(age))

########################################################################

# 9. Print Statement:
# Write a program that prints a pattern using multiple print statements.

print("*    *")
print("* *  *")
print("*  * *")
print("*    *")
########################################################################

# 10. Comments:
# Create a Python script for a simple task and add comments to explain each step.

#task to find the area of a rectangle
length = 5      #length is a variable that stores the length of the rectangle
breadth = 3     #breadth is a variable that stores the breadth of the rectangle
area = length * breadth   #area is a variable that stores the area of the rectangle calculated by multiplying length and breadth
print("Area of the rectangle is:", area)   #print statement is used to display the area of the rectangle on the screen

########################################################################

# 11. Data Structures & Data Types:
# Implement a program that uses a dictionary to store information about a book (title, author, publication year).

my_book = {
    "title" : "Python Crash Course",
    "author" : "Erric Mathews",
    "publication_year" : 2023
    }
print(my_book)

########################################################################

# 12. String Operations:
# Write a python program that takes a string as input ( 35 ) and return float value.

value = input("enter any number : ")
result = float(value)
print(result)
print(type(result))

########################################################################
# 13. Concatenate Strings:
# Write a program to take two names as input and print them together.

first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
print(first_name + last_name)

########################################################################
# 14. Type Conversions:
# Create a program that takes user input for their age, converts it to
# an integer, adds 5, and then prints the result.

user_age = input("Enter your age : ")
result = int(user_age)+ 5
print(result)

########################################################################
# 15. Simple Input & Output:
# Build a calculator program that takes two numbers as input and
# performs the arithmetic operation

number1 = int(input("Enter 1st number : "))
number2 = int(input("Enter 2nd number : "))

print("Addition of given two numbers is : ", number1 + number2)
print("Subtraction of given two numbers is : ", number1 - number2)
print("Multiplication of given two numbers is : ", number1 * number2)
print("Division of given two numbers is : ", number1 / number2)




