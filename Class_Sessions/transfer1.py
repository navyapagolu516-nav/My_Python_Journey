# Syntax:
# for item in iterable:
#     if condition:
#         break

# for i in range(10):
#     if i == 3:
#         break
#     print(i)
# print(f"last iteration {i}")


# students = ["somi","rajesh","vasanth","eswari","pavan","rohit"]
# for i in students:
#     if i == "vasanth":
#         break
#     print(i)

# print(f"last iteration {i}")



# students = ["somi","rajesh","vasanth","eswari","pavan","rohit"]
# for i in students:
#     if i == "vasanth":
#         print(f"student found {i}")
#         break

# print(f"last iteration {i}")



# Syntax:
# for item in iterable:
#     if condition:
#         continue
    # code here will be skipped if the condition is met



# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
# print(f"last iteration {i}")


# product = ["ok","ok","ok","defect","ok","ok","defect","ok"]
# for i in product:
#     if i == "defect":
#         continue
#     print(i)
# print(f"last iteration {i}")





# if cond:
    #block of code

# for var in seq/iter:
    #block of code


# num_1 = 24
# if num_1%2==0:
#     pass


# for i in range(10):
#     pass
# print(f"last iteration {i}")


# **Problem 1: Using `break` in a For Loop**

# Write a Python program that takes a list of numbers as input `numbers = [25, 30, 20, 40, 15, 25]` and prints the sum of the numbers. However, if the sum exceeds 100, stop adding numbers and print "Sum exceeded 100".

numbers = [25, 30, 20, 40, 15, 25]
sum = 0
for i in numbers:
    sum+=i
    if sum>=100:
        break
print(f"sum exceeds 100")