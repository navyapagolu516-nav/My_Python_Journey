#syntax
# def functionname(): #function definition
    #block of code

# def greet():#function definition
#     print(f"welcome to pythonlife..")
# greet()#function calling
# greet()#function calling
# greet()#function calling
# greet()#function calling
# greet()#function calling


# def user():#function definition
#     user_name = input("Enter the username: ")
#     password = input("enter the password: ")
#     print(user_name)
#     print(password)
# user()#function calling


#parameters and arguments

# def add(num_1,num_2):#function definition
#     print(num_1+num_2)
# add(10,5)#function calling, here 10,5 are the arguments passed to the function parameters
# add(10,45)
# add(10,58)
# add(10,785)


# return statement --> Definition: The return statement is used to exit a function and return a value to the caller.
# def add(a,b):
#     return a+b
# obj = add(10,5)
# print(obj)




# arbitary arguments--> function can accept a variable number of arguments by using *args(syntax)


# a = 35,4,53.7,True

# def sample(*a):
#     print(a)
# sample(10,5.7,True,[1,2,3,4])


#keyword arguments :-->keyword arguments are passed to a function with a keyword and a value, allowing for more explicit parameter passing
#**

# def sample(**a):
#     print(a)
# sample(vasu = 1234,kiran=4569,raju=65149)

#*--> tuple
#**--> dictionary


#default parameter
# def details(user=None,emp_id=None,dept=None):
#     print(user,emp_id,dept)
# details("vasu",1234,"python")
# details("kiran",46789,)
# details("raju",)
# details()

# def discount(price,d=10):#function definition
#     d = (price*d)/100
#     final_price = price - d
#     return final_price
# print(discount(10000))
# print(discount(20000))
# print(discount(30000))
# print(discount(50000))
# print(discount(100000,15))


#variables --> 1.local variables(inside function) 2.global variable (outside function)

# def details():
#     user = "kiran"
#     emp_id = 1234
#     salary = 100000
#     print(user)
#     print(emp_id)
#     print(salary)
#     hike = 50000
#     salary += hike
#     print(salary)
# details()

# 2.global variable (outside  the function)

# balance = 50000
# def credit(amount):
#     global balance
#     print(f"amount credited {amount}")
#     balance += amount
#     print(f"total balance {balance}")

# credit(10000)



def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def expo(a,b):
    print(a**b)

# add(10,5)
# add(10,45)
# expo(4,2)