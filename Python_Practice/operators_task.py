#1. Exercise: Create a program that takes user input for their name and age. 
# Use formatted strings (f-strings) to print a message welcoming the user and
# stating their age.

name = input("Enter your name : ")
age = int(input("Enter your age : "))
print(f"Welcome {name}, your age is {age}")

#######################################################
# 2. Create a list called numbers that contains integers from 1 to 10.
# Check if the number 5 is in the list.
# Check if the number 15 is not in the list.

numbers = [1,2,3,4,5,6,7,8,9,10]
print(5 in numbers)
print(15 not in numbers)

#######################################################
# 3. Write a Python program to calculate the area of a rectangle using the given 
# formula: area = length * width . Take the values of length and width as inputs from the user.

length = int(input("Enter the length of area of rectangle : "))
width = int(input("Enter the width of area of rectangle : "))
print(f"Area of rectangle is : {length*width} ")

#######################################################

# 4. Write a Python program to demonstrate incrementing and decrementing a variable

num = 10
num += 5       #incrementing the num variable
print(num)
num -= 5       # decrementing the num variable
print(num)

#######################################################
# 5. Write a Python program to convert temperature from Celsius to Fahrenheit.The formula for conversion is: 
# F = (C * 9/5) + 32 . Take the temperature in Celsius as 2 input from the user.

celsius = int(input("Enter the temparature in celsius : "))
fahrenheit = (celsius * 9/5) + 32
print(f"Converted temperature in fahrenheit is : {fahrenheit} ")

#######################################################
# 6. Write a Python program to calculate the simple interest given the principal 
# amount, rate, and time (in years).

principal = int(input("Enter the principal amount : "))
rate = int(input("Enter the rate of interest : "))
time = int(input("Enter the time in years : "))
simple_interest = (principal * rate * time) / 100
print(f"Simple interest is : {simple_interest} ")

#######################################################
# 7. Write a Python program to concatenate two strings and display the result. The 
# strings should be taken as input from the user.

string1 = input("Enter the 1st string : ")
string2 = input("Enter the 2nd string : ")
print(f"Concatenation of given two strings is : {string1+string2}")

#######################################################
# 8. Write a Python program to convert a distance from kilometers to miles.

kilometers = float(input("Enter the distance in kilometers : "))
miles = kilometers * 0.621371
print(f"Distance in miles is : {miles} ")
