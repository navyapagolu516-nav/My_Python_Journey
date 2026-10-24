# Build a Python-based supermarket billing system that allows users to view a list of products, 
# add items to their cart, calculate the total bill with tax, and display a receipt.

# Functional Requirements:

#     User Interaction:
#         The system should ask for the customer’s name.
#         Display a list of available products with their prices.
#         Allow users to add multiple items to their cart.
#         Validate that the quantity entered is a valid number.
#         Display an itemized bill with total and tax before exiting.

#     Product Catalog:
#         Maintain a dictionary of products and their prices.
#         Display the product list when requested.

#     Billing and Calculations:
#         Compute the total price based on item quantities.
#         Apply a 12% tax on the total amount.
#         Display a detailed invoice with:
#             Item name
#             Quantity
#             Price per unit
#             Total price for each item
#             Total amount before and after tax

#     Receipt Format:
#         Display a well-formatted bill with store name, location, and transaction details.

#     Exit Mechanism:
#         Allow users to exit the purchase process at any time.
#         Display a "Thank you" message upon exiting.

username = input("Please Enter your Name: ")
total = 0
cart = {}

while True:
    print("-"*40)
    print("Enter 1 to buy the products, 2 for exit")
    print("-"*40)
    print("List of Available Products")
    print("-"*40)
    products = {
        "rice"      :   (50, "kg"),
        "sugar"     :   (20, "kg"),
        "oil"       :   (115, "ltr"),
        "bread"     :   (40, "piece"),
        "toordal"   :   (50, "kg")
    }
    for i,j in products.items():
        unit_price, unit = j
        print(f"{i}\t:   {unit_price}/{unit}")
        
    print("-"*40)
    option = int(input("Enter your option: "))

    if option == 1:
        item = input("Enter the item you want to purchase: ").lower()
        if item in products:
            quantity = input("Enter the quantity: ")
            if quantity.isdigit():
                unit_price, unit = products[item]
                price = int(quantity) * unit_price
                print(price)
                total += price
                if item in cart:
                    cart[item] += int(quantity)
                else:
                    cart[item] = int(quantity)
            else:
                print("Please enter valid number: ")
        else: 
            print("Item not found")
            
    elif option == 2:
        print("="*60)
        print("\t\t\t  ABC SUPERMART")
        print("\t\t\tHyderabad, India")
        print("="*60)
        print(f"Customer Name : {username}")
        print(f"Date : 07-10-2026")
        print(f"Bill No : 1001")
        print("="*60)
        print(f"Item\t\tQty\t\tPrice\t\tTotal")
        print("="*60)
        for item, quantity in cart.items():
            unit_price, unit = products[item]
            price = int(quantity) * unit_price
            print(f"{item}\t\t{quantity}\t\t{unit_price:.2f}/{unit}\t{price:.2f}")
        print("="*60)
        print(f"Total Amount\t\t\t\t\t{total:.2f}")
        tax = (total * 12)/100
        print(f"Tax(12%)\t\t\t\t\t{tax:.2f}")
        print("-"*60)
        print(f"Final Price\t\t\t\t\t{total+tax:.2f}")
        print("-"*60)
        print("Thank you! Visit again...")
        break
    else:
        print("Invalid option. Please try again.")


    


