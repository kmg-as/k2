# funkjca= dla zadanej liczby zwroci pare liczba- o jeden mniejsza i wieksza
#
# up_down(5)->(4,6)
def up_down(a):
    return (a-1, a+1)

def test_up_down():
    assert up_down(5) == (4, 6)