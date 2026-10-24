#syntax
# for variable in sequence:
    # code to be executed

#for loop is used to iterate over a sequence or iterable objects

# emp_data = ["Vasu","kiran","raju","ravi","ram"]
# for i in emp_data:
#     print(f"{i} welcome to pythonlife")


# sentence = "pythonlife"
# for i in sentence:
#     print(f"hello everyone... {i}")


# Syntax:
# range(stop)
# range(start, stop)
# range(start, stop, step)


# for i in range(10):
#     print(i)


# for i in range(99,1000):
#     print(f"number {i}")


# for i in range(1,11,4):
#     print(i)

# for i in range(49,100,3):
#     print(i)


#Multiplication of Tables
# for i in range(1,11):
#     print(f"2 X {i} = {i*2}")


# for i in range(1,11):
#     print(f"17 X {i} = {17*i}")


# table = int(input("enter the table number: "))
# for i in range(1,21):
#     print(f"{table} X {i} = {table * i}")



#nested for loop
# for var in seq:#outer for loop
#     for var2 in seq:#inner for loop



# for i in range(3):#outer for loop
#     for j in range(3):#inner for loop
#         print(i,j)




# for i in range(3):
#     print(i)


# print("-"*20)


# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} X {j} = {i*j}")
#     print("-"*25)
#     print("-"*25)



# while condition:
    # code to be executed

# age = 35
# while age>=18:
#     print("you are eligible to vote")

# count = 0
# while count<3:
#     print(count)
#     count +=1 #eq--> count = count + 1

# while True:
#     username = input("enter the username: ") 
#     password = input("enter the username: ") 
#     if username == "pavan" and password == "pavan@1234":
#         print(f"login success......")
#         print(f"welcome {username}")
#         break
#     else:
#         print(f"invalid login credentials...")



# while cond:
#     while cond:


# while True:#outer while
#     print(f"welcome to pythonlife")
#     print(f"hello everyone")
#     while True:#inner while 
#         print(f"hiiiiiiiiiiiii everyone")
#         print(f"join zoom session")
#         break
#     break



# for i in range(1,11): 
#     user_name = input("enter the username: ")
#     print(user_name)


# while True:
#     user_name = input("enter the username:")
#     print(user_name)
#     if user_name == "stop":
#         break



# Exercise 1: Sum of Squares
# Write a Python program that calculates and prints the sum of the squares of numbers from 1 to 5 using a for loop.

# sum = 0
# for i in range(1,6):
#     result = i**2
#     sum += result
#     print(f"{i} squares {result} ")

# print(f"sum of squares {sum}")

# count = 5
# while count>=1:
#     print(count)
#     count-=1


# Write a Python program to print the multiplication table for a user-specified number using a nested for loop.
# table = int(input("enter the table number: "))
# for i in range(1,11):
#     for j in range(1,2):
#         print(f"{table} X {i} = {table*i}")




# for j in range(1,2):
#     print(j)

# Write a Python program that uses a "for" loop to find the sum of all even numbers between 0 and 10 (inclusive).


# for i in range(11):
#     if i%2==0:
#         print(i)

#  Calculate the sum of all numbers from 1 to a given number

# user_number = int(input("enter the number: "))
# sum = 0
# for i in range(1,user_number+1):
#     sum += i
# print(sum)

# Display numbers from -10 to -1 using for loop
# for i in range(-10,11):
#     print(i)




