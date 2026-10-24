#Syntax:
# if condition:
#      statement 1
#      statement 2
#      statement n
# age = 14
# if age>=18:
#     user = input("enter the username: ")
#     print(user)
#     print(f"you are elgible to vote {user}")

# print(f"outside block of code")

# Syntax:
# if condition:
#     # code block to execute if condition is true
# else:
#     # code block to execute if condition is false

# username = "bhaskar"
# password = "bhaskar@1234"
# if username == "bhaskar" and password == "bhaskar@1234":
#     print(f"login success......")
#     print(f"welcome {username}")
# else:
#     print(f"invalid login credentials...")


# Syntax:
# if condition-1:  
#      statement 1
# elif condition-2:
#      stetement 2
# elif condition-3:
#      stetement 3
#      ...        
# else:            
#      statement
#GRADING SYSTEM
# marks = int(input("enter the marks: "))
# if marks>=90 and marks<=100:
#     print(f"you got A grade obtained marks {marks}")
# elif marks>=80:
#     print(f"you got B grade obtained marks {marks}")
# elif marks>=70:
#     print(f"you got C grade obtained marks {marks}")
# elif marks>=35:
#     print(f"pass you got {marks} marks")
# elif marks<=34 and marks>0:
#     print(f"failed..... obtained marks {marks}")
# else:
#     print(f"enter postive marks")


# marks = int(input("enter the marks: "))
# if marks>100 or marks<0:
#     print(f"please enter marks between 0-100")
# elif marks>=90:
#     print(f"you got A grade obtained marks {marks}")
# elif marks>=80:
#     print(f"you got B grade obtained marks {marks}")
# elif marks>=70:
#     print(f"you got C grade obtained marks {marks}")
# elif marks>=35:
#     print(f"pass marks {marks}")
# else:
#     print(f"failed..............")




# Syntax:
# if condition1:#outer condition
#     # code block for condition1
#     if condition2:#inner condition
#         # code block for condition2
#     else:
#         # code block for condition2 being false
# else:
#     # code block for condition1 being false

# user_name = input("enter the username: ")
# password = input("enter the password: ")
# if user_name == "gagan":
#     if password == "gagan@123":
#         print(f"login success")
#         print(f"welcome {user_name}")
#     else:
#         print(f"invalid password")
# else:
#     print(f"invalid username")

# num_1 = int(input("enter the number:"))
# if num_1%2==0:
#     print(f"{num_1} even number")
# else:
#     print(f"not an even number")
# Syntax:
# result = value_if_true if condition else value_if_false
# num_1 = int(input("enter the number:"))
# result = "even number" if num_1%2==0 else "not even"
# print(result)
# num_1 = int(input("enter the number:"))
# print(f"{num_1} is even") if num_1%2==0 else print(f"not even")

# Vowel Checker:
# Write a Python program that takes a character as input and checks whether it is a vowel or not. Use the if-else statement.

# char = input("enter the character")
# if char=="a" or char == "e" or  char=="i" or char == "o":
#     print(f"vowel")
# else:
#     print("not vowel")

# char = input("enter the character: ")
# if char in "aeiouAEIOU":
#     print(f"vowel")
# else:
#     print("not vowel")