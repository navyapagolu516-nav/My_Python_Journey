#Division by zero

try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print(f"Division if given two numbers is: {num1/num2}")
except ZeroDivisionError as e:
    print(e)

    

####################################################################
#ValueError

# try:
#     age = int(input("Enter your age: "))
# except ValueError as e:
#     print(e)

# if age>=18:
#         print("Eligible for voting")
# else:
#         print("Not eligible for voting")