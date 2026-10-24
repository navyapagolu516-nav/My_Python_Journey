#syntax
# class classname():class definition
    #attr 
    #methods



# def sample():
#     return 1
# sample()


# def details(num_1):
#     print(num_1)
# details(10)






# class person_details():#class definition
#     user_name = "kiran" #attributes
#     emp_id = 1234 #attributes
#     def details(self,):#method 1
#         print(f"he works at ABC company..{self.user_name}")
#     def details2(self,): #method 2
#         print(f"he owns ABC company..")
#         self.details()
#syntax
# objname = classname()
# kiran_sagar = person_details()
# kiran_sagar.details()
# kiran_sagar.details2()
# print(kiran_sagar.user_name)
# print(kiran_sagar.emp_id)



# class feature_phone():#class definition
#     brand = "nokia" #attributes
#     color = "black"
#     model = "2015"
#     def calling(self,bn):#method 1
#         print(f"you are calling from {bn}")
#     def message(self,text):#method 2
#         print(f"{text} sent successfully...")
# nokia = feature_phone()
# nokia.calling("nokia")
# nokia.message("good morning")

# samsung = feature_phone()
# samsung.calling("samsung")

# celkon = feature_phone()
# celkon.calling("celkon")


# class feature_phone():
#     def __init__(self,brand,color,model=2012):
#         self.brand = brand
#         self.color = color
#         self.model = model
#     def calling(self,):#method 1
#         print(f"you are calling from {self.brand}")
#     def message(self,text="hi"):#method 2
#         print(f"{text} sent successfully... {self.model}")
# nokia = feature_phone("nokia","black")
# nokia.calling()
# nokia.message()

# samsung = feature_phone("samsung","black",2015)
# samsung.calling()

# celkon = feature_phone("celkon","black",2015)
# celkon.calling()




# class feature_phone():
#     def __init__(self,brand,color,model):
#         self.brand = brand
#         self.color = color
#         self.model = model
#     def calling(self,mn):
#         print(f"you are calling from {self.brand}....... {mn}")
#     def message(self,text):
#         print(f"{text} sent successfully.............")
# class smart_phones(feature_phone):
#     def capture(self,):
#         print(f"photo has been captured {self.brand}")
#     def browsing(self,browser):
#         print(f"browsing from {browser}")
# obj = smart_phones("nokia","white",2018)
# obj.calling(12348549879)
# obj.message("hi")
# obj.capture()
# obj.browsing("chrome")








#hierarchical inheritance
#one base class  --> multiple derived class 
# class a():
#     def parent(self):
#         print("this is parent class")
# class b(a):
#     def child1(self):
#         print("this is child 1 class")
#     def assests(self):
#         print(f"worth 100 cr")
# class c(a):
#     def child2(self):
#         print("this is child 2 class")

# obj1 = b()
# obj1.child1()
# obj1.assests()
# obj1.parent()

# obj2 = c()
# obj2.child2()
# obj2.parent()



# # multiple inheritance -->multiple base class one derived class
# class parent1():
#     def father(self):
#         print("this is father class")
# class parent2():
#     def mother(self):
#         print("this is mother class")
# class child(parent1,parent2,):
#     def child(self):
#         print("this is child class")
# obj = child()
# obj.child()
# obj.mother()
# obj.father()




# class gfather():
#     def output(self):
#         print(f"earned 100cr properties")
# class father(gfather):
#     def output1(self):
#         print(f"this is father class")
# class child(father):
#     def output2(self):
#         print(f"this is child class")
#     def sample(self):
#         print(f"started ABC company")

# obj = child()
# obj.output()
# obj.output1()
# obj.output2()
# obj.sample()


# class details():
#     def login(self,user,password):
#         self.__user = user
#         self.__password = password

        



