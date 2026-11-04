#Creating Products (Blueprint)
class Product:
    def __init__(self, name, itemid, price, stock):
        self.name = name
        self.itemid = itemid
        self.price = price
        self.stock = stock
        self.iteminfo = (self.name,self.price,self.stock)

    #Displays the information
    def display_information(self):
        return f"Product ID: {self.itemid}\nProduct Name: {self.name}\nPrice: {self.price}\nStock: {self.stock}\n"

    def __str__(self):
        return self.display_information()

    #Formats Product Details into dictionary format to load as json as Object cannot be stored in JSON
    def to_dict(self):
        return{"id": self.itemid, "name": self.name, "price": self.price, "stock": self.stock}

class PhysicalProduct(Product):
    def __init__(self, name, itemid, price, stock, weight):
        super().__init__(name,itemid,price,stock)
        self.weight = weight

    def display_information(self):
        base = super().display_information()
        return base + f"Weight: {self.weight}"

class DigitalProduct(Product):
    def __init__(self, name, itemid, price, stock, download_size):
        super().__init__(name,itemid,price,stock)
        self.download_size = download_size

    def display_information(self):
        base = super().display_information()
        return base + f"Download Size: {self.download_size}"


book = PhysicalProduct("Dictionary", "P006", 20.0, 50, 30.05)
ebook = DigitalProduct("Online Article", "P007", 5.0, 50, 300)
print(book.display_information())
print(ebook.display_information())