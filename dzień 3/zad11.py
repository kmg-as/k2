A=set()
odp = input("czy chcesz podać liczbę?")
licznik=0
while odp == "tak":
    liczba=input("podaj liczbę")
    A.add(int(liczba))
    odp = input("podajesz więcej liczb?")
else:
    print(f"podałeś {licznik} liczb")
print(A)
parzyste=set(range(0,101,2))
print(f"liczba unikalnych: {len(A)}, a w tym parzyste: {A&parzyste}")
