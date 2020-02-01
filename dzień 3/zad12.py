lista=[5,4,9,1]

for index_podstaw in range(len(lista)):
    index_min_wart=index_podstaw
    for index_ogona in range(index_podstaw+1, len(lista)):
        if lista[index_ogona]<lista[index_min_wart]:
            index_min_wart=index_ogona
    lista[index_podstaw], lista[index_min_wart]=lista[index_min_wart], lista[index_podstaw]
    print(lista)

assert lista == [1,4,5,9]




