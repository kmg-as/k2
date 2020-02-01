#napisz funkcje o nazwie capital letters, ktora:
#przyjmie 1 argument-napis
#zwroci indeksy liter wielkich

def capital_letters(text):
    result=[]
        for i, letter in enumerate(text):
            if letter.isupper():
                result.append(i)
    return result

def test_capital_letters_all_small_letters():
    assert capital_letters('HeLlO')==[0,2,4]

def test_capital_letters_small_and_big_letters():
    assert capital_letters("hello")==[]


