# Napisz funkjce, ktora przjmie dwa argumenty - dwie liczby
# i zwroci info, czy pierwszy argument jest podzielny przez drugi
#
# Pozwól na podanie 1 argumentu - wtedy domyslnie sprawdzamy czy dzielnikiem jest 2
#
# div(10,5)->true
# div(10,3)-> false
#
# div(10)-> true

def div(a,b=2): #wartosc domyslna, gdy nie podane. Jesli podane - bedzie podane
    if b is None:
        return a%2==0
    else:
        return a%b ==0


def test_div():
    assert div(10,5) is True
    assert div(10,3) is False
    assert div(10) is True
