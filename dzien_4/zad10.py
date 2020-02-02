#Zadanie#4

def formatuj(*args,**kwargs):
    text="\n".koin(args)
    for slowo, wartosc in kwargs.items:
        klucz ="$"+slowo
        text=text.replace(klucz, wartosc)
    return text

def test_formatuj():
    assert formatuj('ala $ma kota')=="ala ma kota"
    assert formatuj("ala $ma kota", "kot ma ale")=="ala ma kota\kota ma ale"
    assert formatuj("ala $ma $kota", ma="miała", kota="psa") == "ala miala psa"

#     'koszt $cena PLN',
#     'kwota $cena brutto',
#     'podatek: $podatek%'
# )

