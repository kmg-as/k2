def is_anagram(text1: str,text2: str) -> bool:
    return sorted(text1.lower()) == sorted(text2.lower())


def test_is_anagram():
    assert is_anagram('typhoon', 'opython')==True
    assert is_anagram('Alice', 'Bob')==False