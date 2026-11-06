#Importing of classes from other files
from Product import PhysicalProduct,DigitalProduct
from Inventory import Inventory

#Menu Display and User Input    
def menu():
    while True:
        print('\n\tMenu\n=======================\n1. Display all products\n2. Add a product\n3. Update Stock\n4. Search for a product\n5. Save Inventory\n6. Exit\n=======================')
        option = input('> \n')
        match(option):
            #Runs display inventory method
            case "1":
                if not inventory:
                    print('Inventory is empty!')
                else:
                    inventory.display_all()
            #Runs add product method
            case "2":
                    while True:
                        try:
                            itemid = input('ID: ')
                            name = input('Name of Product: ')
                            price = float(input('Price: '))
                            stock = int(input('Stock: '))
                            producttype = str(input("Physical or Digital? ")).lower()
                            if producttype == "physical":
                                weight = float(input("Input the weight of this product "))
                                item = PhysicalProduct(name, itemid, price, stock, weight, producttype)
                                inventory._add_product(item)
                                break
                            elif producttype == "digital":
                                download_size = float(input("Input the download size of this product "))
                                item = DigitalProduct(name, itemid, price, stock, download_size, producttype)
                                inventory._add_product(item)
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print("Invalid format, please key in again")
                        

            #Runs update stock method
            case "3":
                updateid = input("Please enter the Product ID of the product that you want to update the stock for. ")
                inventory.update_stock(updateid)
            #Runs search by ID method 
            case "4":
                searchid = input("Please enter the Product ID of the product you are looking for. ")
                inventory.search_product(searchid)
            #Saving inventory to json
            case "5":
                inventory.save_inventory()
            #Save to JSON and exit
            case "6":
                inventory.save_inventory()
                break
            #Handles invalid inputs
            case _:
                print('Invalid Response, please input a value 1-6.')
            

#Loads inventory and menu if file is run
if __name__ == "__main__":
    inventory = Inventory()
    inventory.load_inventory()
    menu()
