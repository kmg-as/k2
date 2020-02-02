#Zadanie#4
# Zaimplementuj funkcje przycinajaca liste na pdsatwie pdanego warunku poczatkowego i koncowego

data=[1,2,3,4,5,6,7]

def przytnij(data, func_start, func_stop):
    result=[]
    for el in data:
        if func_start(el):
            result.append(el)
        if func_stop(el):
            return result



def test_przytnij():
    assert przytnij(data, lambda x: x>3, lambda x: x==6) ==[4,5,6]