x=[1,2]
#pary wartości, key:value
#rozdzielone przecinkiem
#key-unkalna wartość, hashowalna (najcześciej niemutowalna)
#value-dowolny obiekt



pol_ang={ #lista, nie może się powtarzać, lista nie może być kluczem, jest mutowalna, niehashowalna
    "kot":"cat",
    "pies":"dog"
}
print(pol_ang
      )

pol_ang=dict(kot="cat", pies="dog") #dict - funkcja słownika
print(pol_ang)
pol_ang=dict([("kot","cat")])
print(pol_ang)
pol_ang["kaczka"]="duck"
print(pol_ang)
print(pol_ang["kot"])

print(pol_ang.get("jaszczurka")) #poda mi faktyczna wartość = none
print(pol_ang.get("jaszczurka", "brak hasła")) #poda mi faktyczna wartość = brak hasła

print(dir(pol_ang)) #pokazuje mozliwości dla tej zminnej (słownika)