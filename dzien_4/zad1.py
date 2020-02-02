# funkcja is_anagram - tworzy wyrazy z liter w tych samych słowach


def is_anagram(text1: str,text2: str) -> bool:
    """""
    :param text1: str
    :param text2: str
    :param return: bool
    """
    return sorted(text1.lower()) == sorted(text2.lower())


def test_is_anagram():
    assert is_anagram('tokio','kioto') is True
    assert is_anagram("anna","bob") is False