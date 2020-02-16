def capital_index(text):
    result=[]
    for i, letter in enumerate(text):
        if letter.isupper():
            result.append(i)
    return result

def test_capital_index():
    assert capital_index("HeLlO")==[0,2,4]

