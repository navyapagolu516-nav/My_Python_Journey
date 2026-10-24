# Coding exercises:
# Write a Python function square_all(numbers) that takes a list of numbers as input 
# and returns a new list containing the square of each number in the input list. 
# Use the map() function with a lambda function to implement this.

#Using map()
# def square_all(a):
#     return a**2
# numbers = [1,2,3,4,5]
# result = map(square_all, numbers)
# print(list(result))

# #map() using lambda function
# numbers = [1,2,3,4,5]
# result = map(lambda a: a**2, numbers)
# print(list(result))

####################################################################
# Write a Python function 
# filter_positive(numbers) that takes a list of numbers as input 
# and returns a new list containing only the positive numbers from the 
# input list. Use the filter() function with a lambda function to implement this.

#filer()
# numbers = [1,2,3,4,5, -1, -2, -3]
# def filter_positive(numbers):
#     return numbers >= 0
# result = filter(filter_positive, numbers)
# print(list(result))

# #filter() using lambda()
# numbers = [1,2,3,4,5, -1, -2, -3]
# result = filter(lambda a: a>=0, numbers)
# print(list(result))

#####################################################################
# Write a Python function calculate_factorial(n) that calculates the factorial of a given number n. 
# Use the reduce() function with an appropriate lambda function to implement this

# from functools import reduce
# # def calculate_factorial(n):
# #     result = 1
# #     for i in range(1,n+1):
# #         result *= i
# #     return result


# number = int(input("Enter a number to find the Factorial: "))
# result = reduce(lambda a,b : a*b, range(1,number+1),1)
# print(result)

#####################################################################
# Write a Python function count_vowels(string) that takes a string as input and 
# returns the count of vowels (a, e, i, o, u) in the input string. Use the reduce() 
# function with an appropriate lambda function to implement this

# from functools import reduce
# var = input("Enter any string: ")
# vowels = ['a','e','i','o','u','A','E','I','O','U']
# result = reduce(lambda count, char: count + (1 if char in vowels else 0), var, 0)
# print(result)





