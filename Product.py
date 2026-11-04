#Creating Products (Blueprint)
class Product:
    def __init__(self, name, itemid, price, stock):
        self.name = name
        self.itemid = itemid
        self.price = price
        self.stock = stock
        self.iteminfo = (self.name,self.price,self.stock)

    #Displays the information
    def __str__(self):
        return f"Product ID: {self.itemid}\nProduct Name: {self.name}\nPrice: {self.price}\nStock: {self.stock}\n"

    #Formats Product Details into dictionary format to load as json as Object cannot be stored in JSON
    def to_dict(self):
        return{"id": self.itemid, "name": self.name, "price": self.price, "stock": self.stock}

class PhysicalProduct(Product):
    def __init__(self, name, itemid, price, stock, weight):
        super().__init__(name,itemid,price,stock)
        self.weight = weight

    def display_information(self):
        return f"Product ID: {self.itemid}\nProduct Name: {self.name}\nPrice: {self.price}\nStock: {self.stock}\nWeight: {self.weight}"

class DigitalProduct(Product):
    def __init__(self, name, itemid, price, stock, download_size):
        super().__init__(name,itemid,price,stock)
        self.download_size = download_size

    def display_information(self):
        return f"Product ID: {self.itemid}\nProduct Name: {self.name}\nPrice: {self.price}\nStock: {self.stock}\nDownload Size: {self.download_size}"
