# importing tabulate module
from tabulate import tabulate

# creating class Shoe
class Shoe:
    # defining constructor with list
    def __init__(self):
        self.products = []

    # defining method to read data using try except
    def read_data(self):
        # try to open text file and extract key for dictionary
        try:
            f = open("inventory.txt", "r")
            keys = next(f).strip().split(",")
            for line in f:
                self.products.append(dict(zip(keys, line.strip().split(","))))
        # except to display error message
        except FileNotFoundError:
            print("File not found: inventory.txt")

    # method to resotck
    def restock(self):
        lowest_quantity = None
        lowest_product = None
        for product in self.products:
            if lowest_quantity is None or int(product["Quantity"]) < lowest_quantity:
                lowest_quantity = int(product["Quantity"])
                lowest_product = product
        if lowest_product != None:
            product['Quantity'] = 100
            print(lowest_product)

    # method to define sale using for loop and if statement to compare highest_quant
    def sale(self):
        highest_quantity = None
        
        for product in self.products:
            if highest_quantity is None or int(product["Quantity"]) < highest_quantity:
                highest_quantity = int(product["Quantity"])
        
        if product != None:
            product["Cost"] = float(product["Cost"]) * .75

    def value_per_item(self):
        for product in self.products:
            product["Value"] = float(product["Cost"]) * int(product["Quantity"])

def search(shoes, code):
    # creating empty list found
    found = []
    # for loop to iterate through products
    for shoe in shoes:
        for product in shoe.products:
            if product["Code"] == code:
                found.append(shoe)
                break
    return found


shoes = []
# empty list var to append class object
for i in range(5):
    shoe = Shoe()
    shoe.read_data()
    shoe.value_per_item()
    
    shoes.append(shoe)
shoe.restock()
# using the tabulate module to display with according headers 
print(tabulate(shoes[0].products, headers={"Country": "Country", "Code": "Code", "Product": "Product", "Cost": "Cost", "Quantity": "Quantity"}))