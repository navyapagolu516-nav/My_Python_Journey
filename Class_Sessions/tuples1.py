# tuple_1 = ()
# print(tuple_1)
# print(type(tuple_1))


# tuple_2 = tuple()
# print(tuple_2)
# print(type(tuple_2))

# tuple_3 = (35,5.7,"pythonlife",True,[1,2,3],(1,23,4,5.7),25,25,)
# print(tuple_3)



# var = value
# a = 35
# print(a)

# a = 1,2,3,4,5,5.7,True,[1,2,4],{1,2,3}
# print(a)
# print(type(a))

# a,b,c,d = 1,2,3,4
# print(a)
# print(b)
# print(c)
# print(d)


# a=b=c=d = 35
# print(a)
# print(b)
# print(c)
# print(d)


# num_1 = 10 
# num_2 = 30 
# num_1,num_2 = num_2,num_1
# print(num_2)#10
# print(num_1)#30

# sample = (5,"pythonlife",True,[1,2,3,4],5.7)
# print(len(sample))


# sample = (5,"pythonlife",True,[1,2,3,4],5.7)
# print(sample.index(5))

# numbers = (1, 2, 3, 1, 4, 1)
# count_of_ones = numbers.count(1)
# print(count_of_ones)
# count_of_ones will be 3


# numbers = (1, 2, 3, 1, 4, 1)
# print(numbers[2])
# print(numbers[1:4])
# print(numbers[::-1])

# tuple1 = (1, 2, 3)
# tuple2 = ('a', 'b', 'c')
# obj = tuple1+tuple2
# print(obj)


# tuple1 = (1, 2, 3)
# print(tuple1*4)


# fruits = ('apple', 'banana', 'orange')
# is_apple_present = 'apple' in fruits
# print(is_apple_present)
# is_apple_present will be True


# sample = (1,2,3,4,5,)
# print(all(sample))


# sample = ()
# print(all(sample))


# Write a Python program to generate a bill for a supermarket purchase. The program should store the items and their prices in a list of tuples. It should then iterate over this list to print out each item along with its price. Finally, calculate and print the total cost of all the items

# Item		Price
# --------------------
# Apple		99.00
# Banana	99.00
# Milk		49.00
# --------------------
# Total		247.00

# items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
# print(f"Item\tPrice")
# print("-"*20)
# total = 0
# for i,j in items:
#     print(f"{i}\t{j}")
#     total +=j
# print("-"*20)
# print(f"Total\t{total}")