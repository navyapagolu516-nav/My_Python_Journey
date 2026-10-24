# Task 1: Add Function
# Write a Python function named "add"  that takes two arguments a and b and returns their sum.

def add(a,b):
    return a+b
print(f"Addition of 1 and 2 is: {add(1,2)}")

#######################################################################
# Task 2: Square Function
# Write a Python function named square that takes a number x as input and returns its square.

def square(x):
    return x**2
print(f"Square of 5 is: {square(5)}")

#######################################################################
# Task 3: Factorial Function
# Write a Python function named factorial that takes a positive integer n as input and returns its factorial.

def factorial(n):       # 5! = 5*4*3*2*1 = 120
    result = 1
    for i in range(1,n+1):
        result = i * result
    return result
print(f"Factorial of 5 is: {factorial(5)}")

#######################################################################
# Task 4: Maximum Function
# Write a Python function named maximum that takes a list of numbers as input and returns the maximum value in the list.

def maximum(a):
    largest = a[0]
    for i in a:
        if i > largest:
            largest = i
    return largest

a = [1,2,3,4,5,6]
print(f"Maximum value in the list is: {maximum(a)}")

##################################################################################
# Task 5: Reverse Function
# Write a Python function named reverse that takes a string s as input and returns its reverse.

def reverse(s):
    s = s[::-1]
    return s

s = "Welcome to PythonLife"
print(f"Reverse of '{s}' is: {reverse(s)}")

##################################################################################
# Task 6: Check Prime Function
# Write a Python function named is_prime that takes a positive integer n as input and returns True if n is prime, otherwise False

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter any number: "))
print(f"Is {n} prime? {is_prime(n)}")

##################################################################################
# Task 7: Fibonacci Function 
# Write a Python function named fibonacci that takes a positive integer n as input and returns nth Fibonacci number.

def fibonacci(n):
    if n<=0:
        print("Invalid Entry")
        return
    
    a = 0
    b = 1    
    for i in range(n):
        next_num = a + b
        a = b
        b = next_num
    return a

print(f"Fibonacci of 8 is: {fibonacci(8)}")

##################################################################################
# Task 8: Palindrome Function
# Write a Python function named is_palindrome that takes a string s as input and returns True if s is a palindrome, otherwise False.

def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False

s = input("Enter any string: ")
print(f"Is '{s}' a palindrome? {is_palindrome(s)}")

##################################################################################
# Task 9: Sum of Squares Function
# Write a Python function named sum_of_squares that takes a list of numbers as input and returns the sum of the squares of those numbers.

def sum_of_squares(x):
    total =0
    for i in x:
        result = i**2
        total += result
    
    return total

x = [1,2,3,4,5,6]
print(f"Sum of squares of {x} is: {sum_of_squares(x)}")

##################################################################################
# Task 10: Average Function
# Write a Python function named average that takes a list of numbers as input and returns the average value.

def average(x):
    total = 0
    for i in x:
        total += i
    avg = total/len(x)
    return avg

x = [1,2,3,4,5,6]
print(f"Average of {x} is: {average(x)}")



