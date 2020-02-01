import random

#random.seed(10)


"""
Napisz funkcje random number ktora nie przyjmuje anr a zwraca losowa liczbe z przedzialo 1-100
"""

def random_number():
    return random.radint(1,101)

print(random.randint(1,101))

def test_random_number():
    random.seed(0)
    assert random_number()==50
    random.seed(10)
    assert random_number()==74