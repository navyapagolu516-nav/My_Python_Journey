#Practice using classes and objects by writing a program to create Laptop object.

class Laptop:
    def __init__(self, brand, color, ram, price):
        self.brand = brand
        self.color = color
        self.ram = ram
        self.price = price
    def laptop_details(self):
        print(f"""Laptop Specifications 
              Brand : {self.brand}, 
              Color : {self.color}, 
              Ram : {self.ram}, 
              Price : {self.price}""")

obj = Laptop("Mac", "White", "32GB", 69000)
obj.laptop_details()



