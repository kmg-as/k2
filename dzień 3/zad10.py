słownik={}
napis=input("Podaj napis")

for litera in napis.lower():
    if litera in słownik:
        słownik[litera]+=1
    else:
        słownik[litera]=1
print(słownik)
print(len(słownik)) #ile kluczy
print(sorted(słownik)) #posegregowane klucze
