#Vowel Checker:
# Write a Python program that takes a character as input and checks whether 
# it is a vowel or not. Use the "if-else" statement

char = input("Enter a character : ")
if char in "aeiouAEIOU":
    print(f"Entered character {char} is a Vowel")
else:
    print(f"Entered character {char} is not a Vowel")

#######################################################################
# Age Group Classification
# Write a program that takes an age as input and classifies the person into one of the following age groups:
# Child: 0 - 12 years
# Teenager: 13 - 17 years
# Adult: 18 - 64 years
# Senior: 65 years and older

age = int(input("Enter your age : "))
if age < 0:
    print("Invalid entry")
elif age <= 12:
    print("You are a Child")
elif age <= 17:
    print("You are a Teenager")
elif age <= 64:
    print("You are an Adult")
else:
    print("You are a Senior")

#######################################################
# Number Classifier:
# Write a program that takes an integer as input and classifies it as positive, negative, or zero. 
# Use the "if-elif-else" statement

number = int(input("Enter a number : "))
if number>0:
    print(f"Entered number {number} is Positive")
elif number<0:
    print(f"Entered number {number} is Negative")
else:
    print(f"Entered number {number} is Zero")

#######################################################
# Leap Year Checker:
# Create a program that checks whether a given year is a leap year or not. A 
# leap year is divisible by 4, but not by 100 unless it is divisible by 400.

year = int(input("Enter the year : "))

if year % 400 == 0:
    print(f"{year} is a Leap Year")
elif year % 100 == 0:
    print(f"{year} is not a Leap Year")
elif year % 4 == 0:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

#######################################################
# Calculator:
# Build a simple calculator program that takes two numbers and an operator 
# (+, -, *, /) as input and performs the corresponding operation.

num1 = float(input("Enter 1st number : "))
num2 = float(input("Enter 2nd number : "))
operator = input("Enter the operator(+, -, *, /) : ")
if operator == "+":
    print(f"You have selected {operator} operator")
    print(f"Addition of {num1} and {num2} is: {num1 + num2}")
elif operator == "-":
    result = num1 - num2
    print(f"You have selected {operator} operator")
    print(f"Subtraction of {num1} and {num2} is: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"You have selected {operator} operator")
    print(f"Multiplication of {num1} and {num2} is: {result}")
elif operator == "/":
    result = num1 / num2
    print(f"You have selected {operator} operator")
    print(f"Division of {num1} and {num2} is: {result}")
else:
    print(f"Invalid Operator")


#############################################################
# Short Hand If:
# Rewrite the following code using the short-hand 
# if statement:
# x = 8
# if x % 2 == 0: result = "Even"
# else: result = "Odd

x = int(input("Enter a number : "))
print(f"{x} is Even") if x % 2 == 0 else print(f"{x} is Odd")

####################################################################
# Discount Calculator:
# Create a program that calculates the final price after applying a discount. 
# The program should take the original price and the discount percentage as input

original_price = float(input("Enter the Original price of the Product: "))
discount = int(input("Enter the discount percentage: "))
discounted_price = (original_price * discount) / 100
final_price = original_price - discounted_price

print(f"Product Original Price: {original_price}")
print(f"Discount given: {discount}%")
print(f"Discount amount: {discounted_price}")
print(f"Final Product price after {discount}% discount is: {final_price}")

#######################################################################
# BMI Calculator:
# Write a program that calculates the Body Mass Index (BMI) using the 
# formula: BMI = weight (kg) / (height (m))^2. The program should take 
# weight and height as input.

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi}") 