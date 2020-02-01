#napisz funkcje o nazwie: only_ints
#ktora przyjmie argument 2 a i b
#i zwroci ntrue jesli oba sa intami
# w przeciwnym razie zwrci flse
from typing import Any, Union


def only_ints(a,b):
    return type(a)=="int" and type(b)=="int"



def test_only_ints_1():
    assert only_ints(1,2)==True

def test_only_ints_2():
    assert only_ints("a",2)==False

def test_only_ints_3():
    assert only_ints("a",True)==False
