#napisz 2 funcje

# add_dots
#remove_dots

#przyjma one napis jako parametr
#pierwsza z nich ,a wstawic kropki pomiedzy znaki, np
#add_dots('text')-> t.e.x.t

#druga
#remove_dots('t.e.x.t.')-> text

def add_dots(napis):
    return ".".join(napis)



def test_add_dots():
    assert add_dots("text")=="t.e.x.t."


def test_remove_dots():
    assert remove_dots("t.e.x.t.")=="text"