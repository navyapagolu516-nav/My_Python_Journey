#syntax
# lambda arguments: expression

# def add(a,b):#function definition
#     return a+b
# obj = add(10,5)#function calling
# print(obj)

# lambda arguments: expression
# result = lambda a,b,c=10 : a+b+c
# print(result(10,5,))


# Syntax:
# filter(function, iterable)


# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# empty_list = []
# for i in list_1:
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)


# filter(func,iterable)
# def even(a):
#     return a%2==0
# obj = even(24)
# print(obj)


# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# def even(a):
#     return a%2==0
# result = filter(even,list_1)
# print(list(result))

#lambda arg:exp
# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# result = filter(lambda a:a%2==0,list_1)
# print(list(result))



# Syntax:
# map(function, iterable, ...)


# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# empty_list = []
# for i in list_1:
#     result = i**2
#     empty_list.append(result)
# print(empty_list)


# def square(a):
#     return a**2
# obj = square(4)
# print(obj)



# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# def square(a):
#     return a**2
# result = map(square,list_1)
# print(list(result))


# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# list_2 = [4,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,244,89,50,4]
# result = map(lambda a:a**2,list_1)
# print(list(result))



# list_1 = [1,2,3,4]
# list_2 = [1,2,3,4]
# result = map(lambda a,b:a**2,list_1,list_2)
# print(list(result))

#syntax
# from functools import reduce
# reduce(func,iter[intializer-->option])


# def add(a,b,c,d,e):
#     return a+b+c+d+e
# obj = add(10,5,10,10,10)
# print(obj)


# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# from functools import reduce
# def add(a,b):
#     return a+b
# result = reduce(add,list_1)
# print(result)



# list_1 = [1,2,3,4,5]
# from functools import reduce
# result = reduce(lambda a,b:a+b,list_1,)
# print(result)



# """
# generator function --  a genetor -function is defined like a normal function
# but whenever its need to generate a value it does so with the yeild keyword rather than return if body contain yield , the function  automatically becomes a generator function.
# """

# def sample():
#     yield 1#pause or hold
#     yield 2#pause or hold
#     yield "pythonlife" #pause or hold
# obj = sample()
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())


# list_1 = [23,4,5,-67,2,35,84,1,2,-3,4,5,6,7,8,-9,-10,45,18,24,89,50,4]
# result = filter(lambda a:a>=0,list_1)
# print(list(result))