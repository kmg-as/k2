class Osoba:
    def __init__(self,imie):
        self.imie=imie

    def __str__(self):
        return f"<Osoba {self.imie}>"

os1=Osoba("Rafał")

os2=Osoba("Ania")


print(os1)
print(os2)
print(dir(os1))
print(type(os1))