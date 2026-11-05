#Imports
from abc import ABC, abstractmethod
import math

#Interface
class CanBeShipped():
    @abstractmethod
    def calculate_shipping_cost(self):
        pass


#Creating Products(Blueprint)
class Product:
    def __init__(self, name, itemid, price, stock):
        self.name = name
        self.itemid = itemid
        self.price = price
        self.stock = stock
        self.iteminfo = (self.name,self.price,self.stock)

    #Displays the information
    @abstractmethod
    def display_information(self):
        return f"Product ID: {self.itemid}\nProduct Name: {self.name}\nPrice: {self.price}\nStock: {self.stock}\n"

    def __str__(self):
        return self.display_information()

    @abstractmethod
    def get_fulfilment_info(self):
        pass


    @abstractmethod
    #Formats Product Details into dictionary format to load as json as Object cannot be stored in JSON
    def to_dict(self):
        return{"id": self.itemid, "name": self.name, "price": self.price, "stock": self.stock}

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, name, itemid, price, stock, weight):
        super().__init__(name,itemid,price,stock)
        self.weight = weight

    def display_information(self):
        base = super().display_information()
        return base + f"Weight: {self.weight}"

    def get_fulfilment_info(self):
        return f"This product requires physical shipping."

    def calculate_shipping_cost(self):
        if self.weight > 200:
            shipping_cost = math.ceil(self.weight/200) * 3.50
        else:
            shipping_cost = 3.50
        return f"The shipping cost of {self.name} is ${shipping_cost:.2f}"

class DigitalProduct(Product):
    def __init__(self, name, itemid, price, stock, download_size):
        super().__init__(name,itemid,price,stock)
        self.download_size = download_size

    def display_information(self):
        base = super().display_information()
        return base + f"Download Size: {self.download_size}"

    def get_fulfilment_info(self):
            return f"This product will be delivered digitally."


book = PhysicalProduct("Dictionary", "P006", 20.0, 50, 2000.05)
ebook = DigitalProduct("Online Article", "P007", 5.0, 50, 300)
print(book.calculate_shipping_cost())

#print(ebook.get_fulfilment_info())