# class atm():
#     def __init__(self,bank,branch,location,balance=1000):
#         self.bank = bank
#         self.branch = branch
#         self.location = location
#         self._balance = balance
#         self = []
#     def credit(self,):
#         pass
#     def debit(self,):
#         pass
# class atm2(atm):
#     def balance():
#         pass
#     def ministatement():
#         pass
# while True:
#     sbin = atm2("SBIN","tadepalligudem","railway",)
#     print("1.credit")
#     print("1.credit")
#     print("1.credit")
#     print("1.credit")
#     print("1.credit")
#     choice = input("enter choice: ")
#     if choice == "1":
#         sbin.credit()


# print --> it is used to display the info on the screen
# return --> to exit a function and return value to the caller
# yeild --> hold or pause ( to generate multiple values in the function)
# self --> used to access current class attr and methods
# __init__  --> used to initiliaze the attributes






#################  oct 13 2026  #####################
# polymorphism--> implementing same thing in different forms
# 1. overloading -->1.operator overloading 2. method overloading
# 2. method overriding

# (+)
# num_1 = 10
# num_2 = 10
# print(num_1+num_2)


# user = "python"
# user2 = "life"
# print(user+user2)


#method overloading --> method name should be same
#arguments must be different --> in the terms of length or type of arguments
# class calculator():
#     def add(self,a,b):
#         print(a,b)
#     def add(self,a,b,c):
#         print(a,b,c)
# obj = calculator()
# obj.add(10,101,10)
# obj.add("vasu",10)

#method overloading --> method name should be same
#arguments must be different --> in the terms of length or type of arguments
# class calculator():
#     def add(self,a=15,b=5,c=10):
#         print(a,b,c)
# obj = calculator()
# obj.add(10,10,10)
# obj.add(10,10)
# obj.add(10)
# obj.add()
# obj.add("vasu","kumar")
# obj.add("vasu",5.7)
# obj.add(5.7,[1,2,3])
# obj.add()




#2.method overriding
# method overriding --> method name should be same arguments should be also same
# class gfather():
#     def details(self,a):
#         print(f"this is gfather class")
# class father(gfather):
#     def details(self,a):
#         print(f"this is father class")
#         super().details("100cr")
# obj = father()
# obj.details("100cr")




# public
# protect _
# private __

# class gfather():
#     def __init__(self,a):
#         self._a = a
#         print(f"this is base class {a}")
# class father(gfather):
#     def details(self):
#         print(f"this is derived class {self._a}")
# obj = father("100cr")
# obj.details()




# class gfather():
#     def __init__(self,a):
#         self.__a = a
#         print(f"this is base class {a}")
# class father(gfather):
#     def details(self):
#         print(f"this is derived class {self.__a}")
# obj = father("100cr")
# obj.details()


#data abstraction --> hiding the implementation and showing only essential part
# 1.abstract class --> class which contain abstract methods is called abstract class
# 2.abstract method --> the method which is having only declaration but not the definition is called abstract method (hiding the implementation)
# class which does not have abstract method is called concrete class
# concrete class  --> class without abstract methods
# object cannot create for abstract class
# object can create only concrete classes
# To create abstract classes in Python, you can use the abc (Abstract Base Classes) module
# from abc import ABC,abstractmethod
# class abstract_demo(ABC):
#     @abstractmethod
#     def details(self):
#         pass
#     @abstractmethod
#     def details2(self):
#         pass
# class demo(abstract_demo):
#     def details(self):
#         print(f"implementation done 1")
#     def details2(self):
#         print(f"implementaion 2 done")
# obj = demo()
# obj.details()
# obj.details2()



# from abc import ABC, abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class gpay(payment):
#     def pay(self):
#         print(f"payment received")
# class phonepe(payment):
#     def pay(self):
#         print(f"payment received")
# class paytm(payment):
#     def pay(self):
#         print(f"payment received")
# class cred(payment):
#     def pay(self):
#         print(f"payment received")
#     def cashback(self):
#         print(f"received cashback")

# gpay1 = gpay()
# gpay1.pay()
# phonepe1 = phonepe()
# phonepe1.pay()