#Imports
from Product import PhysicalProduct,DigitalProduct
import json,os

#Inventory Class
class Inventory:
    #Initializing inventory as a list
    def __init__(self):
        self.inventory = []

    #Checks if product ID already exists when adding product to inventory, returns boolean value
    def exists(self,product_id):
        return any(item.itemid == product_id for item in self.inventory)

    #Adds Product Object into existing inventory based on boolean value from exists method
    def add_product(self, product_to_add):
       if self.exists(product_to_add.itemid):
           print ("Product already exists, not adding the product.")
           return False
       else:
           self.inventory.append(product_to_add)
           return True

    #Displays all product Objects in the inventory by printing them to terminal
    def display_all(self):
        for item in self.inventory:
            print(f"{item}\n")

    #Update stock for particular product
    def update_stock(self,updateid):
        for product in self.inventory:
            if updateid == product.itemid:
                newqty = input(f"Input the new amount of stock for this product: {product.name} \n")
                if newqty.isnumeric() == False:
                    print("Invalid Product Amount")
                else:
                    product.stock = int(newqty)
                    print(f"The New Stock Amount of {product.name} is now {product.stock} \n")
            else:
                print("Product Not Found")

    #Searches for product by ID
    def search_product(self,searchid):
        for product in self.inventory:
            if searchid == product.itemid:
                if isinstance(product,PhysicalProduct):
                    print(f"{product.display_information()}\n{product.get_fulfilment_info()}\n{product.calculate_shipping_cost()}")
                elif isinstance(product,DigitalProduct):
                   print(f"{product.display_information()}\n{product.get_fulfilment_info()}")
                break
            elif len(self.inventory) == 0:
                print("Your inventory is empty, unable to search for products.")
                break
            else:
                print("Unable to find product, ensure that you have entered product ID in the correct format.")
                break

    #Saves the inventory to json and writes it to inventory.json
    def save_inventory(self):
        data = []
        print("Saving inventory...\nInventory saved successfully to inventory.json")
        if len(self.inventory) != 0:
            for item in self.inventory:
                data.append(item.to_dict())
            with open("inventory.json", "w") as file:
                json.dump(data, file, indent = 4)
        else:
            print("You have no products in your inventory, saved anyways...")
            
    #Method to load inventory from inventory.json file if exists
    def load_inventory(self):
        self.inventory = []
        try:
            file_path = "inventory.json"
            if os.path.isfile(file_path):
                with open('inventory.json', 'r') as file:
                    data = json.load(file)
                    for i in data:
                        if i["producttype"] == "physical":
                            self.inventory.append(PhysicalProduct(i["name"], i["id"], i["price"], i["stock"], i["weight"], i["producttype"]))
                        elif i["producttype"] == "digital":
                            self.inventory.append(DigitalProduct(i["name"], i["id"], i["price"], i["stock"], i["downloadsize"], i["producttype"]))
                    print("inventory.json found and loaded successfully.")
            else:
                print("inventory.json not found, no inventory records loaded.")
                return
        #Error handling for empty json file
        except json.JSONDecodeError:
            print("However, inventory.json is empty, starting with an empty inventory...")

         

