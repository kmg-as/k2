# napisz funkcje, ktrora zwroci dlugosc najdluzszego ciagu
# tego samego znaku w napisie
#
# consecutive("aabbbaabbbb","b")=4

def consecutive(text, sign):
    counter=0
    longest_counter=0
    for s in text:
        if s == sign:
            counter+=1
        else:
            longest_counter=max(counter, longest_counter)
            counter=0
    return longer_counter


def test_consecutive():
    assert consecutive("aabbbaabbbb", "b") == 4
    assert consecutive("aabbbaabbbb", "b") == 2
    assert consecutive("aabbbbaabbb", "b") == 3