def largest_difference(elements):
    return max(elements)- min(elements)

def test_largest_difference():
    assert largest_difference([1,2,3])==2