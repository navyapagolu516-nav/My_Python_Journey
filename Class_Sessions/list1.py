# sample_list = []
# print(sample_list)
# print(type(sample_list))

# sample_list_2 = [35,5.7,True,"pythonlife",[1,2,3,],(1,2,3),24,24,24]
# print(sample_list_2)
# print(type(sample_list_2))


# sample_list_3 = list()
# print(sample_list_3)
# print(type(sample_list_3))




# my_list = [10, 20, 30, 40, 50]
#syntax
# seq[indexvalue]
# print(my_list[2])#30
# print(my_list[0])#10
# print(my_list[4])#50


 

# my_list = [10, 20, 30, 40, 50]
# print(my_list[-3])
# print(my_list[-2])
# print(my_list[-5])



# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# # seq[s:s:s]
# print(my_list[0:8])
# print(my_list[3:6])
# print(my_list[1:3])


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[0:8:1])
# print(my_list[::])
# print(my_list[5:])
# print(my_list[:3])




# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[3:6])
# print(my_list[-5:-2])
# print(my_list[-8:-5])
# print(my_list[-3:])



# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[3::-1])#[40, 30, 20, 10]
# print(my_list[-5::-1])#[40, 30, 20, 10]
# print(my_list[6:4:-1])#[70, 60]
# print(my_list[-2:-4:-1])#[70, 60]
# print(my_list[7:2:-1])#[80, 70, 60, 50, 40]
# print(my_list[:-6:-1])#[80, 70, 60, 50, 40]


# sample = [1,2,3,4]



# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[1][2])
# print(matrix[0][2])
# print(matrix[2][0])
# print(matrix[2][2])


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
#method syntax
# var.methodname(arg)#arguments--> values


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.append([1,2,3,4,])
# print(numbers)


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.extend([1,2,3,4,5,6])
# print(numbers)


# numbers.copy()             # Returns the shallow copy of the list

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# sample = numbers.copy()
# sample.append("pythonlife")
# print(sample)
# print(f"original list {numbers}")



# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.clear()
# print(numbers)


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(numbers.count("pythonlife"))


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(numbers.index(5))

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.remove(5)
# print(numbers)


# list_1 = [10,20,30,40]
# list_1.remove(20)
# print(list_1)



# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# sample = numbers.pop(2)
# print(numbers)
# print(sample)



# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.insert(0,4854)
# print(numbers)


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.reverse()
# print(numbers)



# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.sort(reverse=True)
# print(numbers)



# Syntax
# [exp for item in seq/iter if cond]


# for i in range(11):
#     if i%2==0:
#         print(type(i))


# empty_list = []
# for i in range(11):
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)



# # [exp for item in seq/iter if cond]
# result = [i for i in range(11) if i%2==0]
# print(result)


# print([i for i in range(11) if i%2==0])


# empty_list = []
# for i in range(11):
#     result = i**2
#     empty_list.append(result)
# print(empty_list)

# # [exp for item in iter ]
# result = [i**2 for i in range(11)]
# print(result)

# print([i**2 for i in range(11)])


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(len(numbers))



#remove
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,5,5,555,4,7,5,5,5,5.4,1,2,4,5,7,5,5,5,3,5,5,5,5]
# numbers.remove(5)
# print(numbers)



# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,555,4,7,5,5,5,5.4,1,2,4,5,7,5,5,5,3,5,5,5,5]
# for i in numbers:
#     if i == 5:
#         numbers.remove(i)
# print(numbers)


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,5,5,555,4,7,5,5,5,5.4,1,2,4,5,7,5,5,5,3,5,5,5,5]
# empty_list = []
# for i in numbers:
#     if i!=5:
#         empty_list.append(i)
# print(empty_list)


#index



# list_1 = [1, 2, 3, 4, 5]
# list_2 = [4, 5, 6, 7, 8]

# # expected_output = [4,5]

# empty_list = []
# for i in list_1:
#     for j in list_2:
#         if i == j:
#             empty_list.append(i)
# print(empty_list)





# original_list = [1, 2, 2, 3, 4, 4, 5]
# empty_list = []
# for i in original_list:
#     if i not in empty_list:
#         empty_list.append(i)
# print(empty_list)


# original_list = [1, 2, 3, 4, 5]
# print(original_list*3)