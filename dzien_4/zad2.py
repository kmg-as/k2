""""
napisz funkcje, ktora jako argument przyjmie liste  list
i zwroci liste bedaca ich polaczeniem

flatten([[1,2],[3,4]])-> [1,2,3,4]

dodatkowo:  sprobuj napisac funkjce ktora moze [przyjac wiele argumentow, ktore sa listami i zwroci ich polaczenie
"""


# def flatten(element):
#     result = []
#     for el in element:
#         result.extend(el)
#     return result
#
#
# def test_flatten():
#     assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def flatten(*element):
    if len(element)==1:
        element=element[0]
    result = []
    for el in element:
        result.extend(el)
    return result


def test_flatten():
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten([1, 2], [3, 4]) == [1, 2, 3, 4]