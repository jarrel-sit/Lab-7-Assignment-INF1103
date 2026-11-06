#Imports
from abc import ABC, abstractmethod
import math

#CanBeShipped Interface
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass


#Creating Products(Blueprint)
class Product:
    def __init__(self, name, itemid, price, stock):
        self.name = name
        self.itemid = itemid
        self._price = price
        self.stock = stock

    #Displays the information
    @abstractmethod
    def display_information(self):
        return f"Product ID: {self.itemid}\nProduct Name: {self.name}\nPrice: {self._price}\nStock: {self.stock}\n"

    def __str__(self):
        return self.display_information()

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    #Formats Product Details into dictionary format to load as json as Object cannot be stored in JSON
    @abstractmethod
    def to_dict(self):
        pass

#Physical Product Class
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, name, itemid, price, stock, weight, producttype):
        super().__init__(name,itemid,price,stock)
        self.weight = weight
        self.producttype = producttype

    def display_information(self):
        base = super().display_information()
        return base + f"Weight: {self.weight}" + f"\nProduct Type: Physical"

    def get_fulfilment_info(self):
        return f"This product requires physical shipping."

    def calculate_shipping_cost(self):
        if self.weight > 200:
            shipping_cost = math.ceil(self.weight/200) * 3.50
        else:
            shipping_cost = 3.50
        return f"The shipping cost of {self.name} is ${shipping_cost:.2f}"
    
    def to_dict(self):
        return{"id": self.itemid, "name": self.name, "price": self._price, "stock": self.stock, "weight": self.weight, "producttype": self.producttype}

#DigitalProduct Class      
class DigitalProduct(Product):
    def __init__(self, name, itemid, price, stock, download_size, producttype):
        super().__init__(name,itemid,price,stock)
        self.download_size = download_size
        self.producttype = producttype

    def display_information(self):
        base = super().display_information()
        return base + f"Download Size: {self.download_size}\n"f"Product Type: Digital"

    def get_fulfilment_info(self):
            return f"This product will be delivered digitally."

    def to_dict(self):
        return{"id": self.itemid, "name": self.name, "price": self._price, "stock": self.stock, "downloadsize": self.download_size, "producttype": self.producttype}



