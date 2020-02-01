#napisz funkcje double_letters
# ktora bedzie analizowac napis i sprawdzac czy zawiera powtarzajace sie litery.
# jesli tak zwraca true. w przeciwnym wypadku false

def double_letters(text):
    for i in range(len(text)-1):
        if text[i]==text[i+1]:
            return True
    return False


def test_double_letters():
    assert double_letters('ala')==False
    assert double_letters("alla")==True