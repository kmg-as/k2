# Napisz funkjce largest_difference, ktora przyjmie liste elementów i zwroci najwieksza roznice miedzy nimi
#
# larges_differrence([1,2,3,10])==9
#
# napisz funkcje largest_differenc2, ktora zadziala podobnie ale
# argumenty podajemy osobno a nie w liscie

def largest_difference(elements):
    if elements:        #prawda, gdy element jest niepusty
        return max(elements)- min(elements)
    return

def largest_difference2(*elements):
    if elements:  # prawda, gdy element jest niepusty
        return max(elements) - min(elements)
    return



def test_largest_difference():
    assert largest_difference([1,2,3,10])==9
    assert largest_difference([]) is None
    assert largest_difference([1]) ==0


def test_largest_difference2():
    assert largest_difference2(1,2,3,10)==9
    assert largest_difference2() is None
    assert largest_difference2(1) ==0

