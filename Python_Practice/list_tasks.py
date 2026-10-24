# Task 1:
# Reverse List:
# Write Python code to reverse the order of elements in the given list 
# Print the reversed list. my_list = [10, 20, 30, 40, 50, 11]
#Output should be: [11,50,40,30,20,10]

my_list = [10, 20, 30, 40, 50, 11]
rev = my_list[::-1]
print(rev)

###################################################################
# Task 2: 
# Common Elements: Given two lists them. list1 and list2 ,find and print the common elements between 
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# Output should be: [4, 5]

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = []
for i in list1:
    for j in list2:
        if i == j:
            result.append(i)
print(result)
###################################################################
# Task 3:
# Unique Elements: Create a new list unique_list containing only the unique elements from the 
# given list original_list . Print the unique list.
# original_list = [1, 2, 2, 3, 4, 4, 5]
# Output should be: [1, 2, 3, 4, 5]

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for i in original_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)
###################################################################
# Task 4:
# Remove Duplicates: 
# Remove duplicate elements from the given list duplicated_list and 
# print the list without duplicates while preserving the order.
# duplicated_list = [1, 2, 2, 3, 4, 4, 5]
# Output should be: [1, 2, 3, 4, 5]

duplicated_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for i in duplicated_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

###################################################################
# Exercise 1: List Concatenation
# Write a Python script that concatenates two lists and prints the result

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(list1+list2)

###################################################################
# Exercise 2: List Repetition
# Write a Python script that repeats a list three times and prints the result.

list1 = [1, 2, 3, 4, 5]*3
print(list1)
###################################################################
# Exercise 3 List Removal
# Write a Python script that removes the elements at even indices from a list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[1::2])
###################################################################
# Exercise 4: List Insertion
# Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list[0:0] = [10, 11, 12]
print(list)
###################################################################
# List comprehensions
# 1. Square Numbers: Create a list of squares of numbers from 1 to 10.

squares = [x**2 for x in range(1,11)]
print(f"Squares of numbers from 1 to 10 is : {squares}")
###################################################################
# 2. Even Numbers: Generate a list of even numbers from 1 to 20

even = [x for x in range(1,21) if x%2==0]
print(f"even numbers from 1 to 20 : {even}")
###################################################################
# 3. Words Lengths: Given a list of words, create a list containing the lengths of each word.
# words = ["apple", "banana", "cherry", "date"]

words = ["apple", "banana", "cherry", "date"]
length = [len(word) for word in words]
print(f"length of each word : {words} : {length}")
