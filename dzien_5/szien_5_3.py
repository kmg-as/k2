def only_ints(a, b):
    return type(a) == int and type(b) == int


def test_only_ints():
    assert only_ints(1,2) == True
    assert only_ints(1,True) == False
    assert only_ints('a',1) == False
