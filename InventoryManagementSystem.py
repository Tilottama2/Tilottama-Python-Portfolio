# Simple Inventory Management System in Python where user can add product, view product,
# view inventory, update quantity and can delete product from inventory

inventory = {}


# function to add new product
def add_product(product_id, name, price, quantity):
    if product_id not in inventory:
        inventory[product_id] = {"name": name, "price": price, "quantity": quantity}
        print("Product Added Successfully")
    else:
        print("Product Id Already Exist")


# Function to update quantity of product
def update_product_quantity(product_id, new_quantity):
    if product_id in inventory:
        inventory[product_id]["quantity"] = new_quantity
        print("Quantity Uodate successfully")
    else:
        print("Product Id Does not exist")


# Function to view product details
def view_product_details(product_id):
    if product_id in inventory:
        print("Product Id: ", product_id)
        print("Name: ", inventory[product_id]["name"])
        print("Name: ", inventory[product_id]["price"])
        print("Name: ", inventory[product_id]["quantity"])
    else:
        print("Product Id does not exist")

# Function to view entire inventory
def view_inventory():
    if inventory:
        print("Inventory")
        for product_id, details in inventory.items():
            print("Product Id: ", product_id)
            print("Name: ", details["name"])
            print("Price: ", details["price"])
            print("Quantity: ", details["quantity"])
            print()
    else:
        print("Inventory is empty")

# Function to remove product
def remove_product(product_id):
    if product_id in inventory:
        del inventory[product_id]
        print("Product removed successfully")
    else:
        print("Product id does not exist")


# Examples

add_product(1, "Laptop", 1000, 10)
add_product(2, "I Phone", 500, 15)
add_product(3, "Tablet", 700, 30)

view_inventory()

update_product_quantity(1,5)
view_product_details(1)

remove_product(2)

view_inventory()
