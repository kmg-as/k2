sklep=dict(cebula=6, marchew=2, jabłka=2.99, banany=5)
print(sklep
      )
type=input("zakupy czy magazyn?")
if type == "zakupy":
    zakup=input(f"czego potrzebujesz ze sklepu?")
    if zakup in sklep:
        print("mamy to")
        ilosc=int(input("ile tego potrzebujesz?"))
        cena=sklep[zakup]*ilosc #to jest konstrukcja wywolywania wartosci ze slownika
        print(cena)

    else:
        print("idz gdzies indziej")
else:
    rob=input("witaj w magzynie. Co chcesz zrbić")
    if rob=="dodac":
        nowe=input(f"podaj produkt")
        co = input(f"podaj cena jedn")
        sklep[nowe]=co
        print(sklep)
    else:
        print("pa")