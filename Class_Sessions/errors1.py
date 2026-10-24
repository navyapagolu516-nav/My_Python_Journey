#types of errors
# 1.syntax errors --> (compile time errors)
# 2.runtime errors
# 3.logical errors --> (user need to identified (very difficult to find out))


# num_1 = 10
# num_2 = 5
# print(num_1-num_2)


# print(exp)
# print(10+10)


# for i in range(10):
#     print(i)



# if 10>5:
#     print("sample statement")



# runtime errors-->which disturbs the flow of execution (during the execution) also called exception



# num_1 = int(input("Enter the num_1: "))
# num_2 = int(input("Enter the num_2: "))
# print(num_1+num_2)
# print(num_1-num_2)
# try:
#     print(num_1/num_2)
# except:
#     print(f"error occured")
# print(num_1*num_2)
# print(num_1+num_2)
# print(num_1-num_2)






# num_1 = int(input("Enter the num_1: "))
# num_2 = int(input("Enter the num_2: "))
# print(num_1+num_2)
# print(num_1-num_2)
# try:
#     print(num_1/num_2)
# except:
#     print(f"error occured")
# else:
#     print(num_1*num_2)
#     print(num_1+num_2)
#     print(num_1-num_2)
# finally:
#     print("regardless statement")

# try:
#     num_1 = int(input("enter the number1: "))
#     num_2 = int(input("enter the number2: "))
# except ValueError as e:
#     print(e)
# else:
#     print(num_1+num_2)


# list_1 = [1,2,3,4,]
# print(list_1[1])
# try:
#     print(list_1[6])
# except IndexError as e:
#     print(e)
# else:
#     print(list_1[3])



# sample ={
#     1:"vasu",
#     2:"kiran",
# }
# print(sample.get(5))
# try:
#     print(sample[5])
# except KeyError as e:
#     print(e)



# a = 10
# b = "sample"
# try:    
#     print(a+b)
# except TypeError as e:
#     print(e)

try:
    num_1 = int(input("enter the number1: "))
    num_2 = int(input("enter the number2: "))
    print(num_1/num_2)
    list_1 = [10,20,30,40,50]
    print(list_1[6])
except Exception as e:
    print(e)