# Napisz funkcje, ktora sprawdzi, czy teskt jest palindromem
# tzn czy czytany wspak jest taki sam jak czytany od poczatku
#
# zacznij od prostych palindromow jak ala, kajak
# a potem sporbuj czegos ze spacjaami, przecinkami itd
#
# palindrome("kajak")-> True
# palindrome("Kajak")->True

# palindrome("a to idiota")->true

import string

dozwolone='abc'
def palindrome(text):
    #to_replace=" ,.-?!" jesli nie uzywamy import string to w ten sposob ominiemy niepotrzebne znaki
    text=text.lower()
    for s in string.punctuation+string.whitespace:
        text=text.replace(s,"")
    return text==text[::-1]


def test_palindrome():
    assert palindrome("kajak") is True
    assert palindrome("Kajak") is True
    #assert palindrome("a to idiota") is True