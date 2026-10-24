# Coding Exercise:
# 1. Create a Tuple: Write a program that creates a tuple containing three elements: 
# your name, your age, and your favorite color. Then print the  tuple.

my_tuple = ("Navya", 28, "Black")
print(my_tuple)

##############################################################################
# 2. Access Tuple Elements: Write a program that creates a tuple containing the days of the week. 
# Then, print the third element of the tuple.

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(days[2])

##############################################################################
# 3. Tuple Concatenation: Write a program that creates two tuples, one containing odd numbers from 1 to 5 
# and another containing even numbers from 2 to 6. Concatenate these two tuples and print the result.

odd_num = (1,3,5)
even_num = (2,4,6)
print(odd_num+even_num)

##############################################################################
# 4. Tuple Unpacking: Write a program that defines a tuple containing the dimensions of a rectangle (length and width).
# Then, unpack this tuple into two variables and calculate the area of the rectangle.

dimensions = (10,5)
length, width = dimensions
area = length * width
print(area)

##############################################################################
# 5. Check if an Element Exists: Write a program that checks if a given element exists in a tuple

vowel = ('a','e','i','o','u','A','E','I','O','U')
char = input("Enter any character: ")
print(char in vowel)

##############################################################################
# 6. Write a Python program to generate a bill for a supermarket purchase. 
# The program should store the items and their prices in a list of tuples. 
# It should then iterate over this list to print out each item along with its price. 
# Finally, calculate and print the total cost of all the items
# Sample Input: items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
# Sample Output:
# Item              Price
# ------------------------
# Apple             99.00
# Banana            99.00
# Milk              49.00
# -------------------------
# Total             247.00

items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
total = 0
print(f"Item\t\tPrice")
print("-"*25)

for i,j in items:
    print(f"{i}\t\t{j:.2f}")    
    total += j

print("-"*25)
print(f"Total\t\t{total:.2f}")
    
