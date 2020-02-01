statuses={
    "alice":"online",
    "rafal":"offline",
    "anna":"offline"
}

#Napisz funkcje, ktora przyjmie jako argument
#słownik ze statusami oraz status (napis)
#I zwroci liczbe uzytkownikow o zadanym statusie#

def status_count(statuses, status):
    counter=0
    for osoba, stat in statuses.items():
        if stat == status:
            counter +=1
    return counter


def test_ststus_count_with_existing_status():
    statuses = {
        "alice" : "online",
        "rafal" : "offline",
        "anna" : "offline"
    }
    assert status_count(statuses, "online")==2
    assert status_count(statuses, "offline") == 1