# def incr(a):
#     print(a)
#     incr(a+1)
#
# incr(10
#      )
#

#Zadanie#6
def silnia(a):
    if a==0:
        return 1
    else:
        return a*silnia(a-1)



def test_silnia():
    assert silnia(5)==120