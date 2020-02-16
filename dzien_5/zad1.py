#zaimplementuj klase produkt z info o cenie, nazwie i ID.
#zaimplemenuj metodę wypisujaca info o produkcie na konsolę

#ex: prodct=Product(1,'Woda',10.99)
#product.print_info()

#Produkt 'woda', id:1, cena: 10.99 PLN

class Product:
    def __init__(self, name, ID, cena):
        self.name=name
        self.ID=ID
        self.cena=cena
    def __str__(self):
        return f"<Product {self.name} {self.ID} {self.cena} PLN>"
    def print_info(self):
        print(f"Produkt \"{self.name}\, id: {self.ID}, cena: {self.cena}")

pr1=Product("Woda",1,10.99)
product.print_info()
print(pr1)